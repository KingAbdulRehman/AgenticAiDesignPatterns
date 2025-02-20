from crewai.flow.flow import Flow, listen, start, or_, and_, router

class AgentFlow(Flow):
    
    @start()
    def Human(self):
        print("Start")

    @listen(or_(Human, "Env Method"))
    def llm_call(self):
        print("something")
    
    @router(llm_call)
    def Environment(self):
        return "Env Method"

    @listen(and_(llm_call))
    def Stop(self):
        print("stop")
    

def Run():
    obj = AgentFlow()
    obj.kickoff()

def Plot():
    obj = AgentFlow()
    obj.plot()