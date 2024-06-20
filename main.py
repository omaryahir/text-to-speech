
import os


file = open("text.txt", "r")
text = file.read()
text = text.replace('\n',' ').replace('\r',' ')

os.system(f"say -v Samantha {text}")
