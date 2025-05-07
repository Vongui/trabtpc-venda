from dao.connection import Banco
from model.item_venda import ItemVenda

from controller.controller_generico import ControleGenerico


class ControllerItemVenda(ControleGenerico):

    def listarItensPorVenda(self, codvenda):
        self.ob.abrirConexao()
        sql = f"SELECT * FROM item_venda WHERE codvenda = {codvenda}"
        resultado = self.ob.selectQuery(sql)

        lista_itens = []
        for row in resultado:
            item = ItemVenda()
            item.codvenda = row[0]
            item.codproduto = row[1]
            item.qtde = row[2]
            item.valor = row[3]
            lista_itens.append(item)

        return lista_itens
