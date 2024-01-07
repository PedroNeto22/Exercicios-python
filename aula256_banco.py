import aula256_contas
import aula256_clientes


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[aula256_clientes.Cliente] | None = None,
            contas: list[aula256_contas.Contas] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _verifica_agencia(self, conta: aula256_contas.Contas) -> bool:

        if conta.agencia in self.agencias:
            print('_verifica_agencia', True)
            return True
        print('_verifica_agencia', False)
        return False

    def _verifica_cliente(self, cliente: aula256_clientes.Cliente) -> bool:

        if cliente in self.clientes:
            print('_verifica_cliente', True)
            return True
        print('_verifica_cliente', False)
        return False

    def _verifica_conta(self, conta: aula256_contas.Contas) -> bool:

        if conta in self.contas:
            print('_verifica_conta', True)
            return True
        print('_verifica_conta', False)
        return False

    def _verifica_paridade_conta(self,
                                 cliente: aula256_clientes.Cliente,
                                 conta: aula256_contas.Contas
                                 ) -> bool:

        if conta == cliente.conta:
            print('_verifica_paridade_conta', True)
            return True
        print('_verifica_paridade_conta', False)
        return False

    def autenticar(self, cliente: aula256_clientes.Cliente, conta: aula256_contas.Contas) -> bool:
        verifica_agencia = self._verifica_agencia(conta)
        verifica_cliente = self._verifica_cliente(cliente)
        verifica_conta = self._verifica_conta(conta)
        verifica_paridade_conta = self._verifica_paridade_conta(cliente, conta)
        return verifica_agencia and verifica_cliente and verifica_conta and verifica_paridade_conta


if __name__ == "__main__":
    c1 = aula256_clientes.Cliente('Pedro', 19)
    cc1 = aula256_contas.ContaPoupança(111, 222, 1000)
    c1.conta = cc1
    banco = Banco()
    banco.clientes.append(c1)
    banco.contas.append(cc1)
    banco.agencias.append(111)

    if banco.autenticar(c1, cc1):
        c1.conta.consulta()
        c1.conta.sacar(100)
        c1.conta.consulta()
