# Autosave deletion tool


A tool to automatically delete autosaves and previous flight save files from Flight Simulator X and Prepar3D.


**Download** - [Latest version](https://github.com/codemicro/deleteAutosaves/releases/latest)


I accept no responsibility for any files that mistakenly get deleted. 


**Installation** - Extract the entire contents of the zip file to one directory. Open the file `settings.ini`, and change the entries in the `[paths]` section. You can add as many directories to search as you wish. Each line should begin with `dir.x` where `x` is an integer incrementing from one *Ensure that all paths end with a single backslash.* If an entry is not being used, remove it from the settings file.


**Use** - Simply run `deleteAutosaves.exe`, which will permanently delete all files with names containing one or more of the search keys within the specified directories. If logging is enabled, it will create a new directory (if one does not already exist) in the directory containing the program, and will create a log file within this directory each time it is run. When the program has completed, this log file will be opened.
To allow the program to run at startup, add a shortcut to the `.exe` in the directory `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`. Once this has been done, you can enable and disable running the program from: Task manager -> Start-up and looking for `deleteAutosaves.exe`.


**Changing settings** - To enable or disable logging, change the `logging` parameter to 1 or 0 to enable or disable logging respectively.
To change the search parameters, edit the `keys` parameter. You can specify as many or as few search parameters as you want. Ensure they are separated by a single comma and no whitespace. Capitalisation is ignored.


**Example settings file**

```
[DEFAULT]
logging = 1
keys = autosave,previous

[paths]
dir.1 = C:\Users\tom\Documents\Prepar3D v4 Add-ons\FSLabs\A320\PanelState\
dir.2 = D:\Documents\Flight Simulator X Files\
```
