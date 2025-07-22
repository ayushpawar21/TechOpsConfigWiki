# **Vagrant Ansible Lab Setup Guide**

This guide will walk you through setting up a local Ansible control node and multiple managed nodes using Vagrant.

## **Vagrant Ansible Lab Architecture**


```mermaid
graph TD
    Host[Host Machine] -->|Vagrant| VirtualBox
    VirtualBox --> Control[Control Node 192.168.56.10 Ansible]
    Control -->|SSH| Managed1[Managed Node 1 192.168.56.11]
    Control -->|SSH| Managed2[Managed Node 2 192.168.56.12]
    Control -->|SSH| ManagedN[Managed Node 192.168.56.1X]

```

## **Prerequisites**

Before you begin, ensure you have the following installed on your host machine:

- Vagrant: Download and install from [https://www.vagrantup.com/downloads](https://www.vagrantup.com/downloads)
- VirtualBox (or another Vagrant provider): Download and install from [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

##**Setup Steps**

Follow these steps to get your Ansible lab up and running:

### **Step 1: Create Project Directory and Vagrantfile**

Create a new directory for your project. You can name it `ansible_vagrant_lab` or anything you prefer.

```bash
mkdir ansible_vagrant_lab
cd ansible_vagrant_lab
```

Inside this new directory, create a file named Vagrantfile.

```bash
touch Vagrantfile
```

Open the Vagrantfile with your preferred text editor and paste the following content into it:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # --- User Configuration Variables ---
  # Number of Ansible managed nodes to create (excluding the control node)
  VAGRANT_NUM_MANAGED_NODES = 2

  # Private IP address prefix for the VMs (e.g., "192.168.56.")
  # The control node will be .10, managed nodes will start from .11
  VAGRANT_IP_PREFIX = "192.168.56."
  # --- End User Configuration Variables ---


  # Define the base box for all VMs
  config.vm.box = "ubuntu/focal64" # Ubuntu 20.04 LTS

  # Disable automatic box update checking
  config.vm.box_check_update = false

  # --- Ansible Control Node Setup ---
  config.vm.define "ansible-control" do |control|
    control.vm.hostname = "ansible-control"
    control.vm.network "private_network", ip: "#{VAGRANT_IP_PREFIX}10"

    control.vm.provider "virtualbox" do |vb|
      vb.name = "ansible-control"
      vb.memory = "1024" # Allocate 1GB RAM
      vb.cpus = "1"      # Allocate 1 CPU
    end

    # Provision the control node: install Ansible, create inventory
    control.vm.provision "shell", inline: <<-'SHELL'
      echo "--- Provisioning Ansible Control Node ---"
      sudo apt-get update
      sudo apt-get install -y ansible git python3-pip

      # Create Ansible inventory file dynamically
      echo "[managed]" | sudo tee /etc/ansible/hosts > /dev/null
      for i in $(seq 1 2); do
        ip=$((10 + i))
        echo "ansible-managed-${i} ansible_host=192.168.56.${ip} ansible_user=vagrant" | sudo tee -a /etc/ansible/hosts > /dev/null
      done
      echo "" | sudo tee -a /etc/ansible/hosts > /dev/null

      echo "Ansible control node setup complete."
      echo "Generated Ansible inventory (/etc/ansible/hosts):"
      cat /etc/ansible/hosts
    SHELL
  end

  # --- Ansible Managed Nodes Setup ---
  (1..VAGRANT_NUM_MANAGED_NODES).each do |i|
    config.vm.define "ansible-managed-#{i}" do |managed|
      managed.vm.hostname = "ansible-managed-#{i}"
      managed.vm.network "private_network", ip: "#{VAGRANT_IP_PREFIX}#{10 + i}"

      managed.vm.provider "virtualbox" do |vb|
        vb.name = "ansible-managed-#{i}"
        vb.memory = "512" # Allocate 512MB RAM
        vb.cpus = "1"     # Allocate 1 CPU
      end

      # Provision managed nodes: ensure python3 is installed for Ansible
      managed.vm.provision "shell", inline: <<-SHELL
        echo "--- Provisioning Ansible Managed Node #{i} ---"
        sudo apt-get update
        sudo apt-get install -y python3
        echo "Ansible managed node #{i} setup complete."
      SHELL
    end
  end

  # Optional: Share playbooks between host and control node
  # config.vm.synced_folder "ansible/", "/home/vagrant/ansible", type: "virtualbox"

end


```
## **Step 2: Customize Vagrantfile (Optional)**

You can modify the following variables in your Vagrantfile to suit your needs:
```bash

VAGRANT_NUM_MANAGED_NODES: Change the value 2 to your desired number of Ansible managed nodes.
VAGRANT_IP_PREFIX: If you prefer a different private IP address range for your VMs, change "192.168.56." to your desired prefix.

```

## **Step 3: Start the Virtual Machines**

Navigate to your ansible_vagrant_lab directory in your terminal and run the following command:

```bash
vagrant up
```

This command will:

Download the ubuntu/focal64 Vagrant box (if you don't have it locally).
Create and configure the ansible-control VM.
Create and configure the specified number of ansible-managed-X VMs.
This process may take some time depending on your internet connection and system resources.

## **Step 4: Connect to the Ansible Control Node**

Once vagrant up completes, you can SSH into your Ansible control node:

```bash
vagrant ssh ansible-control
```

## **Step 5: Verify Ansible Setup on Control Node**

After connecting to the ansible-control VM, you can verify that Ansible is installed and the inventory file has been generated correctly:

```bash
ansible --version
cat /etc/ansible/hosts
```

You should see output similar to this, listing your managed nodes with their assigned IP addresses:
```text
[managed]
ansible-managed-1 ansible_host=192.168.56.11 ansible_user=vagrant ansible_ssh_private_key_file=/home/vagrant/.ssh/id_rsa
ansible-managed-2 ansible_host=192.168.56.12 ansible_user=vagrant ansible_ssh_private_key_file=/home/vagrant/.ssh/id_rsa
```

## **Step 6: Clean Up (Optional)**
When you are finished with your lab and want to remove the virtual machines from your system, run the following command from your host machine (in the ansible_vagrant_lab directory):

```bash
vagrant destroy -f
```
This will power down and delete all the VMs created by the Vagrantfile.