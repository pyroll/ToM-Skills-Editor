import logging

from PySide2 import QtWidgets
from core import feed_info_from_json as json_info
# from _dialogues_windows import NoticeWindow


class SkillGrowthMixin(object):
    # def __init__(self):
    #     super().__init__()

    #     self.testVary = 'hello'

    def createSkillGrowthVars(self):
        """ Current information of the tab widget at startup
        This is updated by 'updateCurrentTab' on each tab change"""
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

        currentQWidget = (self.SkillGrowthCharTabs.widget
                          (self.currentTabIndex))

        self.currentQWidget = currentQWidget

        self.currentQList = (self.currentQWidget.findChild
                             (QtWidgets.QListWidget))

        (self.currentQList.itemSelectionChanged.connect
         (self.loadDataOnSelection))

    def loadDataOnSelection(self):
        # Character name
        character = (json_info.findCurrentCharacter
                     (self.tabIndexToChar, self.currentTabIndex))

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
            self.TPointsLineEdit_2A: str(tPointsList[1]),
            self.TPointsLineEdit_2B: str(tPointsList[2]),
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

        logger.info(f'Skill Selected: {character} -'
                    f' {selectedSkill}')

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
            # Get the potentially updated values of training points
            #  for each class
            newTPointsList = []
        for lineEdit in self.tPointsDict.keys():
            newTPointsList.append(lineEdit.text())

        #
        # We need to ensure that changes were made to the skill.
        #

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
            self.WarningWindow(self.centralwidget,
                               'Please ensure you have made edits'
                               'before adding to Edits list.')
            break

        if changes_made:
            # Figure out which character item to add to
            for index, char in self.tabIndexToChar.items():
                if character == char:
                    indexForAdding = index
                    break
            treeToAddTo = self.editsTree.topLevelItem(indexForAdding)

            # Access all children of top item to see if skill already exists
            childList = self._grabNameOfAllTreeChildren(treeToAddTo)

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

    def _grabNameOfAllTreeChildren(self, topLevelItem):
        """
        Create a list of all skills in the toplevelitem provided

        Toplevelitems are the character names
        """
        childList = []

        for childIndex in range(topLevelItem.childCount()):
            childList.append(topLevelItem.child(childIndex).text(0))

        return childList

    def removeEdit(self):
        """Delete current selection in edits tree."""
        # Get current selection in edit list
        currentSelection = self.editsTree.currentItem()
        # Get parent item so we can remove its child
        currentSelectionParent = currentSelection.parent()
        currentSelectionParent.removeChild(currentSelection)

    def _createFinalEditsDict(self):
        """Updates self.finalEditsDict by grabbing info from the edits
        tree."""

        # Get range of toplevelitems/characters
        for i in range(self.editsTree.topLevelItemCount()):
            charTopLevel = self.editsTree.topLevelItem(i)
            charText = charTopLevel.text(0)
            # Iterate through char's children/skills

            # Skip if no children exist
            if charTopLevel.childCount() == 0:
                continue
            else:
                self.finalEditsDict["GrowthTable"] = {}
                tempDict = {}
                tempDict[charText] = {}

            for x in range(charTopLevel.childCount()):
                charSkill = charTopLevel.child(x)
                charSkillText = charSkill.text(0)
                tempDict[charText][charSkillText] = []
                # iterate through skill's items
                for y in range(charSkill.childCount()):
                    skillEdit = charSkill.child(y)
                    skillEditText = skillEdit.text(0)
                    (tempDict[charText]
                        [charSkillText].append(skillEditText))

            self.finalEditsDict["GrowthTable"] = tempDict


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s: %(name)s: '
                              '%(message)s')

fileHandler = logging.FileHandler('main.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
