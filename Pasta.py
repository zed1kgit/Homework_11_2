from __future__ import annotations
from abc import ABC, abstractmethod


class PastaCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def show_pasta(self) -> str:
        product = self.factory_method()
        type_of_pasta = product.type_of_pasta()
        sauce = product.sauce()
        filling = product.filling()
        toppings = product.toppings()
        return f"""Тип пасты: {type_of_pasta}
Соус: {sauce}
Начинка: {filling}
Добавки: {toppings}"""


class PastaConcreteCreator1(PastaCreator):

    def factory_method(self) -> PastaProduct:
        return PastaProduct1()


class PastaConcreteCreator2(PastaCreator):

    def factory_method(self) -> PastaProduct:
        return PastaProduct2()


class PastaConcreteCreator3(PastaCreator):

    def factory_method(self) -> PastaProduct:
        return PastaProduct3()


class PastaProduct(ABC):

    @abstractmethod
    def type_of_pasta(self) -> str:
        pass

    @abstractmethod
    def sauce(self) -> str:
        pass

    @abstractmethod
    def filling(self) -> str:
        pass

    @abstractmethod
    def toppings(self) -> str:
        pass


class PastaProduct1(PastaProduct):

    def type_of_pasta(self) -> str:
        return "Спагетти"

    def sauce(self) -> str:
        return "Томатный соус"

    def filling(self) -> str:
        return "Без начинки"

    def toppings(self) -> str:
        return "Пармезан, базилик"


class PastaProduct2(PastaProduct):

    def type_of_pasta(self) -> str:
        return "Лазанья"

    def sauce(self) -> str:
        return "Болоньезе"

    def filling(self) -> str:
        return "Сыр моцарелла"

    def toppings(self) -> str:
        return "Базилик, орегано"


class PastaProduct3(PastaProduct):

    def type_of_pasta(self) -> str:
        return "Равиоли"

    def sauce(self) -> str:
        return "Сливочный соус"

    def filling(self) -> str:
        return "Грибы, шпинат"

    def toppings(self) -> str:
        return "Сыр пармезан, петрушка"


def client_code(creator) -> None:
    print(creator.show_pasta())


if __name__ == "__main__":
    client_code(PastaConcreteCreator1())
    print("\n")

    client_code(PastaConcreteCreator2())
    print("\n")

    client_code(PastaConcreteCreator3())
    print("\n")