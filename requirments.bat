
@echo off
echo Checking for Python...
where python
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH.
    echo Please install Python (version 3.x) and ensure it's added to your system's PATH.
    pause
    exit /b 1
)

echo Checking for pip (Python package installer)...
where pip
if %errorlevel% neq 0 (
    echo pip is not installed. It usually comes with Python.
    echo Please ensure pip is installed correctly. You might need to reinstall Python.
    pause
    exit /b 1
)

echo Checking if Kivy is installed...
python -c "try: import kivy; print('Kivy is installed.') except ImportError: print('Kivy is not installed.')" | findstr /C:"not installed"
if %errorlevel% equ 0 (
    echo Kivy is not installed. Attempting to install...
    pip install kivy[full]
    if %errorlevel% neq 0 (
        echo Error installing Kivy. Please check your internet connection and Python environment.
        pause
        exit /b 1
    )
    echo Kivy installed successfully.
) else (
    echo Kivy is already installed.
)

echo Checking if Ollama Python library is installed...
python -c "try: import ollama; print('Ollama library is installed.') except ImportError: print('Ollama library is not installed.')" | findstr /C:"not installed"
if %errorlevel% equ 0 (
    echo Ollama library is not installed. Attempting to install...
    pip install ollama
    if %errorlevel% neq 0 (
        echo Error installing Ollama library. Please check your internet connection and Python environment.
        pause
        exit /b 1
    )
    echo Ollama library installed successfully.
) else (
    echo Ollama library is already installed.
)

echo Attempting to pull the llama2 model using Ollama...
ollama pull llama2
if %errorlevel% neq 0 (
    echo Error pulling the llama2 model. Please ensure Ollama is installed and running correctly, and that you have internet access.
    echo You might need to run 'ollama pull llama2' manually if this fails.
) else (
    echo llama2 model pulled successfully.
)

echo Attempting to start the Ollama server...
start ollama serve
echo Ollama server started in the background.

echo All requirements checked and installed (if necessary).
echo The llama2 model has been pulled, and the Ollama server has been started.
echo You can now run your Python script.
echo To run the script, open a command prompt in the script's directory and type:
echo python main.py
pause
