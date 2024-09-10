import xml.etree.ElementTree as ET
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
tree = ET.parse('library.xml')
root = tree.getroot()


##Reading Document

#1
print("exercise 1")
first_title = root.find('book').find('title').text
print(first_title)
print("\n")

#2
print("exercise 2")
for book in root.findall('book'):
    title = book.find('title').text
    author =book.find('author').text
    year = book.find('year').text
    print(f"Title: {title}, Author: {author}, Year: {year}")
print("\n")

#3
print("exercise 3")
authors = [books.find('author').text for books in root.findall('book')]
print("Authors:", authors)
print("\n")



#4
first_book = root.find('book')
first_book.find('title').text = "Update Introduction to Python"
print(first_book.find('title').text)
print("\n")


#Adding Data

new_book = ET.Element('book')
new_title = ET.SubElement(new_book,'title')
new_title.text = "New Book Title"
new_author = ET.SubElement(new_book, 'author')
new_author.text = "New Book Author"
new_year = ET.SubElement(new_book, "year")
new_year.text = "2024"

root.append(new_book)

def print_data():
    print("printing updated root:")
    all_data = root.findall('book')
    for data in all_data:
        print(data.find('title').text)
print_data()
print("\n")

#Removing Data
root.remove(new_book)
print_data()
print("\n")


#Writing to File
tree.write("library_updated.xml")


#5
#Querying
books_2020 = root.findall(".//book[year='2020']")
print("Books in 2020")
for books in books_2020:
    print(books.find('title').text)
print("\n")

#6
#Converting to string 

xml_string = ET.tostring(root, encoding='unicode')
print(xml_string)


#7
#advanced xml

from lxml import etree
tree = etree.parse('library.xml')
root = tree.getroot()

titles = root.xpath("//title/text()")
print("Titles: ", titles)