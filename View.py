# Author: przewnic
from PyQt5.QtWidgets import QWidget, QTabWidget, \
                            QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

# To draw moving Trains
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsRectItem,
    QGraphicsTextItem,
)
from PyQt5.QtGui import QColor


class View():
    def __init__(self, tram_system, msg_label, messages, lock):
        """ Inititation of class variables i.e.
            tabs with labels for lines and tram log
        """
        self.tram_system = tram_system
        self.layouts = []
        self.widgets = []
        self.tabs = QTabWidget()
        self.line_info = {}
        self.label = msg_label
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.messages = messages
        self.lock = lock

        self.tabs_config()
        self.add_graphics()
        self.trams = {}  # Graphic representation of a tram

    def add_graphics(self):
        line_view = QGraphicsView()
        self.scene = QGraphicsScene(line_view)
        self.layout.addWidget(line_view)
        line_view.setScene(self.scene)
        for s in self.tram_system.stations:
            item = QGraphicsRectItem(0, 0, 60, 20)
            item.setPen(QColor(Qt.blue))
            QGraphicsTextItem(s.name, item)
            self.scene.addItem(item)
            item.setPos(s.x, s.y)

    def add_layouts(self):
        """ Adding a horizontal layout for every line in tram system. """
        for line in self.tram_system.lines:
            self.layouts.append(QVBoxLayout())

    def add_widgets(self):
        """ Adding label for every line in tram system"""
        for layout, line in zip(self.layouts, self.tram_system.lines):
            line_label = QLabel(line.info())
            layout.addWidget(line_label)
            self.line_info.update({line: line_label})
            widget = QWidget()
            widget.setLayout(layout)
            self.widgets.append(widget)

    def add_tabs(self):
        """ Adding tabs for every line in tram system """
        for line, widget in zip(self.tram_system.lines, self.widgets):
            self.tabs.addTab(widget, "Linia " + str(line.get_number()))

    def tabs_config(self):
        """ configuration of all gui tabs """
        if self.tram_system.lines is not None:
            self.tabs.addTab(self.widget, "Trams Log")
            self.tabs.setDocumentMode(True)
            self.tabs.setTabPosition(QTabWidget.North)
            self.tabs.setMovable(True)

    def view_config(self):
        """ Configuration of all lines' tabs and labels """
        self.add_layouts()
        self.add_widgets()
        self.add_tabs()
        self.label.setAlignment(Qt.AlignCenter)

    def update(self, new_message=None, tram=None, end=False):
        """ Function used to update informations in gui,
            is used by the trams to send new messages
            after changing state
            Args:
                message: New message to be shown in trams log box
        """
        if new_message is not None:
            if len(self.messages) > 10:
                self.messages.popleft()
            self.messages.append(new_message)
            new_text = f""
            for message in self.messages:
                new_text += message + "\n"
            self.label.setText(new_text)
        if end is False:
            for line in self.line_info:
                self.line_info[line].setText(line.info())

        if tram is not None and end is False:
            self.update_graphics(tram)

    def update_graphics(self, tram):
        """ Update placement of a tram,
            hide if tram is between stations.
            If tram ended shift or stopped delete item.
            Args:
                tram: tram to update
        """
        to_edit_tram = self.trams[tram]
        if tram.current_station is not None:
            to_edit_tram.setVisible(True)
            new_x = tram.get_station(tram.current_station).x
            new_y = tram.get_station(tram.current_station).y+25
            to_edit_tram.setPos(new_x, new_y)
        else:
            to_edit_tram.setVisible(False)
        if tram.end_of_shift is True or tram.stop is True:
            to_edit_tram.setVisible(False)
            self.trams.pop(tram)

    def add_tram_representation(self, tram):
        """ Function to add graphic represetation
            i.e. Rectangle with tram id in it.
            Args:
                tram: tram to update
        """
        item = QGraphicsRectItem(0, 0, 30, 20)
        item.setPen(QColor(Qt.darkRed))
        QGraphicsTextItem(str(tram.tram_id), item)
        item.setVisible(False)
        self.scene.addItem(item)
        self.trams.update({tram: item})

    def update_view(self, msg):
        """ Slot for signals from trams.
            Args:
                msg: message containing informations
                     about change of state of some tram
        """
        self.update(msg[0], msg[1], msg[2])
