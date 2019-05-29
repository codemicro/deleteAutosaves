# deleteAutosaves


A tool to automatically delete autosaves and previous flight save files from Flight Simulator X and Prepar3D.


**Download** - [Version 1.0](https://github.com/codemicro/deleteAutosaves/releases/download/v1.0/deleteAutosaves.zip)


I accept no responsibility for any files that mistakenly get deleted. 


**Installation** - Extract the entire contents of the zip file to one directory. Open the file `settings.ini`, and change the entries in the `[paths]` section. You can add as many directories to search as you wish. Each line should begin with `dir.x` where `x` is an integer incrementing from zero. Ensure that all directories end with a single backslash. If an entry is not being used, remove it from the settings file.


**Use** - Simply run `deleteAutosaves.exe`, which will permanently delete all files with names containing one or more of the search keys. If logging is enabled, it will create a log file in the directory containing the `.exe`, and will create a log file within this directory each time it is run. When the program has completed, this log file will be opened.
To allow the program to run at startup, add a shortcut to the `.exe` in the directory `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`. Once this has been done, you can enable and disable running the program from: Task manager -> Start-up and looking for `deleteAutosaves.exe`.


**Changing settings** - To enable or disable logging, change the `logging` parameter to 1 or 0 to enable or disable logging respectively.
To change the search parameters, edit the `keys` parameter. Two keys must be provided at all times, both of which should be in lowercase and separated by a single comma with no whitespace.


**Example settings file**

```
[DEFAULT]
logging = 1
keys = autosave,previous

[paths]
dir.1 = C:\Users\tom\Documents\Prepar3D v4 Add-ons\FSLabs\A320\PanelState\
dir.2 = D:\Documents\Flight Simulator X Files\
```
