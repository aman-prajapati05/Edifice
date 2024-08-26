import edifice as ed
from edifice import Button, Label, TextInput, ScrollView, View

windowS = {"width": 480, "height": 800, "font-size": 20, "background-color": "pink", "align": "center"}
timerS = {"width": 180, "height": 130, "font-size": 60, "color": "red", "background-color": "black", "align": "center"}
b1style = {"width": 100, "height": 100, "font-size": 20, "color": "white", "background-color": "green", "border-radius": "50%", "margin": 10}
b2style = {"width": 100, "height": 100, "font-size": 20, "color": "white", "background-color": "orange", "border-radius": "50%"}

class Timer(ed.Component):
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.milliseconds = 0
        self.text = "Start"  # Initialize text for start/stop button

    def setText(self):
        if self.text == "Start":
            self.text = "Stop"
            self.timer = ed.Timer(self.increment_time)  # Use a separate function for time update
            self.timer.start(10)  # Update every 10 milliseconds for smoother display
        else:
            self.text = "Start"
            self.timer.stop()
        self.set_state()

    def increment_time(self):
        self.milliseconds += 10  # Increment milliseconds every 10ms
        if self.milliseconds >= 100:
            self.milliseconds = 0
            self.seconds += 1
        self.set_state()

    def restart(self):
        self.seconds = 0
        self.milliseconds = 0
        self.set_state()

    def render(self):
        # Format time string using f-string for clarity
        time_string = f"{self.seconds}:{self.milliseconds:02d}"  # Pad milliseconds with zeros

        return View(
            style=windowS
        )(
            Label(time_string, style=timerS),
            View(layout="row")(
                Button(self.text, style=b1style, on_click=lambda e: self.setText()),
                Button("Restart", style=b2style, on_click=lambda e: self.restart()),
            ),
        )


ed.App(Timer()).start()
