import edifice as ed
from edifice import Label, View

import multiprocessing

# Function to calculate multiples of a number
def calculate_multiples(number, output_queue):
    multiples = [number * i for i in range(1, 11)]  # Calculate multiples of the number
    print(multiples)
    output_queue.put(multiples)  # Put the multiples into the output queue

# Multiples display component
class MultiplesDisplay(ed.Component):
    def __init__(self, multiples):
        super().__init__()
        self.multiples = multiples

    def render(self):
        return View(layout="column", style={"margin": 10, "align": "top"})(
            Label("Multiples:", style={"font-weight": "bold"}),
            *[Label(str(multiple), style={"margin-left": 5}) for multiple in self.multiples]
        )

# Main application component
class App(ed.Component):
    def __init__(self):
        super().__init__()
        self.multiples1 = []
        self.multiples2 = []

    def on_mount(self):
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

        self.multiples1 = output_queue1.get()
        self.multiples2 = output_queue2.get()

    def render(self):
        return View(layout="column", style={"align": "center"})(
            MultiplesDisplay(self.multiples1),
            MultiplesDisplay(self.multiples2)
        )

# Main entry point
if __name__ == "__main__":
    ed.App(App()).start()

