
# service

[[🏷️Linux command]]

The `service` command in Linux is used to manage system services, which are long-running processes that are started at boot time and run in the background. These services are responsible for providing various system functionalities, such as networking, database management, and user authentication.

The `service` command is used to start, stop, restart, and check the status of these services. It is a front-end to the `systemctl` command, which is used to manage the `systemd` service manager.

The basic syntax of the command is as below.

`service ssh status`
`service ssh stop`
`service ssh start`

![[Image 3.17.png]]

As you can see in the image, the `ssh` server is running on our system.

> [!info] Note
> The `service` command can behave differently depending on the init system in use. Various init systems, such as `systemd`, `SysVinit`, `Upstart`, and `runit`, have their own commands and methods for managing services. While `service` provides a convenient interface on some systems, always check the specific documentation for the init system you are working with for accurate command usage.

