
# ln

[[🏷️Linux command]]

To create a link to another file, we use the `ln` command. This is one of the most important Linux commands that you should know if you’re planning to work as a Linux administrator.

`ln -s <source path> <link name>`

![[Image 3.05.png]]

The `-s` flag creates a symbolic link (also known as a symlink or soft link) to a file or directory. A symbolic link is a special type of file that acts as a shortcut or pointer to another file or directory.

By default, the `ln` command will make hard links instead of symbolic or soft links.

> [!note]
> Say you have a text file. If you make a symbolic link to that file, the link is only a pointer to the original file. If you delete the original file, the link will be broken, as it no longer has anything to point to.
> 
> A hard link is a mirror copy of an original file with the exact same contents. Like symbolic links, if you edit the contents of the original file, those changes will be reflected in the hard link. If you delete the original file, though, the hard link will still work, and you can view and edit it as you would a normal copy of the original file.