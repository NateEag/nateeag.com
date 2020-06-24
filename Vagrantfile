# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "bento/ubuntu-20.04"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./src", "/vagrant"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/main.yml"

    ansible.extra_vars = {
        # By default Ansible assumes Python 2. Force it to use Python 3, since
        # that's what we're doing this project in, and that's what's installed
        # on an Ubuntu 16.04 machine by default.
        ansible_python_interpreter: "/usr/bin/python3",
        is_dev_environment: true,
        ssl_cert_dir: "/etc/ssl"
    }
  end

end
