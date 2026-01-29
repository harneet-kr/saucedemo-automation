# saucedemo-automation
# Saucedemo Automation Framework

## Project Description
Automated testing framework for Saucedemo e-commerce website using Python, Selenium, and Pytest with Page Object Model design pattern.

## Technologies Used
- **Python 3.13**
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **WebDriver Manager** - Automatic driver management
- **Page Object Model** - Design pattern for maintainability

## Project Structure
```
saucedemo_automation/
├── pages/              # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/              # Test files
│   ├── conftest.py
│   ├── test_basic_login.py
│   ├── test_basic_scenarios.py
│   └── test_with_pom.py
├── reports/            # HTML test reports
├── screenshots/        # Screenshots of failures
└── README.md
```

## Test Coverage
Login functionality (valid/invalid/empty credentials)
Shopping cart (add/remove products)
Checkout flow (end-to-end purchase)
Data-driven tests with multiple datasets

## Setup Instructions

### Prerequisites
- Python 3.x installed
- Chrome browser installed

### Installation
1. Clone the repository
```bash
git clone <your-repo-url>
cd saucedemo_automation
```

2. Install dependencies
```bash
pip3 install selenium pytest pytest-html webdriver-manager
```

## How to Run Tests

### Run all tests
```bash
pytest tests/ -v
```

### Run specific test file
```bash
pytest tests/test_with_pom.py -v
```

### Run specific test class
```bash
pytest tests/test_with_pom.py::TestLoginWithPOM -v
```

### Generate HTML report
```bash
pytest tests/ --html=reports/report.html
```

### Run tests with print statements visible
```bash
pytest tests/ -v -s
```

## Test Results
- Total Tests: 15
- Passed: 15
- Failed: 0
- Success Rate: 100%

## Author
**Your Name**
- Manual Testing Experience: 6.6 years
- Transitioning to Automation Testing
- GitHub: [your-github-username]
- LinkedIn: [your-linkedin]

## Future Enhancements
- [ ] Add API testing
- [ ] Integrate with CI/CD (GitHub Actions)
- [ ] Add screenshot on failure
- [ ] Cross-browser testing (Firefox, Safari)
- [ ] Performance testing
