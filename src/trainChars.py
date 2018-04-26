#!/usr/bin/env python3

from lstmTesting import *

if __name__ == "__main__":
    allScripts = getData()
    script1 = '\n'.join(allScripts)
    #script1 = allScripts[0]
    
    chars = sorted(list(set(script1)))
    charsToInt = dict((char, i) for i, char in enumerate(chars))
    uniqueChars = len(charsToInt)

    lengthOfSequence = 100
    data, targets = prepSequences(script1, charsToInt, sequenceLength = lengthOfSequence)
    preppedX = prepX(data, lengthOfSequence, uniqueChars)
    preppedY = prepY(targets)
    
    model = generateModel(preppedX, preppedY)
    model = trainModel(model, preppedX, preppedY, numEpochs= 1)

    ###uncomment to load best weights
    #filename = "weights-improvement-19-1.9435.hdf5" #replace with best weights file
    #model.load_weights(filename)
    #model.compile(loss='categorical_crossentropy', optimizer='adam')

    intToChar = dict((i, char) for i, char in enumerate(chars))  #creating a demapping of our original encoding
    seed = generateSeedFromData(data) #get a random starting point from our paper and let the network continue the writing
    numCharacters= 100   #length of each window the network will use to predict the output
    text = generateText(model, seed, intToChar, length= numCharacters, vocabSize= numUniqueChars)
    with open("generated_chars.txt", 'w+') as file:
        file.write(text)
