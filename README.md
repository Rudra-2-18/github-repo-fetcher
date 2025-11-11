# 🐙 GitHub Repo Fetcher

**GitHub Repo Fetcher** is a simple Python automation script that fetches all public repositories of any GitHub user using the GitHub REST API.  
It demonstrates **API pagination**, **rate-limit handling**, **SQLite database storage**, and **structured logging**.

---

## 🚀 Features

- Fetches all public repositories for a given GitHub username  
- Handles **pagination** automatically (fetches up to 100 repos per page)  
- Gracefully waits and resumes when the GitHub **rate limit** is reached  
- Saves repository details in a local **SQLite database**  
- Uses **Rotating Log Files** to manage logs efficiently  
- Command-line support via `argparse`  
- Works cross-platform (Windows, macOS, Linux)

---

## 📦 Requirements

Make sure you have **Python 3.8+** installed.

Then install the required dependencies:

	pip install requests

## ⚙️ Usage

Run the script from your terminal:

	python repo-fetcher.py --user <github-username>


Example:

	python repo-fetcher.py --user bookie212

Optional Arguments:

	Argument	Description	Default
	--user	GitHub username to fetch repos for	bookie212

## 💾 Database Details

A SQLite database file named repos.db is created automatically.
Each record includes:

	Column	Description
	id	Auto-incremented ID
	timestamp	Date and time of the API call
	status_code	HTTP status code
	user	GitHub username
	repo_name	Repository name
	creation_date	Repository creation timestamp
	stars	Number of stars
	url	Repository URL

## 🧠 Concepts Demonstrated

API Pagination: Fetching data page by page until all results are retrieved.

Rate Limiting: Automatically waiting until the GitHub API allows more requests.

Logging: Using Python’s logging with RotatingFileHandler.

Data Persistence: Storing structured data in SQLite for easy querying.

## 🧩 Example Output

Console:

	Fetching repositories for user: bookie212
	Rate limit will reset in 25 seconds
	Resuming API calls.
	Finished fetching repositories for user: bookie212.
	Process finished. Cleaning up logging handlers.

Database record (example):

	id	timestamp	repo_name	stars	url
	1	2025-10-30 14:22:11	cool-project	42	https://github.com/bookie212/cool-project

## 🪪 License

This project is licensed under the MIT License

 — you’re free to use, modify, and share it.
