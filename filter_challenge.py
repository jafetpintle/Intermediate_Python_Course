#Data of employees
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
    #Print all python devs
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_names = map(lambda worker: worker["name"], all_python_devs)
    print("\nPYTHON DEVS")
    for employee in all_python_devs_names:
        print(employee)

    #Print all platzi workers
    all_platzi_worker = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_worker_names = list(map(lambda worker: worker["name"], all_platzi_worker))
    print("\nPLATZI WORKERS")
    for employee in all_platzi_worker_names:
        print(employee)
    
    #Print all the adults using list comprehension
    adults = [worker["name"] for worker in DATA if worker["age"]>=18]
    print("\nAdults")
    for worker in adults:
        print(worker)
    
    #Add a new value named "old" in each dictionary
    #| pipe operator used to join dictionaries (in a list we join use '+')
    old_people = [worker | {"old": worker["age"] >= 70} for worker in DATA]
    print("\nOld People confirmation")
    for worker in old_people:
        print(worker["name"], worker["age"] , worker["old"])

if __name__ == "__main__":
    run()