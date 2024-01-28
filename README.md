# Instagram Follower Bot

This is a Python script that automates the process of logging into Instagram, searching for a similar account, and scraping the list of followers.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Selenium library
- Chrome WebDriver

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/instagram-follower-bot.git
    ```

2. Install the required dependencies:

    ```bash
    pip install selenium
    ```

3. Download the Chrome WebDriver and add it to your system's PATH.

## Usage

1. Set the following environment variables:

    - `EMAIL`: Your Instagram email address
    - `PASS`: Your Instagram password
    - `SIMILAR_ACCOUNT`: The username of the similar account you want to scrape followers from

2. Run the script:

    ```bash
    python main.py
    ```

3. The script will open a Chrome browser, log in to Instagram, search for the similar account, and scrape the list of followers. The follower list will be saved in a file named `Followers.txt`.