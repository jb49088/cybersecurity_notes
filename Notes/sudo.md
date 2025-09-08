
# sudo

[[🏷️Linux command]]

> With great power, comes great responsibility

This is the quote displayed when a sudo-enabled user(sudoer) first uses the `sudo` command to escalate privileges. This command is equivalent to logging in as `root` (based on what permissions you have as a sudoer).

`sudo <command you want to run`

Just add the command `sudo` before any command that you need to run with escalated privileges, and that’s it. It’s very simple to use, but can also be an added security risk if a malicious user gains access to a sudoer.