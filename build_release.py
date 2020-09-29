"""
Script to automate creating the zip file to release to Nexus Mods.

PyInstaller is imported and run first with the desired args,
followed by copying files we want to leave visible to the user
with the shutil module.
"""

# TODO Can we generate the spec file inside the 'build_process'
#  directory without breaking stuff?
import PyInstaller.__main__
import shutil
import os

# Add mod version to top of README.txt and to the name of
#  the zip file we will soon create
modVersion = "0.2"

# Open original readme and use readlines() method
with open('README.txt', 'r') as f:
    readMeData = f.readlines()
    readMeData[0] = "ToM Skills Editor Version " + modVersion + '\n'
# Make new readme and have it overwrite the old one
with open('README.txt', 'w') as f:
    for line in readMeData:
        f.write(line)

# Run PyInstaller from this module; creates 'build' and 'dist' dirs
PyInstaller.__main__.run([
    '--name=%s' % 'ToM_Skills_Editor',
    '--distpath=%s' % 'build\\dist',
    '--workpath=%s' % 'build\\build',
    '--icon=%s' % 'img\\220px-Rabite_Mana.ico',
    '--onefile',
    '--windowed',
    # '--specpath=%s' % 'build_process',
    "skills_app.py"
])

# Add files to the dist folder without adding them inside of the exe
filesToCopy = ['LICENSE.txt', 'README.md', '_arts_acquire_mixin.py',
               '_signals.py', '_skill_growth_mixin.py',
               'OPTIONAL_remove_locked_arts_P.pak']

for file in filesToCopy:
    shutil.copyfile(file, ('{0}\\' + file).format
                    ('build\\dist'))

# Dirs require a different method for copying
sourceDirs = ['config', 'core', 'Game_Files', 'gui',
              'img', 'yaml_files']

# Slight workaround since shutil skips copying the base dir
for dir in sourceDirs:
    if not os.path.exists('build\\dist\\' + dir):
        os.makedirs('build\\dist\\' + dir)
    else:
        # If it exists, we need to delete and then remake it
        #  since copytree doesn't overwrite files
        shutil.rmtree('build\\dist\\' + dir)

        # 'src=dir' grabs all the files INSIDE dir, but doesn't
        #   copy the folder itself
        shutil.copytree(src=dir, dst=('build\\dist\\' + dir))

# We want config folder to be empty in the release, so delete
#  all contents after copying
for file in os.listdir('build\\dist\\config\\'):
    basePath = 'build\\dist\\config\\'
    filePath = basePath + file
    os.remove(filePath)

# Delete __pycache folders
guiPycachePath = "build\\dist\\gui\\__pycache__"
shutil.rmtree(guiPycachePath)

corePycachePath = "build\\dist\\core\\__pycache__"
shutil.rmtree(corePycachePath)

# Remove Edited files if they already exist in dist folder (from debugging)
if os.path.exists(r'build\dist\ToM_Skills_Edit_P'):
    shutil.rmtree(r'build\dist\ToM_Skills_Edit_P')

# Remove zip archive if it already exists in dist folder
if os.path.exists(r'build\dist\ToM_Skills_Editor0.1.zip'):
    shutil.rmtree(r'build\dist\ToM_Skills_Editor0.1.zip')

# Create a zip file of the dist folder
# ~ For some reason the terminal in VS Code hangs if I try to create the
#  ~ the zip file in 'build\\dist' ??

# Where to place the completed zip file
zipPath = 'build\\ToM_Skills_Editor' + modVersion
zipDirName = 'ToM_Skills_Editor' + modVersion
zipDirPath = 'build\\' + zipDirName

# For now it seems easier to temporarily rename the 'dist' folder
#  and just use that as the base directory for archiving
os.rename('build\\dist', zipDirPath)

try:
    shutil.make_archive(base_name=zipPath,
                        format='zip',
                        root_dir='build',
                        base_dir=zipDirName)
# Undo our little renaming scheme if there's an error
except FileNotFoundError:
    os.rename(zipDirPath, 'build\\dist')
    raise Exception

os.rename(zipDirPath, 'build\\dist')
