import datetime
import edifice
from edifice import Button, Label, TextInput, ScrollView, View

class TodoApp(edifice.Component):
    def __init__(self):
        super().__init__()
        self.items = []
        self.text = ""

    def add_item(self, e):
        if not self.text:
            return
        new_item = dict(text=self.text, id=datetime.datetime.now())
        self.set_state(items=self.items + [new_item])
    def render(self):
        return View(style={"width": 800, "height": 800, "font-size": 20})(
            Label("TODO" , style={"font-size": 40}),
            TodoList(items=self.items),
            View(layout="row")(
                Label("What needs to be done?"),
                TextInput(self.text,
                          on_change=lambda text:self.set_state(text=text)),
                Button(f"Add #{len(self.items)+1}",
                       on_click=self.add_item)
            )
        )


class TodoList(edifice.Component):
    @edifice.register_props
    def __init__(self, items):
        pass

    def render(self):
        return ScrollView()(
            *[Label(f"* {item['text']}").set_key(item['id'])
              for item in self.props.items]
        )

edifice.App(TodoApp()).start()
