#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
char player1[] = "Player 1 wins!";
char player2[] = "Player 2 wins!";
char tie[] = "Tie!";

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2) 
    {
        printf("%s", player1);
    }
     else if (score2 > score1) 
     {
         printf("%s", player2);
}
     else if (score1 == score2) 
     {
          printf("%s", tie);
     }
     else {
         printf("%i", 1);
     }

}


int compute_score(string word)
{
    // TODO: Compute and return score for string
    int stringScore = 0;

    for (int i = 0; i < strlen(word); i++)
    {

     if (isupper(word[i]))
     {

      stringScore += POINTS[word[i] - 65];

     }

      else if (islower(word[i]))
      {

       stringScore += POINTS[word[i] - 97];

       }
    }

    return stringScore;
}