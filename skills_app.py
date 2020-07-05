import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QObject
import yaml

from gui import skillsEdit
from core import feed_info_from_json as json_info
from ntpath import basename

# LATEST COMMIT: add signal for exit & create without save action
# TODO (low) Have labels more clearly show what class the tp are for
#  ie. 'Warrior' instead of Class 1A for Duran
# TODO Unignore all pycache folder :/
class MainWindow(QMainWindow, skillsEdit.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Set Window Title
        self.setWindowTitle("ToM Skills Editor")

        # Add icon
        appIcon = QtGui.QIcon("img\\220px-Rabite_Mana.png")
        self.setWindowIcon(appIcon)

        # Disable resizing of window
        self.setFixedSize(766, 612)

        self.addListItems()

        # Current information of the tab widget at startup
        # This is updated by 'updateCurrentTab' on each tab change
        self.currentTabIndex = 0
        self.currentQWidget = (self.SkillGrowthCharTabs.widget
                               (self.currentTabIndex))
        self.currentQList = (self.currentQWidget.findChild
                             (QtWidgets.QListWidget))

        # Used in functions for finding the currently selected character
        self.tabIndexToChar = {
            0: "Duran",
            1: "Angela",
            2: "Kevin",
            3: "Charlotte",
            4: "Hawkeye",
            5: "Riesz"
        }

        # Variable for holding path to currently loaded config file
        self.currentLoadedConfig = 'temp'

        #
        # ~~~ SIGNALS START ~~~
        #

        # Signal for skill selection change
        (self.currentQList.itemSelectionChanged.connect
            (self.loadDataOnSelection))

        # Update the above info for each tab change
        (self.SkillGrowthCharTabs.currentChanged.connect
            (self.updateCurrentTab))

        # Connect Save Edits button to add edit to edit list
        (self.SaveEditsBtn.clicked.connect(self.addToEditTree))

        # Connect Remove Selection button for removing edited skills
        (self.removeSelectionBtn.clicked.connect(self.removeEdit))

        # Connect FINISH button for edited json files from edits
        (self.FINISHbtn.clicked.connect
         (self.processGrowthTableEdits))

        # Connect create without saving action (same as FINISH)
        (self.actionCreate_edited_files.triggered.connect
         (self.processGrowthTableEdits))

        # Connect action for making a new edit file
        # TODO Ask if user wants to save before opening new file
        (self.actionNew_Config_File.triggered.connect
         (self.newConfigAction))

        # Connect Save action to save current config file
        # TODO NoticeWindow when saving is complete
        (self.actionSave.triggered.connect
         (self.saveAction))
        # Add shortcut
        self.actionSave.setShortcut(QtGui.QKeySequence("Ctrl+s"))

        # Connect Save as... action to save config file
        (self.actionSave_as.triggered.connect
         (self.saveAsAction))

        # Connect Save and create edited files action
        (self.actionSave_and_Create_Edited_Files.triggered.connect
         (self.saveAndCreateAction))

        # Connect Load config action to load a config file
        (self.actionLoad_Config_File_2.triggered.connect
         (self.loadIntoEditsTreeAction))
        # Add shortcut
        self.actionLoad_Config_File_2.setShortcut(QtGui.QKeySequence("Ctrl+l"))

        # Connect Load and create edited files action
        (self.actionLoad_and_Create_Edited_Files.triggered.connect
         (self.loadAndCreateAction))

        # Connect Exit action
        (self.actionExit.triggered.connect
         (self.exitProgram))

        #
        # ~~~ SIGNALS END ~~~
        #

    def addListItems(self):
        widgetDict = {'Duran':  self.DuranListWidget,
                      'Angela': self.AngelaListWidget,
                      'Kevin': self.KevinListWidget,
                      'Charlotte': self.CharloListWidget,
                      'Hawkeye': self.HawkListWidget,
                      'Riesz': self.RieszListWidget
                      }

        for char, varName in widgetDict.items():
            for skill in json_info.dictForListingSkills[char]:
                varName.addItem(skill)

    def updateCurrentTab(self):
        currentTab = self.SkillGrowthCharTabs.currentWidget()

        tabIndex = self.SkillGrowthCharTabs.indexOf(currentTab)
        self.currentTabIndex = tabIndex
        # print("self.currentTabIndex: ", self.currentTabIndex)

        currentQWidget = self.SkillGrowthCharTabs.widget(self.currentTabIndex)
        self.currentQWidget = currentQWidget
        # print("self.currentQWidget: ", self.currentQWidget)

        self.currentQList = (self.currentQWidget.findChild
                             (QtWidgets.QListWidget))
        # print("self.currentQList: ", self.currentQList)

        (self.currentQList.itemSelectionChanged.connect
            (self.loadDataOnSelection))

    def loadDataOnSelection(self):
        # Character name
        character = (json_info.findCurrentCharacter
                     (self.tabIndexToChar, self.currentTabIndex))

        # print(self.currentQList.currentItem().text())
        selectedSkill = self.currentQList.currentItem().text()

        # Get all the data we need to update everything
        json_info.extractSkillData(selectedSkill, character)

        # Update current Skill Name
        currentSkillName = self.currentQList.currentItem().text()
        self.UniqueSkillNameLabel.setText(currentSkillName)

        # Update Link Status
        linkStatus = str(json_info.grabLinkStatus(currentSkillName, character))
        self.IsLinkComboBox.setCurrentText(linkStatus)
        # Check if link status needs to be disabled for this skill
        disabled = json_info.checkIfNeedsDisabled(currentSkillName, character)
        if disabled:
            self.IsLinkComboBox.setEnabled(False)
        else:
            self.IsLinkComboBox.setEnabled(True)

        # Populate Training Points required fields
        tPointsList = (json_info.grabTPointsRequired
                       (currentSkillName, character))

        tPointsDict = {
            self.TPointsLineEdit_1A: str(tPointsList[0]),
            self.TPointsLineEdit_2B: str(tPointsList[1]),
            self.TPointsLineEdit_2A: str(tPointsList[2]),
            self.TPointsLineEdit_3A: str(tPointsList[3]),
            self.TPointsLineEdit_3B: str(tPointsList[4]),
            self.TPointsLineEdit_3C: str(tPointsList[5]),
            self.TPointsLineEdit_3D: str(tPointsList[6]),
            self.TPointsLineEdit_4A: str(tPointsList[7]),
            self.TPointsLineEdit_4B: str(tPointsList[8]),
            self.TPointsLineEdit_4C: str(tPointsList[9]),
            self.TPointsLineEdit_4D: str(tPointsList[10]),
        }

        # So that other functions can access this dict
        self.tPointsDict = tPointsDict

        for LineEdit, pointsVal in tPointsDict.items():
            LineEdit.setText(pointsVal)

    def addToEditTree(self):
        # Grab character name
        character = (json_info.findCurrentCharacter
                     (self.tabIndexToChar, self.currentTabIndex))
        # print(character)

        currentSkillName = self.currentQList.currentItem().text()

        # Original link status
        linkStatus = str(json_info.grabLinkStatus(currentSkillName, character))
        # Check the current link status
        currentLinkStatus = self.IsLinkComboBox.currentText()

        # Get original value of training points for each class
        # TODO (low) Change to list comprehension
        originalTPointsList = []
        for lineEdit, value in self.tPointsDict.items():
            originalTValue = value
            originalTPointsList.append(originalTValue)
        # print(originalTPointsList)
        # Get the potentially updated values of training points for each class
        newTPointsList = []
        for lineEdit in self.tPointsDict.keys():
            newTPointsList.append(lineEdit.text())
        # print(newTPointsList)

        # First we need to ensure that changes were made to the skill

        # MAIN LOOP FOR CHECKING FOR CHANGES #
        changes_made = False
        while not changes_made:
            # Check Link Status
            if currentLinkStatus == linkStatus:
                linkStatusEdited = False
                pass
            else:
                # Signal that current link status be added to edit list
                linkStatusEdited = True
                changes_made = True
                break

            # Check training points for each class
            for index in range(len(originalTPointsList)):
                # print("Index: ", index)
                if originalTPointsList[index] != newTPointsList[index]:
                    changes_made = True

            # Need to break here to stop the While loop
            if changes_made:
                break

            # If no changes found, throw warning window and break loop
            WarningWindow(self.centralwidget,
                          'Please ensure you have made edits before adding to '
                          'Edits list.')
            break

        if changes_made:
            # Figure out which character item to add to
            for index, char in self.tabIndexToChar.items():
                if character == char:
                    indexForAdding = index
                    break
            treeToAddTo = self.editsTree.topLevelItem(indexForAdding)

            # Access all children of top item to see if skill already exists
            childList = self.grabNameOfAllTreeChildren(treeToAddTo)

            if currentSkillName in childList:
                root = self.editsTree.invisibleRootItem()
                child_count = root.childCount()
                for i in range(child_count):
                    item = root.child(i)
                    # To prevent it deleting skills in other character's tree
                    if treeToAddTo.text(0) == item.text(0):
                        subChildCount = item.childCount()
                        for i in range(subChildCount):
                            child = item.child(i)
                            # text at first (0) column
                            if child.text(0) == currentSkillName:
                                treeToAddTo.removeChild(item.child(i))

            # Add new skill name
            newChild_Skill = QtWidgets.QTreeWidgetItem(treeToAddTo)
            newChild_Skill.setText(0, currentSkillName)

            # Check if we're adding new link status
            if linkStatusEdited:
                newChild_Link = QtWidgets.QTreeWidgetItem(newChild_Skill)
                newChild_Link.setText(0, u"Link Status: " + currentLinkStatus)

            # Find out which classes we're adding to edit list
            # Access all lineEdits of TPointsFrame
            lineEditList = [
                self.TPointsLineEdit_1A,
                self.TPointsLineEdit_2A,
                self.TPointsLineEdit_2B,
                self.TPointsLineEdit_3A,
                self.TPointsLineEdit_3B,
                self.TPointsLineEdit_3C,
                self.TPointsLineEdit_3D,
                self.TPointsLineEdit_4A,
                self.TPointsLineEdit_4B,
                self.TPointsLineEdit_4C,
                self.TPointsLineEdit_4D,
            ]

            # List of Class labels
            classLabelList = [
                "Class_1A", "Class_2A", "Class_2B", "Class_3A", "Class_3B",
                "Class_3C", "Class_3D", "Class_4A", "Class_4B", "Class_4C",
                "Class_4D"
            ]

            assert len(lineEditList) == len(originalTPointsList)

            for i in range(len(lineEditList)):
                if int(lineEditList[i].text()) != int(originalTPointsList[i]):
                    newChild_TPoints = (QtWidgets.QTreeWidgetItem
                                        (newChild_Skill))
                    # Access labels for adding to edits list
                    newChild_TPoints.setText(0, classLabelList[i] + ": " +
                                             lineEditList[i].text())

    def grabNameOfAllTreeChildren(self, topLevelItem):
        """
        Create a list of all skills in the toplevelitem provided

        Toplevelitems are the character names
        """
        childList = []

        for childIndex in range(topLevelItem.childCount()):
            childList.append(topLevelItem.child(childIndex).text(0))

        return childList

    def removeEdit(self):
        """Delete current selection in edits tree"""
        # Get current selection in edit list
        currentSelection = self.editsTree.currentItem()
        # Get parent item so we can remove its child
        currentSelectionParent = currentSelection.parent()
        currentSelectionParent.removeChild(currentSelection)

    def createFinalEditsDict(self):
        """Creates finalEditsDict by grabbing info from the edits
        tree."""
        # Our dict that will be used for creating a yaml file
        finalEditsDict = {}

        # Get range of toplevelitems/characters
        for i in range(self.editsTree.topLevelItemCount()):
            charTopLevel = self.editsTree.topLevelItem(i)
            charText = charTopLevel.text(0)
            # Iterate through char's children/skills

            # Skip if no children exist
            if charTopLevel.childCount() == 0:
                continue
            else:
                finalEditsDict[charText] = {}

            for x in range(charTopLevel.childCount()):
                charSkill = charTopLevel.child(x)
                charSkillText = charSkill.text(0)
                finalEditsDict[charText][charSkillText] = []
                # iterate through skill's items
                for y in range(charSkill.childCount()):
                    skillEdit = charSkill.child(y)
                    skillEditText = skillEdit.text(0)
                    (finalEditsDict[charText]
                        [charSkillText].append(skillEditText))

        return finalEditsDict

    def processGrowthTableEdits(self):
        """
        Send finalEditsDict to feed_info...py; it'll be used to
        create edited json files.
        """
        # TODO Make this function easily usable by other functions.
        #  There are 3-4 different actions that all do this process.
        finalEditsDict = self.createFinalEditsDict()

        # feed_info...py will work with our dict
        json_info.createFilesFromEdits(finalEditsDict)

        # Clear out/Create required directories
        json_info.createRequiredDirs('GrowthTable')

        # Process and output the final edited files to ToM_Skills_Edit_P
        json_info.convertEditedJsonToPak()

        NoticeWindow(self.centralwidget,
                     ("Edited files should now be "
                      "located in the 'ToM_Skills_Edit_P' "
                      "folder"))

    #
    # ~~~ MENU ACTIONS ~~~
    #
    def newConfigAction(self):
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
