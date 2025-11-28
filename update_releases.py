import json
import requests
import os

CONFIG_FILE = "tools.json"
OUTPUT_FILE = "docs/release.md"   # Updated path

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def fetch_github_latest(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("tag_name", "N/A")
    except:
        pass
    return "N/A"

def fetch_jenkins_version(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("core", {}).get("version", "N/A")
    except:
        pass
    return "N/A"

def generate_markdown(tools):
    md = "# 🛠️ Auto-Updated Technology Release Tracker\n\n"
    md += "This page is updated automatically every day.\n\n---\n\n"

    for tool in tools:
        name = tool["name"]
        notes = tool["notes"]
        api = tool["api"]

        if "jenkins" in name.lower():
            version = fetch_jenkins_version(api)
        else:
            version = fetch_github_latest(api)

        md += f"## {name}\n"
        md += f"**Latest Version:** {version}\n\n"
        md += f"**Release Notes:** {notes}\n\n"
        md += "---\n\n"

    return md

def save_markdown(content):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(content)

if __name__ == "__main__":
    config = load_config()
    tools = config["tools"]
    md_content = generate_markdown(tools)
    save_markdown(md_content)
    print("✔ docs/release.md updated successfully!")
