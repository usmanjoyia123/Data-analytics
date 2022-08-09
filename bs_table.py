# Importing the Libraries
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

# Inializing the Soup object
wikipedia_link = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
html_page = urlopen(wikipedia_link)
soup = BeautifulSoup(html_page)

# Retrieving the desired Table
billionaires_table = soup.find("table", class_="wikitable sortable")
table_body = billionaires_table.find("tbody")

# Parsing the <tr> tags to retrieve the relevant stuff
count = 0
data = list()
table_rows = table_body.find_all("tr")

for row in table_rows:
    if count == 0:
        # As the first <tr> contains the Header of Table
        cols = row.find_all("th")
        count = count + 1
    else:
        cols = row.find_all("td")
        
    cols = [elem.text.strip() for elem in cols]
    data.append([elem for elem in cols if elem])

# Constructing the Dataframe from the extacted rows.
dataframe = pd.DataFrame(columns=data[0])
for i in range(1,len(data)):
    dataframe = dataframe.append(pd.Series(data[i], index=data[0]), ignore_index=True)


print("The constructed Dataframe is \n")
print(dataframe.to_string())