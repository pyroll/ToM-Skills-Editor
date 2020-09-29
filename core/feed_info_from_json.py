"""We will read our json files and feed the data to our gui."""

import json
import os
import yaml
import subprocess


def createRequiredDirs(nameForYamlLookup):
    with open('yaml_files\\required-locations.yaml', 'r') as f:
        locationData = yaml.load(f, Loader=yaml.FullLoader)

        for path in locationData[nameForYamlLookup]:
            if os.path.exists(path):
                removeDirContents(path)
            else:
                os.makedirs(path)


def saveConfigFile(finalEditsDict, outputPath):
    """Saves our finalized dict to a yaml file.

    Args:
        finalEditsDict (dict): dict created by createFinalEditsDict which
         stores all of the user's edits.
    """
    with open(outputPath, 'w') as f:
        yaml.dump(finalEditsDict, f)

    # with open('config\\edits-config.yaml', 'r') as f:
    #     finalEditsDict = yaml.load(f, Loader=yaml.Loader)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions for Growth Table Tab
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def CreateGrowthTableDicts():
    """
    Read all relevant json files and store their data in dict.

    Store key and value for each one in 'growthTableDict'.
    """
    # For naming the keys of each file
    namingDict = {
        "Duran": 'pc01',
        "Angela": 'pc02',
        "Kevin": 'pc03',
        "Charlotte": 'pc04',
        "Hawkeye": 'pc05',
        "Riesz": 'pc06'
    }

    # Set up the name of each character and their data in a dict
    for dirs, subdirs, files in os.walk(r'Game_Files\SkillGrowthTable\orig'):
        for file in files:
            if file[-5:] == '.json':
                fullPath = os.path.join(dirs, file)
                with open(fullPath, 'r') as f:
                    data = json.load(f)

                for name, namingVal in namingDict.items():
                    if namingVal in file:
                        keyName = name
                        break

                growthTableDict[keyName] = data


def CreateGrowthTableLists():
    """
    Creates a dict that we'll use to display all available skills.

    This will be displayed in the 'Skill Growth Table' tab for each
    character as a selectable list.
    """
    for key, value in growthTableDict.items():
        tempSkillList = []
        charTable = growthTableDict[key]
        for skill in charTable:
            tempSkillList.append(skill['Key'])

        dictForListingSkills[key] = tempSkillList


def extractSkillData(selectedSkill, character):
    # Gives a list
    characterData = growthTableDict[character]
    # Find the key that has the same value as 'selectedSkill'
    # TODO Can't we just go exactly to the skill we want instead of
    #  using a loop??
    for x in characterData:
        if x["Key"] == selectedSkill:
            skillData = x["Value"]
            break


def grabLinkStatus(currentSkillName, character):
    characterData = growthTableDict[character]
    for x in characterData:
        if x["Key"] == currentSkillName:
            linkValue = (x["Value"]
                         ['EnableLinkSkill_61_'
                          'F6EE9B314A4394A72F2F67B2C65310DC'])
            return linkValue


def checkIfNeedsDisabled(currentSkillName, character):
    characterData = growthTableDict[character]
    for x in characterData:
        if x["Key"] == currentSkillName:
            if (x["Value"]["SkillType_38_96B762CC4"
                           "B4494FD45"
                           "D6499321F74982"]) == "ESkillType::SKILLTYPE_ID":
                return True
            else:
                return False


def grabTPointsRequired(currentSkillName, character):
    characterData = growthTableDict[character]
    for x in characterData:
        if x["Key"] == currentSkillName:
            class1APoints = \
                (x["Value"]['Class_01a_58_29E23F97458CD01D3E039180868B32A7'])
            class2APoints = \
                (x["Value"]['Class_02a_59_FE7A090845639EE407943085EC0AE875'])
            class2BPoints = \
                (x["Value"]['Class_02b_60_B8D8F32A469F6A1813AF34B4276C4670'])
            class3APoints = \
                (x["Value"]['Class_03a_42_9A2C90E8465057F78961C8B563E3A3D7'])
            class3BPoints = \
                (x["Value"]['Class_03b_43_94C718FD4840B20A830D328B9E5351DE'])
            class3CPoints = \
                (x["Value"]['Class_03c_44_F10F6BBD41AFA312F6CDE7AEC57D8832'])
            class3DPoints = \
                (x["Value"]['Class_03d_45_8F1F1C6D41CF26B2DE0FD483850C07BD'])
            class4APoints = \
                (x["Value"]['Class_04a_46_46A415B44B1B9253DC740DB8D5B90325'])
            class4BPoints = \
                (x["Value"]['Class_04b_47_F53FC4FF444F0C1C966ADFB294CCC9FA'])
            class4CPoints = \
                (x["Value"]['Class_04c_48_90FDC90C45B8FF298CC218AE008432D6'])
            class4DPoints = \
                (x["Value"]['Class_04d_49_7F471F484BF33494D5D408BE71CEE839'])

    tPointsList = [class1APoints, class2APoints, class2BPoints, class3APoints,
                   class3BPoints, class3CPoints, class3DPoints, class4APoints,
                   class4BPoints, class4CPoints, class4DPoints]

    return tPointsList


