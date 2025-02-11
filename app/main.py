import utilis

key, values = utilis.get_population()

print(key,values)

print(utilis.name)

data = [
    {
      "Country" : "Colombia",
      "Population": 500   
    },
    {
      "Country" : "Venezuela",
      "Population": 600
    },
]

result = utilis.population_by_country(data, "Venezuela")
print(result[0]["Population"])