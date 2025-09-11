from rapidfuzz import fuzz
from rapidfuzz import process, utils

class Choice: 

    @staticmethod
    def getChoice(query, options, minConfidence=70):

        (choice, confidence,index)= process.extractOne(query, options,scorer=fuzz.partial_ratio, processor=utils.default_process)

        print(f"Found '{choice}' with confidence {confidence} and index {index}")

        if confidence > minConfidence:
            return choice
        else:
            return None
        
    @staticmethod
    def getChoices(query, options, minConfidence=70):
         
        choices = []

        results = process.extract(query, options,scorer=fuzz.partial_ratio, processor=utils.default_process)

        for (choice, confidence, index) in results:
            print(f"Found '{choice}' with confidence {confidence} and index {index}")

            if confidence > minConfidence:
                choices.append(choice)

        return choices
        
# query = "yeah nah"
# choices = ["Yes", "No"]

# choice = Choice.getChoice(query, choices)
# print(choice)

spellOptions = ["Spell", "Spelling", "Spell Check", "Spell Checker"]
summaryoptions = ["Summary", "Summarize", "Summarization"]
exitOptions = ["Exit", "Quit", "Leave", "Bye"]

options = spellOptions + summaryoptions + exitOptions

query = "I want to Spell some words"

print(f"Check '{query}' in {options}")
choice = Choice.getChoice(query, options)

match choice: 
        case choice if choice in spellOptions:
            print(f"Spell check selected: {choice}")
        case choice if choice in summaryoptions:
            print(f"Summary selected: {choice}")
        case choice if choice in exitOptions:
            print(f"Exit selected {choice}") 

print(f"\n Now checking all matches for '{query}' in {options}: \n")
choices = Choice.getChoices(query, options)

for choice in choices:
    print(f"Choice: ")