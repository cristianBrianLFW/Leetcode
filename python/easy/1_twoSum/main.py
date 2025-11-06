class Solution:
    def twoSum(self, nums, target):
      L = []
      tabela = {}
      for i, num in enumerate (nums):
        value = target - num
        if value in tabela:
            L.append ( tabela [ value ])
            L.append ( i )
            return L
        else:
            tabela[ num ] = i


S = Solution ()

nums = [ 2, 7, 11, 15]

target = 9

print ( S.twoSum ( nums, target))

