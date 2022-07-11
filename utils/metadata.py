import importlib.metadata

from sword_to_json import __package__

_metadata = importlib.metadata.metadata(__package__)

name = _metadata["Name"]
summary = _metadata["Summary"]
version = _metadata["Version"]
