class Cliente:
    def __init__(self):
        self._codcliente = 0
        self._nome = ""
        self._endereco = ""

        self._lista = 'nome, endereco'
        self.__dadosInserir = ""
        self.__dadosDelete = ""
        self.__dadosUpdate = ""
        self.__dadosPesquisa = ""
        self.__tabelaBanco = "cliente"

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self._nome}','{self._endereco}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = ("nome='{}',endereco='{}' where codcliente='{}'").format(self._nome,self._endereco)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where codcliente={}".format(self._codcliente)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from cliente where codcliente={}".format(self._codcliente)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def lista(self):
        return self._lista

    @property
    def codcliente(self):
        return self._codcliente

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @codcliente.setter
    def codcliente(self, value):
        self._codcliente = value

    @nome.setter
    def nome(self, value):
        self._nome = value

    @endereco.setter
    def endereco(self,value):
        self._endereco = value

    def __str__(self):
        return f"Cliente: {self._codcliente}, {self._nome}, {self._endereco}"

    def __repr__(self):
        return f"Cliente: {self._codcliente}, {self._nome}, {self._endereco}"