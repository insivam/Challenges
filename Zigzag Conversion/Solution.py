def convert(s, numRows):
    if numRows == 1:
        return s

    number = []
    n = 0
    forward = True
    word = ""

    for letter in s:

        if n == numRows:
            forward = False
        elif n == 1:
            forward = True

        if forward == True:
            n += 1
        else:
            n -= 1

        number.append(n)

    for i in range(1, numRows + 1):
        for c, item in enumerate(number):
            if item == i:
                word += s[c]

    return(word)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(convert(s, numRows) == "PAHNAPLSIIGYIR")

    numRows = 4
    print(convert(s, numRows) == "PINALSIGYAHRPI")
