from services.bug_reporter.reporter import BugReporter
from shared.utils.logger import app_logger

class BugReportService:
    def generate_report(self, checklist: str, scenarios: str, review: str, tests: str, provider: str = "mistral") -> dict:
        app_logger.info(f"Starting bug report generation with provider: {provider}")
        reporter = BugReporter(provider)
        result = reporter.generate_report(checklist, scenarios, review, tests)
        app_logger.info(f"Bug report generation status: {result.get('status', 'SUCCESS')}")
        return result
