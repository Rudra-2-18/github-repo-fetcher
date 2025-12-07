# 🖥️ github-repo-fetcher - Easily Fetch GitHub Repositories

## 📦 Download Now
[![Download](https://img.shields.io/badge/Download-via%20Releases-brightgreen)](https://github.com/Rudra-2-18/github-repo-fetcher/releases)

## 🚀 Getting Started
Thank you for choosing github-repo-fetcher! This simple Python script helps you fetch all public repositories of a GitHub user. You’ll get the information neatly stored in a local SQLite database. This tool is especially useful for those who wish to automate repository tracking without any programming knowledge.

## 📝 Features
- Fetches all public repositories of a specified GitHub user.
- Automatically handles pagination to ensure you retrieve every repository.
- Accounts for rate limits imposed by the GitHub API.
- Stores results in a local SQLite database.
- Maintains rotating logs to keep track of fetched data and any issues.

## 🛠️ System Requirements
To run github-repo-fetcher, ensure your system meets the following requirements:

- **Operating System:** Windows, macOS, or Linux
- **Python Version:** 3.6 or later
- **SQLite:** Pre-installed (included with Python)

## 🌐 Installation Instructions
1. **Visit the Releases Page**  
   Go to the following link to download the latest release:  
   [Download Latest Release](https://github.com/Rudra-2-18/github-repo-fetcher/releases)

2. **Choose Your Version**  
   On the Releases page, find the latest version. Click on it to view available files for download.

3. **Download the File**  
   Locate the file that matches your system and click to download.

4. **Extract the Files (if necessary)**  
   If the downloaded file is compressed (like .zip or .tar), extract it to a desired folder.

5. **Run the Script**  
   - For Windows: Open Command Prompt and navigate to the folder where the script is located. Use the command:
     ```
     python github_repo_fetcher.py [username]
     ```
   - For macOS/Linux: Open Terminal and navigate to the folder with the script. Use the command:
     ```
     python3 github_repo_fetcher.py [username]
     ```

Replace `[username]` with the GitHub username you wish to fetch repositories for.

## 📚 Usage Guide
Once you run the script:

- The application will start fetching repositories. 
- It writes all related information to the SQLite database.
- If you experience any issues, check the logs generated in the same directory for troubleshooting.

## 🔧 Configuration Options
You can customize the behavior of the script by modifying a configuration file included in the download. This file allows you to set:

- **Database Path:** Change where the SQLite database is stored.
- **Log Level:** Adjust how much information is recorded in the logs.

## 🐞 Troubleshooting
Here are some common issues and their solutions:

- **Problem:** The script doesn't run or throws an error.  
  **Solution:** Ensure Python is installed and added to your system's PATH. Check you are using the correct version of Python.

- **Problem:** Unable to connect to GitHub.  
  **Solution:** Inspect your internet connection and ensure GitHub isn't experiencing downtime.

- **Problem:** No repositories fetched.  
  **Solution:** Verify the GitHub user has public repositories and that you entered the username correctly.

## 👥 Contact and Contributions
We welcome contributions! If you find a bug or have ideas for improvements, feel free to open an issue on our GitHub page.

For direct questions, please create a discussion thread on the forum.

## 📩 Get Help
If you need additional help or support, check the frequently asked questions (FAQ) section available on the project’s main page or reach out via the issues tab.

## 📅 Future Updates
Future versions will include:

- Enhanced error handling to identify and inform users of issues in real-time.
- User authentication feature to fetch private repositories for authorized users.
- A graphical user interface (GUI) for easier interaction.

## 🔗 Additional Resources
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## 📂 License
This project is licensed under the MIT License. Please see the LICENSE file for details. 

We hope you enjoy using github-repo-fetcher! Remember, you can always find the latest release and updates at our [Releases Page](https://github.com/Rudra-2-18/github-repo-fetcher/releases). Happy fetching!