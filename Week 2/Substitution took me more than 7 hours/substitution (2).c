#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, string argv[])
{
    
    int repeated = 0;
    int num = 0;

    if (argc != 2)
    {

        printf("Usage: ./substitution key");

        printf("\n");
        return 1;

    }

    int argvlen = strlen(argv[1]);

    for (int i = 0, n = argvlen; i < n; i++)
    {

        if (isalpha(argv[1][i]) == 0)
        {

            num = 1;

        }

        for (int j = 0, m = argvlen; j < m; j++)
        {

            if (i == j)
            {

            }

            else if (toupper(argv[1][i]) == toupper(argv[1][j]))
            {

                repeated = 1;

            }

        }

    }

    if (argc == 2 && argvlen != 26)
    {

        printf("Key must contain 26 charachters");

        printf("\n");
        return 1;

    }


    else if (repeated == 1)
    {

        printf("Key characters must not be repeated");

        printf("\n");
        return 1;

    }

    else if (num == 1)
    {

        printf("Key must be a Alphabatical");

        printf("\n");
        return 1;

    }
    //Getting the cipher text
    else if (argc == 2 && argvlen == 26)
    {
        //Getting the plain text
        string plaintext = get_string("Please enter your plain text: ");
        //printing our output
        printf("%s%s\n", "plaintext:  ", plaintext);
        printf("%s", "ciphertext: ");
        //Our for loop that goes thro each character
        for (int i = 0, n = strlen(plaintext); i < n ; i++)
        {

            //Checking if the character is Uppercase
            if (isupper(plaintext[i]))
            {
                //Getting the corresponding cypher character for the plain character
                int place = plaintext[i] - 65;
                //Getting the character back to Upper case and then printing it
                printf("%c", toupper(argv[1][place]));

            }
            //Same thing as the Upper case but now Lower case
            else if (islower(plaintext[i]))
            {

                int place = plaintext[i] - 97;

                printf("%c", tolower(argv[1][place]));

            }
            //We print it if its not an Alphabatical character
            else
            {

                printf("%c", plaintext[i]);

            }

        }

        printf("\n");
        return 0;

    }

}




