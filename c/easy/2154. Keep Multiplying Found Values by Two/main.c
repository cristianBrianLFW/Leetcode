# include <stdio.h>

# include <stdlib.h>

int partition (int * nums, int left, int right ){
    int i, j, pivo, temp;

    i = left -1;
    j = left;
    pivo = nums [ right ];

    for ( j; j < right; j++){
        if ( nums [ j ] <= pivo ){
            i++;
            temp = nums [ j ];
            nums [ j ] = nums [ i ];
            nums [ i ] = temp;
        }
    }

    temp = nums [ i + 1];
    nums [ i + 1 ] = nums [ right ];
    nums [ right ] = temp;

    return i + 1;
}

void quicksort ( int * nums, int left, int right ){
    int pi;
    
    if ( left < right ){
        pi = partition ( nums, left, right );
        quicksort ( nums, left, pi - 1);
        quicksort ( nums, pi + 1, right );
    }
}

int findFinalValue(int* nums, int numsSize, int original) {

    int i;

    if ( nums != NULL ){
        if ( numsSize > 0 ){
            quicksort ( nums, 0, numsSize - 1);

            for ( i = 0; i < numsSize; i++){
                if ( nums [ i ] == original ){
                    original *= 2;
                }
            }
        }
    }

    return original;   
    
}


 
void printArr ( int * nums, int numsSize ){
    int i = 0;
    if ( nums != NULL ){
        while ( i < numsSize ){
            printf ("%d ", nums [ i ]);
            i++;
        }
    }
    printf ("\n");
}


int main ( void ){
    int nums [ 5 ] = { 5, 3, 6, 1, 12};

    quicksort ( nums, 0, 4);

    printArr ( nums, 5);

    printf ("%d\n", findFinalValue( nums, 5, 3));

    return 0;

}