[转载于本文](https://bencane.com/2013/09/16/understanding-a-little-more-about-etcprofile-and-etcbashrc/)



# Understanding a little more about /etc/profile and /etc/bashrc

September 16, 2013 · 3 min · Benjamin Cane

Recently I was working on an issue where an application was not retaining the umask setting set in the root users profile or `/etc/profile`. After looking into the issue a bit it seemed that the application in question only applied the umask setting that was set in `/etc/bashrc` and would not even accept the values being the applications own start scripts.

After doing a bit of researched I learned a little bit more about what exactly these files do, the differences between them and when they are executed. I figured this would be a good thing to share as it is not a topic that comes up very often.

## What is /etc/profile used for?

If you have been using Linux for a while you are probably familiar with the `.profile` or `.bash_profile` files in your home directory. These files are used to set environmental items for a users shell. Items such as umask, and variables such as `PS1` or `PATH`.

The `/etc/profile` file is not very different however it is used to set system wide environmental variables on users shells. The variables are sometimes the same ones that are in the `.bash_profile`, however this file is used to set an initial `PATH` or `PS1` for all shell users of the system.

### /etc/profile.d

In addition to the setting environmental items the `/etc/profile` will execute the scripts within `/etc/profile.d/*.sh`. If you plan on setting your own system wide environmental variables it is recommended to place your configuration in a shell script within `/etc/profile.d`.

## What is /etc/bashrc used for?

Like `.bash_profile` you will also commonly see a .bashrc file in your home directory. This file is meant for setting command aliases and functions used by bash shell users.

Just like the `/etc/profile` is the system wide version of `.bash_profile`. The `/etc/bashrc` for Red Hat and `/etc/bash.bashrc` in Ubuntu is the system wide version of `.bashrc`.

Interestingly enough in the Red Hat implementation the `/etc/bashrc` also executes the shell scripts within `/etc/profile.d` but only if the users shell is a Interactive Shell (aka Login Shell)

## When are these files used?

The difference between when these two files are executed are dependent on the type of login being performed. In Linux you can have two types of login shells, Interactive Shells and Non-Interactive Shells. An Interactive shell is used where a user can interact with the shell, i.e. your typical bash prompt. Whereas a non-Interactive shell is used when a user cannot interact with the shell, i.e. a bash scripts execution.

The difference is simple, the `/etc/profile` is executed only for interactive shells and the `/etc/bashrc` is executed for both interactive and non-interactive shells. In fact in Ubuntu the `/etc/profile` calls the `/etc/bashrc` directly.