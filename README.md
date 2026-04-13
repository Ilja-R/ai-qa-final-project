curl -X POST http://localhost:3000/pipeline/run -H "Content-Type: application/json" -d '{
  "checklist": {
    "content": """User john_doe logged in with password 123456 and email john@gmail.com"""
  },
  "variables": {
    "correct_username": "standard_user",
    "password": "secret_sauce",
    "locked_out_username": "locked_out_user"
  },
  "page_locators": {
    "username_field": "#user-name",
    "password_field": "#password",
    "login_button": "#login-button",
    "error_meassage": ".error-message-container"
  },
  "config": {
    "piiMasking": { "mode": "ai" },
    "aiProvider": "mistral"
  }
}'

Site: https://www.saucedemo.com/
Scope: Login only
Scenario Author: John Doe, (+333)555-5555, tester@test.com

Checklist:
1) Valid login -> Products page is opened
2) Invalid password -> error message is shown
3) Invalid username -> error message is shown
4) Empty fields -> error message is shown
5) Locked user -> locked user error is shown