
# top

[[🏷️Linux command]]

A few sections earlier, we talked about the `ps` command. You observed that the `ps` command will output the active processes and end itself.

The `top` command is like a CLI version of the task manager in Windows.

The `top` command in Linux is a system monitoring tool that displays real-time information about system processes and resource usage. It provides a dynamic, real-time view of system activity, including CPU usage, memory usage, and process information.

> [!info] Note
> Here are some examples of using the `top` command:
> 
> Sort processes by memory usage:
> 
> `top -o MEM`
> 
> This will sort the process list by memory usage, with the most memory-intensive processes at the top.
> 
> Display detailed information about a specific process:
> 
> `top -p PID`
> 
> Replace `PID` with the ID of the process you want to inspect.
> 
> Display a summary of system resource usage:
> 
> `top -n 1`
> 
> This will display a single summary screen of system resource usage.

It’s a powerful and flexible tool for monitoring system activity and troubleshooting performance issues.


