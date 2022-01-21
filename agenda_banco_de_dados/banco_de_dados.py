import emoji

global pessoas
pessoas = []

#import os
# criação do arquivo de agenda

planilha = open("./planilha_agenda.csv", 'a+')
planilha.close()

# leitura do arquivo de agenda
planilha = open("./planilha_agenda.csv", 'r+')

auxiliar = planilha.readlines()


planilha.close()
for i in auxiliar:
    if i != '\n':
        pessoas.append(i)
# planilha.close()

# os.remove("./planilha_agenda.csv")


def mostrar():
    print(emoji.emojize('\n   :bust_in_silhouette: CONTATOS REGISTRADOS :bust_in_silhouette:'))
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(';')
        print(emoji.emojize(f''':small_blue_diamond: Mostrando dados de {dados[0]} :small_blue_diamond:
    :bust_in_silhouette: CPF: {dados[1]}
    :telephone_receiver: Número de celular: {dados[2]}
    :e-mail: E-mail: {dados[3]}
    :mortar_board: Curso: {dados[4]}
    :date: Data de nascimento: {dados[5]}
    :red_circle: Observações: {dados[6]}
    -------------------------------------''', use_aliases=True))


def adicionar():
    print(emoji.emojize(''':bust_in_silhouette: Adicionar novo contato :bust_in_silhouette:

    insira os dados:
    '''))
    nome = input('Nome:  ')
    cpf = input('CPF:  ')
    numero = input('Número de telefone:  ')
    email = input('E-mail:  ')
    curso = input('Curso:  ')
    nascimento = input('Data de nascimento:  ')
    observacao = input('Observação:  ')
    dados = nome + ';' + cpf + ';' + numero + \
        ';' + email + ';' + curso + ';' + nascimento + \
             ';' + observacao
    pessoas.append(str(dados))
    salvar()
    return None


def atualizar():
    cpf = input(emoji.emojize(':bust_in_silhouette: Digite o CPF do contato que você deseja atualizar: '))
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(';')
        if cpf in dados:
            #para mostrar a pessoa a ser atualizada
            print ('A pessoa a ser atualizada é:')       #ta conseguindo acessar a pessoa
            print(emoji.emojize(f'''
            :bust_in_silhouette: Nome: {dados[0]}
            :key: CPF: {dados[1]}
            :telephone_receiver: Número de telefone: {dados[2]}
            :e-mail: E-mail: {dados[3]}
            :mortar_board: Curso: {dados[4]}
            :date: Data de nascimento: {dados[5]}
            :bangbang: Observações: {dados[6]}
            ''', use_aliases=True))
            e = input('você concorda em atualizar a pessoa acima? (responda exclusivamente com "sim" ou "não")\nR:  ') #funcionado
            if e == 'sim':
                #para excluir a antiga versão
                pessoas.remove(pessoa)
                #para inserir os novos dados
                print('para atualizar, insira os dados a seguir:')
                nome = input('Nome:  ')
                cpf = input('CPF:  ')
                numero = input('Número de telefone:  ')
                email = input('E-mail:  ')
                curso = input('Curso:  ')
                nascimento = input('Data de nascimento:  ')
                observacao = input('Observação:  ')
                dados = nome + ';' + cpf + ';' + numero + \
                    ';' + email + ';' + curso + ';' + nascimento + ';' + observacao
                pessoas.append(str(dados))                              
                #para salvar as alterações
                salvar()                                                
                return None
            elif e != 'sim':
                print('você será direcionado ao Menu')
                return None
        elif cpf not in dados:
            print('pessoa não encontrada, tente novamente')


def buscar_cpf():
    cpf = input(emoji.emojize(':bust_in_silhouette: Digite o CPF da pessoa que você deseja acessar: '))
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(";")
        print("Resultado da busca: ")
        if cpf in dados:
            print(emoji.emojize(":sparkles: Contato encontrado! "))
            print(emoji.emojize(f'''
            :bust_in_silhouette: Nome: {dados[0]}
            :key: CPF: {dados[1]}
            :telephone_receiver: Número de telefone: {dados[2]}
            :e-mail: E-mail: {dados[3]}
            :mortar_board: Curso: {dados[4]}
            :date: Data de nascimento: {dados[5]}
            :bangbang: Observações: {dados[6]}
            ''', use_aliases=True))
            break
    return None


def buscar_nome():
    nome = input(emoji.emojize(':bust_in_silhouette: digite o nome da pessoa a ser acessada: '))
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(";")
        print("Resultado da busca: ")
        if nome in dados:
            print(emoji.emojize(":sparkles: Contato encontrado! "))
            print(emoji.emojize(f'''
            :bust_in_silhouette: Nome: {dados[0]}
            :key: CPF: {dados[1]}
            :telephone_receiver: Número de telefone: {dados[2]}
            :e-mail: E-mail: {dados[3]}
            :mortar_board: Curso: {dados[4]}
            :date: Data de nascimento: {dados[5]}
            :bangbang: Observações: {dados[6]}
            ''', use_aliases=True))
            break
        else:
            print('nome não encontrado, tente novamente')


