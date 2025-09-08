
# ps, kill & killall

[[🏷️Linux command]]

The `ps`, `kill` and `killall` commands are all used to manage processes in Linux.

The `ps` command is used to display information about the current running processes on the system. Here are some examples of using the `ps` command:

Display a list of all running processes:

`ps -ef`

Display a list of all processes for a specific process ID (PID):

`ps -p PID`

Let’s see all of this in action:

`ps`
`kill <process ID`
`killall <process name>`

For demonstration purposes, we will create a shell script with an infinite loop and will run it in the background.

With the use of the `&` symbol, we can pass a process into the background. As you can see, a new bash process with PID 25098 is created.

![[Image 3.18.png]]

Now, to kill a process with the `kill` command, you can type `kill` followed by the PID(Process Id) of the process.

![[Image 3.19.png]]

But if you do not know the process ID and just want to kill the process with the name, you can make use of the killall command.