import os


class TestFileWriter:

    def __init__(self, base_path: str = "playwright"):
        self.base_path = base_path

    def write_files(self, files: list):
        written_files = []

        for file in files:
            full_path = self._build_path(file["path"])
            self._ensure_directory(full_path)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(file["content"])

            written_files.append(full_path)

        return written_files

    def _build_path(self, relative_path: str):
        return os.path.join(self.base_path, relative_path)

    def _ensure_directory(self, full_path: str):
        directory = os.path.dirname(full_path)
        os.makedirs(directory, exist_ok=True)