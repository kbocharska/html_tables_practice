import requests
import bs4
import csv

resource = requests.get("https://data.uoi.ua/contest/uoi/2024/results")

site = bs4.BeautifulSoup(resource.content, "html.parser")
table_body = site.select(".table > tbody > tr")
table_head = site.select(".table > thead > tr > th")
TABLE = []


row_head = []
for tr in table_head:
    row_head.append(tr.text)
row_head = row_head[:4] + row_head[12:]
TABLE.append(row_head)


for tr in table_body:
    row = []
    for td in tr.select("td"):
        row.append(td.text)
    row = row[:4] + row[12:]
    TABLE.append(row)

for i in TABLE:
    print(i)

with open("first_place.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    counter = 1
    for indx, row in enumerate(TABLE):
        if indx == 0:
            writer.writerow(row)
        if row[-1] == "I":
            row[0] = counter
            writer.writerow(row)
            counter += 1

with open("second_place.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    counter = 1
    for indx, row in enumerate(TABLE):
        if indx == 0:
            writer.writerow(row)
        if row[-1] == "II":
            row[0] = counter
            writer.writerow(row)
            counter += 1

with open("third_place.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    counter = 1
    for indx, row in enumerate(TABLE):
        if indx == 0:
            writer.writerow(row)
        if row[-1] == "III":
            row[0] = counter
            writer.writerow(row)
            counter += 1