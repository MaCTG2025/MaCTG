import json
import os

from .base_agent import BaseAgent
from openai import OpenAI


class GPTAgent(BaseAgent):
    def setup(self, sys_prompt:str=None) -> None:
        with open("./deepseek_api", "r") as f:
            api_key = f.read().strip()
        self.client = OpenAI(api_key=api_key,
                             base_url="https://api.deepseek.com/v1"
        )
        
        # set work directory
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir, exist_ok=True)
        
        # set message cache file
        if os.path.exists(self.msg_cache_file):
            self.load_message()
        else:
            # set system prompt
            if sys_prompt:
                self.sys_prompt = {"role": "system", "content": sys_prompt}
                with open(self.msg_cache_file, 'a') as f:
                    f.write(f"{json.dumps(self.sys_prompt)}\n")
                self.messages = [self.sys_prompt]
            else:
                self.messages = []
        
        # set role cache file
        if os.path.exists(self.role_cache_file):
            with open(self.role_cache_file, 'r') as f:
                self.role = json.load(f)
        else:
            self.role = {"work_dir": self.work_dir}

    def add_prev(self, prev_node) -> None:
        self.prev_nodes.append(prev_node)

    def add_next(self, next_node) -> None:
        self.next_nodes.append(next_node)

    def chat(self) -> str:
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=self.messages
        )
        return response.choices[0].message.content.strip()
    

if __name__ == "__main__":
    agent = GPTAgent(agent_name="gpt_agent", model_id="gpt-3.5-turbo")