VERSION = "1.0.0"

# Local Folders
from .dataprocess.rel2text import nyt_rel2text as rel2text
from .predict import UniRel

__all__ = [
    "UniRel",
    "rel2text",
]
