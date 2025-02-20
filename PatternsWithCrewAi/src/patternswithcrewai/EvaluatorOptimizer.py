from crewai.flow.flow import Flow, start, listen, router, or_, and_ # Import necessary modules
import random # Import the random module

class EvaluatorOptimizerFlow(Flow): # Define a class EvaluatorOptimizerFlow inheriting from Flow
    
    @start() # Decorator to mark the starting point
    def In(self): # Define the In method
        print("Start") # Print "Start"

    @listen(or_(In, "LlmCallGen")) # Decorator to listen to In or "LlmCallGen"
    def LlmCallGenerator(self): # Define the LlmCallGenerator method
        self.state["result"] = random.choice([True, False]) # Randomly choose True or False and store in state

    @router(LlmCallGenerator) # Decorator to route based on LlmCallGenerator
    def LlmCallEvaluator(self): # Define the LlmCallEvaluator method
        if self.state["result"]: # Check if the result in state is True
            return "Accept" # Return "Accept" if True
        else: # Otherwise
            return "LlmCallGen" # Return "LlmCallGen"

    @listen("Accept") # Decorator to listen to "Accept"
    def Output(self): # Define the Output method
        print("Output") # Print "Output"


def Run(): # Define a function Run
    flow = EvaluatorOptimizerFlow() # Create an instance of EvaluatorOptimizerFlow
    flow.kickoff() # Start the flow

def Plot(): # Define a function Plot
    flow = EvaluatorOptimizerFlow() # Create an instance of EvaluatorOptimizerFlow
    flow.plot() # Plot the flow