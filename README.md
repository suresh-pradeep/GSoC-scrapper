# GSoC-scrapper
GSoC 2021 results have been scrapped and added into a csv file using various python libraries such as requests, BeautifulSoup,pandas,re.
Requests library has been used for requesting the gzip file from the server and to make it readable by BeautifulSoup.
BeautifulSoup is used to create a soup object to parse the html of the website.
Re is used for various functions involving regular expression used for parsing the strings into useful text and to search through the strings to find the required strings.
Pandas is used to create a data file object using a python dictionary which is subsequently used to write into a csv file.
