class Produto:
    def __init__(self):
        self._codproduto = 0
        self._descricao = ""
        self._preco = 0.0
        self._lista = 'descricao, preco'

        self.__dadosInserir = ""
        self.__dadosDelete = ""
        self.__dadosUpdate = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = "produto"

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._descricao}','{self._preco}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("descricao='{}',preco='{}' where codproduto='{}'").format(self._descricao, self._preco)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where codproduto={}".format(self._codproduto)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from produto where codproduto={}".format(self._codproduto)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self._lista

    @property
    def codproduto(self):
        return self._codproduto

    @property
    def descricao(self):
        return self._descricao

    @property
    def preco(self):
        return self._preco

    @codproduto.setter
    def codproduto(self, value):
        self._codproduto = value

    @descricao.setter
    def descricao(self,value):
        self._descricao = value

    @preco.setter
    def preco(self, value):
        self._preco = value

    def __repr__(self):
        return f"Produto: {self._codproduto}, {self._descricao}, {self._preco}"