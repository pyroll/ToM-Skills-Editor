from PySide2 import QtWidgets


class NoticeWindow(QtWidgets.QMessageBox):
    """
    Base class for notice popup window.

    Must pass in 'self.centralwidget' as the parent
    parameter since this class can't access it from
    'skillsEdit.py'.
    """
    def __init__(self, parent, noticeMessage):
        super().__init__()

        self.parent = parent
        self.noticeMessage = noticeMessage

        self.window = (QtWidgets.QMessageBox.information
                       (self.parent, 'Notice', self.noticeMessage,
                        QtWidgets.QMessageBox.StandardButton.Ok,
                        QtWidgets.QMessageBox.StandardButton.NoButton))

