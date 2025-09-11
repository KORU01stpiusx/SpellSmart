from rapidfuzz import fuzz
from rapidfuzz import process, utils

class Choice:

    @staticmethod
    def getChoice(query, options, minConfidence=70):

        (choice, confidence,index) = process.extractOne(query, options,scorer=fuzz.partial_ratio, processor=utils.default_process)
        print(f"Found '{choice}' with confidence {confidence} and index {index}")
        if confidence > minConfidence:
            return choice
        else:
            return None

    @staticmethod
    def getChoices(query, options, minConfidence=70):

        choices = []
        results = process.extract(query, options, scorer=fuzz.partial_ratio, processor=utils.default_process)
        # print(f"Found {len(results)} matches for '{query}' in {options}")
        for (choice, confidence, index) in results:
            print(f"Found '{choice}' with confidence {confidence} and index {index}")
            if confidence > minConfidence:
                choices.append(choice)
        return choices

def test():
    # query = "I am going to say yes please"
    # choices = ["Yes","No"]

    # choice = Choice.getChoice(query, choices)
    # print(choice)

    query = "I want to order steak and soup and ice cream"
    choices = ["Steak","Soup","Ice Cream","Fish and Chips", "Pizza", "Pasta"]
    choices = Choice.getChoices(query, choices)
    for choice in choices:
        print(f"Choice: {choice}")

    # spellOptions = ["Spell","Spelling", "Spell Check", "Spell Checker"]
    # summaryOptions = ["Summary", "Summarize", "Summarization"]
    # exitOptions = ["Exit", "Quit", "Leave", "Bye"]

    # options = summaryOptions + spellOptions +  exitOptions

    # query = "I want to do see my Spelling Summary of words please"

    # print(f"Check '{query}' in {options}")
    # choice = Choice.getChoice(query, options)

    # match choice:
    #     case choice if choice in spellOptions:
    #         print(f"Spell Check Selected: {choice}")
    #     case choice if choice in summaryOptions:
    #         print(f"Summary Selected: {choice}")
    #     case choice if choice in exitOptions:
    #         print(f"Exit Selected: {choice}")

    # print(f"\n Now checking all matches for '{query}' in {options}: \n")
    # choices = Choice.getChoices(query, options)

    # for choice in choices:
    #     print(f"Choice: {choice}")





    # for result in results:
    #     print(f"Found '{result[0]}' with confidence {result[1]} and distance {result[2]}")


    # for (choice, confidence, index) in results:
    #     print(f"Found '{choice}' with confidence {confidence} and distance {index}")

if __name__ == "__main__":
    test()