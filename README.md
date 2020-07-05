# ToM Skills Editor Version 0.1

## Usage:
Selecting a skill under a character's tab will display the data on the right side of the
app:

![Update data on selection of skill](https://github.com/pyroll/ToM-Skills-Editor/blob/master/img/img_for_readme/data_on_selection.png)

* Link ability: Set to true to make a link ability.
* Traning Points Required: Set the amount of TP required to unlock for that class of the selected character.

### Editing:
Edits are done on a **per skill** basis. With a skill selected, make all changes you want for that particular skill and then click **Save Edits**.
This will populate the edits tree in the lower left part of the program:

![Adding edits to the edits tree](https://github.com/pyroll/ToM-Skills-Editor/blob/master/img/img_for_readme/add_edit_to_tree.png)

Any changes made to that same skill after saving your edits will overwrite the previous changes. Click **Remove Selection** to remove a
specific edit or a skill entirely from the edits tree. Do this process for every skill you would like to change.

### Saving & Loading config files
Config files can be saved and loaded for convenience. The files are in yaml format and are stored in the config folder of the mod's main directory.
They can be viewed and optionally edited in any text editor of your choice.

When the program is started, you will start with a new config file, which is displayed in the lower right:

![display current config](https://github.com/pyroll/ToM-Skills-Editor/blob/master/img/img_for_readme/display_current_config.png)

If you would like to save your edits for use at a later time, select **Save Config File -> Save** under the File menu. You can also input 'ctrl+s'
as a shortcut. This will bring up a dialog for you to name it and save in the Config folder. Do not save these files anywhere else as the program
won't be able to locate them.

The **Finish** button in the lower left performs **Create Edited Files Without Saving**, which is explained below.

Loading a config file reads the data from it and inserts the edits into the edits tree. You should see the current config file label update in the
lower right as well. Select **Load Config File -> Load Into Edits Tree** to do so. You may use 'ctrl+l' as a shortcut.

## Other Menu options
* **Create Edited Files Without Saving** - Creates final edited files without saving the current edits in the edits tree
* **New Config File** - Clears edits tree as if you had just started up the program
* **Save Config File -> Save As..** - Save current edits to a new file (won't overwrite the currently loaded config file)
* **Save Config File -> Save and Create Edited Files** - Save current edits to a config file and immediately created edited files after
* **Load Config File -> Load and Create Edited Files** - Select a config file to load edits from and immediately created edited files after

### Creating a pak file for the game
Once you've selected to create edited files, the program will show you a notice popup saying that a folder called **ToM_Skills_Edit_P** was created in the mod's main directory. This folder needs to be converted to a pak file to be used as a mod.

Download UnrealPak from this link: https://mega.nz/file/VVlwwCLL#TDBl3WBB2uEHKFhiXpLdynRZ6irUiLW82HmltmoTW8M

Ensure that both 'UnrealPak.exe' AND 'UnrealPak-Without-Compression.bat' are in the same directory. Drag and drop the created **ToM_Skills_Edit_P** folder over 'UnrealPak-Without-Compression.bat'. This should yield **ToM_Skills_Edit_P.pak** in the same location. Ensure that the file size is not 0 kb, as that would indicate an error.

Create a folder named something like '~mod' in Trials of Mana's steam directory if you haven't already. Place **ToM_Skills_Edit_P.pak** in that folder and you should be good to go.

### Oddities/Notes:
- Setting a stat boost such as 'Luck +10' to a link ability will have a strange
    visual effect and doesn't seem to actually apply to status boost to each character.
    So avoid doing this if possible.
- Some skills are unable to be converted to a link ability (the ability to change
    the link status is disabled in the skills editor). The game wasn't nice enough
    to provide a unique id that I need in the game files for some skills, so they
    need to be left as is.
- In some limited testing on a maxed out ng+ save file, edited skills didn't show in the skills list. Perhaps it doesn't update if a character's stat in fully upgraded?

### Future Plans:
- Add ability to change what stat a skill is assigned to
- Add editing for magic/arts
- Add ability to assign mp cost of magic
- Various usability improvements for the app

### *** Final Note - A Request ***
If anyone wants to volunteer to help make the skills more readable, I could use a list of
all the skill names that are shown in game. I used the skill names from the game's files, but
it still isn't clear exactly which skill it's referring to (the Mania difficulty mod has
the same issue). Essentially what I'd need is some kind of txt file that links each skill
name in the skills editor with the English skill name that shows in game.

For example:

    Duran:
    - AttackUp = Strength +5
    - etc.
    - etc.

    Angela:
    - etc.

This is very time consuming as there are likely ~200 skills total, and I don't really have
the resources nor the desire to fix it anytime soon. So if anyone would like to contribute
in this way, feel free to contact me in the discord.
