import os
import sys
import pyttsx3

def save_voice(id):
    try:
        engine.setProperty('voice', voices[int(id)].id)
    except ValueError:
        print(id, "is not valid. Please, select a valid voice. Exiting...")
        sys.exit(1)
    engine.runAndWait()
    save_file = audio_folder + "/" + sys.argv[1][:3] + "_" + engine.getProperty('voice').split("\\")[-1] + ".mp3"
    engine.save_to_file(sys.argv[1], save_file)
    engine.runAndWait()
    print("File: " + save_file + " created.")

def modify_rate(value):
    try:
        engine.setProperty('rate', engine.getProperty('rate') + int(value))
    except ValueError:
        print(value, "is not a valid rate. Exiting...")
        sys.exit(1)
    print("Rate modified by", value)

if len(sys.argv) < 2 or len(sys.argv) > 6 or len(sys.argv) == 3 or len(sys.argv) == 5:
    print("Usage: python3 TTSVoiceSampler.py \"Text to be voiced\" [-v numVoice] [-r rate]")
    sys.exit(1)

audio_folder = "./audio"
line         = "-----------------------------------------------------------------------------------"

print("\n###################################################################################")
print("                                 TTS VOICE SAMPLER")
print("###################################################################################")

if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)
    print("Directory ", audio_folder, "created.")

engine = pyttsx3.init()

if len(sys.argv) > 2 and sys.argv[2] == "-r":
    modify_rate(sys.argv[3])
elif len(sys.argv) > 4 and sys.argv[4] == "-r":
    modify_rate(sys.argv[5])

voices = engine.getProperty('voices')
print(line)
print("Available voices:")
for i, voice in enumerate(voices):
    print(i, voice.id)
print(line)

if len(sys.argv) > 2 and sys.argv[2] == "-v":
    save_voice(sys.argv[3])
elif len(sys.argv) > 4 and sys.argv[4] == "-v":
    save_voice(sys.argv[5])
else:
    for i, voice in enumerate(voices):
        save_voice(i)

print(line)
print("Voice generated: " + sys.argv[1])
print("Rate:", engine.getProperty('rate'))
print(line)
