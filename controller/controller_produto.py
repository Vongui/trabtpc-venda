from controller.controller_generico import ControleGenerico
from model.produto import Produto


class ControllerProduto(ControleGenerico):
    def incluir_produto(self, produto):
        self.incluir(produto)

    def excluir_produto(self, produto):
        self.delete(produto)

    def alterar_produto(self, produto):
        self.alterar(produto)

    def pesquisaCodigo(self, entrada):
        produto = self.procuraRegistro(entrada)
        retorno = Produto()
        if len(produto) >= 1:
            retorno = self.converte_produto(produto)
        return retorno

    def converte_produto(self, produto):
        retorno = Produto()
        retorno.codproduto = produto[0][0]
        retorno.descricao = produto[0][1]
        retorno.preco = produto[0][2]
        return retorno

    def converte_objeto(self, entrada):
        produto = Produto()
        produto.codproduto = entrada[0]
        produto.descricao = entrada[1]
        produto.preco = entrada[2]
        return produto

    def listarTodosRegistros(self, objeto):
        registros = self.listarTodos(objeto)
        produtos = []
        for registro in registros:
            produto = self.converte_objeto(registro)
            produtos.append(produto)
        return produtos

    def dadosJson(self, dados):
        retorno = {}
        retorno["codproduto"] = dados.codproduto()
        retorno["descricao"] = dados.descricao()
        retorno["preco"] = dados.preco()
        return retorno