def findCurrentCharacter(tabIndexToChar, currentTabIndex):
    for index, char in tabIndexToChar.items():
        if currentTabIndex == index:
            character = char
            break

    return character


def createFilesFromEdits(finalEditsDict):
    """
    Use finalized dict to edit json data.

    Write the edited data to new json files.

    Args:
        finalEditsDict (dict): dict created by processGrowthTableEdits which
         stores all of the user's edits.
    """
    # Remove old edits
    basePath = r'Game_Files\SkillGrowthTable\edited'

    for file in os.listdir(basePath):
        if file[-4:] == 'json':
            filePath = basePath + "\\" + file
            os.remove(filePath)

    # Dict for character -> orig json file
    charToJsonDict = {
        "Duran": (r"Game_Files\SkillGrowthTable"
                  r"\orig\_pc01_SkillGrowthTable.json"),
        "Angela": (r"Game_Files\SkillGrowthTable"
                   r"\orig\_pc02_SkillGrowthTable.json"),
        "Kevin": (r"Game_Files\SkillGrowthTable"
                  r"\orig\_pc03_SkillGrowthTable.json"),
        "Charlotte": (r"Game_Files\SkillGrowthTable"
                      r"\orig\_pc04_SkillGrowthTable.json"),
        "Hawkeye": (r"Game_Files\SkillGrowthTable"
                    r"\orig\_pc05_SkillGrowthTable.json"),
        "Riesz": (r"Game_Files\SkillGrowthTable"
                  r"\orig\_pc06_SkillGrowthTable.json")
    }

    # Check if any edits were made to SkillGrowthTable files
    #  End function if none were made
    if 'GrowthTable' not in finalEditsDict.keys():
        return

    # Check if output dir exists, if not create it.
    #  Delete old json files beforehand.
    basePath = 'Game_Files\\SkillGrowthTable\\edited\\'
    if not os.path.exists(basePath):
        os.mkdir(basePath)
    else:
        # Delete old json files so they don't get mixed up with new files
        for file in os.listdir(basePath):
            if file[-5:] == '.json':
                filePath = basePath + file
                os.remove(filePath)

    for game_file_type in finalEditsDict.keys():
        if game_file_type == 'GrowthTable':
            for char, edits in finalEditsDict[game_file_type].items():
                # edits is a dict; the key is a skill; the value is a list of
                #  what was edited

                # Open the json file for the char
                with open(charToJsonDict[char], 'r') as f:
                    charJsonData = json.load(f)

                # Access the data for each skill that exists in edits
                for editedSkill in edits.keys():
                    for skill in charJsonData:
                        if skill["Key"] == editedSkill:
                            # jsonSkillToEdit = charJsonData["Value"][editedSkill]
                            for edit in edits[editedSkill]:
                                #
                                # Handle Link Status edit
                                #
                                if edit.startswith('Link Status'):
                                    # Value of link status will be index 1
                                    splitLinkStatus = edit.split(': ')
                                    newLinkStatus = splitLinkStatus[1]

                                    # Change string value to bool value
                                    if newLinkStatus == "True":
                                        newLinkStatus = True
                                    elif newLinkStatus == "False":
                                        newLinkStatus = False

                                    # function to edit json data with new link status
                                    editLinkStatus(charJsonData, newLinkStatus,
                                                   editedSkill)
                                #
                                # Handle Training Points edited
                                #
                                if edit.startswith('Class_'):
                                    editSplit = edit.split(': ')
                                    editPointer = editSplit[0]
                                    newTValue = int(editSplit[1])
                                    editTrainingPoints(charJsonData, editedSkill,
                                                       editPointer, newTValue)
                            break
        else:
            continue

        # After all editing is complete for one character,
        #  write to a new json file in the final location before
        #  it will be paked

        # Write new character data to new json file
        newJsonFilepath = charToJsonDict[char]

        # Get rid of the leading underscore
        newJsonFilename = newJsonFilepath[34:]

        # Write new json
        charFullPath = basePath + newJsonFilename
        with open(charFullPath, 'w') as f:
            json.dump(charJsonData, f, indent=2)


