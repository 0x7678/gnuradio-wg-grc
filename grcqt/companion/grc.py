import logging
from PyQt5 import QtWidgets

# GRC imports
from . import controllers

'''
Main controller for the whole application.
Handles setting up all the child controllers and views and also global actions.
'''
class AppController(object):
    def __init__(self, gp):
        # Note. Logger must have the correct naming convention to share
        # handlers
        self.log = logging.getLogger("grc.app")
        self.log.debug("__init__")

        # Save the global preferences
        self.gp = gp

        # Load the main view class and initialize QMainWindow
        self.log.debug("ARGV - %s" % gp.argv)
        self.log.debug("INSTALL_DIR - %s" % gp.path.INSTALL)

        # Global signals
        self.signals = {}

        self.log.debug("Creating QApplication instance")
        self._app = QtWidgets.QApplication(gp.argv)

        # Need to setup the slots for the QtAction
        self.log.debug("Creating MainWindow controller")
        self.mainwindow = controllers.MainWindow(self, gp)


    def run(self):

        # Show the main window after everything is initialized.
        self.mainwindow.show()

        # Launch the qt app
        return (self._app.exec_())
