class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        total = 0

        for num in s:
            if ( num == '1'):
                count += 1
            else:
                total += ((count * (count + 1)// 2))
                count = 0

        total += ((count * (count + 1)// 2))

        return total


S = Solution ()


print ( S.numSub("0110111"))


                