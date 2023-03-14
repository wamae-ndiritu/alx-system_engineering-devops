#I/O Redirection\n
#0: Hello World: A simple script file that displays "Hello, World"\n
#1: Confused smiley
To display `"(Ôo)'` the way it is on the screen can be problematic. We need to use quotes as it is one string.
However, we'll have to use the `\`  character to signify that the double quotes after opening double quotes is not a special character.
##2: Let's display a file
`cat` command is used to display the content of a certain file
3. What about 2?
Displaying the content of 2 files simulatenously
4. Last lines of a file
`tail filename` can be used to get the last 10 lines of the file named `filename`
5. I'd prefer the first ones actually
Similary to `tail` command, we can also use `head` command to list the first 10 lines of a file.
6. Line #2
Listing a specific number of lines in a file can be done using the `head` or `tail` command with `-n [n]` option. However, if we want to display just 1 line, let's say the 3rd line we can use pipelines as `head -n 3 | tail -n 1` which will list the first 3 lines and then print the last line of the 3 and therefore we end up printing the 3rd line alone.
7. It is a good file that cuts iron without making a noise
Making a file with a name that has some special characters such as `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` requires you to escape some of the special charcetrs using the `\`.
8. Save current state of directory
Redirectimg the output of `ls -la` to a file named `ls_cwd_content`
9. Duplicate last line
To get the last line, we can use `tail -n 1` and then redirect the output as an appension to `iacta` file
`tail -n 1 >> iacta` will duplicate the last line of the file.
10. No more javascript
Deleting all javascript files `rm -r *.js` in the current working directory.
11. Don't just count your directories, make your directories count
`ls -lRa` lists all the directories and subdirectories together with their count. `-l` is used to list in the long format, `-R` recursively and `-a` all the files and directories including the hidden ones.
12. What’s new
Listing the latest files in the directory. We can use `ls -t | head` to listsorted files based on time and then  take the first 10.

[13. Being unique is better than being perfect](./13-unique)
Sorting input words and prints the words only apearing once. `sort | uniq -u`. The option `-u` is used to only print unique lines.

[14. It must be in that file](./14-findthatword)
Using `grep` command to find pattern is a file.

[15. Count that word](./15-countthatword)
Using `grep` with `-c` option can enable us to display the count of words with the specified pattern.

[16. What's next?](./16-whatsnext)
To get some context after a certain pattern, we can use `grep -A` and specify the number of lines we want after the pattern.

[17. I hate bins](./17-hidethisword)
We can reverse the matching option with a pattern. Instead of displaying lines that match the pattern, we display the lines that do not match.
`grep -v "bin" /etc/passwd`

[18. Letters only please](./18-letteronly)
To search a specific letter without considering it's case, we can use `grep -i "a" filename`. The `-i` optio allows to ignore the case.

[19. A to Z](./19-AZ)
We can replace set of strings with others. This is made possible by the use of `tr` command. eg `tr 'Ac' 'Ze'`

[20. Without C, you would live in hiago](./20-hiago)
`tr` translates characters or delete the characters. To delete characters, we can use `-d` option. `tr -d 'Ac'`

[21. esreveR](./21-reverse)
To reverse characters, we can run `rev`

[22. DJ Cut Killer](./22-users_and_homes)
The `cut` command is used to extract parts of a file by byte position, character or a field. To create a script that displays all users and their home directories, sorted by users.
Based on the the /etc/passwd file, we will run `cut -d: -f1,6 /etc/passwd`. The `-d` options specifies the delimeter which in our case will be the `:`:`, `-f` option shows the field we want to extract and in this case is the user and their home directories. The user is in the 1 field while their home directory is in the 6 field.

[23. Empty casks make the most noise](./100-empty_casks)
To get the empty files and dir in our current directory, we can run `find . -empty`. However, we also want to include the hidden files and therefore we can run `find . -empty -printf '%P\n'`. `-printf` option specifies the format of the output and with our options, `%P\n` prints the file name and adds a new line.

[24. A gif is worth ten thousand words](./101-gifs).
We want find all file with .gif extension in our current dir. `find . -type f -name '*.gif' -printf '%f\n'` the `-type f` specifies that we want a file, `-printf '%f\n'` gives us the filename and adds a new line. However, we want to remove the .gif extension when listing the files. To do this, we have will first reverse the out using `rev` so as to have the extension at the begining. We can  then pipe the output to a `cut` to extract some charcaterss as follows: `find . -type f -name '*.gif' -printf '%f\n' | rev | cut -c 5-`. The `-c` specifies that we are extracting characters and will start with the fifth character. Extracting from the 5 character will have removed the first 4 characters which is the extension. we need to `rev` back the output to have the filenames in their origina form and then sort the files. To sort we'll pipe the output to `sort -f` and the `-f` option will sort in byte order making case-insensitive. `find . -type f -name '*.gif' -printf '%f\n' | rev | cut -c 5- | rev | LC_ALL=C sort -f` `LC_ALL=C` sorts in byte order.

[25. Acrostic](./102-acrostic)
To decode the acrostic by taking the first character of each line and appending them together. `cut -c 1` will extract the first character of the input and then to add the characters together `paste -s -d ''`, this will paste all the characters in a serial way (single line) and no delimeter hence the word will be joined.
