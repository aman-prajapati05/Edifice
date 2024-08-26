import multiprocessing
import edifice as ed
from edifice import View, Label, Button, TextInput


def calculate_multiples(number, queue):
    multiples = []
    for i in range(1, 11):
        multiples.append(number * i)
    queue.put(multiples)


class MyView(ed.Component):
 

    def render(self):
        return View()(
            Label("Hello, World!"),
            Button("Click me!"),
            TextInput("Type here!")
        
        )

    
if __name__ == "__main__":
    ed.App(MyView()).start()







