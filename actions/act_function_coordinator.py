import os
import re
from typing import List

from roles import GPTAgent


class FunctionCoordinatorAction(object):
    @staticmethod
    def setup(agent:GPTAgent) -> None:
        sys_prompt = [
            "You are a Function Coordinator in a software development group. You are under the supervision of a Module Leader, while overseeing the Development Groups responsible for implementing the functions you assign.\n",
            "You are in charge of a series of functions that are part of a module. Your role involves translating the function descriptions provided by the Module Leader into function signatures.\n",
            "Your primary interactions and responsibilities are as follows:\n",
            "1. With Module Leader: Module Leader is responsible for initially breaking down the module into functions in natural language and providing you with the function descriptions.\n",
            "Interaction with You: After the Module Leader has defined the functions and received approval from the Team Leader, you will receive the function descriptions and are responsible for these functions.",
            "You must translate the function descriptions into function signatures, which include the definition of the function name, input and output parameters and types, and the scope and requirements of the function in the docstring.\n",
            "2. With Development Groups: Development Groups are junior developpers responsible for implementing the functions assigned by you.\n",
            "Interaction with You: After you have translated the function descriptions into function signatures, you will assign the functions to Development Groups for implementation.",
            "You must ensure that the function signatures are clear, detailed and well-defined, and that the Development Group understands the requirements of the function.\n",
        ]
        agent.setup(sys_prompt="".join(sys_prompt))
    
    @staticmethod
    def plan(agent:GPTAgent, project:str, module_plans:dict, module_name:str) -> None:
        prompt = [
            f"Your team is working on a software development project:\n",
            "```\n",
            f"{project}\n",
            "```\n",
            f"Here are all module plans for the project:\n",
            "```\n",
            f"{module_plans}\n",
            "```\n",
            f"You are assigned to Module: {module_name}.",
            "Translate the function descriptions into function signatures (in Python) that includes the function name, input and output params with types, and the return type.",
            "Also include the scope and requirements of the function in the docstring, as detailed as possible.",
            "You might also need to provide the dependencies of the functions (the \"import\" statements) at the beginning of the file."
            "Ensure that the function signature is clear and well-defined, and that the Development Group understands the requirements of the function."
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

    @staticmethod
    def think_twice(agent:GPTAgent) -> List[dict]:
        prompt = [
            "Review the function signatures you have created for the module. Only focus on your own module!\n",
            "Ensure that the function signatures are clear, detailed, well-defined and manageable.",
            "Check for any missing information in the function signatures and make sure they are addressed.",
            "Consider the scope and requirements of the functions and make any necessary adjustments.",
            "Make sure that the function signatures are complete and easy to understand for the junior developpers in Development Groups.",
            "Finally list the function signatures in the following format: \n",
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
            "Make sure each function signature is inside the '====================' blocks (always starts with one and ends with one)."
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
        # extract functions
        function_list = []
        part = re.findall(r"(?<=====================\n)(.*?)(?=\n====================)", res, re.DOTALL)
        if part:
            for function in part:
                if "def" in function:
                    function_name = re.findall(r"def (.*?)[(]", function)[0].strip()
                    function_list.append({"name": function_name, "signature": function})

        return function_list
    
    @staticmethod
    def confirm_function_list(agent:GPTAgent, function_list:List[dict]) -> None:
        prompt = [
            "Module Leader has reviewed the function signatures you have created for the module.\n",
            "The confirmed function signatures are as follows:\n",
            "```\n",
            f"{function_list}\n",
            "```\n",
            "You can now proceed with assigning the functions to the Development Groups for implementation."
        ]

        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
    @staticmethod
    def review_test_code(agent:GPTAgent,  function_file_name:str, function_code:str,  function_test_file_name:str, test_code:str, function_number:int) -> str:
        prompt = [
            f"Development Group has implemented the function number {function_number + 1} and the test code for the function.\n",
            f"Function file name: **{function_file_name}**. And the function code is as follows:\n",
            "```\n",
            f"{function_code}\n",
            "```\n",
            f"Test file name: **{function_test_file_name}**. And the test code is as follows:\n",
            "```\n",
            f"{test_code}\n",
            "```\n",
            "Review the *test* code to ensure that it tests the function correctly and thoroughly.",
            "Make sure that there's no cleaning up code in the test code, and the test code should not remove any source file.",
            "And make sure the test code has a proper entry point (e.g., a \"if __name__ == '__main__':\" block) to run the tests.\n",
            "If you approve the test code, just return a single word 'Approved' without any other content.\n",
            "If you want to make any changes, directly re-write the test code in the following format:\n",
            "```\n",
            "import unittest\n",
            "from FUNCTION_FILE import FUNCTION_NAME\n",
            "OTHER IMPORT STATEMENTS\n",
            "\n",
            "YOUR TEST CODE HERE\n",
            "```"
        ]

        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        if res.lower().strip() == "approved":
            return test_code

        # extract test code inside the code block
        test_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        if test_code:
            # sometimes the code starts with ```python, remove it
            if test_code[0].startswith("python"):
                test_code[0] = test_code[0][6:]
            return test_code[0].strip()
        else:
            return ""
        
    @staticmethod
    def analyze_test_result(agent:GPTAgent, test_result:str) -> str:
        prompt = [
            "Development Group has run the test for the implemented function.\n",
            "The test result information are as follows:\n",
            "```\n",
            f"{test_result}\n",
            "```\n",
            "Analyze the test results to identify any issues or errors in the function implementation. ",
            "Provide concise, direct feedback to the Development Group on how to fix the issues if there is a genuine problem with the function. For example:\n",
            "- \"Replace the variable name 'x' with 'y'.\"\n",
            "- \"Add a condition to check for 'z'.\"\n",
            "\n",
            "**If you determine that the function is actually correct and any issue lies with redundant test cases or with the test code itself (not the function), or if there is no real issue at all, then respond with a single word `Approved` and nothing else.**\n",
            "\n",
            "Do not write any long paragraphs. Your final output must be either:\n",
            "1. A list of short, direct modifications if the function is at fault.\n",
            "2. Or a single word `Approved` if the function is correct or the error is in the test code.\n",
            "\n",
            "Return only one of these two types of response."
        ]

        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        if res.lower().strip() == "approved":
            return ""

        return res
    
    @staticmethod
    def assemble_functions(agent:GPTAgent, function_list:List[dict]) -> str:
        function_codes = []
        for function in function_list:
            function_file_name = os.path.join(agent.work_dir, f"{function['name']}.py")
            with open(function_file_name, "r") as f:
                function_codes.append({"file_name": f"{function['name']}.py", "code": f.read()})

        prompt = [
            "Now all the functions have been implemented and tested by the Development Groups.\n",
            "Here are the final implementations of the functions:\n",
            "```\n",
            f"{function_codes}\n",
            "```\n",
            "Each of these functions is defined in separate functions files (e.g., `my_functions_a.py`, `my_functions_b.py`, etc.). \n", 
            "**Do not re-implement or rewrite the function bodies** in the next code block. \n",
            "Instead, **import** them from their respective function files. \n",
            "\n",
            "Now, please assemble all the functions into one final module by: \n",
            "1. Importing each required function from its corresponding file (e.g., `from my_functions_a import functionA`). \n",
            "2. Creating a new module-level function (the “module entry function”) that uses these imported functions. \n",
            "\n", 
            "Your output should be **only** a single code block with the following format (no extra explanations, no additional text outside the code block): \n",
            "```\n",
            "IMPORT STATEMENTS \n",
            "\n",
            "def MODULE_NAME(INPUT_PARAMS: MODULE_INPUT_TYPE) -> MODULE_RETURN_TYPE: \n",
            "    \"\"\" \n",
            "    GoogleDoc style docstring describing what this module-level function does \n",
            "    """
            "    # In this function body, call the imported functions as needed. \n",
            "``` \n",
            " \n",
            "**Remember:** \n",
            "- Do **not** copy the function implementations again; use `import` statements only. \n",
            "- Write a concise, clear GoogleDoc style docstring for the module-level function. \n",
            "- Do **not** add any text before or after the code block. \n",
            "- The code block must strictly follow the format shown above. \n",
        ]

        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract module code inside the code block
        module_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        if module_code:
            # sometimes the code starts with ```python, remove it
            if module_code[0].startswith("python"):
                module_code[0] = module_code[0][6:]
            module_code = module_code[0].strip()
        else:
            module_code = ""

        return module_code
    
    @staticmethod
    def refine_module(agent:GPTAgent, module_code:str, modification:str) -> str:
        prompt = [
            "The Module Leader has reviewed the module code that you have assembled with all the functions.\n",
            "The Module Leader has requested for the following modifications to the module code:\n",
            f"```\n{modification}\n```\n",
            "Please make the necessary changes to the module code and return the updated module code.\n",
            "Write the module code in the following format:\n",
            "```\n",
            "IMPORT STATEMENTS \n",
            "\n",
            "def MODULE_NAME(INPUT_PARAMS: MODULE_INPUT_TYPE) -> MODULE_RETURN_TYPE: \n",
            "    \"\"\" \n",
            "    GoogleDoc style docstring describing what this module-level function does \n",
            "    """
            "    # In this function body, call the imported functions as needed. \n",
            "``` \n",
            " \n",
            "**Remember:** \n",
            "- Do **not** copy the function implementations again; use `import` statements only. \n",
            "- Write a concise, clear GoogleDoc style docstring for the module-level function. \n",
            "- Do **not** add any text before or after the code block. \n",
            "- The code block must strictly follow the format shown above. \n",
        ]

        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract module code inside the code block
        module_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        if module_code:
            # sometimes the code starts with ```python, remove it
            if module_code[0].startswith("python"):
                module_code[0] = module_code[0][6:]
            module_code = module_code[0].strip()
        else:
            module_code = ""

        return module_code