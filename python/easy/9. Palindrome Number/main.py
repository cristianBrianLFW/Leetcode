class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        copy = x

        while x > 0:
            num *= 10
            num += ( x % 10 )
            x //= 10
           
        if ( num == copy ):
            return True
        
        return False
    


s = Solution ()

a = s.isPalindrome ( 121 )