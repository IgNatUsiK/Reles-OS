@echo off
title Install
pip install pyinstaller
cls
title Compile
pyinstaller --onefile main.py
cls
title Unpacking
echo %~dp0dist\main.exe
move /Y "%~dp0dist\main.exe" "%~dp0"
rmdir /S /Q build
rmdir /S /Q dist
rmdir /S /Q __pycache__
del main.spec
cls
title Ready
echo All ready!
pause