import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def translate_speech():
    print("Доступные языки: английский, немецкий, китайский, японский, испанский.")
    lang = input("Выберите язык для перевода: ")

    translator = Translator()

    if lang == "английский":
        dest_lang = "en"
    elif lang == "немецкий":
        dest_lang = "de"
    elif lang == "китайский":
        dest_lang = "zh-CN"
    elif lang == "японский":
        dest_lang = "ja"
    elif lang == "испанский":
        dest_lang = "es"
    else:
        print("Выбран неподдерживаемый язык.")
        return

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Распознан текст: {text}")

        translation = translator.translate(text, dest=dest_lang)
        translated_text = translation.text

        print(f"Переведённый текст: {translated_text}")

        engine = pyttsx3.init()

        engine.say(translated_text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    translate_speech()
