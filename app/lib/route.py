from PyQt5.QtWidgets import QWidget

class Route:
    name: str
    widget: "Controller"
    index: int
    def __init__(self,name: str, widget: "Controller"):
        self.name = name
        self.widget = widget

    def __str__(self):
        return f" index: {self.index} name: {self.name}, widget: {self.widget}"

    def __repr__(self):
        return self.__str__()
