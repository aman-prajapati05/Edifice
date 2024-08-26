import edifice as ed
from edifice import Button, Label, View

windowS = {"width": 480, "height": 800, "font-size": 20, "background-color": "pink", "align": "center"}
timerS = {"width": 180, "height": 130, "font-size": 60, "color": "red", "background-color": "black", "align": "center"}
b1style = {"width": 100, "height": 100, "font-size": 20, "color": "white", "background-color": "green",
           "border-radius": "50%", "margin": 10}
b2style = {"width": 100, "height": 100, "font-size": 20, "color": "white", "background-color": "orange",
           "border-radius": "50%"}


class Timer(ed.Component):
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.milliseconds = 0
        self.text = "Start"
        self.timer = ed.Timer(lambda: self.update_time())
        self.b1style = b1style 

    def update_time(self):
        self.milliseconds += 1
        if self.milliseconds == 1000:
            self.seconds += 1
            self.milliseconds = 0
        self.set_state()

    def setText(self):
        if self.text == "Start":
            self.text = "Stop"
            self.timer.start(1)  # Update timer interval to 1 millisecond
            self.b1style = {"width": 100, "height": 100, "font-size": 20,
                            "color": "white", "background-color": "red",
                            "border-radius": "50%","margin": 10}
        else:
            self.text = "Start"
            self.b1style = b1style
            self.timer.stop()
        self.set_state()

    def restart(self):
        self.seconds = 0
        self.milliseconds = 0
        self.set_state()

    def render(self):
        return ed.View(style=windowS)(
            Label(f"{self.seconds:02}:{self.milliseconds:03}", style=timerS),  
            ed.View(layout="row")(
                Button("Restart", style=b2style, on_click=lambda e: self.restart()),
                Button(self.text, style=self.b1style, on_click=lambda e: self.setText())
            )
        )


ed.App(Timer()).start()
