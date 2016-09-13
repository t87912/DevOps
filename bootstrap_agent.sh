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

echo "" | sudo tee --append /etc/hosts 2> /dev/null && \
echo "127.0.0.1      amagent1.qac.local    puppet" | sudo tee --append /etc/hosts 2> /dev/null && \
echo "192.168.1.9    ammaster.qac.local    puppetmaster" | sudo tee --append /etc/hosts 2> /dev/null && \
echo "127.168.1.8    amagent1.qac.local    puppet" | sudo tee --append /etc/hosts 2> /dev/null


#add server in puppet.conf
sed -i "2i server=ammaster.qac.local" /etc/puppet/puppet.conf

#test master-agent
sudo puppet agent --test --server=ammaster.qac.local

