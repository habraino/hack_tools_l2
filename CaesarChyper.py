def encrypt(key=0, message=''):
    SIMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.?!@#$%&/()=;:-_'
    translated = ''

    for symbol in message:
        if symbol in SIMBOLS:
            symbloIndex = SIMBOLS.find(symbol)
            translatedIndex = symbloIndex + key

            if translatedIndex >= len(SIMBOLS):
                translatedIndex -= len(SIMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SIMBOLS)

            translated += SIMBOLS[translatedIndex]
        else:
            translated += symbol
    print(translated)

def decrypt(key=0, message=''):
    if isinstance(key, int) and isinstance(message, str):
        SIMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.?!@#$%&/()=;:-_'
        translated = ''

        for symbol in message:
            if symbol in SIMBOLS:
                symbloIndex = SIMBOLS.find(symbol)
                translatedIndex = symbloIndex - key

                if translatedIndex >= len(SIMBOLS):
                    translatedIndex -= len(SIMBOLS)
                elif translatedIndex < 0:
                    translatedIndex += len(SIMBOLS)

                translated += SIMBOLS[translatedIndex]
            else:
                translated += symbol
        print(translated)
    else:
        print('Error to Encrypt or Decrypt message!')
