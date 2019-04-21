import urllib
from bs4 import BeautifulSoup
import time

url = "https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #leaving out 'html.parser' yielded the following output in terminal:
'''
C:\Users\Shail\Anaconda3\lib\site-packages\bs4\__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 6 of the file 20190420_checkUniqueTextFromWebpage.py. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

  markup_type=markup_type))
'''

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
print ('*'*50)
beg = time.time()
print (len(set(text)))
end = time.time()
timeTaken = end - beg
print ("Time taken to check number of unique characters on webpage: " + timeTaken)