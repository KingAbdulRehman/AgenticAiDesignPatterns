from crewai.flow.flow import Flow, listen, start, or_, and_

class AugmentedFlow(Flow):
    @start()
    def input_stage(self):
        """Handles user input before passing it to LLM."""
        print("Receiving Input...")
        return "input_received"

    @listen(input_stage)
    def llm_processing(self):
        """LLM processes the input and interacts with retrieval, tools, and memory."""
        print("Processing input using LLM...")

    @listen(and_(llm_processing))
    def retrieval(self):
        """Handles query and retrieval of results."""
        print("Performing Retrieval for Query/Results...")
        self.callback("R Completed")

    @listen(and_(llm_processing))
    def tools(self):
        """Handles calling external tools for response generation."""
        print("Calling External Tools for Processing...")
        self.callback("T Completed")

    @listen(and_(llm_processing))
    def memory(self):
        """Handles memory read/write operations."""
        print("Reading/Writing Memory for Context...")
        self.callback("M Completed")
    

    @listen(llm_processing)
    def output_stage(self):
        """Handles final output generation after LLM processing is complete."""
        print("Generating Final Output...")

    # Functions to run the flow
def Run():
    obj = AugmentedFlow()
    obj.kickoff()

def Plot():
    obj = AugmentedFlow()
    obj.plot()