import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect
import tempfile
import gradio as gr
import logging

logging.basicConfig(level=logging.INFO)

class SpeechConversionUtility:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text(self, audio_path):
        with sr.AudioFile(audio_path) as source:
            audio_data = self.recognizer.record(source)
            return self.recognizer.recognize_google(audio_data)

    def detect_language(self, text):
        return detect(text)

    def translate(self, text, target_lang):
        return GoogleTranslator(source="auto", target=target_lang).translate(text)

    def text_to_speech(self, text, lang):
        temp_path = tempfile.mktemp(suffix=".mp3")
        gTTS(text=text, lang=lang).save(temp_path)
        return temp_path

    def process_audio(self, audio_path, target_language):
        try:
            text = self.speech_to_text(audio_path)
            src_lang = self.detect_language(text)
            translated = self.translate(text, target_language)
            tts_path = self.text_to_speech(translated, target_language)
            return text, src_lang, translated, tts_path
        except Exception as e:
            logging.error(e)
            return "Error", "undetected", "Error", None


util = SpeechConversionUtility()

def translate_audio(audio, target_language):
    if audio is None:
        return "No input", "undetected", "No input", None
    return util.process_audio(audio, target_language)


lang_choices = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

iface = gr.Interface(
    fn=translate_audio,
    inputs=[
        gr.Audio(type="filepath", label="Record your speech"),  # Fixed line
        gr.Dropdown(choices=list(lang_choices.values()), label="Select Target Language")
    ],
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="Detected Language"),
        gr.Textbox(label="Translated Text"),
        gr.Audio(label="Translated Speech")
    ],
    live=False,
    title="Live Speech Translator",
    description="Record your voice, choose a language, and hear it translated."
)

if __name__ == "__main__":
    iface.launch()
