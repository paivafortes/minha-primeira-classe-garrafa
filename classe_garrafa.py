#Criando a classe 'garrafa';
class garrafa:
    #Características e Especificações;
    marca=None
    modelo=None
    cor=None
    dimensoes=None
    composicao=None
    material=None
    capacidade=None
    volume_atual=0
    status='fechada'
#Dados e informações extraídos de um produto na internet, consulte o conteúdo em https://www.mundotupperware.com.br/garrafa-tupperware-eco-tupper-plus-500ml-varias-cores/p.

#DEFININDO FUNÇÕES:
#Abrir garrafa;
    def abrir(self):
      if self.status=='aberta':
            print("A sua garrafa está aberta agora!")
      else:
            self.status='aberta'
            print(f'A sua garrafa está {self.status} agora!')

#Fechar garrafa;
    def fechar(self):
        if self.status=='fechada':
            print("Agora, a sua garrafa está fechada!")
        else:
            self.status='fechada'
            print(f'Agora, a sua garrafa está {self.status}!')

#Verificar a quantidade atual na garrafa;
    def consultar (self):
        print(f'Atualmente, a sua garrafa contém {self.volume_atual} ml.')

#Adicionar líquido da garrafa;
    def adicionar(self,mililitros):
        if self.status=='aberta': 
            if self.volume_atual+mililitros<=self.capacidade: 
                if mililitros > 0 and self.volume_atual<=self.capacidade:
                    self.volume_atual+=mililitros
                    print(f'Foram adicionados {mililitros} ml à sua garrafa!')
                else:
                    print('Valor inválido!')
            else:
                print(f'A quantidade de {mililitros} ml excede a capacidade da garrafa. Verifique a quantidade atual na garrafa e sua capacidade máxima para determinar quanto ainda pode ser adicionado.')
        else:
            print('Antes de adicionar o líquido, é necessário abrir a garrafa primeiro.')

#Retirar líquido da garrafa;
    def retirar (self,mililitros):
        if self.status=='aberta':
            if self.volume_atual>0:
                self.volume_atual-=mililitros
                print(f'Foram retirados {mililitros} ml da sua garrafa!')
            else:
                print('A sua garrafa está vazia.')
        else:
            print('Antes de retirar o líquido, é necessário abrir a garrafa primeiro.')

#Definindo uma variável para 'garrafa';
g1=garrafa()

#Inserindo informações nas características e especificações da garrafa;
g1.marca='Tupperware'
g1.modelo='Eco Tupper Plus'
g1.cor='preto'
g1.dimensoes='7,4 diâmetro x 22 altura (cm)'
g1.composicao='1 peça (base, tampa e alça)'
g1.material='plástico'
g1.capacidade=500

#Executando as funcionalidades da garrafa;
g1.abrir()
g1.adicionar(200)
g1.adicionar(400)
g1.consultar()
g1.adicionar(300)
g1.consultar()
g1.fechar()
