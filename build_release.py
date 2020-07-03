"""
Script to automate creating the zip file to release to Nexus Mods.

PyInstaller is imported and run first with the desired args,
followed by copying files we want to leave visible to the user
with the shutil module.
"""

# TODO Can we generate the spec file inside the 'build_process'
#  directory without breaking stuff?
# TODO Add img icon to .exe
# TODO See if we can hide command prompt
import PyInstaller.__main__
import shutil
import os

# Add mod version to top of README.txt and to the name of
#  the zip file we will soon create
modVersion = "0.1"

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
    # '--scriptname=%s' % 'run_all.py',
    '--distpath=%s' % 'build\\dist',
    '--workpath=%s' % 'build\\build',
    '--onefile',
    # '--specpath=%s' % 'build_process',
    "skills_app.py"
])

# Add files to the dist folder without adding them inside of the exe
filesToCopy = ['README.txt']

for file in filesToCopy:
    shutil.copyfile(file, ('{0}\\' + file).format
                    ('build\\dist'))

# Dirs require a different method for copying
# TODO Do we need to include the venv folder?
sourceDirs = ['config', 'core', 'Game_Files', 'gui',
              'img', 'yaml_files']

# Slight workaround since shutil skips copying the base dir
for dir in sourceDirs:
    if not os.path.exists(dir):
        os.makedirs('build\\dist\\' + dir)
    # 'src=dir' grabs all the files INSIDE dir, but doesn't
    #   copy the folder itself
    shutil.copytree(src=dir, dst=('build\\dist\\' + dir),
                    dirs_exist_ok=True)

# Create a zip file of the dist folder
# For some reason the terminal in VS Code hangs if I try to create the
#  the zip file in 'build\\dist' ??

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
