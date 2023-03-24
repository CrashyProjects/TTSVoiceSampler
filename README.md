# TTS Voice Sampler
TTS Voice Sampler is a Python script that allows you to generate audio files from text using text-to-speech (TTS) technology. With this program you can select different voices and modify the rate of speech to generate audio files that meet your specific needs. 

This script was **designed for Windows**, if you plan to use this script on a Linux distribution, note that it is unlikely to work as expected. 

This script was designed considering that the default TTS voices folder was not changed.

## Requirements
-   Python 3.6 or higher
-   pyttsx3 package

You can install the pyttsx3 package using pip, as shown below:

   ```
    pip install pyttsx3
   ```
   
## Usage
To use this program, open a terminal window and navigate to the directory containing the TTSVoiceSampler.py file. Then, run the following command:

   ```
    python3 TTSVoiceSampler.py "Text to be voiced" [-v numVoice] [-r rate]
   ```
   
The program accepts the following arguments:

- "Text to be voiced": The text you want to convert to speech.
- -v numVoice (optional): The index of the voice you want to use for the conversion. By default, the program will use all available voices and create an audio file for each voice. When running the program, a list of available (found) voices and their respective index will be displayed to the user. This list will be presented every time the program is executed.
- -r rate (optional): The rate of speech you want to use for the conversion in words per minute. By default, the rate is set to 200 words per minute, which is the normal speaking rate.

Note that the program will generate the audio file/s in the "./audio" directory, with a file name that includes the first three characters of the text and the name of the voice used. If the "./audio" folder does not exist, the program will create it.

## Example Output
Suppose we want to generate speech for the text "Hello, world!" using the program. Here's an example command to run the program:
```
python TTSVoiceSampler.py "Hello, world!"
```
The program will use all available voices to generate speech for the given text. The output will include information about each voice used, the rate of speech, and the file name of the generated audio file:
```
###################################################################################
                                 TTS VOICE SAMPLER
###################################################################################
Directory  ./audio created. [Only shown if doesn't exist]
-----------------------------------------------------------------------------------
Available voices:
0 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_voice_A
1 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_voice_B
-----------------------------------------------------------------------------------
File: ./audio/Hel_TTS_voice_A.mp3 created.
File: ./audio/Hel_TTS_voice_B.mp3 created.
-----------------------------------------------------------------------------------
Voice generated: Hello, world!
Rate: 200
-----------------------------------------------------------------------------------
```
Alternatively, we can specify the index of the voice we want to use by passing the -v argument with the corresponding index. We will also decrease the speech rate. For example, suppose we want to use the TTS_voice_B (index 1) to generate speech for the same text. Here's an example command to run the program:
```
$ python3 TTSVoiceSampler.py "Hello world" -v 1 -r -50
````
Will generate:
```
Directory  ./audio created. [Only shown if doesn't exist]
Rate modified by 50
-----------------------------------------------------------------------------------
Available voices:
0 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_voice_A
1 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_voice_B
-----------------------------------------------------------------------------------
File: ./audio/Hel_TTS_voice_B.mp3 created.
-----------------------------------------------------------------------------------
Voice generated: Hello, world!
Rate: 150
-----------------------------------------------------------------------------------
```
Note that we decreased the rate using "-50", but it is also possible to increment it, for example, using "50".

## How do I get more voices?
If you're using Windows, you can easily add new voices by searching for "Speech" and clicking on "Add Language". However, note that this feature may not work properly as it is poorly implemented and may require additional steps to function correctly. If you encounter any issues, you can this: [Potential FIX](https://puneet166.medium.com/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13)

![Add voice on Windows 10](/docs/addVoice.png)
 
If you're using Linux, there are various ways to obtain additional TTS voices depending on your distribution. Remeber that this script is designed for Windows, if you plan to use this script on a Linux distribution, note that it is unlikely to work as expected. 

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

**IMPORTANT**: Please note that the voice used in a conversion is subject to the
license terms of the respective owner. It is important to be aware of these 
terms before using or distributing the generated content.
