import csv
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data =[]
        
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        
        return data


def population_by_country(data, country):
    result = list(filter(lambda item:item["Country"] == country, data))
    return result


def get_population(country_dict):
    population_dict = {
        "2022": int(country_dict["2022 Population"]),
        "2020": int(country_dict["2020 Population"]),
        "2015": int(country_dict["2015 Population"]),
        "2010": int(country_dict["2010 Population"]),
        "2000": int(country_dict["2000 Population"]),
        "1990": int(country_dict["1990 Population"]),
        "1980": int(country_dict["1980 Population"]),
        "1970": int(country_dict["1970 Population"]),
    }
    
    labels, values = zip(*population_dict.items())
    
    return labels, values

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
 
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()