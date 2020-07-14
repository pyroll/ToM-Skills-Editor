import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QObject
import yaml

from gui import skillsEdit
from core import feed_info_from_json as json_info
from ntpath import basename

from _skill_growth_mixin import SkillGrowthMixin
from _arts_acquire_mixin import ArtsAcquireMixin
from _signals import Signals


# TODO (low) Have labels more clearly show what class the tp are for
#  ie. 'Warrior' instead of Class 1A for Duran
class MainWindow(SkillGrowthMixin, ArtsAcquireMixin, Signals,
                 skillsEdit.Ui_MainWindow,
                 QMainWindow):
    """
    Main Class; expanded upon with mixins.

    Accesses Ui_MainWindow class to setup up window from our ui file.
    QMainWindow is also required to do this.
    """

    def __init__(self):
        # super(self.__class__, self).__init__()
        super().__init__()

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # MainWindow Setup
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.setupUi(self)

        # Set Window Title
        self.setWindowTitle("ToM Skills Editor")

        # Add icon
        appIcon = QtGui.QIcon("img\\220px-Rabite_Mana.png")
        self.setWindowIcon(appIcon)

        # Disable resizing of window
        self.setFixedSize(766, 612)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Initial data loading from mixins
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Add all list items
        self.addListItems()
        self.addListItems_Arts()

        self.createSkillGrowthVars()
        self.createArtsAcquireVars()

        # Add all signals
        self.menuSignals()
        self.skillGrowthTabSignals()
        self.artsAcquireTabSignals()

        # Variable for holding path to currently loaded config file
        self.currentLoadedConfig = 'temp'

    #
    # ~~~ MENU ACTIONS ~~~
    #
    def newConfigAction(self):
        """Clear edits table(s) and resets to new config file."""
        # Clear our edits table
        for index, char in self.tabIndexToChar.items():
            currentTree = self.editsTree.topLevelItem(index)

            root = self.editsTree.invisibleRootItem()
            child_count = root.childCount()
            for i in range(child_count):
                item = root.child(i)
                subChildCount = item.childCount()
                for i in range(subChildCount):
                    # text at first (0) column
                    currentTree.removeChild(item.child(i))

        # Reset current config file variable
        self.currentLoadedConfig = 'temp'

        # Reset label that shows loaded config file
        self.CurrentConfigEditLabel.setText("New config file")

    def saveAction(self):
        """Perform save dialog."""
        # Check if a config file is loaded
        if self.currentLoadedConfig == 'temp':
            # do saveAsAction
            self.saveAsAction()
        else:  # Grab current config file path
            currentConfigFilePath = self.currentLoadedConfig

            # Dump edits tree data to yaml file
            finalEditsDict = self.createFinalEditsDict()

            # Overwrite file
            json_info.saveConfigFile(finalEditsDict, currentConfigFilePath)

    def saveAsAction(self):
        mySaveAs = SaveAsDialogue('Config file Save As...', 'config',
                                  "Config (*.yaml)")

        try:
            savedConfigFilepath = mySaveAs.savedConfigFilepath

            # Dump edits tree data to yaml file
            finalEditsDict = self.createFinalEditsDict()

            json_info.saveConfigFile(finalEditsDict, savedConfigFilepath)

            # Update variable for currently loaded config file
            self.currentLoadedConfig = savedConfigFilepath

            # Update Label that displays currently loaded config file
            baseFilename = basename(savedConfigFilepath)
            self.CurrentConfigEditLabel.setText(baseFilename)

        except FileNotFoundError:
            pass

    def saveAndCreateAction(self):
        # Do saveAction
        self.saveAction()

        # Get finalEdits Dict and create files
        finalEditsDict = self.createFinalEditsDict()

        json_info.createFilesFromEdits(finalEditsDict)

        # Clear out/Create required directories
        json_info.createRequiredDirs('GrowthTable')

        # Process and output the final edited files to ToM_Skills_Edit_P
        json_info.convertEditedJsonToPak()

        NoticeWindow(self.centralwidget,
                     ("Edited files should now be "
                      "located in the 'ToM_Skills_Edit_P' "
                      "folder"))

    def loadIntoEditsTreeAction(self):
        """Open dialogue to choose a config file. Feed filepath and tab
        index dict to loadIntoEditsTree
        """
        # Grab path to config file
        try:
            chooseConfig = OpenDialogue('Choose Config file to load...',
                                        'config',
                                        "Config (*.yaml)")

            configFilePath = chooseConfig.openConfigFilepath

            # Load yaml config file into edits tree
            self.loadIntoEditsTree(configFilePath, self.tabIndexToChar)
        except FileNotFoundError:
            pass

    def loadIntoEditsTree(self, configFilePath, tabIndexDict):
        """Load data from config file and insert into edits tree"""
        with open(configFilePath, 'r') as f:
            configData = yaml.load(f, Loader=yaml.FullLoader)

        #
        # Clear all entries in data tree before loading new data
        #
        for index, char in self.tabIndexToChar.items():
            currentTree = self.editsTree.topLevelItem(index)

        root = self.editsTree.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            subChildCount = item.childCount()
            for i in range(subChildCount):
                # text at first (0) column
                currentTree.removeChild(item.child(i))

        #
        # Start with top level dicts/characters
        #

        # configData is a dict; access skills by 'configData[char]'
        for character in configData:
            # Grab index for inserting data under top level items
            for index, char in tabIndexDict.items():
                if char == character:
                    charIndex = index
                    break
            topLevelToAddTo = self.editsTree.topLevelItem(charIndex)

            # Loop through the skills; each skill is a dict
            for skill in configData[character]:
                skillToAdd = skill

                # Add new skill name
                newSkill = QtWidgets.QTreeWidgetItem(topLevelToAddTo)
                newSkill.setText(0, skillToAdd)

                # Loop through edits in skill
                for edit in configData[character][skill]:
                    # Add children/edits for the skill
                    newEdit = QtWidgets.QTreeWidgetItem(newSkill)
                    newEdit.setText(0, edit)

        # Update variable for currently loaded config file
        self.currentLoadedConfig = configFilePath

        # Update Label that displays currently loaded config file
        baseFilename = basename(configFilePath)
        self.CurrentConfigEditLabel.setText(baseFilename)

    def loadAndCreateAction(self):
        """Bypasses loading data into the edits tree. Grabs the
        filename of the config file and sends it for editing."""
        # Grab path to config file
        chooseConfig = OpenDialogue('Choose Config file to load...', 'config',
                                    "Config (*.yaml)")

        configFilePath = chooseConfig.openConfigFilepath

        # Get dict from config file and send it to feed_info...py
        with open(configFilePath, 'r') as f:
            configData = yaml.load(f, Loader=yaml.FullLoader)

        # json_info.createFilesFromEdits(configData)

        # feed_info...py will work with our dict
        json_info.createFilesFromEdits(configData)

        # Clear out/Create required directories
        json_info.createRequiredDirs('GrowthTable')

        # Process and output the final edited files to ToM_Skills_Edit_P
        json_info.convertEditedJsonToPak()

        NoticeWindow(self.centralwidget,
                     ("Edited files should now be "
                      "located in the 'ToM_Skills_Edit_P' "
                      "folder"))

    def exitProgram(self):
        sys.exit()


