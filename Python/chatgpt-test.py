import os
from openai import OpenAI
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
#from dotenv import load_dotenv
from pathlib import Path
from ctypes import *
import pygame
import math
import random

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
BLAU    = ( 0, 0, 255)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

text1_point = [0,0]
text2_point = [0,0]
text3_point = [0,0]
text1 = ""
text2 = ""
text3 = ""
font1_size = 32
font2_size = 32
font3_size = 32
max_font_size = 150
font_name = "Calibri"

def fadeIn(pg, scrn, txt, txt_pt, txt2, txt2_pt, txt3, txt3_pt, dly):
    width, height = pg.display.Info().current_w, pg.display.Info().current_h
    side = 2*height/math.sqrt(3)
    txt_surf = txt.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    print(txt_surf.get_width())
    alpha = 0  # The current alpha value of the surface.
    while alpha < 255:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = min(alpha+4, 255)
        txt_surf = txt.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        scrn.fill((0, 0, 0))
        scrn.blit(txt_surf, txt_pt)
        pg.draw.polygon(scrn, WEISS, [[width/2-side/2,height-2], [width/2,0], [width/2+side/2,height-2]], 2)
        if (txt2 != None):
            scrn.blit(txt2, txt2_pt)
        if (txt3 != None):
            scrn.blit(txt3, txt3_pt)
        pg.display.flip() # if screen is your display
        pg.time.delay(dly)

def fadeOut(pg, scrn, txt, txt_pt, txt2, txt2_pt, txt3, txt3_pt, dly):
    width, height = pg.display.Info().current_w, pg.display.Info().current_h
    side = 2*height/math.sqrt(3)

    txt_surf = txt.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while alpha > 0:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt_surf = txt.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        scrn.fill((0, 0, 0))
        scrn.blit(txt_surf, txt_pt)
        pg.draw.polygon(scrn, WEISS, [[width/2-side/2,height-2], [width/2,0], [width/2+side/2,height-2]], 2)
        if (txt2 != None):
            scrn.blit(txt2, txt2_pt)
        if (txt3 != None):
            scrn.blit(txt3, txt3_pt)
        pg.display.flip() # if screen is your display
        pg.time.delay(dly)

