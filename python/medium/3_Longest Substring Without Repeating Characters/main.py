class Solution:
    def lengthOfLongestSubstring(self, s ):
        i = 0
        j = 0
        maior = 0
        values = set ()

        while j < len ( s ):
            if s [ j ] not in values:
                values.add ( s [ j ])
                if maior < len ( values ):
                    maior = len ( values )
                j += 1
            else:
                values.remove ( s [ i ] )
                i += 1
        return maior



sol = Solution ()

s = "abbacbb"

n = sol.lengthOfLongestSubstring ( s )

print ( n )


 