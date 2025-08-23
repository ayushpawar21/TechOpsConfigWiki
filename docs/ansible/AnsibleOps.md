# ⏰ **NTP/Chrony Ansible Project**

This project provides an Ansible playbook to configure either NTP or Chrony as a time synchronization service on target hosts. It uses roles to modularize the tasks, making it reusable and easy to manage.

-----

## **Project Structure**

The project has the following directory structure:

```
.
├── ansible.cfg
├── inventroy.ini
├── ntp_or_chrony.yml
├── roles
│   └── time_config
│       ├── defaults
│       │   └── main.yml
│       └── tasks
│           └── main.yml
├── Vagrantfile
└── README.md (this file)
```

### **1. `ansible.cfg`**

This is the Ansible configuration file. It specifies the inventory file location, remote user, and disables host key checking for convenience in a lab environment.

### **2. `inventroy.ini`**

This file defines the hosts managed by Ansible. It includes a `[managed]` group with two sample hosts, `ansible-managed-1` and `ansible-managed-2`, with their respective IP addresses and SSH details.

### **3. `ntp_or_chrony.yml`**

This is the main playbook. It prompts the user to select either **`ntp`** or **`chrony`** and then applies the **`time_config`** role to all hosts.

### **4. `roles/time_config/`**

This directory contains the Ansible role for configuring the time service.

  * `defaults/main.yml`: Sets default values for the NTP servers and timezone. These can be overridden at the playbook or command line level.
  * `tasks/main.yml`: Contains all the tasks required to configure the time service. This includes:
      * **Conditional variable setting**: Determines the package name, service name, and configuration file based on the user's choice.
      * **Package installation**: Installs the selected time synchronization package.
      * **Configuration**: Backs up and deploys the new configuration file from a template.
      * **Timezone setup**: Sets the system timezone.
      * **Service management**: Restarts and enables the service.
      * **Verification**: Waits until the NTP synchronization is complete.

-----

## **Prerequisites**

  * **Vagrant**: To provision the virtual machines.
  * **VirtualBox**: As the provider for Vagrant.
  * **Git**: To clone the repository.

-----

## **Setup and Usage**

Follow these steps to set up and run the project:

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/ayushpawar21/TechOpsConfigWiki.git
    cd TechOpsConfigWiki/ntp_chrony_ansible_project
    ```

2.  **Provision Virtual Machines**:
    The `Vagrantfile` will create one **control node** (`ansible-control`) and two **managed nodes** (`ansible-managed-1`, `ansible-managed-2`). It also sets up SSH key-based authentication between the control and managed nodes.

    ```bash
    vagrant up
    ```

3.  **Run the Ansible Playbook**:
    After the VMs are up and running, SSH into the control node and execute the playbook.

    ```bash
    vagrant ssh ansible-control
    cd /vagrant
    ansible-playbook ntp_or_chrony.yml
    ```

    You will be prompted to choose the time service to install.

    ```bash
    Which time service do you want to install? (ntp or chrony): ntp
    ```

4.  **Verify the Configuration**:
    You can verify the status of the time synchronization on any of the managed nodes.

    ```bash
    vagrant ssh ansible-managed-1
    timedatectl
    ```

    The output should show **`NTP synchronized: yes`**.