from crewai.flow.flow import Flow, start, listen, router, or_, and_

class ParallelizationFlow(Flow):
    @start()
    def In(self):
        print("Start")

    @listen(In)
    def LlmCall1(self):
        print("LlmCall1")

    @listen(In)
    def LlmCall2(self):
        print("LlmCall2")

    @listen(In)
    def LlmCall3(self):
        print("LlmCall3")

    @listen(or_(LlmCall1, LlmCall2, LlmCall3))
    def Aggregator(self):
        print("Aggregator")

    @listen(Aggregator)
    def Out(self):
        print("Out")


def Run():
    flow = ParallelizationFlow()
    flow.kickoff()

def Plot():
    flow = ParallelizationFlow()
    flow.plot() 