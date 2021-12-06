# Author: przewnic
from PyQt5.QtWidgets import QDialog, QDialogButtonBox,\
                            QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class LoadDialog(QDialog):
    """ Dialog box for loading simulation files. """
    def __init__(self, tram_system, status, *args, **kwargs):
        """ Creates two line edit fields to get paths from user.
            Creates two buttons to accept (and handle) or cancel.
            Sets status read in main window.
        """
        super(LoadDialog, self).__init__(*args, **kwargs)
        self.tram_system = tram_system
        self.status = status
        self.setWindowTitle("Load system")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowSystemMenuHint
                            | Qt.WindowTitleHint)
        dialog_layout = QVBoxLayout()

        dialog_layout.addWidget(QLabel("Enter stations' file path:"))

        self.path_stations = QLineEdit()
        self.path_stations.setPlaceholderText("Enter your text")
        self.path_stations.setText("tram_system_stations.csv")
        dialog_layout.addWidget(self.path_stations)

        dialog_layout.addWidget(QLabel("Enter lines' file path:"))

        self.path_lines = QLineEdit()
        self.path_lines.setPlaceholderText("Enter your text")
        self.path_lines.setText("tram_system_lines.csv")
        dialog_layout.addWidget(self.path_lines)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        dialog_layout.addWidget(buttonBox)

        self.setLayout(dialog_layout)
        self.exec()

    def accept(self):
        """ Reading stations and lines after pressing Ok button. """
        self.tram_system.stations = []
        self.tram_system.lines = []
        try:
            self.tram_system.load_from_file(self.path_stations.text(),
                                            self.path_lines.text())
        except OSError as e:
            error_dialog_box(f"Unable to read file ({e.filename})")
            return -1
        except Exception as e:
            error_dialog_box(e.__str__())
            return -1
        # Add connections bewtween all different stations
        for station in self.tram_system.stations:
            self.tram_system.add_connecionts(station,
                                             self.tram_system.stations)
        self.status.ok = True
        return super().accept()

    def reject(self):
        """ Setting status after pressing Cancel button"""
        self.status.cancel = True
        return super().reject()


def error_dialog_box(message):
    """ Creates new error dialog box
        Args:
            message: Message shown to the user
    """
    dlg = QDialog()
    dlg.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowSystemMenuHint
                       | Qt.WindowTitleHint)
    dlg.setWindowTitle("Error")
    dialog_layout = QVBoxLayout()
    dialog_layout.addWidget(QLabel(message))
    dlg.setLayout(dialog_layout)
    dlg.resize(250, 20)
    dlg.exec_()
