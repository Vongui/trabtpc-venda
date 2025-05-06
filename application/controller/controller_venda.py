from application.controller.controller_generico import ControleGenerico
from application.model.venda import Venda


class ControllerVenda(ControleGenerico):
    def incluir_venda(self, venda):
        self.incluir(venda)

    def excluir_venda(self, venda):
        self.delete(venda)

    def alterar_venda(self, venda):
        self.alterar(venda)

    def pesquisaCodigo(self, entrada):
        venda = self.procuraRegistro(entrada)
        retorno = Venda()
        if len(venda) >= 1:
            retorno = self.converte_venda(venda)
            print(retorno)
        return retorno

    def converte_venda(self, venda):
        retorno = Venda()
        retorno.codvenda = venda[0][0]
        retorno.data = venda[0][1]
        retorno.valor_total = venda[0][2]
        retorno.codcliente = venda[0][3]
        return retorno

    def converte_objeto(self, entrada):
        #print(entrada)
        venda = Venda()
        venda.codvenda = entrada[0]
        venda.data = entrada[1]
        venda.valor_total = entrada[2]
        venda.codcliente = entrada[3]
        return venda

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        vendas = []
        for registro in registros:
            venda = self.converte_objeto(registro)
            vendas.append(venda)
        return vendas

    def dadosJson(self, dados):
        retorno = {}
        retorno["codvenda"] = dados.codvenda
        retorno["data"] = dados.data
        retorno["valor_total"] = dados.valor_total
        retorno["codcliente"] = dados.codcliente
        return retorno

    def buscarUltimoRegistro(self, objeto, campo):
        self.ob.abrirConexao()
        sql = f"SELECT * FROM {objeto.tabelaBanco} ORDER BY {campo} DESC LIMIT 1"
        return self.ob.selectQuery(sql)[0][0]
