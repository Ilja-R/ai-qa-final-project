import os
import json
from datetime import datetime
from contextvars import ContextVar
from shared.utils.logger import service_logger

# Context variable to store the current run directory thread-safely
_current_run_dir: ContextVar[str] = ContextVar("current_run_dir", default=None)

class ArtifactExporter:
    """
    Utility to export pipeline artifacts to a temporary directory for debugging and visibility.
    """
    def __init__(self, base_dir: str = "tmp/artifacts"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    @property
    def current_run_dir(self):
        return _current_run_dir.get()

    def start_run(self):
        """
        Creates a new directory for the current run based on timestamp.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        run_dir = os.path.join(self.base_dir, f"run_{timestamp}")
        os.makedirs(run_dir, exist_ok=True)
        _current_run_dir.set(run_dir)
        service_logger.info(f"Started new artifact run: {run_dir}")
        return run_dir

    def save_artifact(self, name: str, data: any, extension: str = "json"):
        """
        Saves data to the artifact directory.
        """
        run_dir = _current_run_dir.get()
        if not run_dir:
            run_dir = self.start_run()

        filename = f"{name}.{extension}"
        file_path = os.path.join(run_dir, filename)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                if extension == "json":
                    json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    f.write(str(data))
            
            service_logger.info(f"Artifact saved: {file_path}")
            return file_path
        except Exception as e:
            service_logger.error(f"Failed to save artifact {name}: {str(e)}")
            return None

# Singleton instance for easy access
exporter = ArtifactExporter()
