import logging

from PySide2 import QtWidgets
from core import feed_info_from_json as json_info


class ArtsAcquireMixin(object):
    # def __init__(self):
    #     super().__init__()

    #     self.testVar_art = 'art hello'

    def createArtsAcquireVars(self):
        """ Current information of the tab widget at startup
        This is updated by 'updateCurrentTab' on each tab change"""
        self.currentTabIndex_Arts = 0
        self.currentQWidget_Arts = (self.ArtsAcquireCharTabs.widget
                                    (self.currentTabIndex_Arts))
        self.currentQList_Arts = (self.currentQWidget_Arts.findChild
                                  (QtWidgets.QListWidget))

        # Used in functions for finding the currently selected character
        self.tabIndexToChar_Arts = {
            0: "Duran",
            1: "Angela",
            2: "Kevin",
            3: "Charlotte",
            4: "Hawkeye",
            5: "Riesz"
        }

    def addListItems_Arts(self):
        widgetDict = {'Duran':  self.DuranListWidget_2,
                      'Angela': self.AngelaListWidget_2,
                      'Kevin': self.KevinListWidget_2,
                      'Charlotte': self.CharloListWidget_2,
                      'Hawkeye': self.HawkListWidget_2,
                      'Riesz': self.RieszListWidget_2
                      }

        for char, varName in widgetDict.items():
            for skill in json_info.dictForListingSkills_Arts[char]:
                varName.addItem(skill)

    def updateCurrentTab_Arts(self):
        currentTab = self.ArtsAcquireCharTabs.currentWidget()

        tabIndex = self.ArtsAcquireCharTabs.indexOf(currentTab)
        self.currentTabIndex_Arts = tabIndex

        currentQWidget = (self.ArtsAcquireCharTabs.widget
                          (self.currentTabIndex_Arts))

        self.currentQWidget_Arts = currentQWidget

        self.currentQList_Arts = (self.currentQWidget_Arts.findChild
                                  (QtWidgets.QListWidget))

        (self.currentQList_Arts.itemSelectionChanged.connect
         (self.loadDataOnSelection_Arts))

        self.logger.debug(f'CurrentQList_Arts: {self.currentQList_Arts}')

    def loadDataOnSelection_Arts(self):
        # Character name
        character = (json_info._findCurrentCharacter_Arts
                     (self.tabIndexToChar_Arts, self.currentTabIndex_Arts))

        selectedSkill = self.currentQList_Arts.currentItem().text()

        # Get all the data we need to update everything
        json_info._extractSkillData_Arts(selectedSkill, character)

        # Update current Skill Name
        currentSkillName = self.currentQList_Arts.currentItem().text()
        self.UniqueArtLabel.setText(currentSkillName)

        # Update 'Stat To Acquire From'
        statToAcquireFrom = str(json_info._grabStatToAcquireFrom
                                (currentSkillName, character))

        # dict for matching 'statToAcquireFrom' to combobox text
        statBoxDict = {
            "EStatusRiseType::STATUS_RISE_SPIRIT": "SPR",
            "EStatusRiseType::STATUS_RISE_OFFENCE": "STR",
            "EStatusRiseType::STATUS_RISE_DEFENCE": "STA",
            "EStatusRiseType::STATUS_RISE_INTEL": "INT",
            "EStatusRiseType::STATUS_RISE_LUCK": "LUCK"
        }

        # For other functions to access
        self.statBoxDict = statBoxDict

        for statValue, textValue in statBoxDict.items():
            if statToAcquireFrom == statValue:
                self.StatAcquireComboBox.setCurrentText(textValue)

        # Populate Training Points required fields
        tPointsList = (json_info._grabTPointsRequired_Arts
                       (currentSkillName, character))

        tPointsDict = {
            self.TPointsLineEdit_1A_2: str(tPointsList[0]),
            self.TPointsLineEdit_2A_2: str(tPointsList[1]),
            self.TPointsLineEdit_2B_2: str(tPointsList[2]),
            self.TPointsLineEdit_3A_2: str(tPointsList[3]),
            self.TPointsLineEdit_3B_2: str(tPointsList[4]),
            self.TPointsLineEdit_3C_2: str(tPointsList[5]),
            self.TPointsLineEdit_3D_2: str(tPointsList[6]),
            self.TPointsLineEdit_4A_2: str(tPointsList[7]),
            self.TPointsLineEdit_4B_2: str(tPointsList[8]),
            self.TPointsLineEdit_4C_2: str(tPointsList[9]),
            self.TPointsLineEdit_4D_2: str(tPointsList[10]),
        }

        # So that other functions can access this dict
        self.tPointsDict_Arts = tPointsDict

        for LineEdit, pointsVal in tPointsDict.items():
            LineEdit.setText(pointsVal)

    def addToEditTree_Arts(self):
        # Grab character name
        character = (json_info._findCurrentCharacter_Arts
                     (self.tabIndexToChar_Arts, self.currentTabIndex_Arts))

        currentSkillName = self.currentQList_Arts.currentItem().text()

        # Original status value
        statusValue = str(json_info._grabStatToAcquireFrom(currentSkillName,
                                                           character))
        # Check current status value
        currentStatusValue = self.StatAcquireComboBox.currentText()

        # Get original value of training points for each class
        for lineEdit, value in self.tPointsDict_Arts.items():
            originalTPointsList = [value for lineEdit, value
                                   in self.tPointsDict_Arts.items()]
        # Get the potentially updated values of t points
        #  for each class
            newTPointsList = [lineEdit.text() for lineEdit in
                              self.tPointsDict_Arts.keys()]

        #
        # We need to ensure that changes were made to the skill.
        #

        # MAIN LOOP FOR CHECKING FOR CHANGES #
        changes_made = False
        while not changes_made:
            # check stat to acquire from
            forCheckingStatus = [v for k, v in self.statBoxDict.items()
                                 if k == statusValue]

            if currentStatusValue == forCheckingStatus[0]:
                acqStatEdited = False
                pass
            else:
                # Signal that current status be added to edit list
                acqStatEdited = True
                changes_made = True
                break

            # Check training points for each class
            for index in range(len(originalTPointsList)):
                if originalTPointsList[index] != newTPointsList[index]:
                    changes_made = True
                    break

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
            for index, char in self.tabIndexToChar_Arts.items():
                if character == char:
                    indexForAdding = index
                    break
            treeToAddTo = self.ArtsEditTree.topLevelItem(indexForAdding)

        # Access all children of top item to see if skill already exists
            childList = self._grabNameOfAllTreeChildren_Arts(treeToAddTo)

        if currentSkillName in childList:
            root = self.ArtsEditTree.invisibleRootItem()
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

        # Check if we're adding acq status
        if acqStatEdited:
            newChild_Link = QtWidgets.QTreeWidgetItem(newChild_Skill)
            newChild_Link.setText(0, u"Status to level up: "
                                  + currentStatusValue)

        # Find out which classes we're adding to edit list
        # Access all lineEdits of TPointsFrame
        lineEditList = [
            self.TPointsLineEdit_1A_2,
            self.TPointsLineEdit_2A_2,
            self.TPointsLineEdit_2B_2,
            self.TPointsLineEdit_3A_2,
            self.TPointsLineEdit_3B_2,
            self.TPointsLineEdit_3C_2,
            self.TPointsLineEdit_3D_2,
            self.TPointsLineEdit_4A_2,
            self.TPointsLineEdit_4B_2,
            self.TPointsLineEdit_4C_2,
            self.TPointsLineEdit_4D_2,
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

    def _grabNameOfAllTreeChildren_Arts(self, topLevelItem):
        """
        Create a list of all skills in the toplevelitem provided.

        Toplevelitems are the character names
        """
        childList = []

        for childIndex in range(topLevelItem.childCount()):
            childList.append(topLevelItem.child(childIndex).text(0))

        return childList

    def removeEdit_Arts(self):
        """Delete current selection in arts acquire edits tree."""
        # Get current selection in edit list
        currentSelection = self.ArtsEditTree.currentItem()
        # Get parent item so we can remove its child
        currentSelectionParent = currentSelection.parent()
        currentSelectionParent.removeChild(currentSelection)

        logger.debug(f'Arts Edit Removed:\n'
                     f'\tSelection Removed: {currentSelection.text(0)}\n'
                     f'\tSelection Parent: {currentSelectionParent.text(0)}')

    def processGrowthTableEdits_Arts(self):
        """
        Send finalEditsDict to feed_info...py; it'll be used to
        create edited json files.
        """
        # TODO We can probably delete this method

        # feed_info...py will work with our dict
        json_info.createFilesFromEdits_Arts(self.finalEditsDict)

        # Clear out/Create required directories
        json_info.createRequiredDirs('ArtsAcquireTable')

        # Process and output the final edited files to ToM_Skills_Edit_P
        json_info.convertEditedJsonToPak()

    def _createFinalEditsDict_Arts(self):
        """
        Update self.finalEditsDict.

        Grab info from the edits tree.
        """
        self.finalEditsDict["ArtsAcquireTable"] = {}
        tempDict = {}

        # Get range of toplevelitems/characters
        for i in range(self.ArtsEditTree.topLevelItemCount()):
            charTopLevel = self.ArtsEditTree.topLevelItem(i)
            charText = charTopLevel.text(0)
            # Iterate through char's children/skills

            # Skip if no children exist
            if charTopLevel.childCount() == 0:
                continue

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

        self.finalEditsDict["ArtsAcquireTable"] = tempDict


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s: %(name)s: '
                              '%(message)s')

fileHandler = logging.FileHandler('main.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
