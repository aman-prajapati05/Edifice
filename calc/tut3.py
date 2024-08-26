import edifice as ed
from edifice import Button, Label, TextInput, ScrollView, View


b1style = {"width": 100, "height": 100, "font-size": 40,"color":"white","background-color":"grey","border-radius":"50%"}
b2style = {"width": 100, "height": 100, "font-size": 40,"color":"white","background-color":"orange","border-radius":"50%"}
b3style = {"width": 100, "height": 100, "font-size": 40,"color":"white","background-color":"red","border-radius":"50%"}
b4style = {"width": 100, "height": 100, "font-size": 40,"color":"white","background-color":"green","border-radius":"50%"}
class Calculator(ed.Component):
    def __init__(self):
        super().__init__()
        self.text = "0"
        self.first = 0
        self.second = 0
        self.operator = ""
        self.result = 0


    def on_click(self, e):
        if e == "C":
            self.set_state(text="0")
            self.first = 0
            self.second = 0
            self.operator = ""
            self.result = 0
        elif e == "=":
            self.second = int(self.text)
            if self.operator == "+":
                self.result = self.first + self.second
            elif self.operator == "-":
                self.result = self.first - self.second
            elif self.operator == "*":
                self.result = self.first * self.second
            elif self.operator == "/":
                self.result = self.first / self.second
            self.set_state(text=str(self.result))
        elif e in ["+","-","*","/"]:
            self.first = int(self.text)
            self.operator = e
            self.set_state(text="0")
        else:
            if self.text == "0":
                self.set_state(text=e)
            else:
                self.set_state(text=self.text+e)
        
    
  

  


    def render(self):
     
        return View(style={"width": 480, "height": 800, "font-size": 20,"background-color":"black"})(
          
            TextInput(self.text, style={"width": 480, "height": 100, "font-size": 40,"color":"white","align":"right","background-color":"black"},on_change=lambda text:self.set_state(text=text)),
            View(layout="row")(
                Button("1",style= b1style ,on_click=lambda e:self.on_click("1")),
                Button("2",style=b1style,on_click=lambda e:self.on_click("2")),
                Button("3",style=b1style,on_click=lambda e:self.on_click("3")),
                Button("+",style=b2style,on_click=lambda e:self.on_click("+"))
            ),
            View(layout="row")(
                Button("4",style=b1style,on_click=lambda e:self.on_click("4")),
                Button("5",style=b1style,on_click=lambda e:self.on_click("5")),
                Button("6",style=b1style,on_click=lambda e:self.on_click("6")),
                Button("-",style=b2style,on_click=lambda e:self.on_click("-"))
            ),
            View(layout="row")(
                Button("7",style=b1style,on_click=lambda e:self.on_click("7")),
                Button("8",style=b1style,on_click=lambda e:self.on_click("8")),
                Button("9",style=b1style,on_click=lambda e:self.on_click("9")),
                Button("*",style=b2style,on_click=lambda e:self.on_click("*"))
            ),
            View(layout="row")(
                Button("C",style=b3style,on_click=lambda e:self.on_click("C")),
                Button("0",style=b1style,on_click=lambda e:self.on_click("0")),
                Button("=",style=b4style,on_click=lambda e:self.on_click("=")),
                Button("/",style=b2style,on_click=lambda e:self.on_click("/"))
            )

        )
    
ed.App(Calculator()).start()