from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass


class Tiler(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = TilerProduct()

    @property
    def product(self) -> TilerProduct():
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("подготовка пола")

    def produce_part_b(self) -> None:
        self._product.add("укладка плитки")


class TilerProduct:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Плиточник: {", ".join(self.parts)}", end="")


class Finisher(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = FinisherProduct()

    @property
    def product(self) -> FinisherProduct():
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("нанести шпаклевку")

    def produce_part_b(self) -> None:
        self._product.add("оштукатурить стены")


class FinisherProduct:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Отделочник: {", ".join(self.parts)}", end="")


class Painter(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = PainterProduct()

    @property
    def product(self) -> PainterProduct():
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("загрунтовать стену")

    def produce_part_b(self) -> None:
        self._product.add("покрасить стену")


class PainterProduct:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Маляр: {", ".join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None
        self.reset()
        self.make_floors()
        self.align_walls()
        self.paint_walls()
        self.turnkey_works()

    def reset(self) -> None:
        self._product = DirectorProduct()

    @property
    def builder(self) -> Builder:
        return self._builder

    @property
    def product(self) -> DirectorProduct():
        product = self._product
        self.reset()
        return product

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()

    def make_floors(self) -> None:
        self._product.add("сделать полы")

    def align_walls(self) -> None:
        self._product.add("выровнять стены")

    def paint_walls(self) -> None:
        self._product.add("покрасить стены")

    def turnkey_works(self) -> None:
        self._product.add("работы под ключ")


class DirectorProduct:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Прораб: {", ".join(self.parts)}", end="")


if __name__ == "__main__":
    foreman = Director()
    tiler = Tiler()
    finisher = Finisher()
    painter = Painter()

    foreman.builder = tiler
    foreman.build_product()
    tiler.product.list_parts()

    print("\n")

    foreman.builder = finisher
    foreman.build_product()
    finisher.product.list_parts()

    print("\n")

    foreman.builder = painter
    foreman.build_product()
    painter.product.list_parts()

    print("\n")

    foreman.product.list_parts()
