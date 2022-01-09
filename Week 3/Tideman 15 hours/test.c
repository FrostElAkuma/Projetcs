#include <io.h>
#include <stdio.h>


int main()
{
    typedef struct
{
    int winner;
    int loser;
    int strength;
}
pair;

pair pairs[3];

                int pair_count = 2;

                pairs[0].winner = 0;
                pairs[0].loser = 1;
                pairs[0].strength = 2;

                pairs[1].winner = 2;
                pairs[1].loser = 0;
                pairs[1].strength = 3;


    int highest1 = 0;
    //i is the "compared-to" pair index
    for (int i = 0; i < pair_count; i++)
    {
        pair save[1];
        save[0] = pairs[i];
        int highest = pairs[i].strength;
        highest1 = i;
        //j is the compared pair index
        for (int j = i+1; j < pair_count; j++)
        {
            if (highest < pairs[j].strength)
            {
                highest = pairs[j].strength;
                highest1 = j;
            }
        }

        pairs[i] = pairs[highest1];
        pairs[highest1] = save[0];
    }

cout<<pairs[0];

}
