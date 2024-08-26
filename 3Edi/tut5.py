import edifice as ed
from edifice import Component, StateManager, Button, TextInput, Label

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
        super().__init__()
        self.number1 = StateManager(0)
        self.number2 = StateManager(0)
        self.multiples1 = StateManager([])
        self.multiples2 = StateManager([])

    def render(self):
        return ed.View(layout="column")(
            ed.Button("Calculate 1", on_click=self.calculate_multiples1),
            ed.TextInput(value=str(self.number1.subscribe(self, 'number1')), on_change=self.number1.set),
            ed.Button("Calculate 2", on_click=self.calculate_multiples2),
            ed.TextInput(value=str(self.number2.subscribe(self, 'number2')), on_change=self.number2.set),
            *[ed.Label(f"{m}") for m in self.multiples1.subscribe(self, 'multiples1')],
            *[ed.Label(f"{m}") for m in self.multiples2.subscribe(self, 'multiples2')]
        )

    def calculate_multiples1(self):
        queue = Queue()
        process = Process(target=calculate_multiples, args=(self.number1.subscribe(self, 'number1'), queue))
        process.start()
        self.multiples1.set(queue.get())
        process.join()

    def calculate_multiples2(self):
        queue = Queue()
        process = Process(target=calculate_multiples, args=(self.number2.subscribe(self, 'number2'), queue))
        process.start()
        self.multiples2.set(queue.get())
        process.join()

# Create and run the PyEdifice app
app = ed.App(MultipleCalculator())
app.start()
