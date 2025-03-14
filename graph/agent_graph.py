from roles import GPTAgent, LocalAgent
from typing import List, Tuple, Union

class AgentGraph(object):
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.current = None

    def add_node(self, node:Union[GPTAgent, LocalAgent]) -> None:
        self.nodes[node.agent_name] = node

    def add_edge(self, src_node:Union[GPTAgent, LocalAgent], dst_node:Union[GPTAgent, LocalAgent]) -> None:
        if src_node.agent_name not in self.edges:
            self.edges[src_node.agent_name] = []
        self.edges[src_node.agent_name].append(dst_node.agent_name)

        src_node.add_next(dst_node)
        dst_node.add_prev(src_node)

    def set_current(self, node:Union[GPTAgent, LocalAgent]) -> None:
        self.current = node

    def root_node(self) -> Union[GPTAgent, LocalAgent]:
        self.current = self.current.prev_nodes[0]

    def next_node(self) -> None:
        if self.current is None:
            return None
        if len(self.current.next_nodes) == 0:
            return None
        next_node = self.current.next_nodes[-1]
        self.current = next_node