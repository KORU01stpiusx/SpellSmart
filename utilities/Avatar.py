import pyttsx4
import speech_recognition as sr

class Avatar():
    '''
        # Avatar Class - this class is responsible for speaking and listening.

        # It can be imported into another Class that needs this functionality

        # Need to pre-install: pyttsx4, SpeechRecognition
        # add the following to end of pip install if you have SSL VERIFY errors
        #--trusted-host pypi.org --trusted-host files.pythonhosted.org

    '''
    def __init__(self,name=None, useSR=True,vix=1):
        '''
        Constructor
        '''''
        if name:
            self.__name = name

        self.__useSR = useSR
        self.__initVoice(vix)
        self.__initSR()

    def __initVoice(self,vix=1):
        '''
        Method: Initialise Text to Speech
        '''
        self.__engine = pyttsx4.init()
        self.__voices = self.__engine.getProperty('voices')
        self.__vix = vix
        self.__rate = 250
        self.__voice = self.__voices[self.__vix].id
        self.__engine.setProperty('voice', self.__voice)
        self.__engine.setProperty('rate', self.__rate)
        self.__engine.setProperty('volume', 1.0)

    def __initSR(self, useSR=True):
        self.sample_rate = 48000
        self.chunk_size = 2048
        self.r = sr.Recognizer()
        if useSR is not None:
            self.__useSR = useSR
        else:
            self.__useSR = True  # set this to True if using Speech Recognition

    def say(self, words, show=True, rate=None):
        '''
        Method: Speak the words
        :param words: the words to speak
        :param show: if True, print the words to console
        :param rate: if specified, set the speaking rate

        '''
        if show:
            print(f"{words} ")
        if rate:
            self.__engine.setProperty('rate', rate)
        self.__engine.say(words, self.__name)
        self.__engine.runAndWait()

        self.__engine.setProperty('rate', self.__rate)


    def listen(self,prompt=None, useSR=None, show=True):
        '''
        Method: Listen for a response

        :param prompt: the prompt to show before listening
        :param useSR: if True, use Speech Recognition, otherwise use input()
        :param show: if True, print the prompt to console
        :return: the words spoken or typed by the user

        '''
        # print(useSR)
        if useSR is not None:
            self.__useSR = useSR

        words = ""
        if self.__useSR:
            try:
                with sr.Microphone(sample_rate=self.sample_rate, chunk_size=self.chunk_size) as source:
                    # listen for 1 second to calibrate the energy threshold for ambient noise levels
                    self.r.adjust_for_ambient_noise(source)
                    self.say(prompt,show)
                    audio = self.r.listen(source, timeout=5,phrase_time_limit=3)
                    with open("audio.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                try:
                    print("Ok. Trying to understand what you just said...please wait.")
                    # print("You said: '" + self.r.recognize_google(audio)+"'")
                    # words = self.r.recognize_google(audio,language ="en-US")
                    words = self.r.recognize_whisper(audio,language ="english")

                except sr.UnknownValueError:
                    self.say("Could not understand what you said.",show)
                except sr.RequestError as e:
                    self.say(f"Could not request results; {e}",show)

            except Exception as e:
                print(f"Error listening:'{e}'. ")
                self.say(prompt,show)
                words = input("Please type your response:> ")
        else:
            # print("No SR")
            self.say(prompt,show=True)
            words = input(">")

        return words


    def getName(self):
        return self.__name
#
# This is code to TEST DRIVER our Avatar Class
#
def main():
    george = Avatar("george")
    # george.say(f"My name is {george.getName()} ...eee",rate=150)

    response = george.listen("Please tell me what you want to do.", useSR=True, show=True)
    george.say(f"You said: {response}", show=True,rate=200)




if __name__ == "__main__":
    main()