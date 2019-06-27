# AirBnB_clone
---
### Custom recreation of [`Airbnb's`](https://www.airbnb.com/) front and back end

<!---######--->`AirBnB_clone` is a multi-phase project created for a Holberton School project.

<!---######--->`Phase 1` consists of creating a console, or command interpreter, to manage AirBnB objects. Can create new objects, retrieve objects, update attributes, destroy objects.
```
ls | ./hsh
```
Or they can enter interactive mode then input commands following the '$':
```
./hsh
$
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
### Usage
All files were created and compiled on Ubuntu 14.04.4 LTS using GCC 4.8.4 with
the following input:

`gcc -Wall -Werror -Wextra -pedantic *.c -o hsh`.
Includes:
- `main.c`
- `getpath.c`
- `splitit.c`
- `ifexecutable.c`
- `justdoit.c`
- `words.c`
- `folders.c`
- `_strncmp.c`
- `_strlen.c`
- `_strdup.c`
- `_strcat.c`
- `holberton.h`
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
### Example Usage
- `ls | ./hsh` pipes the ls command into non interactive mode of shell program
- `./hsh` starts the shell in interactive mode with the "$" prompt
- `mkdir test` will create a directory call test, while in interactive mode
```
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$ echo "/bin/ls" | ./hsh
$ #README.md#  _strcat.c			 _strncmp.c  holberton.h     justdoit.c		    splitit.c
AUTHORS      _strdup.c				 folders.c   hsh	     			        main.c		    words.c
README.md    _strlen.c				 getpath.c   ifexecutable.c  man_1_simple_shell.man
$ vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$
```
- `./hsh` starts the shell in interactive mode with the "$" prompt
- `mkdir test` will create a directory call test, while in interactive mode
```
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$ ./hsh
$ ls
AUTHORS    _strdup.c   folders.c    hsh		    main.c		    words.c
README.md  _strlen.c   getpath.c    ifexecutable.c  man_1_simple_shell.man
_strcat.c  _strncmp.c  holberton.h  justdoit.c	        splitit.c
$ exit
vagrant@vagrant-ubuntu-trusty-64:~/simple_shell$
```
- `ls -la` will list all directory contents including hidden files in long format while in interactive mode
- `ctrl+x+c` will exit interactive mode and close the simple_shell
---
### About
This project was created by:
=======
* **Nick O'Keefe** - [GitHub](https://github.com/nokeefe) | [LinkedIn](https://www.linkedin.com/in/nbokeefe/) at [Holberton
School](http://holbertonschool.com).
* **Cynthia Dominguez** - [GitHub](https://github.com/cynergist) | [LinkedIn](https://www.linkedin.com/in/cynthiamdominguez/) at [Holberton
School](http://holbertonschool.com).
