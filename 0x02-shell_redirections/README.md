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
