# TechOps ConfigWiki

A handy, well-organized documentation and configuration wiki for IT professionals, DevOps engineers, and system administrators. This project provides setup guides, best practices, and automation workflows—especially for Ansible—to help teams automate infrastructure setup and configuration.

---

## 1. Project Overview

**TechOps ConfigWiki** is a static documentation site built with [MkDocs](https://www.mkdocs.org/) and the Material theme. It serves as a practical knowledge base for:
- Infrastructure automation
- Configuration management
- DevOps best practices

The main focus is on Ansible, but the structure is extensible for Linux, Docker, Kubernetes, CI/CD, and more.

---

## 2. Features

- 📚 **Comprehensive Guides:** Step-by-step setup and usage instructions for Ansible and related tools
- 🏗️ **Lab Architecture:** Vagrant-based Ansible lab for hands-on practice
- 🗂️ **Organized Structure:** Clear navigation for quick reference
- 🧩 **Extensible:** Easily add new sections for Linux, Docker, Kubernetes, Git, CI/CD, and more
- 🔍 **Searchable:** Instant search with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- 📝 **Best Practices:** Real-world examples and recommendations
- 🚀 **Automated Deployment:** GitHub Actions workflow for CI/CD to GitHub Pages

---

## 3. Folder Structure

```
Aayush_Pawar/
├── docs/                  # Documentation source files
│   ├── index.md           # Home page
│   └── ansible/           # Ansible guides
│       ├── index.md       # Ansible introduction
│       ├── setup.md       # Lab setup and architecture
│       └── jobs.md        # (Reserved for jobs/daily tasks)
├── mkdocs.yml             # MkDocs configuration
├── requirements.txt       # Python dependencies for MkDocs and plugins
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions workflow for deployment
├── venv/                  # (Optional) Python virtual environment
└── site/                  # (Generated) Static site output
```

---

## 4. How to Use

### 📖 Browsing the Wiki
- Visit the live site: [TechOps ConfigWiki](https://ayushpawar21.github.io/TechOpsConfigWiki/)
- Use the navigation menu to explore topics.

### 🛠️ Local Development
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ayushpawar21/TechOpsConfigWiki.git
   cd TechOpsConfigWiki
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the local server:**
   ```bash
   mkdocs serve
   ```
   Then open [http://localhost:8000](http://localhost:8000) in your browser.

### 🚀 Deployment
- Changes to the `main` branch are automatically deployed to GitHub Pages via [GitHub Actions](.github/workflows/deploy.yml).

---

## 5. Lab Architecture

The Ansible lab uses Vagrant and VirtualBox to simulate a real-world automation environment:

```mermaid
graph TD
    "Host Machine" -->|"Vagrant"| "VirtualBox"
    "VirtualBox" --> "Control Node 192.168.56.10 Ansible"
    "Control Node 192.168.56.10 Ansible" -->|"SSH"| "Managed Node 1 192.168.56.11"
    "Control Node 192.168.56.10 Ansible" -->|"SSH"| "Managed Node 2 192.168.56.12"
    "Control Node 192.168.56.10 Ansible" -->|"SSH"| "Managed Node 192.168.56.1X"
```

- **Control Node:** Runs Ansible and manages other nodes
- **Managed Nodes:** Simulated servers for automation practice
- **Inventory:** Dynamically generated for each lab

See [docs/ansible/setup.md](docs/ansible/setup.md) for full setup instructions.

---

## 6. Contributing

Contributions are welcome! To propose changes:
1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes with clear messages
4. Open a Pull Request

For major changes, please open an issue first to discuss your ideas.

---

## 7. License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). (If you add a LICENSE file, update this section accordingly.)

---

## 8. Contact / Author

- **Author:** Aayush Pawar
- **GitHub:** [ayushpawar21](https://github.com/ayushpawar21)
- **Project Site:** [TechOps ConfigWiki](https://ayushpawar21.github.io/TechOpsConfigWiki/)

For questions or suggestions, please open an [issue](https://github.com/ayushpawar21/TechOpsConfigWiki/issues). 