from requests import get
from bs4 import BeautifulSoup

query = raw_input("enter search string: \n")
url = "http://en.wikipedia.org/w/api.php?action=opensearch&search=" + query + "&limit=10&namespace=0&format=json"
r = get(url)
data = r.json()

# print data
i = 1
for d in data[1]:
    print str(i) + ":  " + str(d.encode('utf8'))
    i += 1

number = int(raw_input("which exactly is your query ? select from 1 to specify\n"))
url_to_parse = data[3][number-1]
# print url_to_parse
req = get(url_to_parse)

# getting the infobox data
soup = BeautifulSoup(req.content, "html.parser")
gdata = soup.find_all("table", {"class": "infobox vevent"})

# data = gdata[0].get_text().encode('ascii', 'ignore').replace('\n', ' ').split("  ")
data = gdata[0].find_all("th", {"scope": "row"})
value = gdata[0].find_all("td", {"style": "line-height:1.3em;"})
newdata = []
newvalue = []

if data[0].text == "Hindi":
    data.pop(0)
for d in data:
    newdata.append(str(d.text.replace("\n", "")))

for v in value:
    newvalue.append(str(v.text.encode('ascii', 'ignore').replace("\n\n", " ")))


for d, v in zip(newdata, newvalue):
    print "\n{0}: {1}".format(d, v)
