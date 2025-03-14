import re
from typing import List, Dict

from roles.local_agent import LocalAgent


class TesterAction(object):
    @staticmethod
    def setup(agent:LocalAgent) -> None:
        sys_prompt = [
            "You are a tester responsible for testing the function implemented by a coder.",
            "You will receive the code for the function to be tested.",
            "You are responsible for implementing a test code to test the function."
        ]
        agent.setup(sys_prompt="".join(sys_prompt))
    
    @staticmethod
    def implement_test(agent:LocalAgent, function_name:str, function_code:str) -> str:
        prompt = [
            f"Write a python code to test the following function (function file name: {function_name}.py).\n",
            f"```\n{function_code}\n```\n",
            "\n",
            "Import the original function first and other necessary libraries.",
            "Use unittest module to write the test cases and do not include the clean up code.\n",
            "Return code only in the following format:\n",
            "```\n",
            "import unittest\n",
            "from FUNCTION_FILE import FUNCTION_NAME\n",
            "OTHER IMPORT STATEMENTS\n",
            "\n",
            "YOUR TEST CODE HERE\n",
            "```"
            "Do not inclue any cleaning up code in the test code, and do not remove any source file."
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        agent.mount_to_cuda(1)
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract test code inside the code block
        test_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        if test_code:
            # sometimes the code starts with ```python, remove it
            if test_code[0].startswith("python"):
                test_code[0] = test_code[0][6:]
            return test_code[0].strip()
        else:
            return ""