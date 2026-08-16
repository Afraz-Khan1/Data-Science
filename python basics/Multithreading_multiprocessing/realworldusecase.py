import threading
from bs4 import BeautifulSoup
import requests # used for accessing or reading text from html pages

urls=[
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/"
]

def count_words(urls):
 
   response=requests.get(urls) # sends a get request to the site to get permission of the contents of the url
   soup=BeautifulSoup(response.content,"html.parser") #html parser to get the content inside the html page.
   print(f"Fetched {len(soup.text)} character in the {urls}")

threads=[]

for url in urls: # Need to traverse through urls to change url in new thread.
   thread=threading.Thread(target=count_words,args=(url,)) #thread variable is overwritten as it already appends in threads every iteration.
   threads.append(thread)
   thread.start()

for thread in threads: # Waiting for all threads to complete, else the main thread which is this program running will stop early.
   thread.join()

print("All Webpages Are Fetched")