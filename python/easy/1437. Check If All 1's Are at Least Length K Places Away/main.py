from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        # encontrar o primeiro 1

        i = 0

        while ( i < len ( nums ) and nums [ i ] != 1 ):
            i += 1

        # tem que começar o algoritmo pelo próximo

        i += 1

        count = 0

        while ( i < len ( nums )):
            if ( nums [ i ] == 0 ):
                count += 1
            else:
                if ( count < k ):
                    return False
                else:
                    count = 0
            i += 1

        return True 




S = Solution ()

numss = [1, 0, 0, 0, 1, 0, 0, 1]

print ( S.kLengthApart ( numss, 3))


        
