import random, json

file = 'countries.json'

def get_countries(jsonfile, number):
    """ Choose the file from which the function can select
    a set of random countries. The function returns a JSON
    object with the name and code of the country """

    try:
        with open(jsonfile) as file:
            data = json.load(file)

        country_list = list(data.items())
        countries = random.sample(country_list, number)

        json_countries = []
        for country in countries:
            json_countries.append(
                {
                "code":f"{country[0]}",
                "name":f"{country[1]}"
                })

        package = {
            "countries":json_countries
        }

    except TypeError as error:
        raise Exception("Ensure JSON file is in correct format and number is an int type")


    return json.dumps(package, indent=2)






