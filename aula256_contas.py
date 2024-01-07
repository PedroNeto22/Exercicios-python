from abc import ABC, abstractmethod


class Contas(ABC):

    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self):
        pass

    def depositar(self, valor) -> None:
        self.saldo += valor
        self.consulta(f'(Deposito de {valor})')

    def consulta(self, msg: str = '') -> None:
        print(f'Seu saldo é {self.saldo} {msg}')


class ContaCorrente(Contas):

    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: int = 0) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> None:

        valor_apos_saque = self.saldo - valor
        limite_máximo = -self.limite

        if valor_apos_saque < limite_máximo:
            print('Não foi possível realizar o saque')
            self.consulta(f'(Tentativa de saque no valor de {valor})')
            return

        self.saldo -= valor
        self.consulta(f'(Saque no valor de {valor})')
        return


class ContaPoupança(Contas):

    def sacar(self, valor: float) -> None:
        valor_apos_saque = self.saldo - valor

        if valor_apos_saque < 0:
            print('Não foi possível realizar o saque')
            self.consulta(f'(Tentativa de saque no valor de {valor})')
            return

        self.saldo -= valor
        self.consulta(f'(Saque no valor de {valor})')
        return


if __name__ == '__main__':
    cp = ContaPoupança(111, 222, 10000)
    cp.sacar(10)
    cc = ContaCorrente(222, 111)
