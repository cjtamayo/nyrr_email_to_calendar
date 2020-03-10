import datetime
import eml_parser
from bs4 import BeautifulSoup

with open('email_loc/nyrr_email.eml', 'rb') as fhdl:
    raw_email = fhdl.read()

parsed_eml = eml_parser.eml_parser.decode_email_b(raw_email, include_raw_body=True)

body_html = parsed_eml["body"][0]["content"]

soup = BeautifulSoup(body_html, 'html.parser')

days = list()
day_titles = list()
descrip = list()
paces = list()


for row in soup.find_all('div',attrs={"class" : "training_date_day"}):
    days.append(row.text)

for row in soup.find_all('h1'):
    day_titles.append(row.text)


for row in soup.find_all('p'):
    descrip.append(row.text)

new_descrip = list()
spot = 0
for title in day_titles:
    if title == 'Day Off':
        new_descrip.append(['place_hold', descrip[spot]])
        spot += 1
    else:
        new_descrip.append([descrip[spot], descrip[spot+1]])
        spot += 2

#['Warmup', '1 mile', '(8:35-8:56  per mile)', 'Fartlek', '3 x 2 minutes ', 'Pace: 8:00-8:15  per mile for hard segments', 'with 1 minute running (8:54-8:56  per mile) between each hard segment', 'Warmdown', '1 mile', '(8:54-8:56  per mile)']

for i in range(7):
    print(days[i])
    print(day_titles[i])
    print(new_descrip[i])
    print()