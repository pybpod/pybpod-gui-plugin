#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

if conf.PYFORMS_USE_QT5:
    from PyQt5.QtWidgets import QMessageBox
else:
    from PyQt4.QtGui import QMessageBox

import pyforms
from pyforms import BaseWidget

import logging

logger = logging.getLogger(__name__)

try:
    from pyforms.controls import ControlCodeEditor
except:
    logger.error("Could not import ControlCodeEditor. Is QScintilla installed?")


class CodeEditor(BaseWidget):
    def __init__(self, task):
        BaseWidget.__init__(self, task.name if task else '')

        self.layout().setContentsMargins(5, 5, 5, 5)

        self._code = ControlCodeEditor()
        self._code.value = task.code

        self.task = task
        self._code.changed_event = self.__code_changed_evt

    def __code_changed_evt(self):
        """
        if self.task.filepath is None:
            filepath = QFileDialog.getSaveFileName(self.form, "Save file")
            if filepath:
                self.task.filepath = str(filepath)
            else:
                return False
        """
        self.task.code = self._code.value
        return True

    def beforeClose(self):
        """ 
        Before closing window, ask user if she wants to save (if there are changes)
        
        .. seealso::
            :py:meth:`pyforms.gui.Controls.ControlMdiArea.ControlMdiArea._subWindowClosed`.
        
        """
        if self._code.is_modified:
            reply = QMessageBox.question(self, 'Save the changes', 'Save the file',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                self.__code_changed_evt()

    @property
    def title(self):
        return BaseWidget.title.fget(self)

    @title.setter
    def title(self, value):
        BaseWidget.title.fset(self, "{0} task editor".format(value))


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(CodeEditor)
