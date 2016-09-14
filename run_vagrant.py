# Test Script to get vagrant running etc

# Imports:
import os
import shutil
import errno

# remove bootstrap master 
#os.remove("bootstrap_master.sh")

vagrantText = """
Vagrant.configure("2") do |config|
        config.vm.define "agent" do |agent|
                agent.vm.hostname = "amagent%s.qac.local"
                agent.vm.box = "chad-thompson/ubuntu-trusty64-gui"
                agent.vm.network :public_network, :public_network => "wlan0", ip: "%s"
                agent.vm.provision :shell, path: "bootstrap_agent.sh"
                agent.vm.provider :virtualbox do |agentVM|
                        agentVM.gui = true
                        agentVM.name = "agent%s"
                        agentVM.memory = 4096
                        agentVM.cpus = 2
                end
        end
end
"""

agentBootstrap = """
# update sys
sudo apt-get update

# install ssh
sudo apt-get install -y openssh-server
sudo apt-get install -y openssh-client

# disable the firewall
sudo ufw disable

sudo apt-get install -y puppet
#facter fqdn
#facter ipaddress_eth1

echo "" | sudo tee --append /etc/hosts 2> /dev/null && \\
echo "127.0.0.1      amagent%s.qac.local    puppet" | sudo tee --append /etc/hosts 2> /dev/null && \\
echo "192.168.1.9    ammaster.qac.local    puppetmaster" | sudo tee --append /etc/hosts 2> /dev/null && \\
echo "%s    amagent%s.qac.local    puppet" | sudo tee --append /etc/hosts 2> /dev/null


#add server in puppet.conf
sed -i "2i server=ammaster.qac.local" /etc/puppet/puppet.conf

#test master-agent
sudo puppet agent --test --server=ammaster.qac.local
"""

masterBootstrap = """
#!/bin/bash

# This (master) fqdn: ammaster.qac.local
# This (master) ip: 192.168.1.9

# Start by updating the system
sudo apt-get update

# Install the openssh server/client
sudo apt-get install -y openssh-server openssh-client

# Disable the firewall
sudo ufw disable

# Install puppet
sudo apt-get install -y puppet puppetmaster 

# Adding lines in hosts file: (/etc/hosts)
# This inserts 2 lines in the host.
echo "" | sudo tee --append /etc/hosts 2> /dev/null && \
echo "# Host config for Puppet Master and Agent Nodes" | sudo tee --append /etc/hosts 2> /dev/null && \
echo "127.0.0.1       ammaster.qac.local    puppetmaster" | sudo tee --append /etc/hosts 2> /dev/null && \
echo "192.168.1.9     ammaster.qac.local    puppetmaster" | sudo tee --append /etc/hosts 2> /dev/null
 
# Create the site.pp:
sudo touch /etc/puppet/manifests/site.pp

# Sign the certs:
# sudo puppet cert list
# sudo puppet cert sign --all

# Install java, maven, git, jira, jenkins
sudo puppet module install puppetlabs-java -i /etc/puppet/modules
sudo puppet module install maestrodev-maven -i /etc/puppet/modules
sudo puppet module install puppetlabs-git -i /etc/puppet/modules
sudo puppet module install maestrodev-jenkins -i /etc/puppet/modules


"""

sitepp = """

# Edit site.pp:
echo "" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "node 'amagent%s'{" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "class { 'java':" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "  distribution => 'jdk'," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "  version      => 'latest'," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "}" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "include jenkins" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "include git" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "include maven" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "#include tomcat" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "}" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null

"""

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

print ("Python script to setup and run vagrant")
print ("REMEMBER: if you have ran this script before, delete the VM Master/Agent from VirtualBox.")
print ("Working in: ", os.getcwd())
currentDir = ("cd %s" % os.getcwd())
os.system(currentDir) # Changing directory in CMD
#os.system("vagrant up") # Running Vagrant
#os.system('set /p id="Press enter to quit program..."') # stop CMD from quitting

noMachines = int(input("Please enter the number of agents: "))

# Create the master bootstrap with site.pp stuff for each agent:
#listSitePP = []
for z in range(1, noMachines+1):
    siteppFormatted = sitepp % (z)
    #listSitePP.append(siteppFormatted)
    masterBootstrap = masterBootstrap + siteppFormatted

#for a in range(1, len(listSitePP)):
 #   masterBootstrap.append

#masterBootstrap = masterBootstrap + 

print ("Printing Master Bootstrap")
print (masterBootstrap)
print ("END Master Bootstrap")

masterBootstrapFile = open("bootstrap_master.sh",'a') # create empty text file
masterBootstrapFile.write(masterBootstrap)
masterBootstrapFile.close()


ipAddresses = []
for i in range(1, noMachines+1):
    ip = input("Please input the ip address for agent %s: " % (i))
    ipAddresses.append(ip)

print ("Creating %s agents with the following IP addresses: " % (noMachines))
print (ipAddresses)

print ("Creating the vagrant files...")
vagrantFiles = []
for x in range(1, noMachines+1):
    vagrantConfig = vagrantText % (x, ipAddresses[x-1], x)
    print (vagrantConfig)
    vagrantFiles.append(vagrantConfig)

print ("Creating the agent bootstrap files...")
bootstrapFiles = []
for y in range(1, noMachines+1):
    agentConfig = agentBootstrap % (y, ipAddresses[y-1], y)
    bootstrapFiles.append(agentConfig)
    print (agentConfig)

print ("Creating the folder structure...")
for i in range(1, noMachines+1):
    stringDir = ("Agent%s" % (i))
    os.makedirs(stringDir) # Make the Agent X dir
    os.chdir(stringDir) # cd into Agent X dir
    os.makedirs("Shared") # Make shared folder
    #os.makedirs("Config")

    # Make bootstrap here:
    bootstrapFile = open("bootstrap_agent.sh",'a') # create empty text file
    bootstrapFile.write(bootstrapFiles[i-1])
    bootstrapFile.close()

    # Make vagrant file here:
    vagrantFile = open("Vagrantfile",'a') # create empty text file
    vagrantFile.write(vagrantFiles[i-1])
    vagrantFile.close()
    
    os.chdir("Shared")
    txtFile = open("testTextFile.txt",'a') # create empty text file
    txtFile.close()
    os.chdir("..")
    os.chdir("..")

    #destString = "\\Agent%s\\Config" % (i)
    #copyanything("//Config", destString)

# run vagrant
#os.system("vagrant up") # Running Vagrant
    
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

#print ("Working in: ", os.getcwd())
#copyanything("C:\\Users\\Administrator\\Desktop\\Wed9am\\DevOpsWorkingFolder\\Shared", "C:\\Users\\Administrator\\Desktop\\Wed9am\\DevOpsWorkingFolder\\Agent1")





