class WarningWindow(QtWidgets.QMessageBox):
    """
    Base class for warning popup window.

    Must pass in 'self.centralwidget' as the parent
    parameter since this class can't access it from
    'skillsEdit.py'.
    """
    def __init__(self, parent, warningMessage):
        super().__init__()

        self.parent = parent
        self.warningMessage = warningMessage

        self.window = (QtWidgets.QMessageBox.warning
                       (self.parent, 'Warning', self.warningMessage,
                        QtWidgets.QMessageBox.StandardButton.Ok,
                        QtWidgets.QMessageBox.StandardButton.NoButton))


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


class SaveAsDialogue(QtWidgets.QFileDialog, QObject):
    def __init__(self, caption, directory, filter):
        super().__init__()

        self.caption = caption
        self.directory = directory
        self.filter = filter

        self.dialog = QtWidgets.QFileDialog(self)

        # Returns a tuple; filepath is index 0
        self.savedConfig = (self.dialog.getSaveFileName
                            (self, QObject.tr(self, caption),
                             QObject.tr(self, directory),
                             QObject.tr(self, filter)))

        self.savedConfigFilepath = self.savedConfig[0]


class OpenDialogue(QtWidgets.QFileDialog, QObject):
    def __init__(self, caption, directory, filter):
        super().__init__()

        self.caption = caption
        self.directory = directory
        self.filter = filter

        self.dialog = QtWidgets.QFileDialog(self)

        # Returns a tuple; filepath is index 0
        self.openConfig = (self.dialog.getOpenFileName
                           (self, QObject.tr(self, caption),
                            QObject.tr(self, directory),
                            QObject.tr(self, filter)))

        self.openConfigFilepath = self.openConfig[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
