# import csv
# from bs4 import BeautifulSoup
# import requests

# covid_url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory#covid19-container"
# covid_requests = requests.get(covid_url)
# covid_html = covid_requests.content

# # print(covid_html)

# covid_soup = BeautifulSoup(covid_html, features = "html.parser")

# table = covid_soup.find_all('table')[1]

# world_data = covid_soup.find("tr", {"class":"sorttop"})
# world_data_cells = world_data.find_all("th")
# world_cases, world_deaths, world_recoveries = world_data_cells[2].get_text().replace(",", ""),world_data_cells[3].get_text().replace(",", ""), world_data_cells[4].get_text().replace(",", "")

# countries = table.select('tbody > tr')

# header = [th.text.rstrip() for th in countries[0].find_all('th')]

# with open('output.csv', 'w') as csv_file3:
#         writer = csv.writer(csv_file3)
#         writer.writerow(header)
#         writer.writerow(f"{world_cases}, {world_deaths}, {world_recoveries}")
#         for row in countries[1:]:
#             data = [th.text.rstrip() for th in row.find_all('td')]
#             writer.writerow(data)
            # print(row.text)
            # print()
# if __name__=="__main__":
# print()

import csv
from bs4 import BeautifulSoup
import requests

def write_to_csv(data):

    file = open("coviddata.csv", "a")

    file.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}\n")
    file.close()
    
covid_url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory#covid19-container"
covid_requests = requests.get(covid_url)
covid_html = covid_requests.content

covid_soup = BeautifulSoup(covid_html, features = "html.parser")


# write_to_csv("[location, cases, deaths, recoveries]")
write_to_csv(['location','cases', 'deaths','recoveries'])

world_data = covid_soup.find("tr", {"class":"sorttop"})
world_data_cells = world_data.find_all("th")
world_cases, world_deaths, world_recoveries = world_data_cells[2].get_text(),world_data_cells[3].get_text(), world_data_cells[4].get_text()

world_cases = world_cases.replace("," , "").replace("\n", "")
world_deaths = world_deaths.replace("," , "").replace("\n", "")
world_recoveries = world_recoveries.replace("," , "").replace("\n", "")

write_to_csv(["Global", world_cases, world_deaths, world_recoveries])

other_countries = covid_soup.find("div", {"id":"covid19-container"}).find_all("tr")

for row in other_countries:
    row_cells = row.find_all("td")

    try:

        country_name = row.find("a").get_text()
        print(country_name)

        row_cells_cases, row_cells_deaths, row_cells_recoveries = row_cells[0].get_text(), row_cells[1].get_text(), row_cells[2].get_text()

        country_name = country_name.replace("," , "").replace("\n", "")
        row_cells_cases = row_cells_cases.replace("," , "").replace("\n", "")
        row_cells_deaths = row_cells_deaths.replace("," , "").replace("\n", "")
        row_cells_recoveries = row_cells_recoveries.replace("," , "").replace("\n", "")

        write_to_csv([country_name, row_cells_cases, row_cells_deaths, row_cells_recoveries])

    except:
        pass