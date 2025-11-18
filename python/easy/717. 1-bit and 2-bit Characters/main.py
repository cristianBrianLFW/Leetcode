from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while ( i < len ( bits )):
            last = bits [ i ]
            if ( bits [ i ] == 1 ):
                i += 1
            i += 1
        if i > len ( bits ) or last == 1:
            return False
        return True

S = Solution ()

newBits = [1, 0, 0, 1]

print ( S.isOneBitCharacter ( newBits ))