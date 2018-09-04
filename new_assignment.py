import re
import sys


count=0
subCount=0
subCount1=0
subCount2=0

plus = "+"
minus = "-"
currentVal = plus

#fo = open(inputFile, "rb+")
#fw = open(outputFile, "wb+")

regEx_expression = "^[\\*\\.].*"





for currentLine in sys.stdin:
    if not currentLine: break
    if re.match(regEx_expression, currentLine):
        symbol = currentLine[0:currentLine.index(' ')]
        if re.match("^\\*{1,4}", symbol):
            length= len(symbol)
            if(length == 1):
                count = count + 1;
                subCount=0
                subCount1=0
                subCount2=0
                modLine= currentLine.replace(symbol, str(count))
                print modLine
            elif(length == 2):
                subCount = subCount + 1
                subCount1=0
                subCount2=0
                modLine= currentLine.replace(symbol, str(count)+"."+str(subCount))
                print(modLine)
            elif(length == 3):
                subCount1= subCount1 + 1
                subCount2=0
                modLine= currentLine.replace(symbol, str(count)+"."+str(subCount)+"."+str(subCount1))
                print(modLine)
            elif(length == 4):
                subCount2= subCount2 + 1
                modLine= currentLine.replace(symbol, str(count)+"."+str(subCount)+"."+str(subCount1)+"."+str(subCount2))
                print(modLine)
            else:
                print(currentLine)
                print(modLine)
        elif re.match("^\\.{1,4}", symbol):
            dotLength= len(symbol)
            if( dotLength ==1):
                modLine= currentLine.replace(symbol, " "+currentVal)
                currentVal = minus
                print(modLine)
            elif( dotLength ==2):
                modLine= currentLine.replace(symbol, "  "+currentVal)
                currentVal = plus
                print(modLine)
            elif( dotLength ==3):
                modLine= currentLine.replace(symbol, "   "+currentVal)
                currentVal = minus
                print(modLine)
            elif( dotLength ==4):
                modLine= currentLine.replace(symbol, "    "+currentVal)
                currentVal = plus
                print(modLine)
            else:
                print(currentLine)
    else:
        print(currentLine)
