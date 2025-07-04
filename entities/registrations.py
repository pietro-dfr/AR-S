from entities import Car


class Registrations:
    __car_list: list[Car] = []
    __menu: str = (
            "====================\n" +
            "   MENU PRINCIPAL   \n" +
            "====================\n" +
            "| [1]. Registrar    |\n" +
            "| [2]. Listar       |\n" +
            "| [3]. Vender       |\n" +
            "| [4]. Pesquisar    |\n" +
            "| [5]. Sair         |\n" +
            "====================\n" +
            ">> "
    )
    __search_menu: str = (
            "==========================\n" +
            "      MENU DE PESQUISA     \n" +
            "==========================\n" +
            "| [1]. Pesquisa por nome  |\n" +
            "| [2]. Pesquisa por marca |\n" +
            "| [3]. Pesquisa por ano   |\n" +
            "| [4]. Sair               |\n" +
            "===========================\n" +
            ">> "
    )

    @classmethod
    def add_car(cls, some_car: Car) -> None:
        cls.__car_list.append(some_car)

    @classmethod
    def remove_car(cls, index: int) -> None:
        cls.__car_list.pop(index)

    @classmethod
    def get_registrations(cls):
        print("=============================")
        print("INDEX   MODEL   BRAND   YEAR   VALUE")
        for index, item in enumerate(cls.__car_list, start=1):
            print(f"{index}     {item.model}    {item.brand}    {item.year_of_manufacture}      {item.market_value}")
        # end-for
        print("=============================")

    @classmethod
    def search_by_model(cls, model: str):
        print("=============================")
        quantity: int = 0
        for index, item in enumerate(cls.__car_list, start=1):
            if model == item.model:
                quantity += 1
                print("INDEX   MODEL   BRAND   YEAR   VALUE")
                print(
                    f"{index}     {item.model}    {item.brand}    {item.year_of_manufacture}      {item.market_value}")
        if quantity == 0:
            print("Não há carros desta especificação!")
        print("=============================")

    @classmethod
    def search_by_brand(cls, brand: str):
        print("=============================")
        quantity: int = 0
        for index, item in enumerate(cls.__car_list, start=1):
            if brand == item.brand:
                quantity += 1
                print("INDEX   MODEL   BRAND   YEAR   VALUE")
                print(
                    f"{index}     {item.model}    {item.brand}    {item.year_of_manufacture}      {item.market_value}")
        if quantity == 0:
            print("Não há carros desta especificação!")
        print("=============================")

    @classmethod
    def search_by_year(cls, year: int):
        print("=============================")
        quantity: int = 0
        for index, item in enumerate(cls.__car_list, start=1):
            if year == item.year_of_manufacture:
                quantity += 1
                print("INDEX   MODEL   BRAND   YEAR   VALUE")
                print(
                    f"{index}     {item.model}    {item.brand}    {item.year_of_manufacture}      {item.market_value}")
        if quantity == 0:
            print("Não há carros desta especificação!")
        print("=============================")


    @classmethod
    def search_menu(cls):
        return cls.__search_menu

    @classmethod
    def is_car_list_empty(cls) -> bool:
        return len(cls.__car_list) == 0

    @classmethod
    def get_car_list(cls):
        return cls.__car_list

    @classmethod
    def menu(cls):
        return cls.__menu
