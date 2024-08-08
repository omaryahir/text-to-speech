
import os


file = open("text.txt", "r")
text = file.read()
text = text.replace('\n',' ').replace('\r',' ').replace("'","´")

language = text[0:7]
print(f"Language: {language}")
print("---")
print(text)

if language == "English":
    # English
    os.system(f"say -v Samantha -o output.aiff \"{text}\"")
else:
    # Spanish
    os.system(f"say -v Samantha -o output.aiff \"{text}\"")


