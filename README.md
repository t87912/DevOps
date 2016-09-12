# DevOps

## Instructions for using Git:

**1. Open GitBash**

**2. Navigate to desired location**

<p align="center">
    You can right click on the folder and open in GitBash
</p> <br />
**3. Make a new directory** 

<p align="center">
	mkdir <name-of-directory><br />
	e.g. mkdir DevOpsProject
</p> <br />
**4. Enter the directory you created**

<p align="center">
	cd <name-of-directory><br />
	e.g. cd DevOpsProject
</p> <br />
**5. Initialise Git**
<p align="center">
	git innit
</p> <br />
**6. Clone the Git repo**

<p align="center">
	git clone <repo-url><br />
	e.g. git clone https://github.com/t87912/DevOps.git
</p> <br />

**The repo is now on your local machine and you can start editing it.**

## Saving the changes to Github:

**1. Add the files you want to update**

<p align="center">
	git add <filename><br />
	OR<br />
	git add . (this will add the whole directory, not just single files)
</p> <br />
**2. Commit the changes**

<p align="center">
	git commit -m "commit message"
</p> <br />
**3. Push the changes**

<p align="center">
	git push
</p> <br />

## Installing Vagrant:

**1. Get the vagrant installer from the following location:

<p align="center">
	C:\LocalInstall\SharePoint Repositories\DevOps-CI\Vagrant
</p> <br />
**2. Follow the installation instructions.**

## Running Vagrant:

**1. Clone the Github repo, use the instructions from above**

**2. Copy and paste the repo elsewhere, this is to prevent any files Vagrant creates being accidently pushed to the repo.**

**3. Enter the directory that you pasted the repo into, then cd into the repo**

**4. Run vagrant**
<p align="center">
	vagrant up
</p> <br />

## Vagrant Troubleshooting
This section will troubleshoot common vagrant problems

**A VirtualBox machine with the name 'master'/'agent' already exists.**
You have another virtual machine with the same name as this one, go into VirtualBox and delete the Virtual Machine and all its associated files.

## Brief Project Description
This project is a shared project produced by a group of trainee consultants etc etc...

## New Features/ Changes
* To be filled.

## Next Upload
