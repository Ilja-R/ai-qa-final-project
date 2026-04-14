# AI-Powered QA Automation Pipeline

This project is a comprehensive AI-driven system designed to automate the generation of QA artifacts, including test scenarios, Playwright automation code, and detailed bug reports, starting from simple requirement checklists.

## Features

- **PII Masking**: Automatically detects and masks sensitive information in your requirements using simple regex or AI-driven logic.
- **Scenario Generation**: Converts requirement checklists into structured Gherkin-style test scenarios.
- **Automated Code Generation**: Generates production-ready Playwright (TypeScript) test code based on scenarios, variables, and page locators.
- **AI Code Review**: Analyzes generated code for best practices, potential bugs, and performance improvements.
- **Bug Reporting**: Synthesizes all pipeline outputs into a professional bug report format.

## Project Architecture

The project follows a modular architecture with a clear separation of concerns:

```text
├── app/
│   ├── api/             # FastAPI route definitions (REST API)
│   ├── core/            # Business logic and domain-specific services
│   ├── services/        # High-level orchestration and facades
│   └── main.py          # Application entry point
├── shared/
│   ├── ai/              # AI provider abstractions (Mistral, Gemini)
│   ├── contracts/       # Pydantic models and data schemas
│   └── utils/           # Shared utilities (logging, artifact exporting)
├── ui/                  # React + Vite frontend
├── playwright/          # E2E tests and generated test results
└── prompts/             # System prompts for AI models
```

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- API Keys for AI Providers (Mistral or Gemini)

### Backend Setup

1. Create a `.env` file in the root directory:
   ```env
   MISTRAL_API_KEY=your_mistral_key
   GEMINI_API_KEY=your_gemini_key
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload --port 3000
   ```

### Frontend Setup

1. Navigate to the `ui` directory:
   ```bash
   cd ui
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

### Running Tests

To run the generated Playwright tests:
1. Navigate to the `playwright` directory:
   ```bash
   cd playwright
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run tests:
   ```bash
   npx playwright test
   ```

## Workflow

1. **Input**: Provide a testing checklist, environment variables, and page locators in the UI.
2. **Masking**: The system masks PII to ensure data privacy.
3. **Generation**: AI generates scenarios and Playwright code.
4. **Review**: AI reviews the generated code and provides feedback.
5. **Report**: A final bug report is generated based on the entire pipeline.
6. **Execution**: Generated tests can be executed immediately via Playwright.

## Sample data

### Checklist Input

```
Site: https://www.saucedemo.com/
Scope: Login only
Scenario Author: John Doe, (+333)555-5555, tester@test.com

Checklist:
1) Valid login -> Products page is opened
2) Invalid password -> error message is shown
3) Invalid username -> error message is shown
4) Empty fields -> error message is shown
5) Locked user -> locked user error is shown
```

### Variables
```
correct_username : standard_user
password : secret_sauce
locked_out_username: locked_out_user
```

### Page Locators
```
username_field : #user-name
password_field : #password
login_button : #login-button
error_meassage : .error-message-container
```