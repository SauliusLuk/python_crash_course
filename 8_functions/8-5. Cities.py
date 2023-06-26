def describe_city(city_name, country='USA'):
    print(f"{city_name.title()} is in {country.title()}")

describe_city('kaunas', 'lithuania')
describe_city('new york')
describe_city(country='peru', city_name='lima')
