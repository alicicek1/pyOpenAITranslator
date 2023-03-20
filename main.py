import pyttsx3
import speech_recognition
import openai
import json


def register_chat_gpt():
    openai.api_key = "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"


def chat_gpt_chat_completion_content(text_content) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_content}]
    )

    # Convert the OpenAI object to a JSON-formatted string
    completion_json = json.dumps(completion)

    # Convert the JSON-formatted string back to a Python object
    completion_obj = json.loads(completion_json)

    content = completion_obj['choices'][0]['message']['content']
    return content


def translate(translating_text, translating_from, translating_to) -> str:
    return chat_gpt_chat_completion_content(
        f'{translating_text}.This text is in {translating_from} and translate it to {translating_to}. Just translation.'
    )


def getDit() -> str:
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Start speaking:")
        audio = r.listen(source)

    try:
        txt = r.recognize_google(audio, language='tr-Tr')
        print("Told: " + txt)
        return txt
    except speech_recognition.UnknownValueError:
        print("Couldn't understand what you said.")
    except speech_recognition.RequestError as e:
        print("Google Speech API Error; {0}".format(e))
        raise Exception(f'{format(e)}')


if __name__ == '__main__':
    print("-------------------------------------------------")
    print("Type which language you want to translate from:")
    inputFrom = input()
    print("-------------------------------------------------")
    print("Type which language you want to translate to:")
    inputTo = input()
    register_chat_gpt()
    text = getDit()

    a = translate(text, inputFrom, inputTo)

    engine = pyttsx3.init()
    engine.say(a)
    engine.runAndWait()
