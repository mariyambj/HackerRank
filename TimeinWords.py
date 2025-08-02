def timeInWords(h, m):
    numbers = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty"
    }

    def get_word(n):
        if n in numbers:
            return numbers[n]
        else:
            tens = (n // 10) * 10
            ones = n % 10
            if ones == 0:
                return numbers[tens]
            else:
                return f"{numbers[tens]} {numbers[ones]}"

    if m == 0:
        return f"{get_word(h)} o' clock"
    elif m == 1:
        return f"one minute past {get_word(h)}"
    elif m == 15:
        return f"quarter past {get_word(h)}"
    elif m == 30:
        return f"half past {get_word(h)}"
    elif m == 45:
        return f"quarter to {get_word((h % 12) + 1)}"
    elif m < 30:
        return f"{get_word(m)} minutes past {get_word(h)}"
    else:
        return f"{get_word(60 - m)} minutes to {get_word((h % 12) + 1)}"

print(timeInWords(2, 7))  # seven minutes past two
print(timeInWords(7, 29))  # twenty nine minutes past seven
print(timeInWords(6, 35))  # twenty five minutes to seven

