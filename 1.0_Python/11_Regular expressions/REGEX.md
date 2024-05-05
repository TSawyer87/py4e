- The task of searching and extracting is so common that Python has a very powerful library called *regular expressions*.
- Regular expressions are almost their own language for searching and parsing strings.
- The regular expression library `re` must be imported into your program before you can use it.
- The simplest use of the regex library is the `search()` function.
```python
# Search for lines that contain 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
```
- We open the file, loop through each line, and use the regex `search()` to only print lines that contain 
  "From: ".
- This program doesn't use the real power of regex, since we could have just as easily used `line.find()` here.

- The power of regex comes when we add special characters to the search string that allow us to more precisely control which lines match the string.
- The caret character is used in regex to match "the beginning" of a line.
- We could change our program to only match lines where "From: " was at the beginning of the line:
```python
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
```
- Now we only match lines that *start with* the string "From:"
