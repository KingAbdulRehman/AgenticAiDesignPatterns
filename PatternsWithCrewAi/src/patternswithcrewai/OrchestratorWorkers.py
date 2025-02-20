from crewai.flow.flow import Flow, listen, start, and_, or_, router
import random

class OrchestratorWorkersFlow(Flow):
    @start()
    def In(self):
        print("Input...")
        return "Input"
    
    @router(In)
    def Orchestrator(self):
        llm = ["LLM_call_1", "LLM_call_2","LLM_call_3"]
        self.llm = random.choice(llm)
        if self.llm == "LLM_call_1":
            return 'LLM_call_1'
        if self.llm == "LLM_call_2":
            return 'LLM_call_2'
        if self.llm == "LLM_call_3":
            return 'LLM_call_3'
    
    @listen('LLM_call_1')
    def llm_call_1(self):
        print("LLM Call 1...")
    @listen('LLM_call_2')
    def llm_call_2(self):
        print("LLM Call 2...")
    @listen('LLM_call_3')
    def llm_call_3(self):
        print("LLM Call 3...")
    
    @listen(or_("llm_call_1", "llm_call_2", "llm_call_3"))
    def Synthesizer(self):
        llm_calls =["LLM_Call_1", "LLM_Call_2", "LLM_Call_3"]
        selected_call = random.choice(llm_calls)
        print(f"Routing to: (selected_call)")
        return selected_call
    
    @listen(and_("llm_call_1", "llm_call_2", "llm_call_3"))
    def Synthesizer(self):
        print("Synthesizer")
    
    @listen("Synthesizer")
    def Out(self):
        print("Generating final output...")

def Run():
    """start the flow"""
    obj = OrchestratorWorkersFlow()
    obj.kickoff()

def Plot():
    """plot the flow"""
    obj = OrchestratorWorkersFlow()
    obj.plot()