def editLinkStatus(charJsonData, newLinkStatus, editedSkill):
    """Access the json data and edit the link values.

    Args:
        charJsonData (dict): Json data for the character we're editing.
        newLinkStatus (string): What the new link status will be after editing.
        editedSkill (string): The skill being edited.
    """
    for item in charJsonData:
        for k, v in item.items():
            if k == "Key" and v == editedSkill:
                # Change EnableLinkSkill value
                (item["Value"]
                 ["EnableLinkSkill_61_F6EE9B314A4394A72"
                  "F2F67B2C65310DC"]) = newLinkStatus
                # Set LinkSkillCategory equal to SkillCategory
                (item["Value"]
                 ["LinkSkillCategory_52_511DBFF84D2AB8E7"
                  "09A9BAA2793CEC12"]) = (item["Value"]
                                          ["SkillCategory_37_A7"
                                           "8A648640271F01C5AEA8A15D85BE79"])
                # Set LinkSkillType equal to SkillType
                (item["Value"]
                 ["LinkSkillType_53_6F84424E49C6B812D3074"
                  "1AF76A3F27E"]) = (item["Value"]
                                         ["SkillType_38_96B762CC4B4494FD"
                                          "45D6499321F74982"])
                # Change LinkSkillLevel to 1 if new link is true
                if newLinkStatus:
                    (item["Value"]["LinkSkillLevel_54_6BE8"
                                   "36AD4EB5F7276A0A77825B61205E"]) = 1
                break


def editTrainingPoints(charJsonData, editedSkill, editPointer, newTValue):
    # Dict for editing class points
    editsToJsonPointers = {
        "Class_1A": 'Class_01a_58_29E23F97458CD01D3E039180868B32A7',
        "Class_2A": 'Class_02a_59_FE7A090845639EE407943085EC0AE875',
        "Class_2B": 'Class_02b_60_B8D8F32A469F6A1813AF34B4276C4670',
        "Class_3A": 'Class_03a_42_9A2C90E8465057F78961C8B563E3A3D7',
        "Class_3B": 'Class_03b_43_94C718FD4840B20A830D328B9E5351DE',
        "Class_3C": 'Class_03c_44_F10F6BBD41AFA312F6CDE7AEC57D8832',
        "Class_3D": 'Class_03d_45_8F1F1C6D41CF26B2DE0FD483850C07BD',
        "Class_4A": 'Class_04a_46_46A415B44B1B9253DC740DB8D5B90325',
        "Class_4B": 'Class_04b_47_F53FC4FF444F0C1C966ADFB294CCC9FA',
        "Class_4C": 'Class_04c_48_90FDC90C45B8FF298CC218AE008432D6',
        "Class_4D": 'Class_04d_49_7F471F484BF33494D5D408BE71CEE839'
    }

    jsonPointer = editsToJsonPointers[editPointer]

    for item in charJsonData:
        for k, v in item.items():
            if k == "Key" and v == editedSkill:
                (item["Value"][jsonPointer]) = newTValue
                break


def removeDirContents(basePath):
    """Delete old contents so they don't get mixed up with new files.

    [Args]
    basePath (string): Path to the folder you want to delete the contents of.
    """
    for file in os.listdir(basePath):
        filePath = basePath + file
        os.remove(filePath)


# TODO Remove old 'edited' json files before getting here
def convertEditedJsonToPak():
    """Convert Edited Json to bin files."""
    basePath = 'Game_Files\\SkillGrowthTable\\edited\\'

    # Remove old bin files first
    for file in os.listdir(basePath):
        if file[-4:] == '.bin':
            filePath = basePath + file
            os.remove(filePath)

    for file in os.listdir(basePath):
        if file[-5:] == '.json':
            editedJsonPath = basePath + file

            #
            # Call bat file to output bin files
            #

            # ~ Old method before trying to build with --windowed option
            # subprocess.check_output("core\\hold_for_editing "
            #                         "\\UAsset2Json.exe "
            #                         "-tobin -force " + editedJsonPath)

            # Since the app runs with no console, but we need to call a
            #  subprocess that requires one, run subprocess with
            #  required args here
            p = subprocess.Popen(["core\\hold_for_editing\\UAsset2Json.exe",
                                  "-tobin", "-force", editedJsonPath])

            # ~ These are args that some answers in stack exchange mentioned
            #  ~ might be needed. Noting them here just in case
            #  (stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            #  stdin=subprocess.DEVNULL)

            # We have to wait until the subprocess is finished or else the bin
            #  files won't be created in time
            p.wait()

    #
    # Make required fixes to bin files; split and copy them to correct
    #  location after
    #

    # Dict for 2nd uasset size location in uasset file
    secondOffsetDict = {
        'pc01_SkillGrowthTable.bin': {6761: 6765},
        'pc02_SkillGrowthTable.bin': {6246: 6250},
        'pc03_SkillGrowthTable.bin': {6328: 6332},
        'pc04_SkillGrowthTable.bin': {6344: 6348},
        'pc05_SkillGrowthTable.bin': {6312: 6316},
        'pc06_SkillGrowthTable.bin': {6817: 6821},
    }

    # Grab the output path
    with open('yaml_files\\required-locations.yaml', 'r') as f:
        locationData = yaml.load(f, Loader=yaml.FullLoader)

    outputPath = locationData['GrowthTable']

    # Walks through the bin files in the edited dir
    for file in os.listdir(basePath):
        if file[-4:] == '.bin':
            secondOffset = secondOffsetDict[file]
            binFilePath = basePath + file
            fixBinFiles(binFilePath, file, secondOffset, outputPath[0])


