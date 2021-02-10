import json
from urllib.request import urlopen

with urlopen("https://api.data.gov/ed/collegescorecard/v1/schools.json?school."
             "degrees_awarded.predominant=2,3&fields=id,school.name,2013.student.size") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print('school.name, school.city,2018.student.size,2017.student.size,2017.earnings.'
          '3_yrs_after_completion.overall_count_over_poverty')