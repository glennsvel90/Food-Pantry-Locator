# food-resources
App that shows food pantries around New York's South Bronx neighborhood to help homeless families

The program requires an api key. The app is run from the terminal, and a list of food pantry location addresses are sent to google maps api. Location data is downloaded from google maps into a local sqlite3 database. Python takes this geolocation data from the database and prints it. The printed info is is taken up by a javascript program that renders and displays the data in an open browser with html.

## Getting Started

Clone the repository. Unzip the contents. Open the terminal and change directory to be located inside the repository.

### Prerequisites

Python 3

### Running the program

```
python geoload.py
```

```
python geodump.py
```

```
xdg-open where.html
```

## Web App Preview

![alt text](https://github.com/glennsvel90/food-resources/blob/master/mappreview.PNG "Map Preview")
