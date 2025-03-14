import gc
import json
import os
from uuid import uuid4

import pandas as pd
import torch
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


class BaseAgent(object):
    def __init__(self, agent_name:str, model_id:str, **kwargs) -> None:
        self.model_id = model_id
        # set work directory
        self.work_dir = kwargs.get("work_dir", f"./Case_{uuid4()}")
        self.cache_dir = os.path.join(self.work_dir, "Cache")
        
        # set message cache file
        self.agent_name = agent_name
        self.msg_cache_file = os.path.join(self.cache_dir, self.agent_name + "_msg.jsonl")
        
        # set role cache file
        self.role_cache_file = os.path.join(self.cache_dir, self.agent_name + ".json")

        # set agent status
        self.active = True

        # set connection nodes
        self.prev_nodes = []
        self.next_nodes = []

        # set rag status
        self.rag_enabled = False
    
    def load_knowledge(self, dataset_path:str) -> None:
        df = pd.read_json(dataset_path)
        df_loader = DataFrameLoader(df, page_content_column="requirement")
        df_doc = df_loader.load()
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_db = Chroma.from_documents(documents=df_doc, 
                                               embedding=embeddings, 
                                               persist_directory="chroma_db")
        self.retriever = self.vector_db.as_retriever()

    def retrieve(self, query:str):
        # retrieve top k similar documents to query
        docs = self.retriever.get_relevant_documents(query)
        return docs[:2]

    def combine_prompt(self, c_prompt:dict, combine:bool=True) -> None:
        self.messages.append(c_prompt)
        if combine:
            with open(self.msg_cache_file, 'a') as f:
                f.write(f"{json.dumps(c_prompt)}\n")

    def load_message(self) -> None:
        self.messages = []
        with open(self.msg_cache_file, 'r') as f:
            for line in f:
                self.messages.append(json.loads(line))

    def dump_role_cache(self) -> None:
        with open(self.role_cache_file, 'w') as f:
            json.dump(self.role, f)
    
    def dump_code(self) -> None:
        if "code" in self.role and "filename" in self.role:
            with open(os.path.join(self.work_dir, self.role["filename"]), "w") as f:
                f.write(self.role["code"])

    def dump_files(self) -> None:
        self.dump_role_cache()
        self.dump_code()

    def release(self):
        self.model = None
        self.tokenizer = None
        gc.collect()
        # clear cuda cache
        torch.cuda.empty_cache()