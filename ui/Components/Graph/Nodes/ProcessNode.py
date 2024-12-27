import math
from abc import abstractmethod
from typing import *

import cv2

from cv2 import *

from Dewins.ui.Components.Graph.Nodes.Prototypes.CommonNodeProto import PortOut
from Dewins.ui.NodeGraph import (
    BaseNode, Port
)
from Dewins.ui.Components.Graph.Nodes.Prototypes.ProcessNodeProto import ProcessNodePrototype
from Dewins.ui.Components.Graph.Nodes.widgets.ProcessWidgets import (
    NodeWrapperCountWordsNodeWidget
)
from Dewins.ui.Components.Graph.Nodes.widgets.Processors.TextProcessorWidgets import (
    NodeWrapperCalculatorWidget,
    NodeWrapperTrigCalcWidget,
    NodeWrapperImageTransformWidget
)
from Dewins.backend.file_manager import (File, ImageFile)

class CountWordNode(ProcessNodePrototype):
    __identifier__ = "Processor"
    NODE_NAME = "Word Counter"

    def __init__(self):
        super().__init__()
        self.add_input("Text")
        self.add_output("Int")

        self.node_widget = NodeWrapperCountWordsNodeWidget(self.view)
        self.add_custom_widget(self.node_widget, tab='Custom')

    _last_arg_int: int = 0

    def load_data_from_output_port_for_input(self, port: PortOut) -> Any:
        if port.name() == "Int":
            return self._last_arg_int

    def process(self) -> bool:
        data: str = self.get_data_at_inputs_ports()["Text"]
        self._last_arg_int = len(data.split())
        self.node_widget.custom_widget.count_words_label.setText(f"Count: {self._last_arg_int}")

        return True


class CalculatorNode(ProcessNodePrototype):
    numb1: float = 0.0
    numb2: float = 0.0
    operation_type: str = "sum"

    def __init__(self):
        super().__init__()
        self.add_input('Float 1')
        self.add_input('Float 2')
        self.add_output("Result")
        print("работает")
        self.result = self.numb1 + self.numb2
        self.node_widget = NodeWrapperCalculatorWidget(self.view)
        self.add_custom_widget(self.node_widget, tab="Custom")
        self.node_widget.custom_widget.resultLabel.setText(str(self.result))
        self.node_widget.custom_widget.plusButton.clicked.connect(self.summation)
        self.node_widget.custom_widget.minButton.clicked.connect(self.residal)
        self.node_widget.custom_widget.multButton.clicked.connect(self.multiply)
        self.node_widget.custom_widget.divButton.clicked.connect(self.division)


    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        # if port.name() == "Number":
            return self.result

    def summation(self):
        self.operation_type = "sum"
        self.result = self.numb1 + self.numb2
        self.node_widget.custom_widget.resultLabel.setText(str(self.result))

    def residal(self):
        self.operation_type = "res"
        self.result = self.numb1 - self.numb2
        self.node_widget.custom_widget.resultLabel.setText(str(self.result))

    def multiply(self):
        self.operation_type = "mul"
        self.result = self.numb1 * self.numb2
        self.node_widget.custom_widget.resultLabel.setText(str(self.result))

    def division(self):
        self.operation_type = "div"
        self.result = self.numb1 / self.numb2
        self.node_widget.custom_widget.resultLabel.setText(str(self.result))

    def process(self) -> bool:
        self.numb1 = float(self.get_data_at_inputs_ports()['Float 1'])
        self.numb2 = float(self.get_data_at_inputs_ports()['Float 2'])
        print(self.numb1, self.numb2)
        match self.operation_type:
            case "sum":
                self.result = self.numb1 + self.numb2
            case "res":
                self.result = self.numb1 - self.numb2
            case "mul":
                self.result = self.numb1 * self.numb2
            case "div":
                if self.numb2 != 0.0:
                    self.result = self.numb1/self.numb2
                else:
                    self.node_widget.custom_widget.resultLabel.setText("Делить на ноль нельзя")
            case _:
                print("Всё сломалось, босс")
                self.node_widget.custom_widget.resultLabel.setText("Ошибка!")
        return True


