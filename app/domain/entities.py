from typing import Optional
from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    password: str
