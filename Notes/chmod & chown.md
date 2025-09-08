
# chmod & chown

[[🏷️Linux command]]

The `chmod` and `chown` commands are used to modify file permissions and ownership in Linux.

The `chmod` command is used to change the permissions of a file or directory, and the `chown` command is used to change the ownership of a file or directory

The default syntax for both the commands is `chmod <parameter> filename` and `chown <user:group> filename`

`chmod +x loop.sh`
`chmod root:root loop.sh`

![[Image 3.21.png]]

In the above example, we’re adding executable permissions to the `loop.sh` file with the `chmod` command. In addition, with the `chown` command, we’ve made it accessible only to the root user and users within the root group.

![[Image 3.22.png]]

As you will notice, the `main main` part is now changed to `newuser` which is the new user who has full file ownership.
