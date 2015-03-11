Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"

  config.ssh.forward_agent = true
  config.vm.network "private_network", :ip => "172.16.42.43"
  #config.vm.provision :shell, :path => 'script/provision-vm'
  config.vm.provision "file", source: "third-party/oracle-instantclient11.1-basic-11.1.0.7.0-1.x86_64.rpm", destination: "~/oracle-instantclient11.1-basic-11.1.0.7.0-1.x86_64.rpm"
  config.vm.provision "file", source: "third-party/cx_Oracle-5.1.2-11g-py27-1.x86_64.rpm", destination: "~/cx_Oracle-5.1.2-11g-py27-1.x86_64.rpm"
  config.vm.provision :shell, path: "script/provision.sh"
  
  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--memory', ENV['VM_MEMORY'] || 2048]
    vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
    vb.customize ['modifyvm', :id, '--natdnsproxy1', 'on']
  end

end
