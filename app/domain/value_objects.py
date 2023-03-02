from typing import Optional
from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str
    password: str = None
