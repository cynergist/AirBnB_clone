# AirBnB_clone
---
### Custom recreation of [`Airbnb's`](https://www.airbnb.com/) front and back end

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
All files were created and compiled on Ubuntu 14.04.4 LTS.


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
running and can begin to enter commands. Enter help will display a list of
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
### Prototypes
##### `int main(int ac, char **av, char **envp)`
##### `void getpath(char *line)`
##### `char *splitit(char **token)`
##### `char *_strcat(char *dest, char *src)`
##### `char *_strdup(char *str)`
##### `int folders(char *path)`
##### `int words(char *token)`
##### `int _strncmp(char *s1, char *s2, int n)`
##### `int _strlen(char *string)`
##### `int ifexecutable(char *line)`
##### `void justdoit(char *line)`
---
### Format Specifiers
Function name | Description
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
=======
* **Cynthia Dominguez** - [GitHub](https://github.com/cynergist) | [LinkedIn](https://www.linkedin.com/in/cynthiamdominguez/) at [Holberton
School](http://holbertonschool.com).
* **Nick O'Keefe** - [GitHub](https://github.com/nokeefe) | [LinkedIn](https://www.linkedin.com/in/nbokeefe/) at [Holberton
School](http://holbertonschool.com).