def fixBinFiles(binFilePath, binFile, uassetSizeSecondLocation, outputPath):
    # Open and read our bin file
    with open(binFilePath, 'rb') as f:
        binData = f.read()

    # First we'll change the values that denote the uasset file size.
    #  The two offsets the size is located at:
    uassetSizeOffset = [{24: 28}, uassetSizeSecondLocation]

    # Required size of original uasset file in bytes
    correctUassetSizeDict = {
        'pc01_SkillGrowthTable.bin': 6849,
        'pc02_SkillGrowthTable.bin': 6334,
        'pc03_SkillGrowthTable.bin': 6416,
        'pc04_SkillGrowthTable.bin': 6432,
        'pc05_SkillGrowthTable.bin': 6400,
        'pc06_SkillGrowthTable.bin': 6905,
    }

    # The size it needs to be set to in decimal notation
    correctSize = correctUassetSizeDict[binFile]

    # Our loaded data needs to be set to a bytearray in order to be
    #  mutable.
    mutableBytes = bytearray(binData)

    for offset in uassetSizeOffset:
        # Convert our 'correctSize' int to a byte string
        bytesToInsert = correctSize.to_bytes(4, byteorder='little',
                                             signed=True)

        # Insert new byte slice into mutable byte array
        for k, v in offset.items():
            mutableBytes[k:v] = bytesToInsert

    #
    # Our next issue is we need to insert the footer that was lost back
    #  to its original position.
    #
    footerToAdd = bytes.fromhex('FBFFFFFFFFFFFFFFFEFFFFFF')

    # offset to insert footer will be (correct size of uasset - 12 bytes)
    offsetToInsertFooter = (correctSize - 12)

    # Insert our footer at the correct offset location
    mutableBytes[offsetToInsertFooter:offsetToInsertFooter] = footerToAdd

    # Create our soon-to-be two new files by using string slices.
    uassetBytesData = mutableBytes[0:correctSize]
    uexpBytesData = mutableBytes[correctSize:]

    # Get name of file minus the extension
    filenameNoExtension = binFile[:-4]

    # New filepaths
    newUassetFilepath = outputPath + filenameNoExtension + '.uasset'
    newUexpFilepath = outputPath + filenameNoExtension + '.uexp'

    with open(newUassetFilepath, 'wb') as f:
        f.write(uassetBytesData)

    with open(newUexpFilepath, 'wb') as f:
        f.write(uexpBytesData)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions for Arts Acquire Tab
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def CreateGrowthTableDicts_Arts():
    """
    Read all relevant json files and store their data in dict.

    Store key and value for each one in 'growthTableDict'.
    """
    # For naming the keys of each file
    namingDict = {
        "Duran": 'pc01',
        "Angela": 'pc02',
        "Kevin": 'pc03',
        "Charlotte": 'pc04',
        "Hawkeye": 'pc05',
        "Riesz": 'pc06'
    }

    # Set up the name of each character and their data in a dict
    for dirs, subdirs, files in os.walk(r'Game_Files\ArtsAcquireTable\orig'):
        for file in files:
            if file[-5:] == '.json':
                fullPath = os.path.join(dirs, file)
                with open(fullPath, 'r') as f:
                    data = json.load(f)

                for name, namingVal in namingDict.items():
                    if namingVal in file:
                        keyName = name
                        break

                artsAcquireDict[keyName] = data


def CreateGrowthTableLists_Arts():
    """
    Create a dict that we'll use to display all available skills.

    This will be displayed in the 'Skill Growth Table' tab for each
    character as a selectable list.
    """

    for key, value in artsAcquireDict.items():
        tempSkillList = []
        charTable = artsAcquireDict[key]
        for skill in charTable:
            tempSkillList.append(skill['Key'])

        dictForListingSkills_Arts[key] = tempSkillList


def _extractSkillData_Arts(selectedSkill, character):
    # Gives a list
    characterData = artsAcquireDict[character]
    # Find the key that has the same value as 'selectedSkill'
    # TODO Can't we just go exactly to the skill we want instead of
    #  using a loop??
    for x in characterData:
        if x["Key"] == selectedSkill:
            skillData = x["Value"]
            break


def _findCurrentCharacter_Arts(tabIndexToChar, currentTabIndex):
    for index, char in tabIndexToChar.items():
        if currentTabIndex == index:
            character = char
            break

    return character


def _grabStatToAcquireFrom(currentSkillName, character):
    characterData = artsAcquireDict[character]
    for x in characterData:
        if x["Key"] == currentSkillName:
            statValue = (x["Value"]
                         ['StatusType_53_2739322D4A0547FD00759081978EF4F1'])
            return statValue


