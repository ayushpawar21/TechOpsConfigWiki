# Introduction to Ansible

Ansible is a popular open-source automation tool used by IT professionals and DevOps engineers to automate the configuration, management, and deployment of applications across multiple servers.

---

## Why Ansible?

- **Agentless:** No need to install any agent software on target machines.
- **Simple syntax:** Uses YAML for easy-to-read and write playbooks.
- **Powerful:** Automate complex tasks, deploy applications, and orchestrate workflows.
- **Scalable:** Manage anything from a few servers to thousands.
- **Flexible:** Works with Linux, cloud platforms, containers, and more.

---

## How Ansible Works

Ansible connects to your target machines over SSH and executes small programs called *modules* to perform tasks such as installing software, copying files, or restarting services.

Key components:

- **Inventory:** A list of hosts to manage.
- **Playbooks:** YAML files describing automation workflows.
- **Modules:** Reusable units of work.
- **Roles:** Collections of tasks, templates, and files for modular management.

---

## Basic Example: Ping Test

Check if Ansible can reach all your hosts by running:

```bash
ansible all -i inventory.ini -m ping
```