import sys
import os
import matplotlib.pyplot as plt
import random as rd

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from circuits.tunneling import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(
            os.path.dirname(__file__) + "//widget.ui",
            self,
        )

        # Matplotlib canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.plotLayout.addWidget(self.canvas)

        # Connect buttons
        self.runButton.pressed.connect(self.run_circuit)
        self.saveButton.pressed.connect(self.save_plot)

        self.show()

    def run_circuit(self):
        api_key = str(self.apiKey.text())
        backend_choice = str(self.backendChoice.currentText())
        barrier_strength = float(self.barrierStrength.value())
        shots = int(self.shots.value())

        v = rd.random()  # get a random velocity for the particles
        counts = tunneling_circuit(
            velocity=v,
            api_key=api_key,
            barrier_strength=barrier_strength,
            used_backend=backend_choice,
            shots=shots,
        )

        self.ax.clear()
        self.ax.bar(counts.keys(), counts.values())
        self.ax.set_title(f"Tunneling: v={v:.2f}, barrier={barrier_strength}")
        self.canvas.draw()
        self.counts = counts  # store for saving later

    def save_plot(self):
        """Save the current histogram as PNG or PDF."""
        if not hasattr(self, "counts"):
            QtWidgets.QMessageBox.warning(self, "No Data", "Run the circuit before saving.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Plot",
            "",
            "PNG Files (*.png);;PDF Files (*.pdf)"
        )
        if file_path:
            self.figure.savefig(file_path)


if __name__ == '__main__':
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)
    
    main_window = MainWindow()
    qapp.exec()