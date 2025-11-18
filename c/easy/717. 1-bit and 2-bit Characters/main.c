
# define bool int

# define true 1

# define false 0

# include <stdio.h>

bool isOneBitCharacter(int* bits, int bitsSize) {

    int i, last;
    if ( bits != NULL ){
        if ( bitsSize > 0 ){
            i = 0;
            while ( i < bitsSize ){
                last = bits [ i ];
                if ( bits [ i ] == 1){
                    i++;
                }
                i++;                
            }
            if ( last == 0 && i <= bitsSize ){
                return true;
            }

        }
    }
    return false;
}

int main ( void ){
    int nums [ 4 ] = { 1, 0, 1, 0};

    printf ("%d \n", isOneBitCharacter ( nums, 4 ));

    return 0;
}