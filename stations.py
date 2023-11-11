import json

print("Reading Stations File")
with open('input/stations.json', encoding='utf-8') as stations_file:
  stations = json.load(stations_file)

def get_countrycodes():
  codes = [s['countrycode'] for s in stations]
  return sorted(list(set(codes)))

def create_countries_file():
  print("Creating Countries File")
  countries = ([(s['countrycode'], s['country']) for s in stations])
  countries = sorted(list(set(countries)))
  with open('output/countries.csv', 'w', encoding='utf-8') as countries_file:
    for country in countries:
      countries_file.write("'" + country[0] + "','" + country[1] + "'\n")

def create_m3u_file(countrycode):
  print("Creating Stations File for " + countrycode)
  with open('output/radio_stations_' + countrycode + '.m3u', 'w', encoding='utf-8') as output_file:
    output_file.write("#EXTM3U\n")
    output_file.write("#PLAYLIST:Internet Radio Stations\n")
    for s in stations:
      if (s['lastcheckok'] == 1) and (s['countrycode'] == countrycode) and (s['codec'] == 'MP3'):
        output_file.write("#EXTINF:-1 " + s['name'] + '\n')
        output_file.write(s['url'] + '\n')

create_countries_file()

codes = get_countrycodes()
for code in codes:
  create_m3u_file(code)
