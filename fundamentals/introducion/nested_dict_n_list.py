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

x[1][0] = 15
print(f"\nx after change is: {x}\n")

students[0]["last_name"] = "Bryant"
print(f"\nstudents after change is: {students}\n")

sports_directory['soccer'][0] = "Andres"
print(f"\nsports_directory after change is: {sports_directory}\n")

z[0]["y"] = 30
print(f"\nz after change is: {z}\n")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for student in students:
        print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")

iterateDictionary(students)
print()

def iterateDictionary2(key, students):
    key = str(key)
    for student in students:
        print(f"{student[key]}")

iterateDictionary2("first_name", students)
print()
iterateDictionary2("last_name", students)
print()

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key in dojo:
        print(f"{len(dojo[key])} {key.upper()}")
        for value in dojo[key]:
            print(value)
        print()

printInfo(dojo)

