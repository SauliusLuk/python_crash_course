people = {
    'valma' : ['preila', 'vilnius', 'oslo'],
    'saulius' : ['juodkrante', 'london', 'kaunas'],
    'minde' : ['new york', 'gabsiai'],
    }



for name, places in people.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")