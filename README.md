# Python Text-to-Speech Converter

A simple and efficient text-to-speech converter using Python's `pyttsx3` library. This tool converts written text into spoken words using your computer's text-to-speech engines.

## Features

- Convert text to speech in real-time
- Adjust speech rate and volume
- Support for multiple voices and languages
- Simple and easy-to-use interface
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Install pyttsx3 using pip:
```bash
pip install pyttsx3
```

2. For macOS users, you might need to install additional dependencies:
```bash
pip install pyobjc
```

## Basic Usage

Here's a simple example to get started:

```python
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Convert text to speech
text = "Hello, this is a test of text-to-speech conversion!"
engine.say(text)
engine.runAndWait()
```

## Advanced Features

### Adjusting Voice Properties

```python
import pyttsx3

engine = pyttsx3.init()

# Get current voice properties
rate = engine.getProperty('rate')   # Getting current speaking rate
volume = engine.getProperty('volume')   # Getting current volume
voices = engine.getProperty('voices')   # Getting available voices

# Modify voice properties
engine.setProperty('rate', 150)    # Setting speaking rate (default is 200)
engine.setProperty('volume', 0.9)  # Setting volume (0.0 to 1.0)
engine.setProperty('voice', voices[1].id)  # Setting different voice (index can be 0 or 1)

# Convert text to speech with new properties
text = "This is a test with modified voice properties!"
engine.say(text)
engine.runAndWait()
```

### Saving Speech to File

```python
import pyttsx3

engine = pyttsx3.init()

# Save speech to an audio file
text = "This will be saved as an audio file."
engine.save_to_file(text, 'output.mp3')
engine.runAndWait()
```

## Common Issues and Solutions

1. **No sound output:**
   - Check if your system's audio is working
   - Verify that speakers/headphones are connected
   - Ensure system volume is not muted

2. **Installation errors:**
   - For Windows: Make sure you have the Windows Speech API installed
   - For macOS: Install `pyobjc` dependencies
   - For Linux: Install `espeak` using your package manager

3. **Voice not changing:**
   - Check available voices using `engine.getProperty('voices')`
   - Ensure the voice index exists before setting it

## Best Practices

1. Always use `runAndWait()` after `say()` or `save_to_file()`
2. Release resources when done:
```python
engine.stop()
```

3. Handle errors gracefully:
```python
try:
    engine = pyttsx3.init()
    engine.say("Testing text-to-speech")
    engine.runAndWait()
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to contribute to this project by:
1. Reporting issues
2. Suggesting enhancements
3. Creating pull requests

## Support

For additional support:
- Check the [pyttsx3 documentation](https://pyttsx3.readthedocs.io/)
- Open an issue in the GitHub repository
- Consult the Python community forums
