
# df & mount

[[🏷️Linux command]]

When working with Linux, the `df` and `mount` commands are very efficient utilities to mount filesystems and get details of the file system.

The `df` command is used to display the amount of disk space used and available on the file systems, and the `mount` command is used to mount a file system or device to a specific directory.

When we say `mount`, it means that we’ll connect the device to a folder so we can access the files from our filesystem. The default syntax to mount a filesystem is below:

`mount /dev/cdrom /mnt`
`df -h`

In the above case, `/dev/cdrom` is the device that needs to be mounted. Usually, a mountable device is found inside the `/dev` folder. `mnt` is the destination folder to which to mount the device. You can change it to any folder you want, but we have used `/mnt` as it’s the system’s default folder for mounting devices.

To see the mounted devices and get more information about them, we use the df command. Just typing `df` will give us the data in bytes, which is not readable. So, we’ll use the `-h` parameter to make the data human-readable.

![[Image 3.20.png]]