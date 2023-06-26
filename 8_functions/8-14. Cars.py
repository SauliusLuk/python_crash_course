def make_car(manufacturer, model, **car_info):
    car_info['make']=manufacturer
    car_info['model']=model
    return car_info

car1 = make_car('mercedes', 'c300', colour='white', new=True)
car2 = make_car('bmw', 'i', colour='white', new=True, sunroof=True)
print(car1)
print(car2)