#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{



    //Error wrong usage
    if (argc != 2)
    {
        printf("Usage: ./recover image");
        return 1;
    }

    FILE *memory = fopen(argv[1], "r");

    //Cannot open memory
    if (!memory)
    {
        printf("Cannot open memory");
        return 1;
    }
    //Buffer to check the first 4 bytes and see if it is a JPEG
    BYTE bytes[512];

    //Making our string and total images
    char *imgNo = malloc(40);
    int total = 0, first = 0;

    sprintf(imgNo, "%03i.jpg", total);
    FILE *img = fopen(imgNo, "w");

    while(fread(&bytes, sizeof(BYTE), 512, memory))
    {
        //Checking the first 4 bytes
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] &0xf0) == 0xe0)
        {   
            //If its the start of the first image
            if(total == 0)
            {
                first = 1;
                fwrite(&bytes, sizeof(BYTE), 512, img);
                total++;
            }
            //If its a start of a new image but not the first image
            else
            {
                fclose(img);
                sprintf(imgNo, "%03i.jpg", total);
                fopen(imgNo, "w");
                fwrite(&bytes, sizeof(BYTE), 512, img);
                total++;

            }
        }
        //If its not a start of a new file we just continue to copy image contents from the image
        else if (first == 1)
        {
            fwrite(&bytes, sizeof(BYTE), 512, img);
        }

    }

   fclose(memory);
   free(imgNo);
   return 0;
}