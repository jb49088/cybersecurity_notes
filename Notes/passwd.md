
# passwd

[[🏷️Linux command]]

Now that you know how to create new users, let’s also set the password for them. The `passwd` command lets you set the password for your own account, or if you have the permissions, set the password for other accounts.

Here are some examples of using the `passwd` command:

Change the password for the current user:

`passwd`

This will prompt you to enter a new password for the current user.

Change the password for a specific user:

`passwd <username>`

Replace `username` with the name of the user whose password you want to change.

Force a user to change their password at the next login:

`passwd -f <username>`

Set an expiration date for a user’s password:

`passwd -e -n days -w warndays <username>`

Replace `days` with the number of days before the password expires and `warn days` with the number of days before the password expires that the user will be warned.

These are just a few examples of using the `passwd` command in Linux. By understanding how to use this command effectively, you can manage user accounts and ensure that your system is secure.

![[Image 3.28.png]]