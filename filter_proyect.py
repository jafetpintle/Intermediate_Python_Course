#Data of employees
from concurrent.futures.thread import _worker
from unicodedata import name


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
    ]

def run():
    #Using list comprehensions
    all_python_devs = [employee["name"] for employee in DATA if employee["language"] == "python"]
    print("\nAll python devs")
    for employee in all_python_devs:
        print(employee)

    all_platzi_worker = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print("\nAll python devs")
    for employee in all_platzi_worker:
        print(employee)
    
    #Using filter to filter by age
    adults = list(filter(lambda worker: worker["age"] >= 18 , DATA))
    #Using map to get only names
    adults = list(map(lambda worker: worker["name"], adults))
    print("\nAdults")
    for employee in adults:
        print(employee)
    
    #Add a new value named "old" in each dictionary
    # | pipe operator used to join dictionaries (in a list we join using '+')
    old_people = list(map(lambda worker: worker | { "old": worker["age"]>70} , DATA))
    print("\nDictionaries with old people")
    for employee in old_people:
        print(employee)

if __name__ == "__main__":
    run()