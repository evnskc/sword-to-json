import importlib.metadata

import sword_to_json

_metadata = importlib.metadata.metadata(sword_to_json.__package__)

name = _metadata["Name"]
summary = _metadata["Summary"]
version = _metadata["Version"]
