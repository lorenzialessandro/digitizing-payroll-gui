@echo off
echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Failed to install dependencies. Exiting.
    exit /b %errorlevel%
)

echo Dependencies installed successfully.
echo Running main.py...
python main.py

if %errorlevel% neq 0 (
    echo main.py encountered an error. Exiting.
    exit /b %errorlevel%
)

echo main.py executed successfully.
pause
