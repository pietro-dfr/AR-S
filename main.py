from entities import Car, Registrations as Rt
from datetime import datetime


def main() -> None:
    actual_year: int = datetime.now().year
    max_market_value: float = 1_000_000_000
    min_market_value: float = 0
    min_manufactured_year: int = 1886
    while True:
        print(Rt.menu(), end="")
        try:
            option: int = int(input())
        except ValueError:
            print("Insira apenas números inteiros!")
            continue
        match option:
            case 1:
                print("==================")
                print("REGISTRO DE CARROS")
                print("==================")
                model: str = input("MODELO: ")
                brand: str = input("MARCA: ")
                year: int = ask_year_input()
                market_value: float = ask_market_value_input()

                error: bool = False
                if not min_manufactured_year <= year <= actual_year:
                    print(f"Você só pode registrar carros entre {min_manufactured_year} e {actual_year}!")
                    error = True
                if not min_market_value <= market_value <= max_market_value:
                    print(f"Você só pode registrar carros entre R${min_market_value:,.2f} e R${max_market_value:,.2f}!")
                    error = True
                if error:
                    continue

                # adiciona o carro registrado a lista
                Rt.add_car(Car(model, brand, year, market_value))

            case 2:
                if Rt.is_car_list_empty():
                    print("A lista de carros registrados está vazia!")
                    continue
                Rt.get_registrations()

            case 3:
                if Rt.is_car_list_empty():
                    print("A lista de carros registrados está vazia!")
                    continue
                Rt.get_registrations()
                index: int = ask_int_input(Rt.get_car_list())
                print(f"Removendo carro: {Rt.get_car_list()[index].model}")
                Rt.remove_car(index)

            case 4:
                if Rt.is_car_list_empty():
                    print("A lista de carros registrados está vazia!")
                    continue
                print(Rt.search_menu(), end="")
                choice: str = input().strip()
                match choice:
                    case "1":
                        model: str = input("Digite o modelo para pesquisar!").strip()
                        Rt.search_by_model(model)
                    case "2":
                        brand: str = input("Digite a marca para pesquisar!").strip()
                        Rt.search_by_brand(brand)
                    case "3":
                        year: int = ask_year_input()
                        Rt.search_by_year(year)
                    case "4":
                        print("Saindo da pesquisa.")
                        break

            case 5:
                print("Tchau.")
                break

            case _:
                print(f"Opção inválida!")


# end-main

def ask_year_input() -> int:
    year: int = 0
    while True:
        try:
            year = int(input("ANO: "))
        except ValueError:
            print("Insira apenas números inteiros!")
            continue
        # end-try
        break
    # end-while
    return year


# enf-def

def ask_market_value_input() -> float:
    market_value: float = 0.0
    while True:
        try:
            market_value = int(input("VALOR: R$"))
        except ValueError:
            print("Insira apenas números reais!")
            continue
        # end-try
        break
    # end-while
    return market_value


# end-def
def ask_int_input(car_list: list[Car]):
    index = None
    while True:
        try:
            index = int(input("Index para remover: "))
        except ValueError:
            print("Só números inteiros!")
            continue
        if not 0 <= index <= len(car_list) - 1:
            print("Index inválido!")
            continue
    return index


if __name__ == "__main__":
    main()
