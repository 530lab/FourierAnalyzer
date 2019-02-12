from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import pyqtgraph as pg
import sys


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.data_canvas = pg.PlotWidget()
        self.fourier_canvas = pg.PlotWidget()
        layout.addWidget(self.data_canvas)
        layout.addWidget(self.fourier_canvas)
        self.acceptDrops()
        self.show()

    def dropEvent(self, e):
        print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cw = CentralWidget()
    app.exec_()
