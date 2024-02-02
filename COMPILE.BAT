@echo off

echo Compiling game...

set SRC_FILE=Eterreem_Simulator.py
set APP_NAME="Eterreem_Simulator 0.2.2"

pyinstaller --onefile --name %APP_NAME% %SRC_FILE%