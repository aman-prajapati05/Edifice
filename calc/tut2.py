import edifice

class Timer(edifice.Component):
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.timer = edifice.Timer(lambda: self.set_state(seconds=self.seconds+1))

    def did_mount(self):
        self.timer.start(1000)

    def render(self):
        return edifice.Label(self.seconds, style={"width": 180, "height": 130, "font-size": 20})

edifice.App(Timer()).start()