def _grabTPointsRequired_Arts(currentSkillName, character):
    characterData = artsAcquireDict[character]
    for x in characterData:
        if x["Key"] == currentSkillName:
            class1APoints = \
                (x["Value"]['Class_01a_40_4AA7CDE74AAC33736AA7898D8505F4A9'])
            class2APoints = \
                (x["Value"]['Class_02a_41_A9FD5D344545E989CB4B1794442A1B6F'])
            class2BPoints = \
                (x["Value"]['Class_02b_42_5CE3DD2D4DEECD53A868F2AB6DED3118'])
            class3APoints = \
                (x["Value"]['Class_03a_43_1AB3730E4CFC09AEC814A5A374CE93E0'])
            class3BPoints = \
                (x["Value"]['Class_03b_44_2F159D084E45D6B29788B9A5C7867619'])
            class3CPoints = \
                (x["Value"]['Class_03c_45_55E566EC40EC89F6D05EE3A3697341E9'])
            class3DPoints = \
                (x["Value"]['Class_03d_46_4A3790464BBA35C8EA907BBFAD5041D7'])
            class4APoints = \
                (x["Value"]['Class_04a_47_A1F5132B4021D365310C61BEF80428CE'])
            class4BPoints = \
                (x["Value"]['Class_04b_48_8253184F47B82ACAE943ECACA6996E08'])
            class4CPoints = \
                (x["Value"]['Class_04c_49_75BC8DEF4FAA0DBA36AE679836391F0D'])
            class4DPoints = \
                (x["Value"]['Class_04d_50_1401B69149A59481989D109ACB3D8758'])

    tPointsList = [class1APoints, class2APoints, class2BPoints, class3APoints,
                   class3BPoints, class3CPoints, class3DPoints, class4APoints,
                   class4BPoints, class4CPoints, class4DPoints]

    return tPointsList


def createFilesFromEdits_Arts(finalEditsDict):
    """Takes our finalized dict, uses it to edit json data,
    then writes the edited data to new json files.

    Args:
        finalEditsDict (dict): dict created by processGrowthTableEdits_Arts
        which stores all of the user's edits.
    """

    # Remove old edits
    basePath = r'Game_Files\ArtsAcquireTable\edited'

    for file in os.listdir(basePath):
        if file[-4:] == 'json':
            filePath = basePath + "\\" + file
            os.remove(filePath)

    # Dict for character -> orig json file
    charToJsonDict = {
        "Duran": (r"Game_Files\ArtsAcquireTable"
                  r"\orig\_pc01_ArtsAcquireTable.json"),
        "Angela": (r"Game_Files\ArtsAcquireTable"
                   r"\orig\_pc02_ArtsAcquireTable.json"),
        "Kevin": (r"Game_Files\ArtsAcquireTable"
                  r"\orig\_pc03_ArtsAcquireTable.json"),
        "Charlotte": (r"Game_Files\ArtsAcquireTable"
                      r"\orig\_pc04_ArtsAcquireTable.json"),
        "Hawkeye": (r"Game_Files\ArtsAcquireTable"
                    r"\orig\_pc05_ArtsAcquireTable.json"),
        "Riesz": (r"Game_Files\ArtsAcquireTable"
                  r"\orig\_pc06_ArtsAcquireTable.json")
    }

    # Check if any edits were made to ArtsAcquire Files
    #  End function if none were made
    if 'ArtsAcquireTable' not in finalEditsDict.keys():
        return

    # Check if output dir exists, if not create it.
    #  Delete old json files beforehand.
    basePath = 'Game_Files\\ArtsAcquireTable\\edited\\'
    if not os.path.exists(basePath):
        os.mkdir(basePath)
    else:
        # Delete old json files so they don't get mixed up with new files
        for file in os.listdir(basePath):
            if file[-5:] == '.json':
                filePath = basePath + file
                os.remove(filePath)

    statBoxDict = {
        "EStatusRiseType::STATUS_RISE_OFFENCE": "STR",
        "EStatusRiseType::STATUS_RISE_SPIRIT": "SPR",
        "EStatusRiseType::STATUS_RISE_DEFENCE": "STA",
        "EStatusRiseType::STATUS_RISE_INTEL": "INT",
        "EStatusRiseType::STATUS_RISE_LUCK": "LUCK"
    }

    for game_file_type in finalEditsDict.keys():
        if game_file_type == 'ArtsAcquireTable':
            for char, edits in finalEditsDict[game_file_type].items():
                # edits is a dict; the key is a skill; the value is a list of
                #  what was edited

                # Open the json file for the char
                with open(charToJsonDict[char], 'r') as f:
                    charJsonData = json.load(f)

                # Access the data for each skill that exists in edits
                for editedSkill in edits.keys():
                    for skill in charJsonData:
                        if skill["Key"] == editedSkill:
                            for edit in edits[editedSkill]:
                                #
                                # Handle Status edit
                                #
                                if edit.startswith('Status to level'):
                                    # Value of link status will be index 1
                                    splitStatus = edit.split(': ')

                                    for k, v in statBoxDict.items():
                                        if v == splitStatus[1]:
                                            newStatus = k
                                            break

                                    # function to edit json data with new status
                                    _editStatusToAcquireFrom(charJsonData, newStatus,
                                                             editedSkill)
                                #
                                # Handle Training Points edited
                                #
                                if edit.startswith('Class_'):
                                    editSplit = edit.split(': ')
                                    editPointer = editSplit[0]
                                    newTValue = int(editSplit[1])
                                    _editTrainingPoints_Arts(charJsonData, editedSkill,
                                                             editPointer, newTValue)
                            break

                # After all editing is complete for one character,
                #  write to a new json file in the final location before
                #  it will be paked

                # Write new character data to new json file
                newJsonFilepath = charToJsonDict[char]

                # Get rid of the leading underscore
                newJsonFilename = newJsonFilepath[34:]

                # Write new json
                charFullPath = basePath + newJsonFilename
                with open(charFullPath, 'w') as f:
                    json.dump(charJsonData, f, indent=2)

        else:
            continue


