#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int compute_grade(string text);

int main(void)
{
    // Get input text from user
    string text1 = get_string("Text: ");

    // grading the test
    int grade = compute_grade(text1);

    // Print the grade of the text
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
     else if (grade >= 16)
     {
         printf("Grade 16+\n");
}
     else {
         printf("%s%i\n", "Grade ", grade);
     }

}


int compute_grade(string text)
{
    // calculating the grade
    int numLetters = 0;
    int numWords = 1;
    int numSentences = 0;


    for (int i = 0; i < strlen(text); i++)
    {

     if (isupper(text[i]) || islower(text[i]))
     {

      numLetters += 1;

     }

      else if (text[i] == 32)
      {

       numWords += 1;

  }

     else if (text[i] == 33 || text[i] == 46 || text[i] == 63)
     {

       numSentences += 1;

     }

    }

    float L = ((float) numLetters / numWords) * 100;
    float S = ((float) numSentences / numWords) * 100;

  float beforeRound = 0.0588 * L - 0.296 * S - 15.8;
  int afterRound = round(beforeRound);

    return afterRound;
    
}

