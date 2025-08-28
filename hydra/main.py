import hydra
from omegaconf import DictConfig
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

@hydra.main(config_path="./config", config_name="config", version_base=None)
def main(cfg: DictConfig):
    print("Configuration:")
    print("--------------")
    print("Dataset: ", cfg.dataset)
    print("Model: ", cfg.model)
    print("Training: ", cfg.training)


if __name__ == "__main__":
    main()