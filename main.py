#This is the legal way. 
import time
import random
import webbrowser

f = open("words.txt", "rt")
word = f.read().split()

for x in range(10):
    time.sleep(3)
    words = random.choice(word)

    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    webbrowser.register("microsoft edge",None, webbrowser.BackgroundBrowser(edge_path))

    web = webbrowser.get("microsoft edge").open(f"https://www.bing.com/search?q={words}")
