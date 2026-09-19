'''Real world Eg: Multithreaing for i?o bound tasks
web Scraping
Involves making numerous network requests to fetch web pages .These taks are i?o bound spend more time for responses from servers.
improve performance by using multithreading to handle multiple requests concurrently.
'''

import threading 
import requests
from bs4 import BeautifulSoup

urls=[
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/concepts/'
]
def fetch_url(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'fetched{len(soup.text)} characaters from {url}')
    
threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_url,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()   
    
print("All URLs fetched.")         