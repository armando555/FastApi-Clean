from typing import List, Optional

from fastapi import Depends
from app.models import Department


class DeparmentRepository:
    model: type

    def __init__(
        self, model: Department
    ) -> None:
        self.model = model

    