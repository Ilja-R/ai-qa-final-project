from services.bug_reporter.reporter import BugReporter

class BugReportService:
    def generate_report(self, checklist: str, scenarios: str, review: str, tests: str, provider: str = "mistral") -> dict:
        reporter = BugReporter(provider)
        return reporter.generate_report(checklist, scenarios, review, tests)
