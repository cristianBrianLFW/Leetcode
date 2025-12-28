class Solution:
    def bestClosingTime(self, customers: str) -> int:
        L = []
        count = 0
        for elem in customers:
            if ( elem == 'Y'):
                L.append ( 1 )
                count += 1
            else:
                L.append ( 0 )
        Z = []

        Z.append ( count )

        for x, elem in enumerate (L):
            if ( elem == 1):
                Z.append( Z [ x ] - 1)
            else:
                Z.append ( Z [ x ] + 1)
        
                
