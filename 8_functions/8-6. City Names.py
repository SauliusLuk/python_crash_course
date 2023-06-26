def city_country(city, country):
    city_and_country = f"{city}, {country}"
    return city_and_country.title()

kaunas = city_country('kaunas', 'lithuania')
print(kaunas)
oslo = city_country('oslo', 'norway')
print(oslo)
boston = city_country('boston', 'usa')
print(boston)