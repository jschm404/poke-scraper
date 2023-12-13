from urllib.request import urlopen
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

