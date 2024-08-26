
import edifice as ed
from edifice import  Label, View

import multiprocessing

# Function to calculate multiples of a number
def calculate_multiples(number, output_queue):
    multiples = [number * i for i in range(1, 11)]  # Calculate multiples of the number
    output_queue.put(multiples)  # Put the multiples into the output queue

# Component for displaying multiples
@ed.Component
def MultiplesDisplay(multiples):
    with View(layout="column", style={"margin": 10, "align": "top"}):
        Label("Multiples:", style={"font-weight": "bold"})
        # Display multiples as labels
        for multiple in multiples:
            Label(str(multiple), style={"margin-left": 5})

# Main application component
@ed.Component
def App(self):
    # Queue for communicating multiples between processes
    output_queue1 = multiprocessing.Queue()
    output_queue2 = multiprocessing.Queue()

    # Create and start processes to calculate multiples
    process1 = multiprocessing.Process(target=calculate_multiples, args=(2, output_queue1))
    process2 = multiprocessing.Process(target=calculate_multiples, args=(3, output_queue2))
    process1.start()
    process2.start()

    # Wait for processes to finish and retrieve multiples from the queues
    process1.join()
    process2.join()
    multiples1 = output_queue1.get()
    multiples2 = output_queue2.get()

    with View(layout="column", style={"align": "center"}):
        MultiplesDisplay(multiples1)
        MultiplesDisplay(multiples2)


# Main entry point
if __name__ == "__main__":
    ed.App(App()).start()

