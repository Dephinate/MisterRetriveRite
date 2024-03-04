from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class VectorizationConfig:
    root_dir: Path
    encoder_name: str
    model_ckpt: Path
    data_path: Path
    k:int
    num_of_cells: int
    nprobe: int

@dataclass(frozen=True)
class ModelConfig:
    model_name: str
    temperature: int
    max_tokens: int
    chunk_size: int
    chunk_overlap: int


