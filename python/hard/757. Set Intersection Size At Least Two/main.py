from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        # primeiro precisa ordenar

        intervals.sort ( key =  lambda x : ( x [ 1 ], - x [ 0 ]))

        # define o valor de retorno como 0 para ser incrementado ao longo da execução

        set_min_size = 0

        # define valores de controle

        maior = float ('-inf')

        segundo_maior = float ('-inf')


        for start, end in intervals:
            if start > maior:
                set_min_size += 2
                maior = end
                segundo_maior = end -1
            elif start > segundo_maior:
                set_min_size += 1
                segundo_maior = maior
                maior = end

        return set_min_size


sol = Solution ()

nums = [[1, 3], [3, 7], [8, 9]]

print (sol.intersectionSizeTwo (nums))