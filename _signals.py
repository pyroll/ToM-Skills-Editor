from PySide2 import QtGui


class Signals:
    def menuSignals(self):
        # Connect Remove Selection button for removing edited skills
        (self.removeSelectionBtn.clicked.connect(self.removeEdit))

        # Connect action for making a new edit file
        # TODO Ask if user wants to save before opening new file
        (self.actionNew_Config_File.triggered.connect
         (self.newConfigAction))

        # Connect create without saving action (same as FINISH)
        (self.actionCreate_edited_files.triggered.connect
         (self.processGrowthTableEdits))

        # Connect Save action to save current config file
        # TODO NoticeWindow when saving is complete
        (self.actionSave.triggered.connect
         (self.saveAction))
        # Add shortcut
        self.actionSave.setShortcut(QtGui.QKeySequence("Ctrl+s"))

        # Connect FINISH button for edited json files from edits
        (self.FINISHbtn.clicked.connect
         (self.processGrowthTableEdits))

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

    def skillGrowthTabSignals(self):
        # Signal for skill selection change
        (self.currentQList.itemSelectionChanged.connect
            (self.loadDataOnSelection))

        # Update the above info for each tab change
        (self.SkillGrowthCharTabs.currentChanged.connect
            (self.updateCurrentTab))

        # Connect Save Edits button to add edit to edit list
        (self.SaveEditsBtn.clicked.connect
            (self.addToEditTree))
