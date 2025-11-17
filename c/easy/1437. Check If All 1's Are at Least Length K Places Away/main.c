# include <stdio.h>
# include <stdlib.h>

# define true 1
# define false 0

// usa a mesma forma que no python ( a explicação em excalidraw )

int cmp ( int n, int key ){
    if ( n == key ){
        return true;
    }
    return false; 
}

int kLengthApart(int* nums, int numsSize, int k) {

    int i, count, status = false;
    if ( nums != NULL ){
        if ( numsSize > 0 ){
            i = 0;
            status = cmp ( nums [ i ], 1);

            while ( i < numsSize - 1 && status == false ){
                i++;
                status = cmp ( nums [ i ], 1);
            }

            i++;

            count = 0;

            while ( i < numsSize ){
                if ( nums [ i ] == 0 ){
                    count++;
                } else {
                    if ( count < k ){
                        return false;
                    } else {
                        count = 0;
                    }
                }
                i++;
            }
            return true;
        }
    }

    return false;    
}


int main ( void ){
    int nums [ 8 ] = {1, 0, 0, 0, 1, 0, 0, 1};

    printf ("%d", kLengthApart ( nums, 8, 2));
}