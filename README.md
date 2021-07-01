# 0x00. AirBnB clone - The console

## [](https://github.com/narnat/AirBnB_clone/blob/master/README.md#description)

##Description

This project is about to deploy a simple clone of the AirBnB website - hBnB. The web application will be composed by:

-   A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
-   A website (front-end) that show the final product to everyone: static and dynamic
-   A database or files that store data
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete and update them)

----------

## Final Product

[![Image of hbnb](https://github.com/ethanpasta/AirBnB_clone/raw/master/100-index.png)](https://github.com/ethanpasta/AirBnB_clone/blob/master/100-index.png)

## Step 1: The Console

-   Create a data model
-   Manage (create, update, destroy, etc) objects via a console/command interpreter
-   Store and persist objects to files (JSON files)

The first step is to manipulate a powerful storage system. This storage engine will give an abstraction between objects and how they are stored and persisted.

[![Image of hbnb](https://github.com/ethanpasta/AirBnB_clone/raw/master/815046647d23428a14ca.png)](https://github.com/ethanpasta/AirBnB_clone/blob/master/815046647d23428a14ca.png)

## Commands

| Commands | Description |
|--|--|
| `quit` | Quits the console |
| `Ctrl+D` | Quits the console |
| `help` or `help <command>` | Displays all commands or Displays instructions for a specific command |
| `create <class>` |Creates an object of type , saves it to a JSON file, and prints the objects ID|
| `show <class> <ID>` | Shows string representation of an object |
| `destroy <class> <ID>` | Deletes an objects |
| `all` or `all <class>` | Prints all string representations of all objects or Prints all string representations of all objects of a specific class |
| `update <class> <id> <attribute name> "<attribute value>"` | Updates an object with a certain attribute (new or existing) |
| `<class>.all()` | Same as `all <class>` |
| `<class>.count()` | Retrieves the number of objects of a certain class |
| `<class>.show(<ID>)` | Same as `show <class> <ID>` |
| `<class>.destroy(<ID>)` | Same as `destroy <class> <ID>` |
| `<class>.update(<ID>, <attribute name>, <attribute value>` | Same as `update <class> <ID> <attribute name> <attribute value>` |
| `<class>.update(<ID>, <dictionary representation>)` | Updates an objects based on a dictionary representation of attribute names and values |

Updates an objects based on a dictionary representation of attribute names and values

## More Info

### Execution

Your shell should work like this in interactive mode:

```
andrecast@MED-PF1NQ8WJ:~/AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
andrecast@MED-PF1NQ8WJ:~/AirBnB_clone$

But also in non-interactive mode: (like the Shell project in C)

andrecast@MED-PF1NQ8WJ:~/AirBnB_clone$  echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) andrecast@MED-PF1NQ8WJ:~/AirBnB_clone$ 

```

### Examples

```
andrecast@MED-PF1NQ8WJ:~/AirBnB_clone$ ./console.py 
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
04cd8bf8-6d4d-456c-8e79-ccc5a0a18241
(hbnb) all BaseModel
["[BaseModel] (04cd8bf8-6d4d-456c-8e79-ccc5a0a18241) {'id': '04cd8bf8-6d4d-456c-8e79-ccc5a0a18241', 'created_at': datetime.datetime(2021, 6, 30, 18, 28, 9, 697291), 'updated_at': datetime.datetime(2021, 6, 30, 18, 28, 9, 697301)}"]
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 04cd8bf8-6d4d-456c-8e79-ccc5a0a18241
** attribute name missing **
(hbnb) update BaseModel 04cd8bf8-6d4d-456c-8e79-ccc5a0a18241 first_name "Betty"
(hbnb) show BaseModel 04cd8bf8-6d4d-456c-8e79-ccc5a0a18241
[BaseModel] (04cd8bf8-6d4d-456c-8e79-ccc5a0a18241) {'id': '04cd8bf8-6d4d-456c-8e79-ccc5a0a18241', 'created_at': datetime.datetime(2021, 6, 30, 18, 28, 9, 697291), 'updated_at': datetime.datetime(2021, 6, 30, 18, 28, 9, 697301), 'first_name': 'Betty'}
(hbnb) create BaseModel
6e3efe4b-1cef-48f7-9275-d71e29406b1f
(hbnb) all BaseModel
["[BaseModel] (04cd8bf8-6d4d-456c-8e79-ccc5a0a18241) {'id': '04cd8bf8-6d4d-456c-8e79-ccc5a0a18241', 'created_at': datetime.datetime(2021, 6, 30, 18, 28, 9, 697291), 'updated_at': datetime.datetime(2021, 6, 30, 18, 28, 9, 697301), 'first_name': 'Betty'}", "[BaseModel] (6e3efe4b-1cef-48f7-9275-d71e29406b1f) {'id': '6e3efe4b-1cef-48f7-9275-d71e29406b1f', 'created_at': datetime.datetime(2021, 6, 30, 18, 29, 51, 641764), 'updated_at': datetime.datetime(2021, 6, 30, 18, 29, 51, 641773)}"]
(hbnb) destroy BaseModel 04cd8bf8-6d4d-456c-8e79-ccc5a0a18241
(hbnb) show BaseModel 04cd8bf8-6d4d-456c-8e79-ccc5a0a18241
** no instance found **

```
----------

## Authors

-   **Brian Zapata** - (https://www.github.com/brian-1989)
-   **Andrea Castrillón** - (https://www.github.com/Andrecast)
