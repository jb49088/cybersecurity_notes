
# wget

[[🏷️Linux command]]

If you want to download a file from within the terminal, the `wget` command is one of the handiest command-line utilities available. It is one of the important Linux commands you should know when working with source files.

When you specify the link for download, it has to directly be a link to the file. If the file cannot be accessed by the `wget` command, it will simply download the webpage in HTML format instead of the actual file that you wanted.

Let’s try an example. The basic syntax of the `wget` command is :

`wget <link to file>`

Or,

`wget -c <link to file>`

The `-c` argument allows us to resume an interrupted download.