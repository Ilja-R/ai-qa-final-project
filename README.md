curl -X POST http://localhost:3000/pipeline/run -H "Content-Type: application/json" -d '{
  "jira": {
    "content": "User john_doe logged in with password 123456 and email john@gmail.com"
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

