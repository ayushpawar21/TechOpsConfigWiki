# TechOps ConfigWiki

[![CI/CD](https://github.com/ayushpawar21/TechOpsConfigWiki/actions/workflows/deploy.yml/badge.svg)](https://github.com/ayushpawar21/TechOpsConfigWiki/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A handy, well-organized documentation and configuration wiki for IT professionals, DevOps engineers, and system administrators.  
This project provides setup guides, best practices, and automation workflows—especially for Ansible—to help teams automate infrastructure setup and configuration.

---

## 📑 Table of Contents

- [1. Project Overview](#1-project-overview)  
- [2. Features](#2-features)  
- [3. Folder Structure](#3-folder-structure)  
- [4. How to Use](#4-how-to-use)  
  - [📖 Browsing the Wiki](#-browsing-the-wiki)  
  - [🛠️ Local Development](#️-local-development)  
  - [🚀 Deployment](#-deployment)  
- [5. Contributing](#5-contributing)  
- [6. License](#6-license)  
- [7. Contact / Author](#7-contact--author)  
- [Explore Topics](#explore-topics)  

---

## 1. Project Overview

**TechOps ConfigWiki** is a static documentation site built with [MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).  
It serves as a practical knowledge base for:

- Infrastructure automation  
- Configuration management  
- DevOps best practices  

The main focus is on **Ansible**, but the structure is extensible for Linux, Docker, Kubernetes, CI/CD, and more.

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

??? note "Expand to view"
    ```
    TechOpsConfigWiki/
    ├── docs/                  # Documentation source files
    │   ├── index.md           # Home page
    │   └── ansible/           # Ansible guides
    │       ├── index.md       # Ansible introduction
    │       ├── setup.md       # Lab setup and architecture
    │       └── AnsibleOps.md  # (Reserved for jobs/daily tasks)
    ├── mkdocs.yml             # MkDocs configuration
    ├── requirements.txt       # Python dependencies for MkDocs and plugins
    ├── .github/
    │   └── workflows/
    │       └── deploy.yml     # GitHub Actions workflow for deployment
    ├── venv/                  # (Optional) Python virtual environment
    └── site/                  # (Generated) Static site output
    ```


## 4. How to Use

### 📖 Browsing the Wiki
- Visit the live site: [TechOps ConfigWiki](https://ayushpawar21.github.io/TechOpsConfigWiki/)  
- Use the navigation menu to explore topics  

---

### 🛠️ Local Development

!!! tip "Quick Start"
    Clone the repository, install dependencies, and run the server:

    ```bash
    git clone https://github.com/ayushpawar21/TechOpsConfigWiki.git
    cd TechOpsConfigWiki

    # (Optional) create virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

    # Run local server
    mkdocs serve
    ```

    Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

### 🚀 Deployment

Changes to the `main` branch are automatically deployed to GitHub Pages via  
[GitHub Actions](.github/workflows/deploy.yml).

---

## 5. Contributing

Contributions are welcome! 🎉

1. Fork the repository  
2. Create a new branch (`feature/your-feature`)  
3. Commit your changes with clear messages  
4. Open a Pull Request  

!!! note "Major Changes"
    For significant modifications, please open an issue first to discuss your ideas.

---

## 6. License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).  
(If you add a LICENSE file, update this section accordingly.)

---

## 7. Contact / Author

- **Author:** Aayush Pawar  
- **GitHub:** [ayushpawar21](https://github.com/ayushpawar21)  
- **Project Site:** [TechOps ConfigWiki](https://ayushpawar21.github.io/TechOpsConfigWiki/)  

For questions or suggestions, please open an [issue](https://github.com/ayushpawar21/TechOpsConfigWiki/issues).

---

## Explore Topics

<div class="grid cards" markdown>
- :simple-ansible: **Ansible**
  ---
  Setup, playbooks, and automation guides.
- :simple-docker: **Docker**
  ---
  Containerization and orchestration basics.
- :simple-kubernetes: **Kubernetes**
  ---
  Cluster setup and best practices.
- :simple-git: **CI/CD**
  ---
  Continuous integration and delivery workflows.
</div>
