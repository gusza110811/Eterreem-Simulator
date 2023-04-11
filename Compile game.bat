@echo off

set /p version=game version:
echo Compiling game...

set SRC_FILE=Eterreem_Simulator.py
set APP_NAME="Eterreem_Simulator %version%"

pyinstaller --onefile --name %APP_NAME% %SRC_FILE%
mkdir "dist\saves"

echo Game compiled successfully!