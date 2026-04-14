from app.core.test_generator.file_writer import TestFileWriter
from shared.utils.logger import app_logger

class FileWriterService:
    def write_to_file(self, files: list):
        app_logger.info(f"Writing {len(files)} file(s) to disk")
        file_writer = TestFileWriter()
        file_writer.write_files(files)
        app_logger.info("File writing completed")
