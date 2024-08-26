import edifice as ed
from edifice import Button, Label, TextInput, ScrollView, View
windowS = {"width": 480, "height": 800, "font-size": 20,"background-color":"pink","align":"center"}
timerS = {"width": 180, "height": 130, "font-size": 60,"color":"red","background-color":"black","align":"center"}
b1style = {"width": 100, "height": 100, "font-size": 20,"color":"white","background-color":"green","border-radius":"50%","margin":10}
b2style = {"width": 100, "height": 100, "font-size": 20,"color":"white","background-color":"orange","border-radius":"50%"}

class Timer(ed.Component):
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.milliseconds = 0
        self.text = "Start"
        self.button_style = b1style  # Store the initial button style
        self.timer = ed.Timer(lambda: self.update_time())

    def update_time(self):
        self.milliseconds += 1
        if self.milliseconds == 1000:
            self.seconds += 1
            self.milliseconds = 0
        self.set_state()

    def toggle_button_color(self):
        if self.text == "Start":
            self.button_style = {"width": 100, "height": 100, "font-size": 20,
                                 "color": "white", "background-color": "red",
                                 "border-radius": "50%"}
        else:
            self.button_style = {"width": 100, "height": 100, "font-size": 20,
                                 "color": "white", "background-color": "green",
                                 "border-radius": "50%"}
        self.set_state()

    def setText(self):
        if self.text == "Start":
            self.text = "Stop"
            self.toggle_button_color()
            self.timer.start(10)  # Start timer with 10 milliseconds interval
        else:
            self.text = "Start"
            self.toggle_button_color()
            self.timer.stop()
        self.set_state()

    def restart(self):
        self.seconds = 0
        self.milliseconds = 0
        self.set_state()

    def render(self):
        return View(
            style=windowS
        )(Label(f"{self.milliseconds:03}", style=timerS),  # Format time as mm:ss:ms

            View(layout="row")(
                Button(self.text, style=self.button_style, on_click=lambda e: self.setText()),
                Button("Restart", style=b2style, on_click=lambda e: self.restart()))
        )


ed.App(Timer()).start()

