@echo off

cd /d "%~dp0"

echo Running "bb-remove-windows-garbage.py"...

if not exist ".venv" (
    echo .venv not found. Creating virtual environment...

    py -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

.venv\Scripts\python.exe "bb-remove-windows-garbage.py"

echo.
echo Application exited.
pause
