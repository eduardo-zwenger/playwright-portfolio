# Playwright QA Automation Portfolio 🚀

This repository contains an automated test suite developed with **Python** and **Playwright**, configured within a professional Framework architecture using **Pytest**.

The project also features a **CI/CD Pipeline via GitHub Actions**, ensuring that all tests are automatically executed and verified in the cloud upon every code push.

---

## 2. Project Architecture & Features

* **Framework:** Pytest (for test collection and assertions).
* **Automation Engine:** Playwright (Synchronous API).
* **CI/CD Integration:** GitHub Actions (`ubuntu-latest` environment).
* **Auto-waiting Validation:** Utilizes Playwright's built-in actionability checks to eliminate flaky test issues.

### 🧪 Automated Test Cases Included:
1.  **Sanity Page Load Check:** Navigates to a target web interface and validates the proper title rendering to ensure core accessibility.
2.  **Form Authentication Test:** Automates user interaction by locating inputs (`#username`, `#password`), securely typing credentials (`.fill`), executing actions (`.click`), and asserting contextual success banners.

---

## 🚀 How to Run the Project Locally

### 1. Prerequisites
Ensure you have Python 3.11+ installed on your system.

### 2. Installation
Clone this repository, navigate to the folder, and install the dependencies:

```bash
# Install Pytest and Playwright
pip install pytest-playwright

# Install required browser binaries (Chromium, Firefox, WebKit)
python -m playwright install