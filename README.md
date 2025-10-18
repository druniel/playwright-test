# Playwright Test Automation Project

This project demonstrates automated testing using Playwright with Python. It includes web UI tests, API tests, and examples of different test data approaches.

## Features
- Web UI testing using Playwright
- API testing with FastAPI backend
- Data-driven testing using CSV and JSON
- Page Object Model (POM) implementation
- Multi-browser testing support (Chromium, Firefox, WebKit)
- HTML test reports
- Parallel test execution

## Requirements
- Python 3.13+
- Playwright
- pytest
- FastAPI (for API testing)
- Additional dependencies in `requirements.txt`

## Installation

1. **Create and activate virtual environment:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers:**

   ```bash
   playwright install
   ```

## Project Structure

```
api/           # FastAPI backend for API testing
pages/         # Page Object Model implementations
test_data/     # Test data files (CSV, JSON)
tests/         # Test scripts
reports/       # Test execution reports
pytest.ini     # pytest configuration
requirements.txt  # Project dependencies
```

## Running Tests

- **Run all tests:**

  ```bash
  pytest
  ```

- **Run specific test file:**

  ```bash
  pytest tests/test_login.py
  ```

- **Generate HTML report:**

  ```bash
  pytest --html=reports/report.html
  ```

## API Testing

To run API tests:

1. **Start the FastAPI server:**

   ```bash
   click run.bat
   ```

2. **Run API tests:**

   ```bash
   pytest tests/test_api_*.py
   ```

## Test Examples

- **Login test with POM:** `test_login.py`
- **Data-driven testing:**  
  - Using CSV: `test_datadrivedemo_csv.py`  
  - Using JSON: `test_datadrivedemo_json.py`
- **API testing:** `test_api_get.py`



## Configuration

The `pytest.ini` file configures:

- Multi-browser parallel testing
- HTML report generation
- Test directory location

## Reports

Test reports are generated in HTML format and stored in the `reports` directory.
