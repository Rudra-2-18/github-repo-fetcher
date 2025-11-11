import requests
import sqlite3
import logging
import argparse
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler

# SETTING UP CLI ARGUMENT
parser = argparse.ArgumentParser(prog='repo-fetcher', description='Fetches all repositories from a user')
parser.add_argument("--user", type=str, default='bookie212', help="user-name")

# SETTING UP LOGGING
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
  'repo-fetcher.log',
  maxBytes=10000,
  backupCount=50
)

file_formatter = logging.Formatter(
  '%(asctime)s - %(levelname)s - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# CREATES THE DATABASE
def create_db():
  with sqlite3.connect('repos.db') as conn:
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS repo(id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, status_code INTEGER, user TEXT, repo_name TEXT, creation_date TEXT, stars INTEGER, url TEXT)")

    conn.commit()

# FETCHES THE REPOSITORY
def repo_fetcher(user):

  page = 1

  while True:
    try:
      headers = {'User-Agent': 'repo-fetcher-script'}
      api_url = f"https://api.github.com/users/{user}/repos?type=owner&per_page=100&page={page}"
      response = requests.get(api_url, headers=headers)

      # Handle rate limiting (403 Forbidden is common)
      if response.status_code == 403 and "API rate limit exceeded" in response.text:
        
        # Check if the body text confirms rate limit exceeded before waiting
        if "X-RateLimit-Reset" in response.headers:
          reset_time_str = response.headers['X-RateLimit-Reset']

          try:
            reset_timestamp = int(reset_time_str)
            current_timestamp = int(time.time())
            time_to_wait = reset_timestamp - current_timestamp

            if time_to_wait > 0:
              logger.info(f"Rate limit will reset in {time_to_wait}")
              time.sleep(time_to_wait + 1)
              logger.info("Resuming API calls.")
            else:
              logger.info("Rate limit has already reset or is not applicable.")
              time.sleep(1)

          except ValueError:
            logger.error(f"Could not parse X-RateLimit-Reset header: {reset_time_str}")
        else:
           logger.info("X-RateLimit-Reset header not found in the response.")
           time.sleep(60)
        continue

      data = response.json()
      
      # Check for end of pagination (empty list means no more repos)
      if not data:
        logger.info(f"Finished fetching repositories for user: {user}.")
        break

      for repo in data:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        yield {
          'timestamp': current_time,
          'status_code': response.status_code,
          'user': user,
          'repo_name': repo.get('name'),
          'creation_date': repo.get('created_at'),
          'stars': repo.get('stargazers_count'),
          'url': repo.get('html_url')
        }

      page += 1
      time.sleep(1)

    except requests.exceptions.RequestException as e:
      error_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      yield {
        'timestamp': error_time,
        'status_code': 0,
        'user': user,
        'repo_name': None,
        'creation_date': None,
        'stars': None,
        'url': f"Request Error: {str(e)}"
      }
      logger.error(f"Request failed: {str(e)}")
      break
    
# SAVES THE VALUES GOTTING FROM THE REPO_FETCHER
def log_data(log_record):
  with sqlite3.connect('repos.db') as conn:
    cursor = conn.cursor()

    cursor.execute ('''
    INSERT INTO repo (timestamp, status_code, user, repo_name, creation_date, stars, url)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (log_record['timestamp'],
          log_record['status_code'],
          log_record['user'],
          log_record['repo_name'],
          log_record['creation_date'],
          log_record['stars'],
          log_record['url']))
    

# RUNS ALL OTHER FUNCTIONS
def main(user):
  logger.info(f"Fetching repositories for user: {user}")

  create_db()

  for log_record in repo_fetcher(user):
    log_data(log_record)



if __name__ == "__main__":
  try:
    args = parser.parse_args()
    main(args.user)
  except KeyboardInterrupt:
    logger.info("\nRepository fetch stopped by user.")
  except Exception:
    logger.exception(f"\nAn unexpected fatal error occurred")
  finally:
    logger.info("Process finished. Cleaning up logging handlers.")
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)
    file_handler.close()
    console_handler.close()