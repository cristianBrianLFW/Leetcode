/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;

    int *p = ( int * ) malloc (sizeof ( int ) * 2);

    if ( p != NULL){
        for ( i = 0; i < numsSize -1; i++){
            for ( j = i + 1; j < numsSize; j++){
                if ( nums[i] + nums[j] == target ){
                    *returnSize = 2;
                    p[0] = i;
                    p[1] = j;
                    return p;
                }
            }
        }
    }

    *returnSize = 0;
    free ( p );
    return NULL;
    
}

/*---------------------------------------------------------------------
                            Ideia do Algoritmo
    Voce tem uma variavel que permite percorrer todos os elementos do
    vetor ate o penultimo ( i )

    Enquanto tem outra que percorre do proximo elemento ate o final do
    vetor ( j )

    Se esse valor em nums [i] + nums[j] == target retornamos 

    Caso nao percorremos por completo e nao encontramos enviamos 
    NULL
-----------------------------------------------------------------------*/

