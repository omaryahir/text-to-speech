
import os


file = open("text.txt", "r")
text = file.read()
text = text.replace('\n',' ').replace('\r',' ').replace("'","´")
print(text)

os.system(f"say -v Samantha -o output.aiff \"{text}\"")
