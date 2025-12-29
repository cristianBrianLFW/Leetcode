
# usar busca binaria 

from typing import List

def binarySearch (lista, l, r):

    tam = len ( lista )

    while ( l <= r ):

        if ( lista [ l ] < 0 ):
            return tam - l 

        m = ( r + l ) // 2

        if ( lista [ m ] < 0 ):
            r = m - 1
        else:
            l = m + 1
    
    if ( l < tam ):
        return tam - l
    return 0


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        nNegativos = 0
        
        i = 0
        
        for linha in grid:

            print ( i )

            i += 1
            

            nNegativos += binarySearch ( linha, 0, len ( linha ) - 1)

        return nNegativos
    


resposta = Solution ()

a =  [[3, 0], [2, 1]]
print ( resposta.countNegatives (a))









        