
# cat, echo & less

[[🏷️Linux command]]

When you want to output the contents of a file or print anything to the terminal output, we use the `cat` or `echo` commands. Let’s see their basic usage.

`cat <file name>`
`echo <Text to print on terminal>`

![[Image 3.06.png]]

As you can see in the above example, the `cat` command, when used on our `New-File`, prints the contents of the file. At the same time, when we use `echo` command, it simply prints whatever follows after the command.

The `less` command is used when the output printed by any command is larger than the screen space and needs scrolling. The `less` command allows the user to break down the output and scroll through it with the use of the enter or space keys.

The simple way to do this is with the use of the pipe operator (`|`).

`cat /boot/grub/grub.cfg | less`

> [!note]
> Use the `-S` flag with `less` to enable line wrapping. This will allow you to view long lines of text without scrolling horizontally.
> 
> Use the `-N` flag with `less` to display line numbers. This can be useful when you need to know the line number of a specific piece of text.
> 
> You can use these useful flags in the following way:
> 
> `cat /boot/grub/grub.cfg | less -SN`
> 
> Using `less` with the pipe operator can be useful in many different situations. Here are a few examples:
> - Viewing the output of a long-running command, such as `top` or `htop`.
> - Searching for specific text in the output of a command, such as `grep` or `cat` .

