# Speech Text Generation App

This application uses the Ollama large language model to generate a paragraph of text based on a user-provided topic. It features a simple user interface built with Kivy and includes a typing animation effect for the generated text.

## Requirements

Before running the application, ensure you have the following installed:

* **Python 3.x:** The application is written in Python 3.
* **pip:** The Python package installer (usually comes with Python).
* **Ollama:** You need to have the Ollama server installed and running with the `llama2` model available.

    * **Installation:** Follow the instructions on the [official Ollama website](https://ollama.ai/download). Choose the installation method appropriate for your operating system (macOS, Linux, Windows Subsystem for Linux).
    * **Model Download:** Once Ollama is installed and running, open your terminal or command prompt and pull the `llama2` model by running:
        ```bash
        ollama pull llama2
        ```

## Installation of Python Libraries

A `requirement.bat` file is provided to help you install the necessary Python libraries. Follow these steps:

1.  **Save the files:** Ensure that the `main.py` (your Python code) and the `requirement.bat` file are in the same directory.
2.  **Run `requirement.bat`:** Double-click the `requirement.bat` file. This script will:
    * Check if Python and pip are installed.
    * Attempt to install the `kivy[full]` and `ollama` Python libraries if they are not already installed.
3.  **Wait for completion:** The script will display messages indicating the progress of the installation. Once it finishes without errors, you have the required Python libraries.

## Running the Application

Follow these steps to run the Speech Text Generation App:

1.  **Ensure Ollama is running:** Open a new terminal or command prompt and start the Ollama server in the background. The command to do this might vary slightly depending on your operating system, but it's often simply:
    ```bash
    ollama serve
    ```
    Leave this terminal window open while you use the application.
2.  **Open another command prompt or terminal:** Navigate to the directory where you saved the `main.py` file.
3.  **Run the Python script:** Execute the following command:
    ```bash
    python main.py
    ```
4.  **Use the application:** The Kivy application window will appear.
    * Adjust the desired word count using the slider.
    * Enter a topic in the "Enter Topic" text input field.
    * Click Enter
    * The generated text will appear in the "Generated Speech" area with a letter-by-letter typing animation.
    * To skip the typing animation simply double press spacebar
    * If you want to copy the generated text, click the "Copy" button. The button text will briefly change to "Copied!".

## Features

* **Topic-based text generation:** Generates a paragraph based on the topic you provide using the Ollama `llama2` model.
* **Word count control:** Allows you to specify an approximate word limit for the generated text.
* **Typing animation:** Displays the generated text with a letter-by-letter typing effect.
* **Skip animation:** You can quickly skip the typing animation by pressing the spacebar twice.
* **Copy to clipboard:** Easily copy the generated text to your system's clipboard.
* **Loading indicator:** Provides visual feedback while the application is waiting for the Ollama response.

## Notes

* This application requires the Ollama server to be running in the background for text generation. **Make sure you start the Ollama server before running the Python script.**
* Ensure you have pulled the `llama2` model in Ollama before running the application for the first time (`ollama pull llama2`).
* The quality and relevance of the generated text depend on the Ollama model and the provided topic.
* The word count is an approximation, and the generated paragraph might have slightly more or fewer words than specified.
