
# uname & whoami

[[🏷️Linux command]]

The `uname` and `whoami` commands allow you to access some basic information that comes in handy when you work on multiple systems.

The `uname` command in Linux displays information about the system’s kernel, including the kernel name, hostname, kernel release, kernel version, and machine hardware name.

The `whoami` command in Linux returns the current user’s username. It stands for “who am I?” and it’s often used to determine the current user’s identity in shell scripts or the terminal.

Let’s see the output of both the commands and the way we can use these.

![[Image 2.94.png]]

The parameter `-a` with `uname` command stands for “all”. This prints out the complete information. If the parameter is not added, all you will get as the output is “Linux”.

> [!note]
> Some important flags you can use with the `uname` command.
> 1. Use `uname -s` to display the kernel name.
> 2. Use `uname -n` to display the hostname.
> 3. Use `uname -r` to display the kernel release.
> 4. Use `uname -v` to display the kernel version.
> 5. Use `uname -m` to display the machine hardware name.
