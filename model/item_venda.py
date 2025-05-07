class ItemVenda:
    def __init__(self):
        self._codvenda = 0
        self._codproduto = 0
        self._qtde = 0
        self._valor = 0.0

        self._lista = "codvenda, codproduto, qtde, valor"
        self.__tabelaBanco = "item_venda"
        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._codvenda}', '{self._codproduto}', '{self._qtde}', '{self._valor}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("qtde='{}', valor='{}' WHERE codvenda='{}' AND codproduto='{}'").format(
            self._qtde, self._valor, self._codvenda, self._codproduto)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = f"WHERE codvenda={self._codvenda} AND codproduto={self._codproduto}"
        return self.__dadosDelete

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self._lista

    @property
    def codvenda(self):
        return self._codvenda

    @property
    def codproduto(self):
        return self._codproduto

    @property
    def qtde(self):
        return self._qtde

    @property
    def valor(self):
        return self._valor

    @codvenda.setter
    def codvenda(self, value):
        self._codvenda = value

    @codproduto.setter
    def codproduto(self, value):
        self._codproduto = value

    @qtde.setter
    def qtde(self, value):
        self._qtde = value

    @valor.setter
    def valor(self, value):
        self._valor = value

    def __repr__(self):
        return f"ItemVenda: Venda={self._codvenda}, Produto={self._codproduto}, Qtde={self._qtde}, Valor={self._valor}"
