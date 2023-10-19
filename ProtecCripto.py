def encrypt(msg):
    GO_HAED = 4
    COME_BACK = 3
    result = ''

    upper_letter = [chr(letter) for letter in range(65, 91)]
    lower_letter = [chr(letter) for letter in range(97, 123)]

    for letter in msg:
        if upper_letter.count(letter) != 0:
            try:
                letter = upper_letter[upper_letter.index(letter) - COME_BACK]
            except IndexError:
                letter = upper_letter[::-COME_BACK]
            finally:
                result += letter.lower()
        if lower_letter.count(letter) != 0:
            try:
                letter = lower_letter[lower_letter.index(letter) + GO_HAED]
            except IndexError:
                letter = chr(ord(letter) - 22)
            finally:
                result += letter.upper()

    print(result)

encrypt('abcdWXYZ')