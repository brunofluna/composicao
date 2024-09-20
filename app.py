from modulo import *

if __name__ == "__main__":
    # instacia dos objetos
    endereco_pessoal = Endereco('','','','')
    telefone = Contato(0,0,0,0)
    usuario = Pessoa('',0,'','')
    

    '''endereco_pessoal.cep = "72.666-666" #métodos de entrada pesquisar sobre
    endereco_pessoal.uf = 'DF'
    endereco_pessoal.uf = 'DF'
    endereco_pessoal.uf = 'DF'
    '''
    # entrada de dados
    usuario.nome = input('Digite o nome do usuário: ')
    usuario.idade = int(input('Digite a idade do usuário: '))
    
    # composição usuário - endereço
    usuario.endereco = endereco_pessoal
    usuario.telefone = telefone

    # composição de dados do telefone


    # entrada de dados do endereço
    usuario.endereco.cep = input('Informe o CEP: ')
    usuario.endereco.uf = input('Informe a UF: ')
    usuario.endereco.cidade = input('Informe a cidade: ')
    usuario.endereco.bairro = input('Informe o bairro: ')
    usuario.telefone.fixo = int(input('Digite o telefone fixo: '))
    usuario.telefone.cel = int(input('Digite o telefone celular: '))
    usuario.telefone.com = int(input('Digite o telefone comercial: '))
    usuario.telefone.sos = int(input('Digite o telefone de emergência: '))


    
    # saída de dados
    print(usuario.obter_info_pessoal())