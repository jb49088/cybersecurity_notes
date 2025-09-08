
# useradd & usermod

[[🏷️Linux command]]

The `useradd` and `usermod` commands are used in Linux to manage user accounts.

The `useradd` or `adduser` commands are the exact same commands where `adduser` is just a symbolic link to the `useradd` command. This command allows us to create a new user in Linux.

`useradd newuser -d /home/newuser`

The above command will create a new user named `newuser` with the home directory as `/home/newuser`.

The `usermod` command, on the other hand, is used to modify existing users. You can modify any value of the user including the groups, the permissions, etc.

For example, if you want to add more groups to the user, you can type in:

`usermod newuser -a -G sudo, audio, mysql`