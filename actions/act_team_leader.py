import os
import re
from typing import List, Dict

from roles import GPTAgent


class TeamLeaderAction(object):
    @staticmethod
    def setup(agent:GPTAgent) -> None:
        sys_prompt = [
            "You are responsible for virtually managing a development project.\n",
            "You are at the top of the project hierarchy and responsible for overseeing the following roles:\n",
            "1. Module Leaders: Each Module Leader oversees a specific segment of the project. ",
            "Interaction with You: Module Leaders are at the next level of the hierarchy. You will assign modules to Module Leaders and receive final codes from them.\n",
            "2. Function Coordinators: Function Coordinators act as intermediaries between the Module Leaders and the Development Groups. They translate broad project tasks into specific, actionable functions. ",
            "Interaction with You: While you do not typically interact directly with Function Coordinators, they will typically assemble the functions written by Development Groups and prepare them for Module Leaders to review.\n",
            "3. Development Groups: Each group consists of a Junior Coder and a Tester. They are responsible for the hands-on implementation of project functions. Junior Coders write the code, while Testers ensure the code meets quality standards.",
            "Interaction with You: While you do not typically interact directly with Development Groups, the fundamental functions of the project are implemented by them and they report to Function Coordinators.\n\n",
            "Upon Receiving a new Project: You split the project into modules and define the scope and objectives for each. Then You assign modules to respective Module Leaders, providing them with clear instructions and resources. Do not include testing or any GUI development in modules.\n"
        ]
        agent.setup(sys_prompt="".join(sys_prompt))
    
    @staticmethod
    def plan(agent:GPTAgent, project:str) -> None:
        prompt = [
            f"You have received a new software development project: {project}.\n",
            "Break down the requirement into the smallest possible number of modules. \n",
            "The project is not that complicated. Do not overthink. If it makes sense, use only one single module for the entire project to avoid unnecessary complexity.\n",
            "\n",
            "For each module you do create:\n",
            "1. Clearly define its objectives and deliverables.\n",
            "2. Consider any dependencies between modules.\n",
            "3. Prioritize the order in which modules (if more than one) should be developed.\n",
            "\n",
            "Keep the plan concise and easy to follow, with as few modules as possible.\n",
            ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
    
    @staticmethod
    def think_twice(agent:GPTAgent) -> List[dict]:
        prompt = [
            "Review the plan you have created for the project.\n",
            "Ensure that the modules are clear, detailed, well-defined, and manageable.\n",
            "Check for any dependencies between modules and make sure they are addressed.\n",
            "Consider the order in which the modules should be developed and make any necessary adjustments.\n",
            "Make sure that the plan is clear and easy to understand for the following module leaders.\n",
            "\n",
            "Finally, list the modules using the exact format below (no extra text or lines):\n",
            "```\n"
            "[\n",
            "    NUMBER. MODULE_NAME: MODULE_DESCRIPTION\n",
            "    NUMBER. MODULE_NAME: MODULE_DESCRIPTION\n",
            "    ...\n",
            "]\n",
            "```\n",
            "**Important**:\n",
            "- Do **not** include any `[` or `]` inside the MODULE_DESCRIPTION.\n",
            "- The line with `[` must be the first line of your output and the line with `]` must be the last line of your output.\n",
            "- Do not add extra spaces or line breaks.  \n",
            "- Do not include any other text or explanation outside of the bracketed list.\n",
            "\n",
            "Your response should follow exactly this bracketed list format (including these specific line breaks).\n",
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract modules
        module_list = []
        part = re.findall(r"\[.*?\]", res, re.DOTALL)
        if part:
            modules = re.findall(r"\d+\..*?:.*", part[0])
            for module in modules:
                module_name = re.findall(r"\d+\.(.*?):", module)[0].strip()
                module_desc = re.findall(r"\d+\..*?:(.*)", module)[0].strip()
                module_list.append({"name": module_name, "description": module_desc})
        return module_list
    
    @staticmethod
    def approve_module_plan(agent:GPTAgent, module_plan:List[Dict[str, str]], module_number:int) -> List[Dict[str, str]]:
        prompt = [
            f"Module {module_number+1} Leader has planned the following functions for the module:\n",
            "```\n",
            f"{module_plan}\n",
            "```\n",
            "Review the functions and ensure that they are within the scope of the module and well-defined with the necessary input and output definitions and types.\n",
            "If you approve the plan, just return a single word 'Approved' without any other content.\n",
            "If you want to make any changes, list the new module plan in the following format:\n",
            "```\n"
            "[\n",
            "    NUMBER. FUNCTION_NAME: FUNCTION_DESCRIPTION(INCLUDING INPUT AND OUTPUT TYPES)\n",
            "    NUMBER. FUNCTION_NAME: FUNCTION_DESCRIPTION(INCLUDING INPUT AND OUTPUT TYPES)\n",
            "    ...\n",
            "]\n"
            "```",
            "Do not use \"[\" and \"]\" inside the FUNCTION_DESCRIPTION to avoid confusion."
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract functions
        if res.lower().strip() == "approved":
            return module_plan
        else:
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
    def assemble_modules(agent:GPTAgent, modules:List[Dict[str, str]]) -> str:
        module_codes = []
        for module in modules:
            module_file_name = os.path.join(agent.work_dir, f"{module['name'].replace(' ', '_')}.py")
            with open(module_file_name, "r") as f:
                module_codes.append({"file_name": f"{module['name']}.py", "code": f.read()})

        prompt = [
            "You have received the final functions from the Module Leaders:\n",
            "```\n",
            f"{module_codes}\n",
            "```\n",
            "\n",
            "Import the modules from the files and assemble them into a final single project code in the following format:\n",
            "```\n",
            "IMPORT STATEMENTS\n",
            "def FUNCTION_NAME(INPUT_PARAMS) -> RETURN_TYPE:\n",
            "    \"\"\"\n",
            "    GOOGLEDOC STYLE DOCSTRING DESCRIBING THE FUNCTION\n",
            "    \"\"\"\n",
            "    YOUR CODE HERE\n",
            "if __name__ == '__main__':\n",
            "    ENTRY POINT FUNCTION CALLS\n",
            "```",
            "Ensure that the functions are well-organized and follow the standard format.\n",
            "Do not rewrite any functions, just import the modules from the files and assemble them."
            "Do not wirte any test modules or GUI code. Just assemble the modules togenther and leave a main function call at the end."
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract final code
        final_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        if final_code:
            # sometimes the code starts with ```python, remove it
            if final_code[0].startswith("python"):
                final_code[0] = final_code[0][6:]
            return final_code[0].strip()
        else:
            return ""