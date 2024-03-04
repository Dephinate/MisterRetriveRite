from misterRetriveRite.constants import  *
from misterRetriveRite.entity import VectorizationConfig, ModelConfig, SpltterConfig
from misterRetriveRite.utils.common import read_yaml, create_directory, create_file

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 param_filepath=PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(param_filepath)

        create_directory([self.config.artifacts_root])

    def get_vectorization_config(self)->VectorizationConfig:
        config = self.config.vectorization
        params = self.params.Vector_dbArguments
        create_directory([config.root_dir])

        vectorizationConfig = VectorizationConfig(
            root_dir = config.root_dir,
            encoder_name = config.encoder_name,
            model_ckpt = config.model_ckpt,
            data_path = config.data_path,
            k = params.k,
            num_of_cell = params.num_of_cells,
            nprobe = params.nprobe  
        )
        return vectorizationConfig
    
    def get_model_config(self)->ModelConfig:
        config = self.config.model
        params_model = self.params.ModelArguments
        parmas_splitter = self.params.SplitterArguments

        modelConfig = ModelConfig(
            model_name = config.model_name,
            temperature = params_model.temperature,
            max_tokens = params_model.max_tokens,
            chunk_size = parmas_splitter.chunk_size,
            chunk_overlap = parmas_splitter.chunk_overlap
        )
        return modelConfig


