# This program lists out 10 Florida states and asks the user for a
# number 0-10, then graphs a 20-year population growth chart at 2% growth rate

import matplotlib.pyplot as plt

# Initialize variables for use later
population_BW = []
population = []

# List of cities available to choose from and their population
cities = {
    "Miami": 2735908,
    "Tampa": 4092474,
    "Orlando": 3217608,
    "Jacksonville": 977778,
    "St. Petersburg": 268787,
    "Hialeah": 235733,
    "Fort Lauderdale": 187113,
    "Port St. Lucie": 203741,
    "Cape Coral": 194978,
    "Tallahassee": 199410
}

# Create multiple dictionaries in 'population' containing ID, city, year, and population
for i, (city, pop) in enumerate(cities.items()):
    population.append({"ID": i+1, "city": city, "year": 2023, "population": pop})

# Simulates the growth of a specified city over 20 years at 2% growth rate
def sim_growth(city):

    # Finds the city in 'population'
    for city_dict in population:
        if city_dict['city'] == city:

            # simulates 20 years of growth at 2%
            for i in range(20):
                city_dict['population'] *= 1.02

                # Appends the new information to database
                population_BW.append(
                    {"city": city,
                     "year": city_dict['year'] + i,
                     "population": city_dict['population']}
                )

# Generates data to fill into population_BW
for city in cities:
    sim_growth(city)

# Plots a specified city
def plot_growth(city):

    # Collects data for the specified city from the database
    city_data = [entry for entry in population_BW if entry['city'] == city]
    years = [city['year'] for city in city_data]
    populations = [city["population"] for city in city_data]

    # Plots the data on a graph, x is years, y is population
    plt.plot(years, populations)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"Population Growth of {city}")
    plt.grid(True)
    plt.show()

# User interaction loop
while True:
    print('Choose a city to see it\'s grown in 20 years')

    # Lists all available cities
    for i, city in enumerate(cities):
        print(f'{i+1}. {city}')

    print('Press 0 to exit.')

    # try-except to get user input, find their chosen city, and plot it
    try:
        usr_choice = int(input('Enter your choice: '))
        if usr_choice == 0:
            break
        elif 1 <= usr_choice <= 10:

            # City ID is the same as enumerated on line 71
            for city in population:
                if city['ID'] == usr_choice:
                    chosen_city = city['city']
            plot_growth(chosen_city)
        else:
            print('Invalid. Try a lower number.')

    except ValueError:
        print("Only numbers please 0-10, please.")