"""Environment-backed service settings."""
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    max_upload_mb: int = int(os.getenv("MAX_UPLOAD_MB", "25"))
    max_files_per_batch: int = int(os.getenv("MAX_FILES_PER_BATCH", "50"))

    def __post_init__(self):
        if self.max_upload_mb < 1 or self.max_files_per_batch < 1:
            raise ValueError("Upload and file-count limits must be positive")


settings = Settings()
