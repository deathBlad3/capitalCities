from bs4 import BeautifulSoup
import requests

country = raw_input("Enter the country:")
#print(country)

site_to_scrape = "https://en.wikipedia.org/wiki/List_of_national_capitals_and_largest_cities_by_country"
r = requests.get(site_to_scrape)
data = r.text
soup = BeautifulSoup(data)

print("Capital: "+soup.find('a',title=country).parent.findNext('td').find('a').string)
