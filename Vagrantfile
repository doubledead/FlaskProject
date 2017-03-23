Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "web-dev"

  config.vm.provision "shell", path: "provision.sh"

  config.vm.network "forwarded_port", guest: 5000, host: 8080, id: "flask"
end
