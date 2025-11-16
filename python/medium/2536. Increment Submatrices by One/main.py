# my idea is use brute force

from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        # preenchemos a matriz, usando forca bruta 

        m = []
        
        for i in range ( n ):
            L = []
            for j in range ( n ):
                num = 0
                for query in queries:
                    rowStart = query [ 0 ]
                    colStart = query [ 1 ]
                    rowEnd   = query [ 2 ]
                    colEnd   = query [ 3 ]

                    if ( i >= rowStart and i <= rowEnd ):
                        if ( j >= colStart and j <= colEnd):
                            num += 1  
                L.append ( num )
            m.append ( L )
        return m


    def rangeAddQueries2(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        # aqui seria usando uma logica diferente da força bruta ( mas da quase no mesmo ) que depende das diferenças de linhas

        m = []

        for i in range ( n ):
            L = []
            for j in range ( n + 1 ):
                L.append ( 0 )
            m.append ( L )

        for query in queries:
            rowStart = query [ 0 ]
            colStart = query [ 1 ]
            rowEnd   = query [ 2 ]
            colEnd   = query [ 3 ]

            while rowStart <= rowEnd:
                m [ rowStart ][ colStart] += 1
                m [ rowStart ][ colEnd + 1] -= 1
                rowStart += 1
            
        for i in range ( n ):
            for j in range ( 1, n + 1):
                m [ i ][ j ] = m [ i ][ j ] + m [ i ][ j - 1]
        
        return m

    def rangeAddQueries3(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        # aqui seria definindo o tam correto do array porque a de cima fica errado

        m = []

        m2 = []

        for i in range ( n ):
            L = []
            for j in range ( n + 1 ):
                L.append ( 0 )
            m.append ( L )


        for query in queries:
            rowStart = query [ 0 ]
            colStart = query [ 1 ]
            rowEnd   = query [ 2 ]
            colEnd   = query [ 3 ]

            while rowStart <= rowEnd:
                m [ rowStart ][ colStart] += 1
                m [ rowStart ][ colEnd + 1] -= 1
                rowStart += 1
            
        for i in range ( n ):
            L2 = []
            for j in range ( n ):
                if ( j == 0 ):
                    L2.append ( m [ i ][ j ])
                else:
                    m [ i ] [ j ] +=  m [ i ][ j - 1]
                    L2.append ( m [ i ][ j ])
            m2.append ( L2 )
        
        return m2

    def rangeAddQueries4(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        # criar matriz e preencher com 0 // melhor versão e a mais clara também

        m = []

        for i in range ( n + 1 ):
            L = []
            for j in range ( n + 1):
                L.append ( 0 )
            m.append ( L )

        # marcar os valores dos queries na matriz 

        for query in queries:
            r1 = query [ 0 ]
            c1 = query [ 1 ]
            r2 = query [ 2 ]
            c2 = query [ 3 ]

            m [ r1 ][ c1 ] += 1
            m [ r1 ][ c2 + 1] -= 1
            m [ r2 + 1][ c1 ] -= 1
            m [ r2 + 1 ][ c2 + 1 ] += 1
        
        #prefix horizontal

        for i in range ( n + 1 ):
            for j in range ( 1, n + 1):
                m [ i ][ j ] +=  m [ i ][ j - 1]

        # prefix vertical

        for i in range ( 1, n + 1 ):
            for j in range ( n + 1):
                m [ i ][ j ] += m [ i - 1][ j ]

        m2 = []

        for i in range ( n ):
            L2 = []
            for j in range ( n ):
                L2.append ( m [ i ][ j ])
            m2.append ( L2 )

        return m2

    def rangeAddQueries5 (self, n: int, queries: List[List[int]]) -> List[List[int]]:

        m = []

        for i in range ( n + 1):
            L = []
            for j in range ( n + 1 ):
                L.append ( 0 )
            m.append ( L )

        
        for query in queries:
            r1, c1, r2, c2 = query [ 0 ], query [ 1 ], query [ 2 ], query [ 3 ]

            m [ r1 ][ c1 ] += 1
            m [ r1 ][ c2 + 1] -= 1
            m [ r2 + 1][ c1 ] -= 1
            m [ r2 + 1 ][ c2 + 1] += 1

        m2 = []

        for i in range ( n ):
            L2 = []
            for j in range ( n ):
                if ( i > 0 ):
                    m [ i ][ j ] += m [ i - 1][ j ]
                if ( j > 0 ):
                    m [ i ][ j ] += m [ i ][ j - 1]
                if ( i > 0 ) and ( j > 0 ):
                    m [ i ][ j ] -= m [ i - 1][ j - 1]
                
                L2.append ( m [ i ][ j ])
            m2.append( L2 )

        return m2

            

    

def printMatrizQuadrada ( L, n ):
    for i in range ( n ):
        for j in range ( n ):
            print (f"{L[i][j]} ", end = "")
        print ()



S = Solution ()

queries = [ [0, 0, 1, 1], [ 1, 1, 2, 2]]

m3 = S.rangeAddQueries5( 3, queries)

printMatrizQuadrada ( m3, 3)

                    
                    




