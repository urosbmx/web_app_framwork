# Web App Framework

## 📌 Overview

This repository contains an automated testing framework implemented in **Python**, leveraging **Pytest** and **Playwright** for end-to-end UI and API testing.

The project demonstrates:
* Modular, maintainable test structure
* Page Object Model (POM) for UI tests
* Strategies for dynamic web content (SPA, lazy-loading)
* Reusable utility functions for scrolling, clicking, and taking screenshots
* Pytest fixtures for robust setup and teardown processes

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/urosbmx/web_app_framwork.git
cd web_app_framwork
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

---

## 🤛 Running Tests

### 1. UI Tests (Playwright)

Run all UI tests:

```bash
pytest ui_tests/
```

### 2. API Tests

Run all API tests:

```bash
pytest api_tests/
```

### 3. Running Tests with Markers

You can run specific types of tests using pytest markers. For example:

- Run only UI tests:
  ```bash
  pytest -m "smoke_test_twitch"
  ```

- Run only API tests:
  ```bash
  pytest -m "smoke_test_api"
  ```

---

## 📂 Project Structure

```
web_app_framwork/
│
├── api_tests/    # API automation tests
├── ui_tests/     # UI automation tests
├── docs/         # Documentation and test artifacts
│
├── .env          # Environment variables
├── pytest.ini    # Pytest configuration
├── requirements.txt # Python dependencies
└── README.md     # This documentation file
```

---

## ⚡ Features

* **Page Object Model (POM)** for structured UI tests
* **Dynamic element handling** (scrolling, lazy-loading)
* **Safe click helpers** to mitigate flaky tests
* **Automatic screenshots on failure** for easy debugging
* **Comprehensive API testing** and validation utilities

---

## 🎬 Demo GIF

![Test Running GIF](docs/test_run.gif)

> A GIF showing UI or API tests running locally.

---
