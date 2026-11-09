import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mplfx import Ui_MainWindow  # reemplazar con el archivo py de la interfaz
import numpy as np

# requiere numpy, matplotlib y pyside6
# hola
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # dibuja los widgets
        self.line = None
        self.ui.actualizar_btn.clicked.connect(self.actualizar)
        self.ui.ypos_ui.valueChanged.connect(self.actualizar_linea)
        self.ui.guardar_btn.clicked.connect(self.guardar)

    def guardar(self):
        ruta, _ = QFileDialog.getSaveFileName(self, 'Guardar gráfico', 'grafico.png', 'Imágenes PNG (*.png)')
        
        if ruta:
            self.ui.grafico.figure.savefig(ruta)

    def actualizar_linea(self):
        ax = self.ui.grafico.axes
        canvas = self.ui.grafico.canvas
        ypos = self.ui.ypos_ui.value()
        colortxt = self.ui.combo_color.currentText()
        match(colortxt):
            case 'Rojo':
                color = 'r'
            case 'Azul':
                color = 'b'
            case 'Verde':
                color = 'g'

        if self.line is not None:
            self.line.remove()
        
        self.line = ax.axhline(y=ypos, linestyle = '--', color=color)
        canvas.draw()


    def actualizar(self):
        npuntos = self.ui.npuntos_ui.value()
        fx_seleccionada = self.ui.listafx.currentItem()
        if fx_seleccionada is not None:
            self.funcion = fx_seleccionada.text()
        else:
            self.funcion = 'Seno'



        # ahora prepararemos el vector con la funcion
        x = np.linspace(1, 20, npuntos)
        match(self.funcion):
            case 'Seno':
                y = np.sin(x)
            case 'Coseno':
                y = np.cos(x)
            case 'Log':
                y = np.log(x)

        ax = self.ui.grafico.axes
        canvas = self.ui.grafico.canvas
        if self.ui.limpiar_ui.isChecked():
            ax.clear()
            self.line = None
        
        ax.plot(x,y)
        ax.set_xlabel('Puntos')
        ax.set_ylabel('Amplitud')
        self.actualizar_linea()
        canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
