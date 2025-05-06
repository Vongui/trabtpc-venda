from application.controller.controller_generico import ControleGenerico
from application.model.cliente import Cliente


class ControllerCliente(ControleGenerico):
    def incluir_cliente(self, cliente):
        self.incluir(cliente)

    def excluir_cliente(self, cliente):
        self.delete(cliente)

    def alterar_cliente(self, cliente):
        self.alterar(cliente)

    def pesquisaCodigo(self, entrada):
        cliente = self.procuraRegistro(entrada)
        retorno = Cliente()
        if len(cliente) >= 1:
            retorno = self.converte_cliente(cliente)
        return retorno

    def converte_cliente(self, cliente):
        retorno = Cliente()
        retorno.codcliente = cliente[0][0]
        retorno.nome = cliente[0][1]
        retorno.endereco = cliente[0][2]
        return retorno

    def converte_objeto(self, entrada):
        cliente = Cliente()
        cliente.codcliente = entrada[0]
        cliente.nome = entrada[1]
        cliente.endereco = entrada[2]
        return cliente

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        clientes = []
        for registro in registros:
            cliente = self.converte_objeto(registro)
            clientes.append(cliente)
        return clientes

    def dadosJson(self, dados):
        retorno = {}
        retorno["codcliente"] = dados.codcliente()
        retorno["nome"] = dados.nome()
        retorno["endereco"] = dados.endereco()
        return retorno