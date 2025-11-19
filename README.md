# Twitch Automation Testing Framework

## 📌 Overview

This repository contains two automated test frameworks implemented in **Python** using **Pytest**:

1. **Playwright-based UI automation** for Twitch mobile website.
2. **API automation framework** for testing Twitch endpoints.

The project demonstrates:

* Robust test structure
* Page Object Model (POM) for UI tests
* Handling dynamic content (lazy-loading, SPA)
* Reusable helper functions for scrolling, clicking, and screenshots
* Pytest fixtures for setup and teardown

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/twitch-automation-framework.git
cd twitch-automation-framework
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
pytest tests/tests_twitch.py
```


### 2. API Tests

Run all API tests:

```bash
pytest tests/api
```

---

## 📂 Project Structure

```
web_app_automation_framework/
│
├─ pages/                  # Page Objects for Playwright
│   ├─ home_page.py
│   └─ base_page.py
│
├─ helpers/                # Helper utilities
│   └─ utils.py
│
├─ tests/                  # Test cases
│   ├─ tests_twitch.py     # UI tests
│   └─ api/                # API tests
│
├─ requirements.txt        # Python dependencies
├─ pytest.ini              # Pytest configuration
└─ README.md               # Project documentation
```

---

## ⚡ Features

* **Page Object Model (POM)** for maintainable UI tests
* **Dynamic element handling** (scroll, lazy-load)
* **Safe click helpers** to avoid timeout issues
* **Screenshot on failure** for debugging
* **API testing** with request validation

---

## 🎬 Demo GIF

![Test Running GIF](docs/test_run.gif)

> A GIF showing UI tests running locally.
