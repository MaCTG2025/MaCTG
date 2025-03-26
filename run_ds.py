import json
import os
import shutil
from typing import Dict, List

from actions.act_coder import CoderAction
from actions.act_function_coordinator import FunctionCoordinatorAction
from actions.act_module_leader import ModuleLeaderAction
from actions.act_team_leader import TeamLeaderAction
from actions.act_tester import TesterAction
from graph.agent_graph import AgentGraph
from roles.gpt_agent import GPTAgent
from roles.local_agent import LocalAgent
from utils import dump_python_code, run_test

project_req = "\nGiven an RGB image (\"./test_image.png\"), slpit it into R, G, and B channels. For each channel, save it as RGB image with the channel as the only non-zero channel. For example, the red channel image should have the red channel as the only non-zero channel, and the green and blue channels should be zero. Save the three images as \"red_channel.png\", \"green_channel.png\" and \"blue_channel.png\".\n"

def run_graph(project_req:str, case_id:str):
    work_dir = f"./evaluation_ds/Case_{case_id}"
    source_file_dir = os.path.join("../BCVPP", case_id)
    # clear project directory
    if os.path.exists(work_dir):
        shutil.rmtree(work_dir)
        shutil.copytree(source_file_dir, work_dir)
    else:
        shutil.copytree(source_file_dir, work_dir)

    # create agent graph
    AG = AgentGraph()

    # create team leader agent and add to agent graph
    TL = GPTAgent(agent_name="Team_leader", model_id="deepseek-chat", work_dir=work_dir)
    AG.add_node(TL)
    AG.set_current(TL)

    # setup team leader agent
    TeamLeaderAction.setup(AG.current)

    # initialize plan
    TeamLeaderAction.plan(AG.current, project_req)

    # Team Leader thinks twice and rephrases the plan
    AG.add_edge(AG.current, TL)
    AG.next_node()
    modules = TeamLeaderAction.think_twice(AG.current)
    print(modules)

    # based on the modules, invoke the module leaders
    ML_list = []
    module_plan = {}
    for i in range(len(modules)):
        AG.set_current(TL)
        # create module leader agent and add to agent graph
        ML = GPTAgent(agent_name=f"Module_leader_{i+1}", model_id="deepseek-chat", work_dir=work_dir)
        AG.add_node(ML)
        AG.add_edge(AG.current, ML)
        AG.next_node()

        # setup module leader agent
        ModuleLeaderAction.setup(AG.current)

        # plan the module
        ModuleLeaderAction.plan(AG.current, project_req, modules, i)

        # Module Leader thinks twice and rephrases the plan
        AG.add_edge(AG.current, ML)
        AG.next_node()
        cur_module_plan = ModuleLeaderAction.think_twice(AG.current, module_plan)

        # send the plan to the Team Leader for approval
        AG.add_edge(AG.current, TL)
        AG.next_node()
        cur_module_plan = TeamLeaderAction.approve_module_plan(AG.current, cur_module_plan, i)
        print(cur_module_plan)

        # confirm the approved plan
        AG.add_edge(AG.current, ML)
        AG.next_node()
        ModuleLeaderAction.confirm_module_plan(AG.current, cur_module_plan)

        # save the approved plan for the next module leader
        module_plan[modules[i]['name']] = cur_module_plan

        # save the module leader for future reference
        ML_list.append(ML)


    # based on the approved plan, refactor the functions into function signature by function coorindators
    FC_list = []
    function_plan = {}
    for i in range(len(ML_list)):
        # create function coordinator agent and add to agent graph
        FC = GPTAgent(agent_name=f"Function_coordinator_{i+1}", model_id="deepseek-chat", work_dir=work_dir)
        AG.add_node(FC)
        AG.set_current(ML_list[i])
        AG.add_edge(AG.current, FC)
        AG.next_node()

        # setup function coordinator agent
        FunctionCoordinatorAction.setup(AG.current)

        # plan the functions
        FunctionCoordinatorAction.plan(AG.current, project_req, module_plan, modules[i]['name'])

        # Function Coordinator thinks twice and rephrases the plan
        AG.add_edge(AG.current, FC)
        AG.next_node()
        function_list = FunctionCoordinatorAction.think_twice(AG.current)

        # send the plan to the Module Leader for approval
        AG.add_edge(AG.current, ML_list[i])
        AG.next_node()
        function_list = ModuleLeaderAction.approve_function_list(AG.current, function_list)
        print(function_list)

        # confirm the approved plan
        AG.add_edge(AG.current, FC)
        AG.next_node()
        FunctionCoordinatorAction.confirm_function_list(AG.current, function_list)

        FC_list.append(FC)
        function_plan[modules[i]['name']] = function_list

    # invoke development group to implement the functions
    for i in range(len(FC_list)):
        AG.set_current(FC_list[i])
        for j in range(len(function_plan[modules[i]['name']])):
            coder = LocalAgent(model_id="Qwen/Qwen2.5-Coder-7B-Instruct", agent_name=f"Coder_{i+1}_{j+1}", work_dir=work_dir)
            AG.add_node(coder)
            AG.add_edge(AG.current, coder)
            AG.next_node()

            # setup coder agent
            CoderAction.setup(AG.current, use_rag=False)

            # coder implements the function
            function_code = CoderAction.implement_function(AG.current, function_plan[modules[i]['name']][j])
            function_file_name = f"{function_plan[modules[i]['name']][j]['name']}.py"
            dump_python_code(function_code, f"{os.path.join(work_dir, function_file_name)}")
            print(function_code)

            # setup tester agent
            tester = LocalAgent(model_id="Qwen/Qwen2.5-Coder-7B-Instruct", agent_name=f"Tester_{i+1}_{j+1}", work_dir=work_dir)
            AG.add_node(tester)
            AG.add_edge(AG.current, tester)
            AG.next_node()
            TesterAction.setup(AG.current)

            # tester implements the test code
            test_code = TesterAction.implement_test(AG.current, function_plan[modules[i]['name']][j]['name'], function_code)
            function_test_file_name = f"{function_plan[modules[i]['name']][j]['name']}_test.py"

            # function coordinator reviews the implementation
            AG.add_edge(AG.current, FC_list[i])
            AG.next_node()
            test_code = FunctionCoordinatorAction.review_test_code(AG.current, function_file_name, function_code, function_test_file_name, test_code, j)
            dump_python_code(test_code, f"{os.path.join(work_dir, function_test_file_name)}")

            # run the test
            test_result = run_test(work_dir, f"{function_plan[modules[i]['name']][j]['name']}_test.py")

            # if error, function coordinator analyzes the test result
            if "Traceback" in test_result:
                AG.add_edge(AG.current, FC_list[i])
                AG.next_node()
                modification = FunctionCoordinatorAction.analyze_test_result(AG.current, test_result)

                # coder implements the modification
                if modification:
                    AG.add_edge(AG.current, coder)
                    AG.next_node()
                    function_code = CoderAction.refine_function(AG.current, function_code, modification)
                    dump_python_code(function_code, f"{os.path.join(work_dir, function_plan[modules[i]['name']][j]['name'])}.py")

            coder.release()
            tester.release()

    # backward workflow - assembly
    # function coordinator assembles the functions
    assembled_modules = []
    for i in range(len(FC_list)):
        AG.set_current(FC_list[i])
        AG.add_edge(AG.current, FC_list[i])
        AG.next_node()
        module_code = FunctionCoordinatorAction.assemble_functions(AG.current, function_plan[modules[i]['name']])
        module_file_name = f"{modules[i]['name'].replace(' ', '_')}.py"
        dump_python_code(module_code, f"{os.path.join(work_dir, module_file_name)}")

        # module leader test the module
        AG.add_edge(AG.current, ML_list[i])
        AG.next_node()
        module_test_code = ModuleLeaderAction.implement_module_test(AG.current, modules[i]['name'], module_code, module_file_name, assembled_modules)
        test_file_name = f"{modules[i]['name'].replace(' ', '_')}_module_test.py"
        dump_python_code(module_test_code, f"{os.path.join(work_dir, test_file_name)}")

        # run the test
        test_result = run_test(work_dir, f"{modules[i]['name']}_module_test.py")

        # if error, module leader analyzes the test result
        if "Traceback" in test_result:
            AG.add_edge(AG.current, ML_list[i])
            AG.next_node()
            modification = ModuleLeaderAction.analyze_module_test_result(AG.current, test_result)

            # function coordinator implements the modification
            if modification:
                AG.add_edge(AG.current, FC_list[i])
                AG.next_node()
                module_code = FunctionCoordinatorAction.refine_module(AG.current, module_code, modification)
                dump_python_code(module_code, f"{os.path.join(work_dir, modules[i]['name'])}.py")

        assembled_modules.append({"module_name": modules[i]['name'], "module_file_name": module_file_name, "code": module_code})

    # Team leader assembles the modules
    AG.set_current(TL)
    AG.add_edge(AG.current, TL)
    AG.next_node()
    project_code = TeamLeaderAction.assemble_modules(AG.current, modules)
    dump_python_code(project_code, f"{os.path.join(work_dir, 'main')}.py")


if __name__ == "__main__":
    test_data = "../BCVPP/requirements.json"
    with open(test_data, "r") as f:
        data = json.load(f)
        for i, req in enumerate(data[1:]):
            print(req["req_idx"])
            run_graph(req["requirement"], req["req_idx"])
