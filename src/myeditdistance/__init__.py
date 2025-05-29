from importlib.metadata import version

from . import pl, pp, tl
from .tl.edit_distance import edit_distance

__all__ = ["pl", "pp", "tl", "edit_distance"]

__version__ = version("myeditdistance")
