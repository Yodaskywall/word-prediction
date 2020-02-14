import random

text = [[""]]

with open("text.txt", "r") as file:
    data = file.read()

    i = 0
    j = 0

    for char in data:

        if char == ",":
            j += 1
            text[i].append("")

        elif char == "\n":
            j = 0
            i += 1
            text.append([""])

        else:
            text[i][j] += char



class Chain:
    def __init__(self):
        self.data = {"" : {}}
        self.prob = {}

    def train(self, text):
        for sentence in text:
            for i in range(len(sentence)):
                word = sentence[i]
                if i == 0:
                    if word in self.data[""]:
                        self.data[""][word] += 1

                    else:
                        self.data[""][word] = 1

                elif i == 1:
                    previous_word = sentence[i-1]
                    if previous_word not in self.data:
                        self.data[previous_word] = {}

                    if word in self.data[previous_word]:
                        self.data[previous_word][word] += 1

                    else:
                        self.data[previous_word][word] = 1

                else:
                    previous_words = sentence[i - 2] + "." + sentence[i-1]
                    if previous_words not in self.data:
                        self.data[previous_words] = {}

                    if word in self.data[previous_words]:
                        self.data[previous_words][word] += 1

                    else:
                        self.data[previous_words][word] = 1

        for previous_word in self.data:
            self.prob[previous_word] = {}
            c = 0
            p = 0
            for word in self.data[previous_word]:
                c += self.data[previous_word][word]

            for word in self.data[previous_word]:
                p += self.data[previous_word][word] / c
                self.prob[previous_word][word] = p

    def predict(self, string):
        sentence = string.split(".")[-1].split(" ")

        if sentence == [""]:
            n = random.random()
            for word in self.prob[""]:
                if n <= self.prob[""][word]:
                    sentence = [word]
                    break

        elif len(sentence) == 1:
            previous = sentence[0]
            n = random.random()
            try:
                for word in self.prob[sentence[0]]:
                    print("xd")
                    if n <= self.prob[sentence[0]][word]:
                        print(sentence)
                        sentence = [sentence[0], word]
                        break
                if len(sentence) == 1:
                    for prev in self.prob:
                        if prev[-len(previous)] in [previous, "."+previous]:
                            for word in self.prob[prev]:
                                if n <= self.prob[prev][word]:
                                    print(sentence)
                                    sentence = [prev, word]
                                    break

            except Exception as e:
                print(e)

        else:
            n = random.random()
            previous_words = sentence[-2] + "." + sentence[-1]
            try:
                for word in self.prob[previous_words]:
                    if n <= self.prob[previous_words][word]:
                        sentence.append(word)
                        break

            except Exception as e:
                print(e)

        return sentence

chain = Chain()
chain.train(text)

import pickle

with open("chain.pkl", "wb") as file:
    pickle.dump(chain, file)