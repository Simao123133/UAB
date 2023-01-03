import string


def buildMatrix(keyword):
    keyword = list(dict.fromkeys(keyword.replace('j', 'i')))
    remainingAlphabet = ''.join([c for c in string.ascii_lowercase if c not in keyword]).replace('j','')

    letterToRow = {}
    letterToCol = {}
    matrix = [[0 for j in range(0, 5)] for i in range(0, 5)]
    allLetters = keyword + list(remainingAlphabet)
    letterIdx = 0

    for row in range(0, 5):
        for col in range(0 ,5):
            letterToRow[allLetters[letterIdx]] = row 
            letterToCol[allLetters[letterIdx]] = col
            matrix[row][col] = allLetters[letterIdx]
            letterIdx += 1

    letterToRow['j'] = letterToRow['i']
    letterToCol['j'] = letterToCol['i']
        
    return matrix, letterToRow, letterToCol
            

def encrypt(message, matrix, letterToRow, letterToCol):

    encryptedMessage = ""
    if len(message) % 2 != 0:
        message += "x"

    for idx in range(0, len(message), 2): 
        if  message[idx] == message[idx+1]:
            encryptedMessage += message[idx] + 'x'
        elif letterToRow[message[idx]] == letterToRow[message[idx+1]]:
            row = letterToRow[idx]
            firstCol = circShiftRight(letterToCol[message[idx]])
            secondCol = circShiftRight(letterToCol[message[idx+1]])
            encryptedMessage += matrix[row][firstCol] + matrix[row][secondCol]
        elif letterToCol[message[idx]] == letterToCol[message[idx+1]]:
            col = letterToCol[message[idx]]
            firstRow = circShiftRight(letterToRow[message[idx]])
            secondRow = circShiftRight(letterToRow[message[idx+1]])
            encryptedMessage += matrix[firstRow][col] + matrix[secondRow][col]
        else:
            letter1 = matrix[letterToRow[message[idx]]][letterToCol[message[idx+1]]]
            letter2 = matrix[letterToRow[message[idx+1]]][letterToCol[message[idx]]]
            encryptedMessage += letter1 + letter2

    return encryptedMessage

def circShiftRight(idx):
    if idx == 4:
        return 0
    else:
        return idx + 1


def main():
    keyword = "monarchy"
    matrix, letterToRow, letterToCol = buildMatrix(keyword)
    message = "NinguemVaiDescobrir".lower()
    encryptedMessage = encrypt(message, matrix, letterToRow, letterToCol)
    print("original message", message)
    print("encoded message", encryptedMessage)
    


if __name__ == "__main__":
    main()