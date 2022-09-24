from typing import List, Optional

from fastapi import Depends
from app.models import Client


class ClientRepository:
    model: type

    def __init__(
        self, model: Client
    ) -> None:
        self.model = model

    