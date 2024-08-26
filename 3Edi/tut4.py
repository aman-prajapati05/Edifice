from edifice import Component, StateManager, Button, TextInput,Label
import edifice as ed
from multiprocessing import Process, Queue


def calculate_multiples(number, output_queue):
    """Calculates the multiples of a number and puts them into an output queue.

    Args:
        number: The number to calculate the multiples of.
        output_queue: A queue to put the multiples into.
    """

    multiples = [number * i for i in range(1, 11)]
    output_queue.put(multiples)


class MultipleCalculator(Component):
    def __init__(self):
        self.number1 = StateManager(0)
        self.number2 = StateManager(0)
        self.multiples1 = StateManager([])
        self.multiples2 = StateManager([])

    def render(self):
        return [
            Button("Calculate 1", on_click=self.calculate_multiples1),
            TextInput(value=str(self.number1.get()), on_change=self.number1.set),
            Button("Calculate 2", on_click=self.calculate_multiples2),
            TextInput(value=str(self.number2.get()), on_change=self.number2.set),
            *[Label(f"{m}") for m in self.multiples1.get()],
            *[Label(f"{m}") for m in self.multiples2.get()]
        ]

    def calculate_multiples1(self):
        queue = Queue()
        process = Process(target=calculate_multiples, args=(self.number1.get(), queue))
        process.start()
        self.multiples1.set(queue.get())
        process.join()

    def calculate_multiples2(self):
        # Similar to calculate_multiples1, update self.multiples2
        queue2 = Queue()
        process = Process(target=calculate_multiples, args=(self.number2.get(), queue2))
        process.start()
        self.multiples2.set(queue2.get())
        process.join()




# Create and run the PyEdifice app
# Replace this with integration with PySimpleGUI
app = ed.App(MultipleCalculator())
app.start()