def fadeOutAll(pg, scrn, txt1, txt1_pt, txt2, txt2_pt, txt3, txt3_pt, dly):
    width, height = pg.display.Info().current_w, pg.display.Info().current_h
    side = 2*height/math.sqrt(3)

    txt1_surf = txt1.copy()
    txt2_surf = txt2.copy()
    txt3_surf = txt3.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha1_surf = pg.Surface(txt1_surf.get_size(), pg.SRCALPHA)
    alpha2_surf = pg.Surface(txt2_surf.get_size(), pg.SRCALPHA)
    alpha3_surf = pg.Surface(txt3_surf.get_size(), pg.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.
    while alpha > 0:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt1_surf = txt1.copy()  # Don't modify the original text surf.
        txt2_surf = txt2.copy()  # Don't modify the original text surf.
        txt3_surf = txt3.copy()  # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha1_surf.fill((255, 255, 255, alpha))
        alpha2_surf.fill((255, 255, 255, alpha))
        alpha3_surf.fill((255, 255, 255, alpha))
         # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt1_surf.blit(alpha1_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        txt2_surf.blit(alpha2_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        txt3_surf.blit(alpha3_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        scrn.fill((0, 0, 0))
        scrn.blit(txt1_surf, txt1_pt)
        scrn.blit(txt2_surf, txt2_pt)
        scrn.blit(txt3_surf, txt3_pt)
        pg.draw.polygon(scrn, WEISS, [[width/2-side/2,height-2], [width/2,0], [width/2+side/2,height-2]], 2)
        pg.display.flip() # if screen is your display
        pg.time.delay(dly)

def getFontSize(txt, side):
    global font_name, max_font_size
    fsz=32
    font=pygame.font.SysFont(font_name, fsz, True, False)
    text = font.render(txt, True, WEISS)
    size, height=text.get_size()
    if float(size) < side:
        while float(size) < side:
            fsz += 2
            font=pygame.font.SysFont(font_name, fsz, True, False)
            text = font.render(txt, True, WEISS)
            size, height=text.get_size()
            #break
    elif float(size) > side:    
        while float(size) > side:
            fsz -= 2
            font=pygame.font.SysFont(font_name, fsz, True, False)
            text = font.render(txt, True, WEISS)
            size, height=text.get_size()
            #break
    return fsz if fsz < max_font_size else max_font_size



def initText(width, side, height, txt1, txt2, txt3):
    global font_name, text1_point, text2_point, text3_point, text1, text2, text3
    font1_size = 32
    font2_size = 32
    font3_size = 32
  # Select the font to use, size, bold, italics
    font1 = pygame.font.SysFont(font_name, font1_size, True, False)
    font2 = pygame.font.SysFont(font_name, font2_size, True, False)
    font3 = pygame.font.SysFont(font_name, font3_size, True, False)
    if txt1 != "":
        text1 = font1.render(txt1, True, WEISS)
        font1_size = getFontSize(txt1, side*0.7)
        font1 = pygame.font.SysFont(font_name, font1_size, True, False)
        text1 = font1.render(txt1, True, WEISS)
        print(text1.get_size())
        print(font1_size)
        txt1_height = text1.get_height()
        txt1_width = text1.get_width()
        text1_point = pygame.math.Vector2(width/2-txt1_width/2, height-4-txt1_height)
    if txt2 != "":
        text2 = font2.render(txt2, True, WEISS)
        font2_size = getFontSize(txt2, side*0.7)
        font2 = pygame.font.SysFont(font_name, font2_size, True, False)
        text2 = font2.render(txt2, True, WEISS)
        print(text2.get_size())
        text2 = pygame.transform.rotate(text2, 120)
        #print(text2.get_size())
        txt2_height = text2.get_height()
        txt2_width = text2.get_width()
        text2_point = pygame.math.Vector2(width/2+side/4-txt1_height-txt2_width/2, height/2-txt2_height/2)
    if txt3 != "": 
        text3 = font3.render(txt3, True, WEISS)
        font3_size = getFontSize(txt3, side*0.7)
        font3 = pygame.font.SysFont(font_name, font3_size, True, False)
        text3 = font3.render(txt3, True, WEISS)
        print(text3.get_size())
        text3 = pygame.transform.rotate(text3, 240)
        #print(text3.get_size())
        txt3_height = text3.get_height()
        txt3_width = text3.get_width()
        text3_point = pygame.math.Vector2(width/2-side/4+txt1_height-txt3_width/2, height/2-txt3_height/2)


    
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
#load_dotenv()
# Create an OpenAI API client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# settings and keys
model_engine = "gpt-4-turbo-preview"
language = 'de'

def recognize_speech():
    #return True   # FOR TESTING ONLY!!!
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
                if "oracle" not in words:
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
    #return "What is the meaning of live"  # FOR TESTING ONLY!!
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Activated! Waiting for your question...")
        try:
            audio_stream = r.listen(source)
            # recognize speech using OpenAI Speech Recognition
            try:
                # convert the audio to text
                speech = r.recognize_whisper_api(audio_stream)
                print("This is what we think was said: " + speech)
            except sr.UnknownValueError:
                print("Whisper Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Whisper Speech Recognition service; {0}".format(e))
            return speech
        except KeyboardInterrupt:
            print("Interrupted by User Keyboard")
            pass
    return ""
 
def chatgpt_response(prompt):
    # Add a holding messsage like the one below to deal with current TTS delays until such time that TTS can be streamed.
    #playsound("sounds/holding.mp3") # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
    # send the converted audio text to chatgpt
    response = client.chat.completions.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are an I Ching oracle. Answer the questions in 9 words"},
                  {"role": "user", "content": prompt}],
        max_tokens=256,
        n=1,
        temperature=0.7,
    )
    return response
 
def chatgpt_poem_response(prompt):
    # Add a holding messsage like the one below to deal with current TTS delays until such time that TTS can be streamed.
    #playsound("sounds/holding.mp3") # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
    # send the converted audio text to chatgpt
    response = client.chat.completions.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are an haiku poem generator. Generate poems from the user message. The poems shoud not exceed 9 words"},
                  {"role": "user", "content": prompt}],
        max_tokens=256,
        n=1,
        temperature=0.7,
    )
    return response

def find_longest_word(word_list):  
    longest_word =  max(word_list, key=len)
    return longest_word