def buscar_email():
    email = input('digite o email da pessoa que você deseja acessar: ')
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(";")
        print("Resultado da busca: ")
        if email in pessoa:
            print(':sparkles: Contato encontrado!')
            print(emoji.emojize(f'''
            :bust_in_silhouette: Nome: {dados[0]}
            :key: CPF: {dados[1]}
            :telephone_receiver: Número de telefone: {dados[2]}
            :e-mail: E-mail: {dados[3]}
            :mortar_board: Curso: {dados[4]}
            :date: Data de nascimento: {dados[5]}
            :bangbang: Observações: {dados[6]}
            ''', use_aliases=True))
        else:
            print('pessoa não encontrada, tente novamente')


#def buscar_curso():
    #curso = input('Digite o curso da pessoa que você deseja acessar: ')
    #for pessoa in pessoas:
      #  n = pessoa.replace("\n", "")
       # dados = n.split(";")
        #print("Resultado da busca: ")
        #if curso in pessoa:
  #          print(emoji.emojize(':smile: Contato encontrado! :smile:', use_aliases=True))
   #         print(emoji.emojize(f'''
    #        :bust_in_silhouette: Nome: {dados[0]}
     #       :key: CPF: {dados[1]}
      #      :telephone_receiver: Número de telefone: {dados[2]}
       #     :e-mail: E-mail: {dados[3]}
        #    :mortar_board: Curso: {dados[4]}
         #   :date: Data de nascimento: {dados[5]}
          #  :bangbang: Observações: {dados[6]}
           # ''', use_aliases=True))
      #  elif curso not in pessoa:
       #     print('pessoa não encontrada, tente novamente')


def remover_cpf():
    cpf = input(emoji.emojize(':x: digite o CPF da pessoa que deseja remover: use_aliases=True'))
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(';')
        if cpf in dados:
            print ('A pessoa a ser excluída é:')       #ta conseguindo acessar a pessoa
            print(emoji.emojize(f'''
            :bust_in_silhouette: Nome: {dados[0]}
            :key: CPF: {dados[1]}
            :telephone_receiver: Número de telefone: {dados[2]}
            :e-mail: E-mail: {dados[3]}
            :mortar_board: Curso: {dados[4]}
            :date: Data de nascimento: {dados[5]}
            :bangbang: Observações: {dados[6]}
            ''', use_aliases=True))

            e = input(emoji.emojize(':eyes: Você concorda em remover a pessoa acima? (responda exclusivamente com "sim" ou "não"\nR:  )', use_aliases=True))
            if e == 'sim':
                pessoas.remove(pessoa)
                salvar()
                print(emoji.emojize(':x: Pessoa removida com sucesso :x:', use_aliases=True))
                break
            if e != 'sim':
                print('Você será direcionado(a) ao Menu')
                return None
        else:
            print(emoji.emojize(':tired_face: Não foi possível remover. Pessoa não encontrada. :tired_face:', use_aliases=True))


def remover_nome():
    nome = input('Digite o nome da pessoa que deseja remover: ')
    for pessoa in pessoas:
        n = pessoa.replace("\n", "")
        dados = n.split(';')
        if nome in dados:                  #alterei n > dados
            print ('A pessoa a ser excluída é:')       #ta conseguindo acessar a pessoa
            print(emoji.emojize(f'''
            :bust_in_silhouette: Nome: {dados[0]}
            :key: CPF: {dados[1]}
            :telephone_receiver: Número de telefone: {dados[2]}
            :e-mail: E-mail: {dados[3]}
            :mortar_board: Curso: {dados[4]}
            :date: Data de nascimento: {dados[5]}
            :bangbang: Observações: {dados[6]}
            ''', use_aliases=True))

            e = input(emoji.emojize(':eyes: Você concorda em remover a pessoa acima? (responda exclusivamente com "sim" ou "não"\nR:  )', use_aliases=True))
            if e == 'sim':
                pessoas.remove(pessoa)
                salvar()
                print(emoji.emojize(':x: Pessoa removida com sucesso :x:', use_aliases=True))
                break
            if e != 'sim':
                print('Você será direcionado(a) ao Menu')
                return None
        else:
            print(emoji.emojize(':tired_face: Não foi possível remover. Pessoa não encontrada. :tired_face:', use_aliases=True))


def quantidade():
    quantidade = len(pessoas)
    print(emoji.emojize(f':bust_in_silhouette: você possui {quantidade} contato(s) cadastrados :sweat_smile:', use_aliases=True))
    return quantidade


def salvar():
    planilha_escrever = open("./planilha_agenda.csv", 'w')
    linhas = len(pessoas)
    print("quantidade de linhas:", linhas)
    for i in pessoas:
        planilha_escrever.write(i + str('\n'))
    planilha_escrever.close()

    # planilha_escrever.write('\r')
    print('alterações salvas')

    return None


planilha.close()
