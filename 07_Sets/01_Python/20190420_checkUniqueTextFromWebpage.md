# 20190420_checkUniqueTextFromWebpage.py
The program output of this program is inconsistent for the same webpage. By inconsistent, I'm not taking about the runtime of the program, which understandably may vary each time depending on the machine being used and the other processes that may be running on that machine, but inconsistent in the sense that running the program on the same page multiple times returned a different number of characters each time.

The ```Length of webpage (characters):``` output on the terminal is noticeably inconsistent. Since the number of unique characters on a webpage count is dependent on BeautifulSoup and how it scrapes the page, it makes sense that the number of unique characters is also consistent. Here is a sample of multiple runs of the program with different outputs:

```bash
$ python 20190420_checkUniqueTextFromWebpage.py
The url of the webpage being analyzed is:
https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
**************************************************
Length of webpage (characters):  33097
The number of unique characters on the page is: 116
Time taken to check number of unique characters on webpage (seconds):
0.0009982585906982422


$ python 20190420_checkUniqueTextFromWebpage.py
The url of the webpage being analyzed is:
https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
**************************************************
Length of webpage (characters):  32995
The number of unique characters on the page is: 116
Time taken to check number of unique characters on webpage (seconds):
0.0009968280792236328


$ python 20190420_checkUniqueTextFromWebpage.py
The url of the webpage being analyzed is:
https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
**************************************************
Length of webpage (characters):  32962
The number of unique characters on the page is: 117
Time taken to check number of unique characters on webpage (seconds):
0.0009984970092773438


$ python 20190420_checkUniqueTextFromWebpage.py
The url of the webpage being analyzed is:
https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
**************************************************
Length of webpage (characters):  33100
The number of unique characters on the page is: 116
Time taken to check number of unique characters on webpage (seconds):
0.0009989738464355469


$ python 20190420_checkUniqueTextFromWebpage.py
The url of the webpage being analyzed is:
https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
**************************************************
Length of webpage (characters):  32882
The number of unique characters on the page is: 119
Time taken to check number of unique characters on webpage (seconds):
0.0004994869232177734
```

As we can see, the program being run was the exact same every time (no modifications were made to the program between these runs), but the output varied slightly. Uncertain if the different output is due to inconsistencies with BeautifulSoup parsing, or if there was some content on the webpage being scraped that changed slightly in the time that the program was run. 

Possible things that could change include the time (if the page displays time somewhere on the page), links to other pages that are dynamically updated, the number of comments/upvotes/posts on the page (if someone posts something new in the gap between the previous run and the current run), or perhaps some meta information that BeautifulSoup collects while scraping the page, but isn't apparent by looking at the UI.

This is a topic I want to investigate further, will update as I find more information.