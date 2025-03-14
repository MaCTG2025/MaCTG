import re
from typing import List

from roles import GPTAgent


class ModuleLeaderAction(object):
    @staticmethod
    def setup(agent:GPTAgent) -> None:
        sys_prompt = [
            "You are a Module Leader in a software development group.",
            "You are in charge of a module, which is a distinct part of the project. Your role involves decomposing the module into functions, checking your plan with the Team Leader, and delegating tasks to Function Coordinators for further development.\n",
            "Your primary interactions and responsibilities are as follows:\n",
            "1. With Team Leader: Team Leader is responsible for virtually managing the development project at the highest level.\n",
            "Interaction with You: You will receive all module descriptions from the Team Leader, and you are in charge of a single module.",
            "Upon receiving the module description, you will break down the module into actionable functions. You must ensure that the functions are within the scope of the module and you define clear input and output type requirements for each function.",
            "Your module will be reviewed by the Team Leader before you delegate the functions to Function Coordinators.\n",
            "2. With Function Coordinators: Function Coordinators act as intermediaries between the you and the Development Groups. They translate your function descriptions into function signatures and assign them to Development Groups for implementation.\n",
            "Interaction with You: After you have defined the functions and received approval from the Team Leader, you will delegate the functions to the Function Coordinators. Again, you must ensure that the functions are clear and well-defined, especially the input and output types.\n",
        ]
        agent.setup(sys_prompt="".join(sys_prompt))
    
    @staticmethod
    def plan(agent:GPTAgent, project:str, modules:List[dict], module_number:int) -> None:
        prompt = [
            f"Your team is working on a software development project: {project}.\n",
            f"Team Leader has planned the following modules for the project:\n",
            "```\n",
            f"{modules}\n",
            "```\n",
            f"You are assigned to Module {module_number+1}: {modules[module_number]}.\n",
            "\n",
            "Break down your module into smaller, actionable functions that can be implemented by Development Groups.",
            "Use as less functions as possible to avoid unnecessary complexity. It is possible to have a single function for the entire module.\n",
            "Ensure that each function is well-defined, with clear input and output type requirements (give clear type specifications such as int, str, np.array, etc.).",
            "If there are mutiple functions, consider dependencies between functions and prioritize the order in which they should be developed.",
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
    
    @staticmethod
    def think_twice(agent:GPTAgent, prev_plan:dict) -> List[dict]:
        prompt = [
            "Review the functions you have created for your module. \n",
            "Ensure that the functions are clear, detailed, well-defined, and manageable.\n",
            "Check for any dependencies between functions and make sure they are addressed.\n",
            "Consider the order in which the functions should be developed and make any necessary adjustments.\n",
            "Make sure the plan is clear and easy to understand for the following Function Coordinators.\n",
            "\n",
            "Finally, list the functions and their specified input/output types using the exact format below. \n",
            "**Important**: do not include any \"[\" or \"]\" in the function descriptions themselves, to avoid confusion with the list brackets.\n",
            "\n",
            "Your output should be only the following code block in Markdown format (no extra explanations or text), and it must look exactly like this (except with the real function details inserted):\n",
            "```\n",
            "[\n",
            "1. FUNCTION_NAME: FUNCTION_DESCRIPTION (including input and output types)\n",
            "2. FUNCTION_NAME: FUNCTION_DESCRIPTION (including input and output types)\n",
            "...\n",
            "]\n",
            "```",
        ]
        if prev_plan:
            additional_prompt = [
                            f"Based on the plans of previous Module Leaders:\n",
                            f"```\n",
                            f"{prev_plan}\n",
                            f"```\n",
            ]
            prompt = additional_prompt + prompt
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
        # extract functions
        function_list = []
        part = re.findall(r"\[.*?\]", res, re.DOTALL)
        if part:
            functions = re.findall(r"\d+\..*?:.*", part[0])
            for function in functions:
                function_name = re.findall(r"\d+\.(.*?):", function)[0].strip()
                function_desc = re.findall(r"\d+\..*?:(.*)", function)[0].strip()
                function_list.append({"name": function_name, "description": function_desc})
        return function_list
    
    @staticmethod
    def confirm_module_plan(agent:GPTAgent, module_plan:List[dict]) -> None:
        prompt = [
            "Team Leader has reviewed your module plan. Your module are as follows:\n",
            "```\n",
            f"{module_plan}\n",
            "```\n",
            "Function Coordinator will now translate these functions into function signatures for Development Groups to implement.",
            "In the later step, they will confirm the function signatures with you before proceeding with the development.",
            "Make sure their function signatures align with your plan and the requirements of the module."
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

    @staticmethod
    def approve_function_list(agent:GPTAgent, function_list:List[dict]) -> List[dict]:
        prompt = [
            "Function Coordinator has translated the functions into function signatures for the Development Groups to implement.\n",
            "Review the function signatures and make sure they align with the requirements of the module:\n",
            "```\n",
            f"{function_list}\n",
            "```\n",
            "\n",
            "Check for any missing information in the function signatures and make sure they are addressed, such as import statements, input and output types, and docstrings.",
            "Make sure that the function signatures are complete and easy to understand for the junior developpers in Development Groups.",
            "If you approve the plan, just return a single word 'Approved' without any other content.\n",
            "If you want to make any changes, list the new function plan in the following format:\n",
            "```\n"
            "====================\n",
            "IMPORT STATEMENTS\n",
            "\n",
            "def FUNCTION_NAME(INPUT_PARAMS) -> RETURN_TYPE:\n",
            "    \"\"\"\n",
            "    GOOGLEDOC STYLE DOCSTRING DESCRIBING THE FUNCTION\n",
            "    \"\"\"\n",
            "====================\n",
            "IMPORT STATEMENTS\n",
            "\n",
            "def FUNCTION_NAME(INPUT_PARAMS) -> RETURN_TYPE:\n",
            "    \"\"\"\n",
            "    GOOGLEDOC STYLE DOCSTRING DESCRIBING THE FUNCTION\n",
            "    \"\"\"\n",
            "====================\n",
            "    ...\n",
            "====================\n",
            "```"
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
        # extract functions
        if res.lower().strip() == "approved":
            return function_list
        else:
            function_list = []
            part = re.findall(r"(?<=====================\n)(.*?)(?=\n====================)", res, re.DOTALL)
            if part:
                for function in part:
                    function_name = re.findall(r"def (.*?)[(]", function)[0].strip()
                    function_list.append({"name": function_name, "signature": function})
            return function_list
        
    @staticmethod
    def implement_module_test(agent:GPTAgent, module_name:str, module_code:str, module_file_name:str, prev_modules:List[dict]) -> str:
        prompt = [
            f"You have received the code for the module *{module_name}* you are in charge of from the Function Coordinator.\n",
            f"The module code is in {module_file_name}, as follows:\n",
            "```\n",
            f"{module_code}\n",
            "```\n",
            "Write a test code for the module to ensure that the functions are working as expected.\n",
            "You only need to test the basic functionality of the module, such as input and output types, and the correctness of the functions.",
            "Import the module code at the beginning of the test code and finish the test code with the following format:\n",
            "```\n",
            "IMPORT STATEMENTS\n",
            "def test_MODULE_NAME(INPUT_PARAMS) -> RETURN_TYPE:\n",
            "    YOUR TEST CODE HERE\n",
            "if __name__ == '__main__':\n",
            "    test_MODULE_NAME(INPUT_PARAMS)\n",
            "```"
            "Do not inclue any cleaning up code in the test code, and do not remove any source file."
        ]
        if prev_modules:
            additional_prompt = [
                "You might need previous modules output, here are the previous modules:\n",
                "```\n",
                f"{prev_modules}\n",
                "```\n",
            ]
            prompt = additional_prompt + prompt
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
        # extract test code
        test_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        if test_code:
            # sometimes the code starts with ```python, remove it
            if test_code[0].startswith("python"):
                test_code[0] = test_code[0][6:]
            return test_code[0].strip()
        else:
            return "" 
        
    @staticmethod
    def analyze_module_test_result(agent:GPTAgent, test_result:str) -> str:
        prompt = [
            "After running the module test code. The test result is as follows:\n",
            "```\n",
            f"{test_result}\n",
            "```\n",
            "Analyze the test result and provide feedback to the Function Coordinator.\n",
            "Sometimes the error will not affect the functionality of the module, then you can ignore the error and approve the module by returning a single word 'Approved' without any other content.\n",
            "If there are errors that need to be fixed, list the errors and the necessary modifications in detailed format.\n",
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
        if res.lower().strip() == "approved":
            return ""
        
        return res