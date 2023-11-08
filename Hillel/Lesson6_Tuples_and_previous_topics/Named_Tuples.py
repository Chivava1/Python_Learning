from collections import namedtuple

city = namedtuple("city",["name", "population", "country"])

Kyiv = city(name="Kyiv", population=8.4, country="Ukraine")
New_York = city(name="New_York", population=8.4, country="USA")
Paris = city(name="Paris", population=8, country="France")
cities = (Kyiv, New_York, Paris)


for i in cities:
    if type(i.name) == str and type(i.country) == str and type(i.population) == float:
        print(f"Everything is ok, all data type of, {i.name}, is Valid")
    else:
        print(f"Warning! Invalid data type detected for this string , Expected <class 'str'>, <class 'float'>, <class 'str'>. Actual is {type(i.name)}, {type(i.population)}, {type(i.country)}")
        break