def _editStatusToAcquireFrom(charJsonData, newStatus, editedSkill):
    """Access the json data and edit the status value.

    Args:
        charJsonData (dict): Json data for the character we're editing.
        newLinkStatus (string): What the new status will be after editing.
        editedSkill (string): The skill being edited.
    """
    for item in charJsonData:
        for k, v in item.items():
            if k == "Key" and v == editedSkill:
                # Change StatusType value
                (item["Value"]
                 ["StatusType_53_2739322D4A0547"
                  "FD00759081978EF4F1"]) = newStatus


def _editTrainingPoints_Arts(charJsonData, editedSkill, editPointer,
                             newTValue):
    # Dict for editing class points
    editsToJsonPointers = {
        "Class_1A": 'Class_01a_40_4AA7CDE74AAC33736AA7898D8505F4A9',
        "Class_2A": 'Class_02a_41_A9FD5D344545E989CB4B1794442A1B6F',
        "Class_2B": 'Class_02b_42_5CE3DD2D4DEECD53A868F2AB6DED3118',
        "Class_3A": 'Class_03a_43_1AB3730E4CFC09AEC814A5A374CE93E0',
        "Class_3B": 'Class_03b_44_2F159D084E45D6B29788B9A5C7867619',
        "Class_3C": 'Class_03c_45_55E566EC40EC89F6D05EE3A3697341E9',
        "Class_3D": 'Class_03d_46_4A3790464BBA35C8EA907BBFAD5041D7',
        "Class_4A": 'Class_04a_47_A1F5132B4021D365310C61BEF80428CE',
        "Class_4B": 'Class_04b_48_8253184F47B82ACAE943ECACA6996E08',
        "Class_4C": 'Class_04c_49_75BC8DEF4FAA0DBA36AE679836391F0D',
        "Class_4D": 'Class_04d_50_1401B69149A59481989D109ACB3D8758'
    }

    jsonPointer = editsToJsonPointers[editPointer]

    for item in charJsonData:
        for k, v in item.items():
            if k == "Key" and v == editedSkill:
                (item["Value"][jsonPointer]) = newTValue
                break


def convertEditedJsonToPak_Arts(finalEditsDict):
    """Convert edited Json to bin files."""
    basePath = 'Game_Files\\ArtsAcquireTable\\edited\\'

    # Remove old bin files first
    for file in os.listdir(basePath):
        if file[-4:] == '.bin':
            filePath = basePath + file
            os.remove(filePath)

    for file in os.listdir(basePath):
        if file[-5:] == '.json':
            editedJsonPath = basePath + file

            # Figure out which character's file we're editing
            charEditingDict = {
                'pc01_ArtsAcquireTable.json': 'Duran',
                'pc02_ArtsAcquireTable.json': 'Angela',
                'pc03_ArtsAcquireTable.json': 'Kevin',
                'pc04_ArtsAcquireTable.json': 'Charlotte',
                'pc05_ArtsAcquireTable.json': 'Hawkeye',
                'pc06_ArtsAcquireTable.json': 'Riesz',
            }

            # Get char name
            for filename, char in charEditingDict.items():
                if file == filename:
                    editingChar = char

            # The lists contain all the skills that are already included in
            #  the game file, aka use the non 'newentry' bat file
            dictForBatFileChoosing = {
                'Duran': ['SPR'],
                # For angela we can use the non force bat no matter what
                'Angela': ['STR', 'STA', 'INT', 'SPR', 'LUCK'],
                'Kevin': ['STA', 'SPR'],
                'Charlotte': ['SPR'],
                'Hawkeye': ['INT', 'LUCK', 'SPR'],
                'Riesz': ['SPR', 'INT']
            }

            needToUseNewEntryBat = False
            if editingChar not in finalEditsDict['ArtsAcquireTable'].keys():
                continue
            else:
                for art in finalEditsDict['ArtsAcquireTable'][editingChar]:
                    for edit in (finalEditsDict['ArtsAcquireTable']
                                 [editingChar][art]):
                        if edit.startswith('Status'):
                            statToCheck = edit.split(':')[1]
                            if statToCheck in (dictForBatFileChoosing
                                               [editingChar]):
                                continue
                            else:
                                needToUseNewEntryBat = True
                                break

                if not needToUseNewEntryBat:
                    _runForceBat(editedJsonPath, basePath)
                else:
                    _runNewEntryBat(editedJsonPath, basePath)


