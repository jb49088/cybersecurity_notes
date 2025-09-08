
# head & tail

[[🏷️Linux command]]

When outputting large files, the `head` and `tail` commands come in handy. These commands display the beginning or end of a file, respectively. They are commonly used to quickly view the contents of a file without having to open it in a text editor.

The `head` and `tail` commands display the first 10 lines of a file by default. To display a different number of lines, you can use the `-n` option, followed by the number of lines you want to display.

Here’s an example of using the `head` and `tail` commands:

`head <file name>`
`tail <file name>`

![[Image 3.10.png]]

As you can see, the head command showed 10 lines from the top of the file.

![[Image 3.11.png]]

The tail command outputted the bottom 10 lines from the file.

These commands can be used to quickly view a file’s contents, monitor real-time updates for troubleshooting issues, filter output from other commands, and perform log analysis.