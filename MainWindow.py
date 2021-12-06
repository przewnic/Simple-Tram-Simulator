# Author: przewnic

from queue import Empty
from PyQt5.QtWidgets import QAction, QMainWindow, QSpinBox,\
                            QStatusBar, QToolBar, QLabel
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon
from Dialogs import LoadDialog, error_dialog_box
from View import View
from tram_model.Simulation import SystemSimulation
import threading
from collections import deque
ICON_HEIGHT = 16
ICON_WIDTH = 16


class MainWindow(QMainWindow):
    """ Class representing custom window
        with all widgets and reference to tram system"""

    def __init__(self, tram_system, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Trams Simulation")
        self.tram_system = tram_system
        self.view = None
        self.simulation = None
        self.setWindowIcon(QIcon("train.png"))
        self.msg_label = QLabel("Click: Start to start the simulation \n")
        self.messages = deque()
        self.lock = threading.Lock()

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(ICON_HEIGHT, ICON_WIDTH))
        self.addToolBar(toolbar)

        self.nr_of_trams = QSpinBox()
        self.nr_of_trams.setMinimum(1)
        status_tip = "Set number of trams after the start of simulation."
        self.nr_of_trams.setStatusTip(status_tip)
        toolbar.addWidget(self.nr_of_trams)
        self.intervals = QSpinBox()
        status_tip = "Set time delay before running the next tram."
        self.intervals.setStatusTip(status_tip)
        toolbar.addWidget(self.intervals)

        button_action = QAction(QIcon("arrow-transition.png"), "Start", self)
        button_action.setStatusTip("Start simulation")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        button_stop = QAction(QIcon("cross.png"), "Stop", self)
        button_stop.setStatusTip("Stop simulation")
        button_stop.triggered.connect(self.onMyToolBarStopButtonClick)
        toolbar.addAction(button_stop)

        self.line_number = QSpinBox()
        self.line_number.setStatusTip("Set line number to add a tram")
        toolbar.addWidget(self.line_number)

        button_add = QAction(QIcon("plus-button.png"), "Add tram", self)
        button_add.setStatusTip("Add new tram on chosen from the box line")
        button_add.triggered.connect(self.onMyToolBarAddButtonClick)
        toolbar.addAction(button_add)

        button_load = QAction("Load tram system", self)
        button_load.setStatusTip("Load stations and lines from files")
        button_load.triggered.connect(self.onMyToolBarLoadButtonClick)
        toolbar.addAction(button_load)

        self.setStatusBar(QStatusBar(self))

        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.update_view)

    def update_view(self):
        try:
            msg = self.view.msg_queue.get(False)
            self.view.update(msg[0], msg[1])
        except Empty:
            pass

    def onMyToolBarLoadButtonClick(self):
        """ Reaction on pressing Load tram system button
            Reads two files containing stations and lines
            and assings those to tram system
        """
        if len(self.tram_system.trams) != 0:
            message = "Simulation working! \nLoading will stop previous."
            error_dialog_box(message)
        status = LoadStatus()
        LoadDialog(self.tram_system, status)
        if status.ok is True:
            if self.simulation is not None:
                self.simulation.stop_simulation()
            self.view = View(self.tram_system, self.msg_label,
                             self.messages, self.lock)
            self.view.view_config()
            self.setCentralWidget(self.view.tabs)
            status.ok = False
            status.cancel = False
            # self.timer.start()

    def onMyToolBarButtonClick(self):
        """ Reaction on pressing Start button
            If not already working new simulation starts.
        """
        if self.view is None:
            error_dialog_box("Load Simulation!")
        else:
            if len(self.tram_system.trams) != 0:
                message = "Simulation still working! \nEnd previous one!"
                error_dialog_box(message)
            else:
                self.start_simulation()

    def onMyToolBarStopButtonClick(self):
        """ Reaction on pressing Stop button
            The current simulation is stopped
        """
        if self.view is None:
            error_dialog_box("Load Simulation!")
        elif self.simulation is None:
            error_dialog_box("Start Simulation!")
        else:
            self.simulation.stop_simulation()

    def onMyToolBarAddButtonClick(self):
        """ Reaction on pressing Add tram button
            New tram is added if line of given number exists
        """
        if self.view is None:
            error_dialog_box("Load Simulation!")
        elif self.simulation is None:
            error_dialog_box("Start Simulation!")
        else:
            line_number = self.line_number.value() - 1
            lines_count = len(self.tram_system.lines)
            if line_number < 0 or line_number >= lines_count:
                error_dialog_box("Wrong line number!")
            else:
                self.add_tram(self.tram_system.lines[line_number])

    def start_simulation(self):
        """ Starting new simulation """
        intervals = self.intervals.value()
        nr_of_trams = self.nr_of_trams.value()
        self.simulation = SystemSimulation(self.tram_system, self.view,
                                           intervals, nr_of_trams)
        self.simulation.start_simulation()

    def add_tram(self, line):
        """ Adding new tram during simulation
            Args:
                line: on which tram should be added
        """
        if len(self.tram_system.trams) == 0:
            error_dialog_box("Start Simulation!")
        else:
            try:
                self.simulation.add_tram_on_line(line)
            except Exception as e:
                error_dialog_box(e.args[0])


class LoadStatus():
    def __init__(self):
        self.ok = False
        self.cancel = False

    def get_ok(self):
        return self.ok

    def get_cancel(self):
        return self.cancel
