#include <stdio.h>

int main(){
int row, column, number;
int sum = 0;
int product = 1;

printf("Type the value of the row and column separated by space: ");
scanf("%d %d", &row, &column);

int matrix[row][column];

for (int i = 0; i < row; i++){
    printf("Enter %d integers in row %d: ", column, i + 1);
    for (int j = 0; j < column; j++){
        scanf("%d", &number);
        matrix[i][j] = number;
        sum += number;
        product *= number;
    }
}

printf("\n");

for (int i = 0; i < row; i++){
    for (int j = 0; j < column; j++){
        printf("%d ", matrix[i][j]);
    }
    printf("\n");
}

printf("\nSum: %d\nProduct: %d\n", sum, product);
return 0;
}
