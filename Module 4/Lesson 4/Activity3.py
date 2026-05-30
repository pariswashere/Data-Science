def romantoint(number):
    roman = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }
    resultInt = 0

    for i in range(0, len(number)-1):
        if roman[number[i]] < roman[number[i+1]]:
            resultInt = resultInt - roman[number[i]]

        else:
            resultInt = resultInt + roman[number[i]]

    return resultInt + roman[number[-1]]

number = input("Enter the roman numeral : ")
print('Integer equivalent : ',romantoint(number))