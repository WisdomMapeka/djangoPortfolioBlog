import json
from pathlib import Path
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
import os


config_file_path = os.path.join(BASE_DIR, "portfoliosite.json")
with open(config_file_path) as config_file:
    config = json.load(config_file)
print(config)