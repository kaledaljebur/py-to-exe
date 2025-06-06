# py-to-exe
The following steps are on how to convert Python file in Windows into `exe` execution file:
It is better to do the work inside Python virtual `env` folder.
The converted exe file is in [dist folder](dist).
- Create `env` folder for isolated Python environment:
    - `python3 -m venv env`.
    - `.\env\Scripts\Activate.ps1`.
- Install the needed packages for your Python file: 
    - For example `pip install pyfiglet`.
- Install `pyinstaller` the converter Python package:
    - `pip install pyinstaller`.
- Run the converting command:
    - `pyinstaller --onefile fun.py`.   
- Check and run the exe file:
    - `dist\script.exe`.
- Remove `dist\script.exe` each time you would like to convert the same Python file.
- When you run the `exe` file, if you see missing packages error like `ModuleNotFoundError: No module named 'pyfiglet'`, then make sure they are installed while `env` activated, and try to include the missing packages in the command, like:
    - Sample error image: \
    ![image](img/pyfiglet.png)
    - `pyinstaller --onefile --hidden-import=pyfiglet fun.py`.
    
- If you get error like `No module named 'pyfiglet.fonts'` even though `pyfiglet` is installed already, then search for `fonts` folder inside `py-to-exe/env/Lib/site-packages/pyfiglet/`, then include it in the command:
    - Sample error: \
    ![image](img/pyfiglet.fonts.png)
    - `pyinstaller --onefile --hidden-import=pyfiglet --add-data "env\Lib\site-packages\pyfiglet\fonts;pyfiglet/fonts" fun.py`.
- Include `--noconsole`, `-w`, or `--windowed` to remove the console window:
    - `pyinstaller --onefile --noconsole --hidden-import=pyfiglet fun.py`.   
- Use `--icon=myicon.ico` to add icon for your exe file:
    - Use any online icons generated like [icon-icons](https://icon-icons.com/) or [icoconverter](https://icoconvert.com), and save it in the same directory with fun.py. 
    - `pyinstaller --onefile --noconsole --hidden-import=pyfiglet --add-data "env\Lib\site-packages\pyfiglet\fonts;pyfiglet/fonts" --icon=.\img\fun2.ico fun.py`.
