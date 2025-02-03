from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path  # Directory for storing data ingestion artifacts
    source_URL: str  # URL to fetch the data from
    local_data_file: Path  # Path to store the downloaded data locally
    unzip_dir: Path  # Directory to unzip the data