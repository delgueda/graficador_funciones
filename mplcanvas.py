from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # crear una figura y un lienzo (canvas)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        # crea un layout simple
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0) # Remove default padding
        self.setLayout(layout)
        
        # se crea un atajo para los axes
        self.axes = self.figure.add_subplot(111)