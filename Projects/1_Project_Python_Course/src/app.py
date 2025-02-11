import utils

def run():
    path = "../data/data_a2a96400-8d27-4730-83e9-3998f00eb9b6.csv"
    data = utils.read_csv(path)
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    countries = list(map(lambda x: x["Country"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    utils.generate_pie_chart(countries,percentages)
    
    '''country = input("Type Country => ")
    
    result = utils.population_by_country(data=data, country=country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        utils.generate_bar_chart(labels, values)'''

if __name__ == "__main__":
    run()