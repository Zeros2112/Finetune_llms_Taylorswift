from utilities import *

# Function to sample a subset of history for visualization
def sample_history(history):
    # Check if the history list is empty
    if not history:
        return history

    # Calculate the step size for sampling
    step = (len(history) + 99) // 100

    # Return a sampled subset of the history list
    return history[0 : len(history) : step]
