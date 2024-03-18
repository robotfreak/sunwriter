import os
from openai import OpenAI
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from dotenv import load_dotenv
from pathlib import Path
from ctypes import *

# From alsa-lib Git 3fd4ab9be0db7c7430ebd258f2717a976381715d
# $ grep -rn snd_lib_error_handler_t
# include/error.h:59:typedef void (*snd_lib_error_handler_t)(const char *file, int line, const char *function, int err, const char *fmt, ...) /* __attribute__ ((format (printf, 5, 6))) */;
# Define our error handler type
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
def py_error_handler(filename, line, function, err, fmt):
  #print( 'messages are yummy')
  return
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary('libasound.so')
# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)


# Load the environment variables
load_dotenv()
# Create an OpenAI API client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# settings and keys
model_engine = "gpt-3.5-turbo"
language = 'de'

def recognize_speech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio_stream = r.listen(source)
            print("Waiting for wake word...")
            # recognize speech using Google Speech Recognition
            try:
                # convert the audio to text
                print("Google Speech Recognition thinks you said " + r.recognize_google(audio_stream))
                speech = r.recognize_google(audio_stream)
                print("Recognized Speech:", speech)  # Print the recognized speech for debugging
                words = speech.lower().split()  # Split the speech into words
                if "computer" not in words:
                    print("Wake word not detected in the speech")
                    return False
                else:
                    # Add recognition of activation messsage to improve the user experience.
                    #playsound("sounds/start.mp3") # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
                    print("Found wake word!")
                    return True
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            print("Interrupted by User Keyboard")
            pass

def speech():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Activated! Waiting for your question...")
        try:
            audio_stream = r.listen(source)
            # recognize speech using Google Speech Recognition
            # recognize speech using Google Speech Recognition
            try:
                # convert the audio to text
                print("Google Speech Recognition thinks you said " + r.recognize_google(audio_stream))
                speech = r.recognize_google(audio_stream)
                #pixels.think()
                return speech
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            print("Interrupted by User Keyboard")
            pass
    return ""
 
def chatgpt_response(prompt):
    # Add a holding messsage like the one below to deal with current TTS delays until such time that TTS can be streamed.
    #playsound("sounds/holding.mp3") # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
    # send the converted audio text to chatgpt
    chat_de =  "Frage an das I Ching Orakel: Was bedeutet die Frage '" + prompt  + "?'. Antworte bitte mit maximal 10 Worten"
    chat_en =  "Question to the I Ching orakle: What is the asnwer to the question '" + prompt  + "?'. Answe in 10 words, please"
    response = client.chat.completions.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are a helpful smart speaker called Jeffers!"},
                  {"role": "user", "content": chat_en}],
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )
    return response
 
def generate_audio_file(message):
    # Add another checking messsage like the one below to improve the user experience.
    #playsound("sounds/checking.mp3") # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
    speech_file_path = Path(__file__).parent / "response.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input=message
)
    response.stream_to_file(speech_file_path)
 
def play_audio_file():
    # play the audio file
    # os.system("mpg321 response.mp3")
    playsound("response.mp3", block=False) # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.

def main():
    # run the program
    while True:
        if recognize_speech():
            prompt = speech()
            if prompt != "":
                print(f"This is the prompt being sent to OpenAI: {prompt}")
                responses = chatgpt_response(prompt)
                message = responses.choices[0].message.content
                print(message)
            else:
                continue
            #generate_audio_file(message)
            #play_audio_file()
        else:
            print("Wake word not detected. Listening again...")
            continue

if __name__ == "__main__":
    main()
