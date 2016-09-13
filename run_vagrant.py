# Test Script to get vagrant running etc

# Imports:
import os

print ("Python Script")
print ("REMEMBER: if you have ran this script before, delete the VM Master/Agent from VirtualBox.")
print ("Working in: ", os.getcwd())
currentDir = ("cd %s" % os.getcwd())
os.system(currentDir) # Changing directory in CMD
os.system("vagrant up") # Running Vagrant
os.system('set /p id="Press enter to quit program..."') # stop CMD from quitting
