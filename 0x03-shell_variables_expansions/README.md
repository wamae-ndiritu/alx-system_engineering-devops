#Shell Variable and expansions#

[0. <o>](./0-alias) - Creating an alias

[1. Hello you](./1-hello_you) - Printing hello user

[2. The path to success is to take massive, determined action](./2-path) - Appending path to the PATH variable

[3. If the path be beautiful, let us not ask where it leads](./3-paths) - Counting the number of directories in PATH variable. `printf $PATH | tr ":" "\n" | wc -w`. Running `printf $PATH` will return all the directories in the PATH variable separated by a colon. To separate this directories, we are piping the output to a `tr` to translate the `:` to a new line `\n`. This will list all the paths separated by a new line. Then this output can be piped again to the `wc` command so as we can count the words using the `-w` option. Note that a directory name that has been used in multiple paths will only be counted once.
 
[4. Global variables](./4-global_variables) - Global variables are provided on the system by default and can be used on any Bash script. These variables are mainly environment and configuration variables. To list all environment variables we can use `env`.

[5. Local variables](./5-local_variables) - The `set` command lists all local variables and environment variables, and functions.

[6. Local variable](./6-create_local_variable) - Creating a local variable. `BEST="School"` The variable named `BEST` will only be accessed locally.

[7. Global variable](./7-create_global_variable) - A Global variable on the other hand is accessed by any shell unlike the local one that can only be accessed by the current shell. Therefore, to define a global variable, it must be exported. `export BEST="School"`.

[8. Every addition to true knowledge is an addition to human power](./8-true_knowledge) - addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE. 

[9. Divide and rule](./9-divide_and_rule) - POWER divided by DIVIDE. Prforming arithmetic operations with global Variables.

[10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](./10-love_exponent_breath) - To perform an arithmetic operation based on exponential (power). `echo $((BREATH ** LOVE))` will return value of`BREATH` to power `LOVE`.

[11. There are 10 types of people in the world -- Those who understand binary, and those who don't](./11-binary_to_decimal) - Changing base 2 to base base 10. This is essentially converting a binary to a decimal with use an environment variable.

[12. Combination](./12-combinations) - The aim is to list all possible combinations of two letters, except oo. We first need to list all the possible combinations of characters. For every letter in set 1 must be combined with all the letters in set 2. To print a-z, we can `echo {a..z}` and to combines each with another character, `echo {a..z}{a..z}`. This will output all these combinations in a single line, and as a result we can translate the space between each combination as a new line `tr " " "\n". This will list all the combinations with a new line at the end. Finally we, can pipe this output to a `grep -v` command with the pattern "oo". This will ensure the combination `oo` is not listed. `echo {a..z}{a..z} | tr " " "\n" | egrep -v "oo"`

[13. Floats](./13-print_float) - prints a number with two decimal places, followed by a new line. To do this, we can use `printf` and use a format specifier. In this case `%f` will format the it to a floating-point integer and add a new line at the end. `printf "%.2f\n"`. `.2f` will give us two decimal places.


