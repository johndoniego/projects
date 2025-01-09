#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
srand(time(NULL));

int low, high, random, guess;
int ctr = 0;
char choices;
_Bool valid;

do{
    valid = 0;
    while (!valid){
        printf("Type the value of low and high separated by space: ");
        if (scanf("%d %d", &low, &high) == 2){
            valid = 1;
        } else {
            printf("Enter valid input with 2 integers separated by space. \n\n");
            while (getchar() != '\n');
        }
    }
    random = rand()% high + low;
        while (guess != random && ctr != 5){
            printf("Guess the number: ");
            if(scanf("%d", &guess) == 1){
                if (guess == random){
                    printf("You guessed correctly: %d\n", random);
                }
                else if (guess>random){
                    printf("Overshoot!\n");
                }
                else if (guess<random){
                    printf("Undershoot!\n");
                }
                valid = 1;
                ctr++;
            }else{
                printf("\nEnter valid input with 1 integer.\n");
                while (getchar() != '\n');
            }
        }
        if (ctr == 5){
            printf("You reached the maximum number of tries. \n");
        }

    printf("Wanna play again? (y/n) :");
    scanf("%c", &choices);

} while (choices == 'y');
return 0;
}
