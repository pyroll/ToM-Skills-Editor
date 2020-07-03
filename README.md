# ToM Skills Editor Version 0.1

## BASIC USAGE:
Selecting a skill under a character's tab will display the data on the right side of the
app:

![Update data on selection of skill](https://github.com/pyroll/ToM-Skills-Editor/blob/master/img/img_for_readme/data_on_selection.png)

* Link ability: Set to true to make a link ability.
* Traning Points Required: Set the amount of TP required to unlock for that class of the selected character.

### Oddities/Notes:
- Setting a stat boost such as 'Luck +10' to a link ability will have a strange
    visual effect and doesn't seem to actually apply to status boost to each character.
    So avoid doing this if possible.
- Some skills are unable to be converted to a link ability (the ability to change
    the link status is disabled in the skills editor). The game wasn't nice enough
    to provide a unique id that I need in the game files for some skills, so they
    need to be left as is.

### Changelog from previous version:
- 

### Future Plans:
- Add ability to change what stat a skill is assigned to
- Add editing for magic/arts

#### *** Final Note - A Request ***
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
