from cs50 import get_string  


def main():
    text1 = get_string("Text: ")
    
    grade = compute_grade(text1)
    
    if grade < 1:
        print("Before Grade 1")
    
    elif grade >= 16:
        print("Grade 16+")
        
    else:
        print(f"Grade, {grade}")    


def compute_grade(text):
    # calculating the grade
    numLetters = 0
    numWords = 1
    numSentences = 0

    for i in range(0, len(text), 1):
    
        if (text[i].isupper() or text[i].islower()):
            numLetters += 1

        elif (text[i] == " "):
            numWords += 1

        elif (text[i] == "!" or text[i] == "." or text[i] == "?"):
    
            numSentences += 1

    L = (numLetters / numWords) * 100
    S = (numSentences / numWords) * 100

    beforeRound = 0.0588 * L - 0.296 * S - 15.8
    afterRound = round(beforeRound)

    return afterRound
    
    
main()