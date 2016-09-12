# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.boot_timeout = 400
	config.vm.synced_folder "shared", "/shared"
		
	config.vm.define "master" do |master|
		master.vm.hostname = "ammaster.qac.local"
		master.vm.box = "chad-thompson/ubuntu-trusty64-gui"
		master.vm.network :public_network, :public_network => "wlan0", ip: "192.168.1.11"
		master.vm.provision :shell, path: "bootstrap_master.sh"
		master.vm.provider :virtualbox do |masterVM|
			masterVM.gui = true
			masterVM.name = "master"
			masterVM.memory = 4096
			masterVM.cpus = 2
		end
	end
	
	config.vm.define "agent" do |agent|
		agent.vm.hostname = "amagent1.qac.local"
		agent.vm.box = "chad-thompson/ubuntu-trusty64-gui"
		agent.vm.network :public_network, :public_network => "wlan0", ip: "192.168.1.12"
		agent.vm.provision :shell, path: "bootstrap_agent.sh"
		agent.vm.provider :virtualbox do |agentVM|
			agentVM.gui = true
			agentVM.name = "agent1"
			agentVM.memory = 4096
			agentVM.cpus = 2
		end
	end
	
end

