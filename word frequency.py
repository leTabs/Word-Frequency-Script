# word frequency
sentence = input('Enter a sentece:')


def removal(setning):
    setning = setning.strip()
    symbols = ['!', '@', '#', '$', '%', '^', '&','*','(',')','-', '/', '?', ',', '.']
    for symbol in symbols:
        if symbol in setning:
            setning =  setning.replace(symbol, '')
        else: pass
    setning = setning.upper().split(' ')
    word_requency = {}

    for word in setning:
        if word in word_requency:
            word_requency[word] += 1
        else:
            word_requency[word] = 1

    for key, value in word_requency.items():
        print(f'{key} : {value}' )

removal(sentence)
