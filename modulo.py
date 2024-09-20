class Endereco:
    def __init__(self, cep, uf, cidade, bairro):
        self.__cep = cep
        self.__uf = uf
        self.__cidade = cidade
        self.__bairro = bairro
    
    @property
    def cep(self):
        return self.__cep
    @property
    def uf(self):
        return self.__uf
    @property
    def cidade(self):
        return self.__cidade
    @property
    def bairro(self):
        return self.__bairro
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep
    @uf.setter
    def uf(self, uf):
        self.__uf = uf
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    # método de ação
    def obter_endereco(self):
        return f'{self.__bairro}, cidade de {self.__cidade}, {self.__uf}, CEP: {self.__cep}.'
    
class Contato:
    def __init__(self, fixo, cel, com, sos):
        self.__fixo = fixo
        self.__cel = cel
        self.__com = com
        self.__sos = sos
    
    @property
    def fixo(self):
        return self.__fixo
    @property
    def cel(self):
        return self.__cel
    @property
    def com(self):
        return self.__com
    @property
    def sos(self):
        return self.__sos
    
    @fixo.setter
    def fixo(self, fixo):
        self.__fixo = fixo
    @cel.setter
    def cel(self, cel):
        self.__cel = cel
    @com.setter
    def com(self, com):
        self.__com = com
    @sos.setter
    def sos(self, sos):
        self.__sos = sos

    def obter_telefone(self):
        return f'Fixo - {self.__fixo}, Celular - {self.__cel}, Comercial - {self.__com}, Emergência - {self.__sos}.'

class Pessoa:
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def endereco(self):
        return self.__endereco
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # método de ação
    def obter_info_pessoal(self):
        return f'{self.__nome}, {self.__idade} anos, mora em {self.__endereco.obter_endereco()}, e tem os seguintes contatos:\n {self.__telefone.obter_telefone()}.'