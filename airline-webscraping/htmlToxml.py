import BeautifulSoup
f = open('https://www.interjet.com/en-us')
soup = BeautifulSoup.BeautifulSoup(f)
f.close()
g = open('a.xml', w)
print >>g, soup.prettify()
g.close()

