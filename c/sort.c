
#include <stdio.h>

void printarray(float arr[], int size);
void sort(float arr[], int size);
void descending(float arr[], int size);

int main(void){
    int size;
    float numbers;
    printf("Size? ");
    scanf("%d",&size);
    float arr[size];
    for (int i = 0; i < size; i++){
        printf("Give me the element %d: ", i + 1);
        scanf("%f", &numbers);
        arr[i] = numbers;
    }
    printarray(arr, size);
    printf("\n");
    sort(arr, size);
    printarray(arr, size);
    printf("\n");
    descending(arr,size);
}

void printarray(float arr[], int size){
    for (int i = 0; i < size; i++){
        printf("%.2f ", arr[i]);
    }
}

void descending(float arr[], int size){
    for (int i = size-1; i >= 0; i--){
        printf("%.2f ", arr[i]);
    }
}

void sort(float arr[], int size){
    float temp;
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size-1; j++){
            if (arr[j] >= arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}


