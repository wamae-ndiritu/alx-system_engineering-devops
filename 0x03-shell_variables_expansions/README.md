#Shell Variable and expansions#

[0. <o>](./0-alias) - Creating an alias

[1. Hello you](./1-hello_you) - Printing hello user

[2. The path to success is to take massive, determined action](./2-path) - Appending path to the PATH variable

[3. If the path be beautiful, let us not ask where it leads](./3-paths) - Counting the number of directories in PATH variable. `printf $PATH | tr ":" "\n" | wc -w`. Running `printf $PATH` will return all the directories in the PATH variable separated by a colon. To separate this directories, we are piping the output to a `tr` to translate the `:` to a new line `\n`. This will list all the paths separated by a new line. Then this output can be piped again to the `wc` command so as we can count the words using the `-w` option. Note that a directory name that has been used in multiple paths will only be counted once.
 
[4. Global variables](./4-global_variables) - Global variables are provided on the system by default and can be used on any Bash script. These variables are mainly environment and configuration variables. To list all environment variables we can use `env`.

[5. Local variables](./5-local_variables) - The `set` command lists all local variables and environment variables, and functions.


