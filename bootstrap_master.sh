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
sudo puppet cert list
sudo puppet cert sign --all

# Install java, maven, git, jira, jenkins
sudo puppet module install puppetlabs-java -i /etc/puppet/modules
sudo puppet module install maestrodev-maven -i /etc/puppet/modules
sudo puppet module install puppetlabs-git -i /etc/puppet/modules
#sudo puppet module install puppet-jira -i /etc/puppet/modules
#sudo puppet module install mkrakowitzer-jira -i /etc/puppet/modules
sudo puppet module install rtyler-jenkins -i /etc/puppet/modules
#sudo puppet module install puppetlabs-java



# Edit site.pp:
echo "" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "node 'amagent1'{" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "class { 'java':" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "  distribution => 'jdk'," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "  version      => 'latest'," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "}" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "include jenkins" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "include git" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "include maven" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "#include tomcat" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
echo "}" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null






#echo "class { 'jenkins':" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
#echo "config_hash  => { 'HTTP_PORT' => { 'value' => 8081 } }," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
#echo "}" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \


#echo "class { 'jira':" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
#echo "javahome    => '/opt/java'," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
#echo "version     => '6.3.7'," | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \
#echo "}" | sudo tee --append /etc/puppet/manifests/site.pp 2> /dev/null && \


