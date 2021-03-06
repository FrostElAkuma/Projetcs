#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

int strength[MAX];

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

//An array that I created

int check [MAX];

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    //Clear the Check Array that I created
    for (int i = 0; i < candidate_count; i++)
    {
        check[i] = 0;
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    bool plz;
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0)
        {
            ranks[rank] = i;
            plz = true;
            break;
        }

        else
        {
            plz = false;
        }
    }
    return plz;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            int after = ranks[j];
            int candidateNum = ranks[i];

            preferences[candidateNum][after] += 1;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pair_count += 1;
                pairs[pair_count - 1].winner = i;
                pairs[pair_count - 1].loser = j;
                strength[pair_count - 1] = preferences[i][j] - preferences[j][i];

            }

            else if (preferences[i][j] < preferences[j][i])
            {
                pair_count += 1;
                pairs[pair_count - 1].winner = j;
                pairs[pair_count - 1].loser = i;
                strength[pair_count - 1] = preferences[j][i] - preferences[i][j];
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{

    for (int i = 0; i < pair_count; i++)
    {
        printf("%s%i\n", "This is the win strength before sorting ", strength[i]);
        printf("%s%i\n", "This is the winner before sorting ", pairs[i].winner);
        printf("%s%i\n", "This is the loser before sorting ", pairs[i].loser);

    }

    int highest1 = 0;
    pair save[1];
    int strengthSave;
    //i is the "compared-to" pair index
    for (int i = 0; i < pair_count; i++)
    {
        save[0] = pairs[i];
        strengthSave = strength[i];
        int highest = strength[i];
        highest1 = i;
        //j is the compared pair index
        for (int j = i + 1; j < pair_count; j++)
        {
            if (highest < strength[j])
            {
                highest = strength[j];
                highest1 = j;
            }
        }

        strength[i] = highest;
        strength[highest1] = strengthSave;

        pairs[i] = pairs[highest1];
        pairs[highest1] = save[0];
    }

    for (int i = 0; i < pair_count; i++)
    {
        printf("%s%i\n", "This is the win strength after sorting ", strength[i]);
        printf("%s%i\n", "This is the winner after sorting ", pairs[i].winner);
        printf("%s%i\n", "This is the loser after sorting ", pairs[i].loser);
    }

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    int check_total = 0;
    int total = 0;
    int winner = 99; //Just wanted a number that is non of the candidates

    printf("%s%i\n", "The number of pairs ", pair_count);

    for (int i = 0; i < pair_count; i++)
    {
        printf("%s%i\n", "this is i ", i);
        total = 0;
        printf("%s%i\n", "This is check total ", check_total);
        if (check_total + 1 == candidate_count)
        {
            for (int h = 0; h < candidate_count; h++)
            {
               // printf("%i\n", h);
                if (check[h] == 0)
                {
                    winner = h;
                    printf("%s%i\n", "This is the winner ", winner);
                }
            }
        }
        printf("%s%i\n", "this is the loser1 ", pairs[i].loser);
        if (pairs[i].loser != winner)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
            check[pairs[i].loser] = 1;
            total = 0;
            printf("%s%i\n", "this is the loser2 ", pairs[i].loser);

            for (int j = 0; j < candidate_count; j++)
            {
                total += check[j];
                printf("%s%i\n", "this is total ", total);
            }

            check_total = total;
        }

        else
        {
            printf("%s\n", "SKIPPED");
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (check[i] == 0)
        {
            printf("%s\n", candidates[i]);
        }
    }
    return;
}

