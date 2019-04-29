#!python

def redact_words(arrayOne, arrayTwo):
    result = []
    for word in arrayOne:
        if word not in arrayTwo:
            result.append(word)
    print(result)
    return result

if __name__ == '__main__':
    arrayOne = ['A','B', 'C']
    arrayTwo = ['A']
    redact_words(arrayOne, arrayTwo)

    redact_words(['A', 'B', 'C'], ['B'])

    redact_words(['A', 'B', 'C'], ['C'])