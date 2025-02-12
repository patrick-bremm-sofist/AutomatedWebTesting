# Automation with Selenium

This project demonstrates how to use Selenium with Python to automate a Google search. The project uses `webdriver-manager` to automatically manage the ChromeDriver installation.

## Requirements

- Python 3.12.4

## Installation

1. Clone the repository

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script to perform a Google search and print the results:

```bash
python src/google_search.py
```

## Dependencies

The project depends on the following Python packages:

* selenium==4.22.0
* webdriver-manager==4.0.1