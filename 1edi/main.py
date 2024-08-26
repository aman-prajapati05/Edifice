import edifice as ed
from edifice import Label, TextInput, View

window = View(layout="row")(  # Layout children in a row
    Label("Measurement in meters:"),
    TextInput(""),
    Label("Measurement in feet:"),
)

if __name__ == "__main__":
    app = ed.App(window)
    app.start()
    print("Running app")

