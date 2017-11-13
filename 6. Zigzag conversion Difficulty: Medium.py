#python3
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rowsOfLetters = [ [] for _ in range(numRows) ]
        # print(json.dumps( rowsOfLetters ))
        lastRow = numRows-1
        firstRow = currentRow = 0
        climbingToLastRow = True
        climbingToFirstRow = False
        for c in s:
            # print("for " + c, end=' when ')
            if ( climbingToLastRow ):
                # print("climbingToLastRow")
                # print("::currentRow="+ str(currentRow))
                # print("::lastRow="+str(lastRow))
                if ( currentRow <= lastRow ):
                    rowsOfLetters[ currentRow ].append(c)
                    currentRow += 1
                if (currentRow > lastRow):
                    climbingToLastRow = False
                    climbingToFirstRow = True
                    currentRow = lastRow-1 if numRows > 1 else 0
            elif ( climbingToFirstRow ):
                # print("climbingToFirstRow")
                # print("::currentRow="+ str(currentRow))
                # print("::firstRow="+str(firstRow))
                if (currentRow >= firstRow):
                    rowsOfLetters[ currentRow ].append(c)
                    currentRow -= 1
                if (currentRow < firstRow):
                    climbingToLastRow = True
                    climbingToFirstRow = False
                    currentRow = firstRow if numRows == 1 else firstRow+1 
            # print(json.dumps( rowsOfLetters ))
        return ''.join( str(c) for row in rowsOfLetters for c in row  )
          # ''.join([str(item) for sublist in a for item in sublist])
        
''' 
P Y A I H R N 
A P L S I I G

P  A   H   N
A P L S I I G
Y   I   R

P     P     I
A   Y A   H R
Y A   L S   I G
P     I     N

        P     h
        a   s i
        y  i  r
        p l   i g
        a     n
'''

def stringToString(input):
    input = input[1:-1].encode('latin1')
    return input.decode('unicode_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.__next__()
            s = stringToString(line);
            line = lines.__next__()
            numRows = int(line);
            
            ret = Solution().convert(s, numRows)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
