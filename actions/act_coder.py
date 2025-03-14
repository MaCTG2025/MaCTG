import re
from typing import List, Dict

from roles.local_agent import LocalAgent


class CoderAction(object):
    @staticmethod
    def setup(agent:LocalAgent, use_rag:bool=True) -> None:
        sys_prompt = [
            "You are a coder responsible for implementing the functions assigned to you by your leader.",
            "You will receive a detailed function signature to be implemented including the import statements, expected input and output and a docstring.",
            "You are responsible for finishing the code for the function and ensuring that it meets the requirements.\n",
        ]
        agent.setup()

        if use_rag:
            agent.rag_enabled = True
            agent.load_knowledge("./RAG/Coder_RAG.json")
    
    @staticmethod
    def implement_function(agent:LocalAgent, function:Dict) -> str:
        prompt = [
            f"Implement the following function:\n",
            f"```\n{function['signature']}\n```\n",
            "\n",
            "You must follow these rules strictly:\n",
            "1. **Check whether any import statements are required.** For example:\n", 
            "   - If the function signature or return type mentions external libraries/classes (e.g. `pd.DataFrame`, `typing.List`, etc.), you **must** import them in `IMPORT STATEMENTS`.\n", 
            "2. Use the exact function signature as provided (including imports and return type annotation, if present). \n",
            "3. Include a Google-style docstring that describes the function’s purpose, the parameters, and the return value. \n",
            "4. Return the code wrapped in a markdown code fence (triple backticks) with no additional text outside it.\n ",
            "5. The final code must appear *exactly* in the following format:\n", 
            "```\n",
            "IMPORT STATEMENTS\n",
            "def FUNCTION_NAME(INPUT_PARAMS) -> RETURN_TYPE:\n",
            "    \"\"\"\n",
            "    GOOGLEDOC STYLE DOCSTRING DESCRIBING THE FUNCTION\n",
            "    \"\"\"\n",
            "    #YOUR CODE HERE\n",
            "```\n",
            "Output *only* the code block above!"
        ]
        if agent.rag_enabled:
            context = agent.retrieve(function["signature"])
            if context:
                prompt += ["\n", "Here are some similar examples that might help you:\n", f"```\n{context}\n```\n"]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        agent.mount_to_cuda()
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})

        # extract function code inside the code block
        function_code = re.findall(r"```(.*?)```", res, re.DOTALL)
        return_code = ""
        if function_code:
            for i in function_code:
                # sometimes the code starts with ```python, remove it
                if i.startswith("python"):
                    i = i[6:]
                return_code += i
        return return_code.strip()
        
    @staticmethod
    def refine_function(agent:LocalAgent, function_code:str, modification:str) -> str:
        prompt = [
            "Here is the code for the function you have implemented:\n",
            "```\n",
            f"{function_code}\n",
            "```\n",
            "\n",
            "The Function Coordinator has reviewed the code and has requested for the following modifications:\n",
            f"```\n{modification}\n```\n",
            "Please make the necessary changes to the code and return the updated code.\n",
            "Return code only in the following format:\n",
            "```\n",
            "IMPORT STATEMENTS\n",
            "def FUNCTION_NAME(INPUT_PARAMS) -> RETURN_TYPE:\n",
            "    \"\"\"\n",
            "    GOOGLEDOC STYLE DOCSTRING DESCRIBING THE FUNCTION\n",
            "    \"\"\"\n",
            "    YOUR CODE HERE\n",
            "```\n",
            "The \"FUNCTION_NAME\" and \"INPUT_PARAMS\" should be exactly the same as the original function signature, do not capitalize or change them.\n",
            "Output *only* the code block above!"
        ]
        agent.combine_prompt({"role": "user", "content": "".join(prompt)})
        agent.mount_to_cuda()
        res = agent.chat()
        agent.combine_prompt({"role": "assistant", "content": res})
        
        # extract function code inside the code block
        function_code = res.split("```")[1:-1]
        return_code = ""
        if function_code:
            for i in function_code:
                # sometimes the code starts with ```python, remove it
                if i.startswith("python"):
                    i = i[6:]
                return_code += i
        return return_code.strip()
