# Learn command line

Please follow and complete the free online [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. You should be able to go through these in a couple of hours.

**Note:** Bash is not installed on a PC. Rather, PC users must install Cygwin. Once Cygwin has been installed, the command line interface witll _emulate_ bash. You can find all information regarding Cygwin [here](https://www.cygwin.com/).

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

1. show current working directory path: ```pwd```

2. creating a directory: ```mkdir directory_name```

3. deleting a directory: ```rmdir -r directory_name```
`-r`: recursively; can use `-f` to force delete if file will not delete for permission reasons

4. create file using touch: ```touch foo.txt```

5. delete a file: ```rm foo.txt```

6. rename a file: 
- in the same directory: ```mv file1.txt file2.txt```
- to rename and *move* file to a different directory, include path and new name: 
```mv ~/projects/file1.txt ~/projects/metis/file2.txt```

7. list hidden files: ```ls -a```

8. copy a file from one directory to another: 
- leave copy in present directory and copy file to another directory use `cp` instead of `mv`
```cp ~/projects/file.txt ~/projects/metis/file.txt```

- as with `mv` can simultaneously rename file as below: 
 ```cp ~/projects/file1.txt ~/projects/metis/file2.txt```

- use `cp` with a new file name to copy the contents of one file into a new file with a different name within the same directory (note: this will override file contents): ```cp file1.txt file2.txt```


#### Print / Save Text

1) `echo` prints what follows to the `stdout`

```bash
$ echo "hello world"
"hello world"

$ echo file.txt
file.txt
```

Can also use echo to get the value of environment variables: 

```bash
$ echo $PATH
~/metis/metishgh/prework/dsp

``` 

2) Direct output to a file using a single caret (`>`) or append to end of a file using double carets to (`>>`). If the file does not exist, it will be created. 
- this can be used for text typed directly in terminal using `echo` or for the output of a different process

```bash
$ echo "hello" > hello_world.txt
$ echo "word" >> hello_world.txt

$ ls >> files_in_directory.txt
```

3) `cat` : concatenate and print files; this will read in however many files are passed as arguments and print them to standard output or to file if specified

- ```console $ cat file1``` prints contents of file1 to standard out
- ```console $ cat file1 file2 > file3``` prints contents of file1 and file2 sequentially to file3, truncating file3 if it already exists.

- the following would print "hello" followed by "world" (words on the first and second line of file *hello_world.txt* above)

```bash
$ cat hello_world.txt
hello
world
```

#### Find files

4) ```du -sh *```: display list of files and (sub)directories in current directory and memory usage  in human readable form 


5) list files and memory used in human readable form for files and top-level directories, including hidden directories and files (here output is sorted & redirected to a text file):
 ```du -sh .[!.]* * | sort -nr >> ~/virtualenv_space.txt```

6) ```locate -i *red*house**city*``` : locate a file with "Red", "House" and "City"; `-i` flag means case-insensitive search; asterisk is a wilcard (matches anything); thus, this command will pull any and all files containing search criteria)

[important_linux_commands](http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands)


#### Other: 
7. chain commands using pipe (`|`);
example: sort output of above command in reverse numerical order: ```du -sh * | sort -nr```

8. `ps`: process status; information about all processes with controlling terminals

#### Get Help! 

9. `info` followed by a command name, will open the BSD manual page describing the command and its options

10. `man info`: this brings up the manual page for the command info (or whichever follows); `man command` provides a brief overview of the command including it's name, synopsis, description, and options 

11. `man -k cd` or `apropos keyword` or `whatis keyword`:  searches the whatis database for strings, specifically database files with short descriptions of system commands for keywords and displays results on `stdout`

12. `howdoi`: use with natural language to ask how to perform certain tasks
for example, the following brings up the postgresql database configuration file:

```bash
$ howdoi configure postgres
pg_hba.conf

```

13. `help locate` : help followed by the name of a command will print to `stdout` a very brief description of the command and its usage

14 `alias p` : to list all aliases, or shortcuts available'; for instance, `ls`='`ls -G` by default

15. to create new aliases in bash that are set each time, add to `~/.bash_profile`:

