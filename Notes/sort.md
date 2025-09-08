
# sort

[[🏷️Linux command]]

The `sort` command is used to sort lines in a text file or standard input in Linux and Unix-based operating systems. It can be used to sort lines in ascending or descending order and to perform other sorting operations, such as sorting by fields or using a custom sorting order.

The basic syntax of the `sort` command is:

`sort <filename>`

![[Image 3.15.png]]

By default, the `sort` command sorts lines in ASCII collating sequence, which can lead to unexpected results when sorting numbers or special characters. To sort numbers in numerical order, you can use the `-n` option.

Here’s an example of using the `-n` option:

`sort -n file.txt`

The above command will sort the lines in `file.txt` in numerical order.

The `sort` command can also be used to sort lines based on specific fields using the `-k` option.

Here’s an example of using the `-k` option:

`sort -k 2 file.txt`

This command will sort the lines in `file.txt` based on the second field.

The `sort` command is a powerful and flexible tool for working with text files in Linux and Unix-based operating systems. By understanding how to use the `sort` command effectively, you can sort lines in text files, sort lines based on specific fields, and perform other sorting operations.

These commands can help you organize and analyze data and perform other file manipulation tasks. Whether you’re a developer or a system administrator, the `sort` command is an essential part of your toolkit.