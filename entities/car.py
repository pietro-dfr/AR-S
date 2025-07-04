from dataclasses import dataclass


@dataclass
class Car:
    __model: str
    __brand: str
    __year_of_manufacture: int
    __market_value: float

    # getters:
    @property
    def model(self) -> str:
        return self.__model

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def year_of_manufacture(self) -> int:
        return self.__year_of_manufacture

    @property
    def market_value(self) -> float:
        return self.__market_value

    @model.setter
    def model(self, new_model: str):
        self.__model = new_model

    @brand.setter
    def brand(self, new_brand: str):
        self.__brand = new_brand

    @year_of_manufacture.setter
    def year_of_manufacture(self, new_year: int):
        self.__year_of_manufacture = new_year

    @market_value.setter
    def market_value(self, new_value: float):
        self.__market_value = new_value
