from urllib.request import urlopen
import re


url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
    #urlopen() returns an HTTPResponse object
page 
    #<http.client.HTTPResponse object at 0x105fef820>
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
    #<html>
    #<head>
    #<title>Profile: Aphrodite</title>
    #...

#extracting information using string methods
title_index = html.find("<title>")
print(title_index)
    #14

start_index = title_index + len("<title>")
print(start_index)
    #21

end_index = html.find("</title>")
print(end_index)
    #39

title = html[start_index:end_index]
print(title)
    #Profile: Aphrodite


#regular expressions - metacharacters denote different patters
#for example, * stans for zero or more instances
re.findall("ab*c", "ac")
    #['ac']
re.findall("ab*c", "abcd")
    #['abc']
re.findall("ab*c", "abcac")
    #['abc', 'abcac']
re.findall("ab*c", "abdc")
    #[]
#there is also ".", which stands for any since character in a regular expression
re.findall("a.c", "abc")
    #['abc']
re.findall("a.c", "abbc")
    #[]
re.findall("a.c", "ac")
    #[]
re.findall("a.c", "acc")
    #['acc']
#they can be used together
re.findall("a.*c", "abc")
    #['abc']
re.findall("a.*c", "abbc")
    #['abbc']
re.findall("a.*c", "ac")
    #['ac']
re.findall("a.*c", "acc")
    #['acc']

