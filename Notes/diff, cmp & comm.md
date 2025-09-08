
# diff, cmp & comm

[[🏷️Linux command]]

The `diff`, `comm`, and `cmp` commands are all used to compare files in Linux and Unix-based operating systems. These commands can be used to identify differences between two files, merge changes, and perform other file comparison tasks.

`diff <file 1> <file 2>`

![[Image 3.12.png]]

The `cmp` command is used to compare two files and display the first byte that is different between them. It can be used to identify differences between binary files or to check for corruption in files.

`cmp <file 1> <file 2>`

![[Image 3.13.png]]

`comm <file 1> <file2>`

![[Image 3.14.png]]

The text that’s aligned to the left is only present in `file 1`. The centre-aligned text is present only in `file 2`. And the right-aligned text is present in both files.

By the looks of it, `comm` command makes the most sense when we’re trying to compare larger files and would like to see everything arranged together.

All three of these commands are essential tools for working with files in Linux and Unix-based operating systems. By understanding how to use the `diff`, `comm`, and `cmp` commands effectively, you can identify differences between files, merge changes, and perform other file comparison tasks.

These commands can help you to identify and resolve issues with files, as well as to track changes and maintain version control. Whether you’re a developer or a system administrator, these commands are an essential part of your toolkit.