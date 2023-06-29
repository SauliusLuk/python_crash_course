from city_functions import city_country

print("Where do you live?")
while True:
    city = input("Entr your city")
    if city == 'q':
            break
    country = input("Enter your country")
    if country == 'q':
        break

    city_and_country = city_country(city, country)
    print(f"You live in {city_and_country}")