```console $ alias cm='git commit -m'```

16. `grep` : search input files and selects lines matching one or more basic regular expressions (examples from `info grep`)

- To find all o ccurrences of the word `patricia' in a file
- To find all occurrences of the pattern `.Pp' at the beginning of a line


```bash
$ grep 'patricia' myfile
$ grep '^\.Pp' myfile

```



## TO DO: - AG 
15.  ```console $ aux ```



16.  change file or directory permissions using `chown`



### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls`: list files and directories in current directory (or specified directory if followed by path)

The following flags modify the command in different ways:

`-a`	displays *all* files, including hidden files and directories

`-l`	long form (includes total sum of all file sizes preceding files); includes permissions, file name, size in bytes 

- `lh`	long form with memory in human readable form (kilobytes, megabytes, GB etc) rather than bytes

- `lah` combines above; long form with memory used by file in human readable form; displaying hidden files as well

` -t `  sort by time modified (most recently modified first) before sorting the operands by lexicographical order.

`-p`  Write a slash (`/') after each filename if that file is a directory.

- `Glp` :  `ls` is an alias for `ls -G` so together with the `-l` flag and `-p` flags, this lists all files and directories in long format with slashes after the name of each directory

```bash
amelie at amu in ~/metis/metisgh/prework/dsp on master*
$ ls -Glp
total 144
-rw-r--r--   1 amelie  staff  4347 Jan  3 22:14 00a-markdown.md
-rw-r--r--   1 amelie  staff  2436 Jan  3 22:14 00b-fork_repo.md
-rw-r--r--   1 amelie  staff  1395 Jan  3 22:14 01a-install.md
-rw-r--r--   1 amelie  staff   660 Jan  3 22:14 01b-install_jupyter.md
-rw-r--r--   1 amelie  staff  3730 Jan  3 22:14 02-editors.md
-rw-r--r--@  1 amelie  staff  7093 Jan  4 00:15 03-command_line.md
-rw-r--r--   1 amelie  staff  4924 Jan  3 22:14 04-git.md
-rw-r--r--   1 amelie  staff  1106 Jan  3 22:14 05a-python.md
-rw-r--r--   1 amelie  staff   747 Jan  3 22:14 05b-python_advanced.md
-rw-r--r--   1 amelie  staff  2249 Jan  3 22:14 05c-python_pandas.md
-rw-r--r--   1 amelie  staff   803 Jan  3 22:14 06-linear_algebra.md
-rw-r--r--   1 amelie  staff  7971 Jan  3 22:14 07-statistics.md
-rw-r--r--   1 amelie  staff  2554 Jan  3 22:14 08-more_resources.md
-rw-r--r--   1 amelie  staff  2305 Jan  3 22:14 README.md
drwxr-xr-x  22 amelie  staff   748 Jan  3 22:14 img/
drwxr-xr-x   3 amelie  staff   102 Jan  3 22:14 math/
drwxr-xr-x   5 amelie  staff   170 Jan  3 22:14 python/
drwxr-xr-x   7 amelie  staff   238 Jan  3 22:14 resources/
drwxr-xr-x  12 amelie  staff   408 Jan  3 22:14 statistics/
```

#### The Long Format (`l`)
(from BSD)
     If the -l option is given, the following information is displayed for
     each file: file mode, number of links, owner name, group name, number of
     bytes in the file, abbreviated month, day-of-month file was last modi-
     fied, hour file last modified, minute file last modified, and the path-
     name.  In addition, for each directory whose contents are displayed, the
     total number of 512-byte blocks used by the files in the directory is
     displayed on a line by itself, immediately before the information for the
     files in the directory.  If the file or directory has extended
     attributes, the permissions field printed by the -l option is followed by
     a '@' character.  Otherwise, if the file or directory has extended secu-
     rity information (such as an access control list), the permissions field
     printed by the -l option is followed by a '+' character.
  


### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs -- construct argument list(s) and execute utility; it reads space, tab, newline and end-of-file delimited strings from stdin of xargs and executes utility with the strings as arguments (utility is repeatedly executed until standard input is exhausted) 

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