def _runForceBat(editedJsonPath, basePath):
    #
    # Call bat file to output bin files
    #

    # Since the app runs with no console, but we need to call a
    #  subprocess that requires one, run subprocess with
    #  required args here
    p = subprocess.Popen(["core\\hold_for_editing\\UAsset2Json.exe",
                          "-tobin", "-force", editedJsonPath])

    # We have to wait until the subprocess is finished or else the bin
    #  files won't be created in time
    p.wait()

    #
    # Make required fixes to bin files; split and copy them to correct
    #  location after
    #

    # Dict for 2nd uasset size location in uasset file
    secondOffsetDict = {
        'pc01_ArtsAcquireTable.bin': {2574: 2578},
        'pc02_ArtsAcquireTable.bin': {3765: 3769},
        'pc03_ArtsAcquireTable.bin': {2105: 2109},
        'pc04_ArtsAcquireTable.bin': {3350: 3354},
        'pc05_ArtsAcquireTable.bin': {3865: 3869},
        'pc06_ArtsAcquireTable.bin': {2663: 2667},
    }

    # Grab the output path
    with open('yaml_files\\required-locations.yaml', 'r') as f:
        locationData = yaml.load(f, Loader=yaml.FullLoader)

    outputPath = locationData['ArtsAcquireTable']

    # Walks through the bin files in the edited dir
    for file in os.listdir(basePath):
        if file[-4:] == '.bin':
            secondOffset = secondOffsetDict[file]
            binFilePath = basePath + file
            _fixBinFiles_Arts(binFilePath, file,
                              secondOffset, outputPath[0])


def _runNewEntryBat(editedJsonPath, basePath):
    # Since the app runs with no console, but we need to call a
    #  subprocess that requires one, run subprocess with
    #  required args here
    p = subprocess.Popen(["core\\hold_for_editing\\UAsset2Json.exe",
                          "-tobin", "-force", "-newentries",
                          editedJsonPath])

    # We have to wait until the subprocess is finished or else the bin
    #  files won't be created in time
    p.wait()

    #
    # Make required fixes to bin files; split and copy them to correct
    #  location after
    #

    # Dict for 2nd uasset size location in uasset file
    secondOffsetDict = {
        'pc01_ArtsAcquireTable.bin': {2574: 2578},
        'pc02_ArtsAcquireTable.bin': {3765: 3769},
        'pc03_ArtsAcquireTable.bin': {2105: 2109},
        'pc04_ArtsAcquireTable.bin': {3350: 3354},
        'pc05_ArtsAcquireTable.bin': {3865: 3869},
        'pc06_ArtsAcquireTable.bin': {2663: 2667},
    }

    # Grab the output path
    with open('yaml_files\\required-locations.yaml', 'r') as f:
        locationData = yaml.load(f, Loader=yaml.FullLoader)

    outputPath = locationData['ArtsAcquireTable']

    # Walks through the bin files in the edited dir
    for file in os.listdir(basePath):
        if file[-4:] == '.bin':
            secondOffset = secondOffsetDict[file]
            binFilePath = basePath + file
            _fixBinFiles_Arts_NewEntries(binFilePath, file,
                                         secondOffset, outputPath[0])


