import menu
import banco_de_dados as banco


while True:
    escolha = menu.menu()
    
    if escolha == 1:
        banco.mostrar()

    elif escolha == 2:
        banco.adicionar()

    elif escolha == 3:
        banco.atualizar()

    elif escolha == 4:
        banco.buscar_cpf()

    elif escolha == 5:
        banco.buscar_nome()

    elif escolha == 6:
        banco.buscar_email()

    #elif escolha == 7:
       # banco.buscar_curso()

    elif escolha == 7:
        banco.remover_cpf()

    elif escolha == 8:
        banco.remover_nome()

    elif escolha == 9:
        banco.quantidade()

    elif escolha == 10:
        banco.salvar()

    else:
        print ('Opção inválida, tente novamente')
        




