"""
This module provides the 'config' object, which allows the program to sync the
user's configuration with a JSON file and get/set options into it. Use the
'config' object to load and save configuration settings to a JSON file and
access/modify these options.

Example:
```
# Load the user config.
config.load()

# Access a configuration option.
value = config['key']

# Set a configuration option.
config['key'] = 'new_value'

# Save the updated configuration.
config.save()
```
"""

import json
import os
from pathlib import Path
from typing import Any, Dict

from platformdirs import PlatformDirs


default_options: Dict[str, Any] = {
    'intro_completed': False,
    'completed_lessons': []
}


class Config:
    """
    Config class allows the program to sync the user's config with a JSON file
    and get/set options into it.

    Retrieve or set an option using a dictionary style:
    ```
    config['key'] = 'value'
    ```

    Methods:
        load(self):
            Load the user config from the JSON config file.
        save(self):
            Write the user config into the JSON config file.
    """

    FILE_NAME = 'config.json'

    def __init__(self, path: str):
        """
        Initialize the Config instance.

        Args:
            dirs (PlatformDirs):
                An instance of PlatformDirs to get the user data directory.
        """

        self.path = Path(path)
        self.options = None

        if not self.path.exists():
            self.seed_config()

    def __getitem__(self, key: str) -> Any:
        """
        Allows accessing configuration options like a dictionary.

        Args:
            key (str): The key for the configuration option to retrieve.

        Returns:
            Any: The value associated with the given key in the configuration.

        Raises:
            ValueError: If user config is not loaded yet.
        """

        if self.options is None:
            raise ValueError(
                'user config not loaded, run config.load() first.')

        return self.options[key]

    def __setitem__(self, key: str, value: Any):
        """
        Allows setting configuration options like a dictionary.

        Args:
            key (str): The key for the configuration option to set.
            value (Any): The value to be associated with the given key.

        Raises:
            ValueError: If user config is not loaded yet.
        """

        if self.options is None:
            raise ValueError(
                'user config not loaded, run config.load() first.')

        self.options[key] = value

    def seed_config(self):
        """Create the initial JSON config in the user's data directory."""
        self.path.mkdir(parents=True)
        with open(self.path / self.FILE_NAME, 'w') as config_file:
            json.dump(default_options, config_file, indent=2)

    def load(self):
        """Load the user config from the JSON config file."""
        with open(self.path / self.FILE_NAME) as config_file:
            self.options = json.load(config_file)

    def save(self):
        """Write the user config into the JSON config file."""
        if self.options is None:
            raise ValueError(
                'user config not loaded, run config.load() first.')

        with open(self.path / self.FILE_NAME, 'w') as config_file:
            json.dump(self.options, config_file, indent=2)


# Use 'AP_CONFIG_PATH' for testing purposes, else use default config directory.
dirs = PlatformDirs('aprendepython')
config = Config(os.environ.get('AP_CONFIG_PATH', dirs.user_data_dir))
