# AirBnB_clone
![HolbertonBnB logo, image credit: Holberton
School](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20190705%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190705T140914Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9bab52d841eb4673da3ded2ece6e75617ef31f6f7f2d468697481f1fd02b209f)
Image credit: Holberton School

---
# Custom recreation of [`Airbnb's`](https://www.airbnb.com/) front and back end

<!---######---> `AirBnB_clone` is a multi-phase project created for a Holberton School project.

<!---######---> `Phase 1` consists of creating a console, or command interpreter, to manage AirBnB objects. Can create new objects, retrieve objects, update attributes, destroy objects.

The folder/file structure of the repository is as follows:
```
.
├── AUTHORS
├── console.py
├── __init__.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── file_storage.cpython-34.pyc
│   │       └── __init__.cpython-34.pyc
│   ├── __init__.py
│   ├── place.py
│   ├── __pycache__
│   │   ├── amenity.cpython-34.pyc
│   │   ├── base_model.cpython-34.pyc
│   │   ├── city.cpython-34.pyc
│   │   ├── __init__.cpython-34.pyc
│   │   ├── place.cpython-34.pyc
│   │   ├── review.cpython-34.pyc
│   │   ├── state.cpython-34.pyc
│   │   └── user.cpython-34.pyc
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    ├── __init__.py
        └── test_models
	        ├── __init__.py
		        ├── __pycache__
			        │   ├── __init__.cpython-34.pyc
				        │   ├── test_amenity.cpython-34.pyc
					        │   ├──
						test_base_model.cpython-34.pyc
						        │   ├──
							test_city.cpython-34.pyc
							        │   ├──
								test_place.cpython-34.pyc
								        │  
									├──
									test_review.cpython-34.pyc
									        │  
										├──
										test_state.cpython-34.pyc
										        │  
											└──
											test_user.cpython-34.pyc
											        ├──
												test_amenity.py
												        ├──
													test_base_model.py
													        ├──
														test_city.py
														        ├──
															test_engine
															        │  
																└──
																__init__.py
																        ├──
																	test_place.py
																	        ├──
																		test_review.py
																		        ├──
																			test_state.py
																			        └──
																				test_user.py

																				8
																				directories,
																				42
																				files
```

---
### Usage
All files were created on Ubuntu 14.04.4 LTS.


Upon cloning or forking the directory, the user will be met with the
following files in the base project folder:
```
vagrant@user:~/AirBnB_clone$ ls
AUTHORS  console.py  __init__.py  models  README.md  tests
vagrant@user:~/AirBnB_clone$
```
To run the console, the user should type as follows:
```
vagrant@user:~/AirBnB_clone$ ./console.py
(hbnb)
```
Upon seeing the `(hbnb)` prompt, the user will know that the console is
running and can begin to enter commands. Entering help will display a list of
commands that can be used with the console:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

```
Users can recieve descriptions of commands by entering help
`<command name>` into the console, for example:
```
(hbnb) help create
 Creates new instance of BaseModel. Saves to JSON when specified
(hbnb) help quit
 Quit command to exit the program
(hbnb) help update
 Updates class name and id by adding/updating attribute
```
---
### Demo of Usage
Users can begin to create instances of classes, add attributes show class
information and destroy created classes. Lets see the `(hbnb)` console in
action!
```
vagrant@user:~/AirBnB_clone$ ./console.py
(hbnb) create BaseModel
81b118e3-d8fa-48e5-929c-2c4b74a40579
(hbnb) all
["[BaseModel] (81b118e3-d8fa-48e5-929c-2c4b74a40579) {'id':
'81b118e3-d8fa-48e5-929c-2c4b74a40579', 'updated_at':
datetime.datetime(2019, 7, 5, 14, 57, 5, 368470), 'created_at':
datetime.datetime(2019, 7, 5, 14, 57, 5, 368445)}"]
```
When entering `create` and specifying a class name, the console will copy the
base class and create an instance that can be manipulated. The usage of
`all` by itself shows all instances created, at time of execution. We can
`create` more classes and view them `all` like so:
```
(hbnb) create User
465187c4-a5b2-4950-8098-a1ec1f520a7e
(hbnb) create City
8f51c04a-eab5-42e9-a38a-db897fcf111c
(hbnb) all
["[City] (8f51c04a-eab5-42e9-a38a-db897fcf111c) {'id':
'8f51c04a-eab5-42e9-a38a-db897fcf111c', 'updated_at':
datetime.datetime(2019, 7, 5, 14, 57, 27, 597028), 'created_at':
datetime.datetime(2019, 7, 5, 14, 57, 27, 597002)}", "[BaseModel]
(81b118e3-d8fa-48e5-929c-2c4b74a40579) {'id':
'81b118e3-d8fa-48e5-929c-2c4b74a40579', 'updated_at':
datetime.datetime(2019, 7, 5, 14, 57, 5, 368470), 'created_at':
datetime.datetime(2019, 7, 5, 14, 57, 5, 368445)}", "[User]
(465187c4-a5b2-4950-8098-a1ec1f520a7e) {'id':
'465187c4-a5b2-4950-8098-a1ec1f520a7e', 'updated_at':
datetime.datetime(2019, 7, 5, 14, 57, 23, 204817), 'created_at':
datetime.datetime(2019, 7, 5, 14, 57, 23, 204791)}"]
```
If a user mistakenly made a class, they can `destroy` the instance safely as
the class name and unique id is needed:
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 465187c4-a5b2-4950-8098-a1ec1f520a7e
(hbnb) show User 465187c4-a5b2-4950-8098-a1ec1f520a7e
** no instance found **
```
Attributes and values can be added as well by making use of `update`.
Currently our console only supports the addition of a single attribute and
value at a time.
```
(hbnb) update BaseModel 81b118e3-d8fa-48e5-929c-2c4b74a40579 fishing_level
seventy-eight
(hbnb) show BaseModel 81b118e3-d8fa-48e5-929c-2c4b74a40579
[BaseModel] (81b118e3-d8fa-48e5-929c-2c4b74a40579) {'fishing_level':
'eventy-eigh', 'created_at': datetime.datetime(2019, 7, 5, 14, 57, 5, 368445), 'updated_at': datetime.datetime(2019, 7, 5, 14, 57, 5, 368470), 'id': '81b118e3-d8fa-48e5-929c-2c4b74a40579'}
```

---
### File Descriptions
File Name | Description
--- | --- |
`main` | prints "$" and takes input
`getpath` | gets PATH and removes colons
`splitit` | tokenizes input then executes in child
`ifexecutable` | adds spaces to user input, sees if file exists and has execute permissions
`justdoit` | handles execution of additional arguments
`words` | tokenizes string with space as delimiters
`folders` | counts number of filepaths after deliminating
`_strncmp` | compares number of characters of two strings
`_strlen` | counts number of characters in a string
`_strdup` | duplicates string for read or writing
`_strcat` | mallocs for PATH, increments through separated filepaths
---
## About
### This project was created by:

* **Cynthia Dominguez** - [GitHub](https://github.com/cynergist) | [LinkedIn](https://www.linkedin.com/in/cynthiamdominguez/) at [Holberton
School](http://holbertonschool.com).
* **Nick O'Keefe** - [GitHub](https://github.com/nokeefe) | [LinkedIn](https://www.linkedin.com/in/nbokeefe/) at [Holberton
School](http://holbertonschool.com).
