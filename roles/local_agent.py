import json
import os
import gc

import torch
from .base_agent import BaseAgent
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          BitsAndBytesConfig)


class LocalAgent(BaseAgent):
    def setup(self, sys_prompt:str=None, quantization:bool=False) -> None:
        # load model (init to cpu)
        if quantization:
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                quantization_config=quantization_config,
                device_map="cpu",
                trust_remote_code=True, 
                temperature=0.6
            )
        else:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                device_map="cpu",
                trust_remote_code=True
            )
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id, trust_remote_code=True)

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir, exist_ok=True)

        # load message cache
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

        # load role cache
        if os.path.exists(self.role_cache_file):
            with open(self.role_cache_file, 'r') as f:
                self.role = json.load(f)
        else:
            self.role = {"work_dir": self.work_dir}

    def add_prev(self, prev_node) -> None:
        self.prev_nodes.append(prev_node)

    def add_next(self, next_node) -> None:
        self.next_nodes.append(next_node)

    def chat(self, max_token:int=1024) -> str:
        # tokenize the messages
        inputs = self.tokenizer.apply_chat_template(self.messages, add_generation_prompt=True, return_tensors="pt").to(self.model.device)
        # generate response
        output = self.model.generate(
            inputs,
            max_new_tokens=max_token,
            do_sample=False,
            num_return_sequences=1,
            top_k=50,
            top_p=0.95,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        output = output[0][len(inputs[0]):].to("cpu")
        # decode the response
        response = self.tokenizer.decode(output)
        return response


    def mount_to_cuda(self, device_id:int=0) -> None:
        self.model = self.model.to(f"cuda:{device_id}")
        print("Model mounted to cuda!")
    
    def mount_to_cpu(self) -> None:
        self.model = self.model.to("cpu")
        torch.cuda.empty_cache()
        print("Model mounted to cpu!")

    def release(self):
        self.model = None
        self.tokenizer = None
        gc.collect()
        # clear cuda cache
        torch.cuda.empty_cache()


if __name__ == "__main__":
    agent = LocalAgent(model_id="deepseek-ai/deepseek-coder-7b-instruct-v1.5", agent_name="LocalAgent", work_dir="./Case_1")
    agent.setup()
    agent.mount_to_cuda()
    agent.mount_to_cpu()
    print(agent.model.device)