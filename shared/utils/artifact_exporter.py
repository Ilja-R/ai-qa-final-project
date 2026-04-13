import os
import json
from datetime import datetime
from shared.utils.logger import service_logger

class ArtifactExporter:
    """
    Utility to export pipeline artifacts to a temporary directory for debugging and visibility.
    """
    def __init__(self, base_dir: str = "tmp/artifacts"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save_artifact(self, name: str, data: any, extension: str = "json"):
        """
        Saves data to the artifact directory.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.{extension}"
        file_path = os.path.join(self.base_dir, filename)

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
