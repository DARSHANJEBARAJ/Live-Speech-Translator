# Portable Speech Translator

This Python script implements a portable speech translator that can:

- Transcribe audio from various file formats (it will automatically convert them to WAV).
- Detect the language of the transcribed text.
- Translate the text to a specified target language using Google Translate.
- Generate speech audio of the translated text.

## Features

- **Audio Format Conversion:** Automatically converts input audio files to WAV format using `pydub`, ensuring compatibility with the `speech_recognition` library.
- **Speech to Text:** Utilizes the Google Speech Recognition service via the `speech_recognition` library to transcribe spoken audio into text.
- **Language Detection:** Employs the `langdetect` library to automatically identify the language of the transcribed text.
- **Text Translation:** Leverages the `deep_translator` library, specifically the Google Translator, to translate the detected text into the desired target language.
- **Text to Speech:** Uses the `gTTS` (Google Text-to-Speech) library to convert the translated text into audible speech, saving it as an MP3 file.
- **Error Handling:** Includes robust error handling for speech recognition, language detection, translation, and text-to-speech processes.
- **Clear Output:** Provides a dictionary containing the original text, detected language, translated text, target language, and the path to the translated audio file.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

```bash
pip install SpeechRecognition deep-translator gTTS langdetect pydub
