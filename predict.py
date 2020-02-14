import pickle
import time
import marcov_chain

with open("chain.pkl", "rb") as file:
    chain = pickle.load(file)

c = 0
close = False
while not close:
    try:
        if c == 0:
            sentence = input("please enter an input: ")
            sentence += " " + chain.predict(sentence)[-1]

        else:
            sentence += " " + chain.predict(sentence)[-1]

    except Exception as e:
        print(sentence)
        close = True

    c += 1
    if c == 50:
        print(sentence)
        close = True