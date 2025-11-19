from typing import List

def quicksort ( arr: List [ int ], left: int, right: int ):
    if left < right:
        pi = partition ( arr, left, right )
        quicksort ( arr, left, pi -1 )
        quicksort ( arr, pi + 1, right )

def partition ( arr: List [ int ], left: int, right: int ) -> int:
    pivot = arr [ right ]

    i = left - 1

    for j in range ( left, right ):
        if arr [ j ] <= pivot:
            i += 1
            arr [ j ], arr [ i ] = arr [ i ], arr [ j ]
    
    arr [ i + 1], arr [ right ] = arr [ right ], arr [ i + 1]

    return i + 1

class Solution:

    # esse jeito foi para treinar quicksort

    def findFinalValue(self, nums: List[int], original: int) -> int:

        quicksort ( nums, 0, len ( nums ) - 1)

        for num in nums:
            if ( num == key ):
                original *= 2
        
        return original 

    def findFinalValue2 (self, nums: List[int], original: int) -> int:
        nums = set ( nums )

        while original in nums:
            original *= 2
        
        return original

sol = Solution ()

arr2 = [5, 3, 6, 1, 12]

print ( sol.findFinalValue ( arr2, 7))



        