def chatgpt_palindrome_response(prompt):
    # Add a holding messsage like the one below to deal with current TTS delays until such time that TTS can be streamed.
    #playsound("sounds/holding.mp3") # There’s an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.
    # send the converted audio text to chatgpt
    response = client.chat.completions.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are a palindrome poem generator. Answer in less than 10 words\n".strip()},
                  {"role": "user", "content": prompt.strip()}],
        max_tokens=256,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
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
    # initialisieren von pygame
    pygame.init()

    # Fenster oeffnen
    #screen = pygame.display.set_mode((280, 200))  # small screen
    #screen = pygame.display.set_mode((640, 480))  # big screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    side = 2*height/math.sqrt(3)
    print("width ", width)
    print("height ", height)
    print("side ", side)
    words = []

    # Bildschirm Aktualisierungen einstellen
    clock = pygame.time.Clock()

    # run the program
    while True:
       # Ueberpruefen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Spieler hat Quit-Button angeklickt")

        # Spielfeld loeschen
        screen.fill(SCHWARZ)
        pygame.display.flip()
        pygame.time.delay(2000)
        #pygame.draw.polygon(screen, WEISS, [[10,470], [165,200], [320,470]], 2)
        pygame.draw.polygon(screen, WEISS, [[width/2-side/2,height-2], [width/2,0], [width/2+side/2,height-2]], 2)
        #pygame.draw.polygon(screen, WEISS, [[width/2,height-2], [width/2+side/4,height/2], [width/2-side/4,height/2]], 2)

        # Fenster aktualisieren
        pygame.display.flip()
        pygame.time.delay(2000)

        if recognize_speech():
            txt1="???"
            txt2=""
            txt3=""
            initText(width, side, height, txt1, txt2, txt3)
            fadeIn(pygame, screen, text1, text1_point, None, None, None, None, 60)
            pygame.time.delay(500)

            prompt = speech()
            if prompt != "":
                #prompt = prompt.encode('utf-8')
                print(f"This is the prompt being sent to OpenAI: {prompt}")
                responses = chatgpt_response(prompt)
                message = responses.choices[0].message.content
                print(message)
                words.clear()
                words = message.split()
                size = len(words)
                ssize = size / 3
                sadd = size % 3
                print(size)
                print(ssize)
                print(size%3)
                sofs1 = 0
                sofs2 = 0
                if sadd == 2:
                    sofs1 = 1
                    sofs2 = 1
                else:
                    if sadd == 1:
                        sofs1 = 1
                        sofs2 = 0
                i = 0
                txt1 = ""
                txt2 = ""
                txt3 = ""
                for word in words: 
                    if i < (ssize+sofs1):
                        txt1 += word + " "
                    else:
                        if i < (2*ssize+sofs1+sofs2):
                            txt2 += word + " "
                        else: 
                            if i < (3*ssize+sofs1+sofs2):
                                txt3 += word + " "
                    i = i+1
                initText(width, side, height, txt1, txt2, txt3)
                fadeIn(pygame, screen, text1, text1_point, None, None, None, None, 60)
                pygame.time.delay(500)
                fadeIn(pygame, screen, text2, text2_point, text1, text1_point, None, None, 60)
                pygame.time.delay(500)
                fadeIn(pygame, screen, text3, text3_point, text1, text1_point, text2, text2_point, 60)
                pygame.time.delay(3000)

                fadeOutAll(pygame, screen, text1, text1_point, text2, text2_point, text3, text3_point, 60)
                pygame.time.delay(1000)
                # Refresh-Zeiten festlegen
                clock.tick(60)
                
                # show anagram or poem 
                #prompt = ""
                #prompt = words[random.randint(0,8)]
                #responses = chatgpt_anagram_response(prompt)
                prompt = ""
                prompt = find_longest_word(words)
                responses = chatgpt_poem_response(prompt)
                #for i in range(3):
                #    prompt += words[random.randint(0,8)] + " "
                #print(f"This is the prompt being sent to OpenAI: {prompt}")
                #prompt = prompt.encode('utf-8')
                #responses = chatgpt_palindrome_response(prompt)
                message = responses.choices[0].message.content
                print(message)
                words.clear()
                words = message.split()
                size = len(words)
                ssize = size / 3
                sadd = size % 3
                print(size)
                print(ssize)
                print(size%3)
                sofs1 = 0
                sofs2 = 0
                if sadd == 2:
                    sofs1 = 1
                    sofs2 = 1
                else:
                    if sadd == 1:
                        sofs1 = 1
                        sofs2 = 0
                i = 0
                txt1 = ""
                txt2 = ""
                txt3 = ""
                for word in words: 
                    if i < (ssize+sofs1):
                        txt1 += word + " "
                    else:
                        if i < (2*ssize+sofs1+sofs2):
                            txt2 += word + " "
                        else: 
                            if i < (3*ssize+sofs1+sofs2):
                                txt3 += word + " "
                    i = i+1
                initText(width, side, height, txt1, txt2, txt3)
                fadeIn(pygame, screen, text1, text1_point, None, None, None, None, 60)
                pygame.time.delay(500)
                fadeIn(pygame, screen, text2, text2_point, text1, text1_point, None, None, 60)
                pygame.time.delay(500)
                fadeIn(pygame, screen, text3, text3_point, text1, text1_point, text2, text2_point, 60)
                pygame.time.delay(3000)

                fadeOutAll(pygame, screen, text1, text1_point, text2, text2_point, text3, text3_point, 60)
                pygame.time.delay(1000)
                # Refresh-Zeiten festlegen
                clock.tick(60)

                screen.fill(WEISS)
                pygame.display.flip()
                pygame.time.delay(5000)
            else:
                continue
        else:
            print("Wake word not detected. Listening again...")
            continue

if __name__ == "__main__":
    main()
