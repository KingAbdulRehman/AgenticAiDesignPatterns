from crewai.flow.flow import Flow, start, listen, or_, and_, router # Import necessary modules from crewai

class RouteFlow(Flow): # Define a class RouteFlow that inherits from Flow

    @start() # Decorator to mark the entry point of the flow
    def In(self): # Define the In method
        print("Receiving Input...") # Print a message indicating input reception

    @listen(In) # Decorator to listen to the In method
    def llm_call_router(self): # Define the llm_call_router method
        print("Routing LLM Calls...") # Print a message indicating LLM call routing

    @listen(llm_call_router) # Decorator to listen to the llm_call_router method
    def llm_call_1(self): # Define the llm_call_1 method
        print("Processing in LLM Call 1...") # Print a message indicating processing in LLM Call 1

    @router(and_(llm_call_router)) # Decorator to route based on llm_call_router
    def llm_call_2(self): # Define the llm_call_2 method
        return "Optional Out" # Return a string "Optional Out"

    @router(and_(llm_call_router)) # Decorator to route based on llm_call_router
    def llm_call_3(self): # Define the llm_call_3 method
        return "Optional Out" # Return a string "Optional Out"

    @listen(or_(llm_call_1, "Optional Out")) # Decorator to listen to either llm_call_1 or "Optional Out"
    def Out(self): # Define the Out method
        print("Final Output Generated...") # Print a message indicating final output generation

def Run(): # Define a function Run
    obj = RouteFlow() # Create an instance of RouteFlow
    obj.kickoff() # Start the flow

def Plot(): # Define a function Plot
    obj = RouteFlow() # Create an instance of RouteFlow
    obj.plot() # Plot the flow
