x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x = [(5, 2, 3), (15, 8, 9)]

students = [{"first_name": "Michael", "last_name": "Jordan"}, {"first_name": "John", "last_name": "Rosales"}]
students[0]["last_name"] = "Bryant"

sports_directory = {"basketball": ["Kobe", "Jordan", "James", "Curry"], "soccer": ["Messi", "Ronaldo", "Rooney"]}
sports_directory["soccer"][0] = "Andres"

z = [10, 20, 30]
z[1] = 30

def iterate_dictionary(some_list):
    for item in some_list:
        for key, value in item.items():
            print(f"{key} - {value}")

students = [{"first_name": "Michael", "last_name": "Jordan"}, {"first_name": "Rosales", "last_name": "John"}]
iterate_dictionary(students)

def statedictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

students = [{"first_name": "Michael", "last_name": "Jordan"}, {"first_name": "John", "last_name": "Rosales"}]
statedictionary2("first_name", students)

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)

daja = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Richael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Winh", "Dave"],
}
printInfo(daja)
