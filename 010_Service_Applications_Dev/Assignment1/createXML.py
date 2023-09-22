# Folosind Python creați un XML care conține o listă de filme. Pentru fiecare film trebuie să salvaţi informații despre nume, an și gen. XML trebuie creat folosind modulul xml.etree.ElementTree. XML-ul rezultat trebuie tipărit sub forma unui string.

import xml.etree.ElementTree as ET

# Creating the root element: <movies>
root = ET.Element("movies")

# Hardcoded movies list
movies = [
    {"title": "Heart of Stone", "year": "2023", "genre": "Action"},
    {"title": "They Cloned Tyrone", "year": "2023", "genre": "Comedy"},
    {"title": "Bird Box Barcelona", "year": "2023", "genre": "Thriller"},
]

# Creating movie elements with sub-elements for each movie in the list
for movie in movies:
    movie_element = ET.Element("movie")
    
    title_element = ET.SubElement(movie_element, "title")
    title_element.text = movie["title"]
    
    year_element = ET.SubElement(movie_element, "year")
    year_element.text = movie["year"]
    
    genre_element = ET.SubElement(movie_element, "genre")
    genre_element.text = movie["genre"]
    
    root.append(movie_element)

# Creatin the XML tree inside the root element
tree = ET.ElementTree(root)

# Serializing the XML tree into a string
xml_string = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")

# Print the resulted XML
print(xml_string)

# Saving the XML into a .xml file
with open("movies.xml", "w") as f:
    f.write(xml_string)