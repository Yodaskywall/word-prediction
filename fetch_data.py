from bs4 import BeautifulSoup
import requests
import string


source = requests.get("https://www.gutenberg.org/files/28054/28054-h/28054-h.html").text
soup = BeautifulSoup(source, "lxml")

paragraphs = soup.findAll("span", class_="tei-q")
processed_string = ""

for paragraph in paragraphs:
    paragraph = paragraph.text.strip("\n")

    for char in paragraph:
        if char in string.printable and char not in ["\n", "\r", "\t", "!", "?"]:
            processed_string += char

processed_string = processed_string.lower()

sentences = processed_string.split(".")

with open("text.txt", "w") as file:
    for sentence in sentences:
        sentence = sentence.split(" ")
        print(sentence)
        if len(sentence) > 1 or sentence != [""]:

            for word in sentence[:-1]:
                word = word.strip(",")
                if (word not in [" "] and word != "" and len(word) >= 2) or word == "a":
                    file.write(word + ",")

            if len(sentence[-1]) >= 2 or sentence[-1] == "a":
                file.write(sentence[-1])

            file.write("\n")

