from utilities.Choice import Choice
from utilities.NLP import NLP
from utilities.Avatar import Avatar
from datetime import datetime
from utilities import Weather

class Demo(Avatar):

    __menuOptions = ["weather", "time", "date", "exit"]

    __weatherOptions = ["weather", "temperature", "forecast", "humidity"]
    __timeOptions = ["time", "date", "day of the week", "month", "year"]
    __dateOptions = ["date", "day of the week", "month", "year"]
    __exitOptions = ["exit", "quit", "goodbye", "bye", "leave", "stop"]

    __mainOptions = __weatherOptions + __timeOptions + __dateOptions + __exitOptions

    def __init__(self):
        super().__init__(name="Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr", useSR=True, vix=2)
        self.nlp = NLP()

        self.say(f"Hello, i am {self.getName()}, your virtual assistant how can i help you today?", show=True, rate=200)
   
    def getPerson(self):
        self.name = None
        while not self.name:
            response = self.listen("Please tell me your name.", useSR=True, show=True)
            names = self.nlp.getNameByEntityType(response)
            if len(names) == 1:
                self.name = names[0]
            else:
                self.say("I didnt catch your name or too many names. please try again.", show = True)
        self.say(f"Nice to meet you, {self.name}. How can I assist you?", show=True)
       
   
    def getRequest(self):
        choice = None
        while not choice:
            request = self.listen(f" {self.name}, what would you like to do? You can ask for ", useSR=True, show=True)
            choice = Choice.getChoice(request, Demo.__menuOptions)
            if not choice:
                self.say("I didnt understand that. Please choose from weather, news, time, date, or exit", show = True)
        return choice
 
    def sayTime(self):
        self.say(f"The current time is {datetime.now().strftime('%H:%M')}", show=True)

    def sayDate(self):
        self.say(f"Today's date is {datetime.now().strftime('%H:%M')}", show=True)

    def sayWeather(self):
        weather = Weather()
        data = weather.get_current_conditions()
        if data:
            self.say("Here are the current weather conditions:", show=True)
            weather.display_current_conditions(data)
        else:
            self.say("Sorry, I couldn't retrieve the ewather information at this time.", show=True)
   
    def run(self):
        self.getPerson()
       
        while True:
            request = self.getRequest()
            match request:
                case "time":
                    self.sayTime()
                case "date":
                    self.sayDate()
                case "weather":
                    self.sayWeather()
                case "news":
                    self.sayNews()
                case "exit":
                    self.say("Goodbye!", show =True)
                    break
                case _:
                    self.say("I'm sorry, I can only help with weather, news, time, date", show=True)
def test():
    demo = Demo()
    demo.run()

if __name__ == "__main__":
    test()