class TrigCalcNode(ProcessNodePrototype):
    angle: Any = 0.0
    degrees: bool = True


    def __init__(self):
        super().__init__()
        self.add_input('Angle')
        self.add_output("Result")
        self.result = math.sin(self.angle)
        self.node_widget = NodeWrapperTrigCalcWidget(self.view)
        self.add_custom_widget(self.node_widget, tab="Custom")

        self.node_widget.custom_widget.sinButton.clicked.connect(self.sinCount)
        self.node_widget.custom_widget.cosButton.clicked.connect(self.cosCount)
        self.node_widget.custom_widget.tanButton.clicked.connect(self.tanCount)
        self.node_widget.custom_widget.cotanButton.clicked.connect(self.cotanCount)
        self.node_widget.custom_widget.degreeButton.clicked.connect(self.rad2degr)
        self.node_widget.custom_widget.radianButton.clicked.connect(self.degr2rad)

    type_calculation: str = "sin"

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        if port.name() == "Result":
            return self.node_widget.custom_widget.resultLabel.text()

    def sinCount(self):
        self.type_calculation = "sin"

    def cosCount(self):
        self.type_calculation = "cos"

    def tanCount(self):
        self.type_calculation = "tan"

    def cotanCount(self):
        self.type_calculation = "cotan"

    def degr2rad(self):
        self.degrees = False

    def rad2degr(self):
        self.degrees = True

    def process(self) -> bool:
        self.angle = float(self.get_data_at_inputs_ports()['Angle'])
        match self.type_calculation:
            case "sin":
                self.result = math.degrees(math.sin(self.angle)) if self.degrees else math.sin(self.angle)
            case "cos":
                self.result = math.degrees(math.cos(self.angle)) if self.degrees else math.cos(self.angle)
            case "tan":
                self.result = math.degrees(math.tan(self.angle)) if self.degrees else math.tan(self.angle)
            case "cotan":
                self.result = math.degrees(math.tan(self.angle)**(-1)) if self.degrees else math.sin(self.angle)**(-1)
            case _:
                print("Ну, что сказать... Ошибка")
                self.node_widget.custom_widget.resultLabel.setText("Ошибка!")
        self.node_widget.custom_widget.resultLabel.setText(str(self.result))
        return True


class ImageTransform(ProcessNodePrototype):
    fileImage: Union[File, ImageFile]
    image: Any
    type: str
    width: int
    height: int
    rotation: int = 0


    def __init__(self):
        super().__init__()
        self.add_input("Image")
        self.add_input("Type")
        self.add_input("Width")
        self.add_input("Height")
        self.add_input("Rotation")
        self.add_output("Image")
        self.node_widget = NodeWrapperImageTransformWidget(self.view)
        self.add_custom_widget(self.node_widget, tab="Custom")
        print("Инициализация")
        self.node_widget.custom_widget.rotationTextEdit.setText(str(self.rotation))
        self.node_widget.custom_widget.rotationTextEdit.textChanged.connect(self.changeRotation)
        self.node_widget.custom_widget.widthTextEdit.textChanged.connect(self.changeWidth)
        self.node_widget.custom_widget.heightTextEdit.textChanged.connect(self.changeHeight)

    def load_data_from_output_port_for_input(self, port: PortOut) -> Optional[Any]:
        return self.image

    @staticmethod
    def rotate_image(image, angle):
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, M, (w, h))

        return rotated_image

    def changeRotation(self):
        self.rotation = int(self.node_widget.custom_widget.rotationTextEdit.Text())
        self.image = self.rotate_image(self.image, self.rotation)

    def resize(self):
        self.image = cv2.resize(self.image, (self.width, self.height))

    def changeWidth(self):
        self.width = int(self.node_widget.custom_widget.widthTextEdit.Text())
        self.resize()

    def changeHeight(self):
        self.height = int(self.node_widget.custom_widget.heightTextEdit.Text())
        self.resize()

    def process(self) -> bool:
        self.fileImage = self.get_data_at_inputs_ports()["Image"]
        self.image = cv2.imread(str(self.fileImage.path))
        self.type = self.get_data_at_inputs_ports()["Type"]
        self.width = self.get_data_at_inputs_ports()["Width"]
        self.height = self.get_data_at_inputs_ports()["Height"]
        self.rotation = self.get_data_at_inputs_ports()["Rotation"]
        self.type = self.get_data_at_inputs_ports()["Type"]

        return True

