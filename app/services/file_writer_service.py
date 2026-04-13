from services.test_generator.file_writer import TestFileWriter


class FileWriterService:
    def write_to_file(self, files: list):
        file_writer = TestFileWriter()
        file_writer.write_files(files)
