
# rm

[[🏷️Linux command]]

The rm command is used to delete files and folders and is one of the important Linux commands you must know.

`rm <file name>`

![[Image 3.03.png]]

To delete a directory, you must add the `-r` argument to it. Without the `-r` argument, the `rm` command won’t delete directories.

`rm -r <folder/directory name>`

The `-r` flag in the `rm` command in Linux stands for “**recursive**”. When used with the `rm` command, it will remove not only the specified file but also all of its subdirectories and the files within those subdirectories recursively.

> [!note]
> It’s important to be careful when using the `rm` command with the `-r` flag, as it can quickly and permanently delete a large number of files and directories. It’s a good idea to use the `-i` flag in conjunction with the `-r` flag, which will prompt you for confirmation before deleting each file and directory.
> 
> For example, to remove the `mydir` directory and its contents with confirmation, you can use this command:
> 
> `rm -ri mydir`
> 
> This will prompt you for confirmation before deleting each file and directory within the `mydir` directory.

