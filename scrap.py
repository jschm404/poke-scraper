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

