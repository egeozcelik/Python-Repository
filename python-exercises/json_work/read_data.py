import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 1
# Read Data
with open('library.json', 'r') as file:
    data = json.load(file)

print(data)


# 2
# Converting string to JSON

json_string = '''
{
    "library": [
        {
            "title": "Book One",
            "author": "Author One",
            "year": 2020
        },
        {
            "title": "Book Two",
            "author": "Author Two",
            "year": 2021
        }
    ]
}
'''

data2 = json.loads(json_string)
print(data2)


# 3 
# Converting python data to JSON (Serialize)
print("\n")
print("Converting python data to JSON (Serialize)")


library = {
    "library": [
        {
            "title": "Movie One",
            "author": "Director One",
            "year": 2020
        },
        {
            "title": "Movie Two",
            "author": "Director Two",
            "year": 2021
        }
    ]
}
with open('library_output.json', 'w') as file:
    json.dump(library, file, indent=4)

json_data = json.dumps(library, indent=4)
print(json_data)


# 4
# Json Operations

for book in data['library']:
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

data['library'][0]['year'] = 2029 #updated specified data

with open('library_updated.json', 'w') as file:
    json.dump(data, file, indent=4)
