import re


def format_file(inputFile, outputFile):
    #Please call the function with the path of the input and the output file.
    count=0
    subCount=0
    subCount1=0
    subCount2=0

    plus = "+"
    minus = "-"
    currentVal = plus

    fo = open(inputFile, "rb+")
    fw = open(outputFile, "wb+")
    regEx_expression = "^[\\*\\.].*"

    while True:
        currentLine = fo.readline()
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
                    fw.write(modLine)
                elif(length == 2):
                    subCount = subCount + 1
                    subCount1=0
                    subCount2=0
                    modLine= currentLine.replace(symbol, str(count)+"."+str(subCount))
                    fw.write(modLine)
                elif(length == 3):
                    subCount1= subCount1 + 1
                    subCount2=0
                    modLine= currentLine.replace(symbol, str(count)+"."+str(subCount)+"."+str(subCount1))
                    fw.write(modLine)
                elif(length == 4):
                    subCount2= subCount2 + 1
                    modLine= currentLine.replace(symbol, str(count)+"."+str(subCount)+"."+str(subCount1)+"."+str(subCount2))
                    fw.write(modLine)
                else:
                    fw.write(currentLine)
                    fw.write(modLine)
            elif re.match("^\\.{1,4}", symbol):
                dotLength= len(symbol)
                if( dotLength ==1):
                    modLine= currentLine.replace(symbol, " "+currentVal)
                    currentVal = minus
                    fw.write(modLine)
                elif( dotLength ==2):
                    modLine= currentLine.replace(symbol, "  "+currentVal)
                    currentVal = plus
                    fw.write(modLine)
                elif( dotLength ==3):
                    modLine= currentLine.replace(symbol, "   "+currentVal)
                    currentVal = minus
                    fw.write(modLine)
                elif( dotLength ==4):
                    modLine= currentLine.replace(symbol, "    "+currentVal)
                    currentVal = plus
                    fw.write(modLine)
                else:
                    fw.write(currentLine)
        else:
            fw.write(currentLine)

    fw.close()
