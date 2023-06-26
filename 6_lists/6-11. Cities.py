cities = {
    'kaunas' : {'country': 'lietuva', 'population': '300k', 'fact': 'aukstaitija'},
    'oslo' : {'country': 'norway', 'population': '900k', 'fact': 'cold'},
    'new york': {'country': 'usa', 'population': '12mln', 'fact': 'big'},
    }

for city, facts in cities.items():
    print(f"here are some facts about {city}: ")
    country = facts['country']
    population = facts['population']
    fact = facts['fact']
    print(f"{city.title()} is in {country.title()}, population: {population}, fun fact: {fact}")