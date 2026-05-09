import yaml
import json
import logging

logger = logging.getLogger(__name__)

class DeltaCore:
    def __init__(self, config_path="config/delta_config.yaml",
                       pid_path="config/pid_config.json"):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        with open(pid_path) as f:
            self.pid_config = json.load(f)

        logger.info("DeltaCore initialized")

    def get(self, *keys):
        result = self.config
        for key in keys:
            result = result[key]
        return result