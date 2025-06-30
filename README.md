# QA Automation Assignment – Saleshandy

Candidate: Vaibhav Gahlot  
App URL: https://pyxis.lifeisgoodforlearner.com

# Tech Stack
- Python, Selenium, PyTest
- POM Structure, Soft Assertions
- JSON Test Data, HTML Report

# Covered Tasks

# Task 1 – Login Page
- UI element validations (logo, inputs, buttons, carousel)
- Login flow (valid, invalid, blank credentials)
- Resolution check @ 1366x768

# Task 2 – Domain & Email Flow
- Domain search & add to cart  (JSON)
- Email auto-generation (3/domain)
- Pricing checks ($14/domain, $4/email)
- Cart summary validations

# BASH
- python -m pytest Task1_Login_Page/tests/test_login.py --html=Task1_Login_Page/reports/task1_login_report.html --self-contained-html
- python -m pytest Task2_DomainSearch_EmailGeneration\tests\test_domain_flow.py --html=report.html --self-contained-html


