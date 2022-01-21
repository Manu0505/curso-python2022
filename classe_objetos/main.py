
#classe: entidade que gera os objetos
#objeto: dados pela classe, resultado
#atributo: características do objeto 
#métodos: coisas que o objeto faz e sua forma



class Pessoa:
    def __init__(self, cpf, nome, idade, cidade, genero):
        #atributos
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero



    def __str__(self) -> str:
        return f"nome:{self.nome} cpf: {self.cpf} idade: {self.idade} cidade: {self.cidade} genero: {self.genero}"


    #metodos
    def comer(self, alimento):
        print (f'{self.nome} está comendo {alimento}')

    def estudar(self, materia):
        print (f'{self.nome} está estudando {materia}')

    def dormir(self):
        print (f'{self.nome} está dormindo')

    def jogar(self, jogo):
        print (f'{self.nome} está jogando {jogo}')

    
    
pessoa = Pessoa(888 ,' manu', 17, 'são caetano', 'feminino')
pessoa.comer('uva')
pessoa.dormir()
pessoa.estudar('francês')
pessoa.jogar('uno')
print(pessoa)

#para usar a herança, basta criar uma nova classe com (nome da classe superior)