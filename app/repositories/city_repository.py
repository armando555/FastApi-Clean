from typing import List, Optional

from fastapi import Depends
from app.models import City


class CityRepository:
    model: type

    def __init__(
        self, model: City
    ) -> None:
        self.model = model

    