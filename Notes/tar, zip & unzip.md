# tar, zip & unzip

[[🏷️Linux command]]

The `tar` command in Linux is used to create and extract archived files. We can extract multiple different archive files using the `tar` command.

To create an archive, we use the `-c` parameter, and to extract an archive, we use the `-x` parameter. Let’s see how it works.

Compress:

`tar-cvf <archive name> <files separated by space`

Extract:

`tar -xvf <archive name>`

![[Image 3.07.png]]

In the first line, we created an archive named Compress.tar with the New-File and New-File-Link. In the next command, we have extracted those files from the archive.

Let’s discuss the `zip` and `unzip` commands. Both are very straightforward. You can use them without any parameters, and they’ll work as intended. Let’s see an example below.

`zip <archive name> <file names separated by space`

`unzip <archive name>`

![[Image 3.08.png]]

Since we already have those files in the same directory, the `unzip` command prompts us before overwriting those files.