def _fixBinFiles_Arts(binFilePath, binFile, uassetSizeSecondLocation,
                      outputPath):

    # First we'll change the values that denote the uasset file size.
    #  The two offsets the size is located at:
    uassetSizeOffset = [{24: 28}, uassetSizeSecondLocation]

    # Required size of original uasset file in bytes
    correctUassetSizeDict = {
        'pc01_ArtsAcquireTable.bin': 2662,
        'pc02_ArtsAcquireTable.bin': 3853,
        'pc03_ArtsAcquireTable.bin': 2193,
        'pc04_ArtsAcquireTable.bin': 3438,
        'pc05_ArtsAcquireTable.bin': 3953,
        'pc06_ArtsAcquireTable.bin': 2751,
    }

    # The size it needs to be set to in decimal notation
    correctSize = correctUassetSizeDict[binFile]

    # Open and read our bin file
    with open(binFilePath, 'rb') as f:
        binData = f.read()

    # Our loaded data needs to be set to a bytearray in order to be
    #  mutable.
    mutableBytes = bytearray(binData)

    for offset in uassetSizeOffset:
        # Convert our 'correctSize' int to a byte string
        bytesToInsert = correctSize.to_bytes(4, byteorder='little',
                                             signed=True)

        # Insert new byte slice into mutable byte array
        for k, v in offset.items():
            mutableBytes[k:v] = bytesToInsert

    #
    # Our next issue is we need to insert the footer that was lost back
    #  to its original position.
    #
    footerToAdd = bytes.fromhex('FBFFFFFFFFFFFFFFFEFFFFFF')

    # offset to insert footer will be (correct size of uasset - 12 bytes)
    offsetToInsertFooter = (correctSize - 12)

    # Insert our footer at the correct offset location
    mutableBytes[offsetToInsertFooter:offsetToInsertFooter] = footerToAdd

    # Create our soon-to-be two new files by using string slices.
    uassetBytesData = mutableBytes[0:correctSize]
    uexpBytesData = mutableBytes[correctSize:]

    # Get name of file minus the extension
    filenameNoExtension = binFile[:-4]

    # New filepaths
    newUassetFilepath = outputPath + filenameNoExtension + '.uasset'
    newUexpFilepath = outputPath + filenameNoExtension + '.uexp'

    with open(newUassetFilepath, 'wb') as f:
        f.write(uassetBytesData)

    with open(newUexpFilepath, 'wb') as f:
        f.write(uexpBytesData)


def _fixBinFiles_Arts_NewEntries(binFilePath, binFile,
                                 uassetSizeSecondLocation,
                                 outputPath):
    # Open and read our bin file
    with open(binFilePath, 'rb') as f:
        binData = f.read()

    # Our loaded data needs to be set to a bytearray in order to be
    #  mutable.
    mutableBytes = bytearray(binData)

    # Size of uexp file is the same after editing, luckily, so we can
    #  use this for splitting the bin file since we won't know what
    #  the new size of the uasset will be ahead of time
    uexpSizeDict = {
        "pc01_ArtsAcquireTable.uexp": 6919,
        "pc02_ArtsAcquireTable.uexp": 14705,
        "pc03_ArtsAcquireTable.uexp": 3255,
        "pc04_ArtsAcquireTable.uexp": 12873,
        "pc05_ArtsAcquireTable.uexp": 16995,
        "pc06_ArtsAcquireTable.uexp": 7377
    }

    # Get total size of bin file in bytes
    totalBinSize = len(mutableBytes)

    # Name of uexp file
    uexpName = (binFile[:-3]) + 'uexp'

    # Correct size of uasset will be 'total size - uexp size +
    #  size of footer'
    correctSizeForUasset = (totalBinSize - (uexpSizeDict[uexpName])
                            + 12)

    footerToAdd = bytes.fromhex('FBFFFFFFFFFFFFFFFEFFFFFF')

    # offset to insert footer will be (correct size of uasset - 12 bytes)
    offsetToInsertFooter = (correctSizeForUasset - 12)

    # Insert our footer at the correct offset location
    mutableBytes[offsetToInsertFooter:offsetToInsertFooter] = footerToAdd

    # Change size to correct value

    # The two offsets the size is located at:
    uassetSizeOffset = [{24: 28}, {(correctSizeForUasset - 88):
                                   correctSizeForUasset - 84}]

    for offset in uassetSizeOffset:
        # Convert our 'correctSize' int to a byte string
        bytesToInsert = correctSizeForUasset.to_bytes(4, byteorder='little',
                                                      signed=True)

        # Insert new byte slice into mutable byte array
        for k, v in offset.items():
            mutableBytes[k:v] = bytesToInsert

    # Create our soon-to-be two new files by using string slices.
    uassetBytesData = mutableBytes[0:correctSizeForUasset]
    uexpBytesData = mutableBytes[correctSizeForUasset:]

    # Get name of file minus the extension
    filenameNoExtension = binFile[:-4]

    # New filepaths
    newUassetFilepath = outputPath + filenameNoExtension + '.uasset'
    newUexpFilepath = outputPath + filenameNoExtension + '.uexp'

    with open(newUassetFilepath, 'wb') as f:
        f.write(uassetBytesData)

    with open(newUexpFilepath, 'wb') as f:
        f.write(uexpBytesData)


# Dict for
growthTableDict = {}
artsAcquireDict = {}

# List for storing list of skills for each character
dictForListingSkills = {}
dictForListingSkills_Arts = {}

# Function calls
CreateGrowthTableDicts()
CreateGrowthTableLists()

CreateGrowthTableDicts_Arts()
CreateGrowthTableLists_Arts()
