Vagrant.configure("2") do |config|

  config.vm.box = "azure"
  config.env.enable #enable the plugin
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  config.vm.hostname = "localhost"
  config.vm.network "public_network"
  config.vm.network "private_network", ip: "40.68.191.37", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 80, host: 80

  config.ssh.private_key_path = '~/.ssh/id_rsa'


  config.vm.provider :azure do |azure|
    # mgmt_certificate = File.expand_path('C:\Users\Mmar\botdietas\azurevagrant.cer')
    # mgmt_endpoint = 'https://management.core.windows.net'

    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    # azure.vm_image_urn = 'Canonical:UbuntuServer:14.04.3-LTS:14.04.201508050'
    azure.vm_size = 'Basic_A0'
    # azure.vm_size = 'Standard_D1'
    azure.location = 'westeurope'
    azure.vm_name = 'BOT-DIETAS'
    azure.tcp_endpoints = '80:80'
    azure.vm_password = 'aabbcc'

    azure.tenant_id = ENV['TENANT_ID']
    azure.client_id = ENV['CLIENT_ID']
    azure.client_secret = ENV['CLIENT_SECRET']
    azure.subscription_id =ENV['SUBSCRIPTION_ID']
   end


   #Provisionamiento
   config.vm.provision "ansible" do |ansible|
       ansible.sudo = true
       ansible.playbook = "configuracion.yml"
       ansible.verbose = "-vvvv"
       ansible.host_key_checking = false
  end

end
