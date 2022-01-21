
import emoji



print(emoji.emojize('''
:green_book: AGENDA DE CONTATOS :green_book:

:small_red_triangle_down: Menu de opções:
[1] :page_with_curl:  Mostrar todos os contatos
[2] :pencil:  Adicionar novo contato
[3] :repeat:  Atualizar contato
[4] :mag_right:  Buscar contato pelo CPF 
[5] :mag_right:  Buscar contato pelo NOME 
[6] :mag_right:  Buscar contato pelo EMAIL 
[7] :mag_right:  Buscar contato pelo CURSO 
[8] :x:  Excluir um contato pelo CPF
[9] :x:  Excluir um contato pelo NOME
[10] :iphone:  Mostrar quantidade de contatos cadastrados
[11] :file_folder:  Salvar alterações
''', use_aliases=True))

escolha = int(input(emoji.emojize(':small_orange_diamond: Escolha e digite a opção desejada: ')))

