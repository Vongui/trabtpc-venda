class Venda:
    def __init__(self):
        self._codvenda = 0
        self._data = ""
        self._valor_total = 0.0
        self._codcliente = 0
        self._itens = []

        self._lista = 'data, valor_total, codcliente'
        self.__tabelaBanco = "venda"
        self.__dadosInserir = ""
        self.__dadosUpdate = ""
        self.__dadosDelete = ""
        self.__dadosPesquisa = ""

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._data}','{self._valor_total}', '{self._codcliente}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("data='{}',valor_total='{}',codcliente='{}' where codvenda='{}'").format(self._data, self._valor_total, self._codcliente, self._codvenda)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where codvenda={}".format(self._codvenda)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from venda where codvenda={}".format(self._codvenda)
        return self.__dadosPesquisa

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
    def data(self):
        return self._data

    @property
    def valor_total(self):
        return self._valor_total

    @property
    def codcliente(self):
        return self._codcliente

    @property
    def itens(self):
        return self._itens

    @codvenda.setter
    def codvenda(self, value):
        self._codvenda = value

    @data.setter
    def data(self, value):
        self._data = value

    @valor_total.setter
    def valor_total(self, value):
        self._valor_total = value

    @codcliente.setter
    def codcliente(self, value):
        self._codcliente = value

    @itens.setter
    def itens(self, value):
        self._itens = value

    def __repr__(self):
        return f"Venda: {self._codvenda}, {self._data}, {self._valor_total}, Cliente: {self._codcliente}, Itens: {self._itens}"
