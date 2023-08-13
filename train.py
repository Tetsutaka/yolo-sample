import configparser
import logging
from ultralytics import YOLO


class ConfigLoader:
    def __init__(self, config_path: str) -> None:
        """
        Initialize and load the config from the specified path.
        
        :param config_path: Path to the .ini configuration file.
        """
        self.path = config_path
        self.config = configparser.ConfigParser()
        # Attempt to read the config file
        if not self.config.read(self.path, encoding="utf-8"):
            raise FileNotFoundError(f"'{self.path}' file not found or failed to load!")

    def get_config_sections(self) -> list:
        """
        Retrieve all section names from the configuration.
        
        :return: List of section names.
        """
        return self.config.sections()


class TrainYOLO:
    def __init__(self, config_path) -> None:
        self.config = ConfigLoader(config_path)
        self.set_logger()

    def set_logger(self):
        # Set logger
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        file_handler = logging.FileHandler("sample.log")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        
    def train(self):
        # load config sections
        sections = self.config.get_config_sections()
        settings = self.config.config
        for section in sections:
            yaml = settings[section]["model_yaml"]
            initial_weight = settings[section]["initial_weight"]
            data_yaml = settings[section]["data_yaml"]
            epoch_num = int(settings[section]["epochs"])
            image_size = int(settings[section]["image_size"])
            try:
                self.logger.info("Loading weight to start training")
                model = YOLO(yaml).load(initial_weight)
                self.logger.info("start training the model")
                model.train(data=data_yaml, epochs=epoch_num, imgsz=image_size)
            except BaseException as e:
                self.logger.error(e)


def main():
    yolo = TrainYOLO(config_path="config.ini")
    yolo.train()


if __name__ == "__main__":
    main()
