from abc import ABC
import aula256_contas


class Pessoa(ABC):

    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade


class Cliente(Pessoa):

    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: aula256_contas.Contas | None = None


if __name__ == '__main__':
    cl = Cliente('Pedro', 15)
    cl.conta = aula256_contas.ContaPoupança(111, 111, 1000)
    cl.conta.consulta()
