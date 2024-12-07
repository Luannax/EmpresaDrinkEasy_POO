comandasGeral = []

#---------------------------------------- CLASSES ----------------------------------------#        
# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco):
        self.__nome = nome  # Nome da pessoa
        self.__cpf = cpf    # CPF da pessoa
        self._telefone = telefone  # Telefone da pessoa
        self._endereco = endereco  # Endereço da pessoa

    @property
    def nome(self):
        return self.__nome  # Getter para o nome

    @property
    def cpf(self):
        return self.__cpf    # Getter para o CPF

    def telefone(self):
        return self._telefone  # Getter para o telefone

    def endereco(self):
        return self._endereco  # Getter para o endereço

    #pessoas diferentes podem exibir a comanda, o que irá mudar é sua perminssão
    @property
    def exibirComanda(self):
        print("Nenhuma comanda")
        
# Classe Cliente que herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, comandas):
        super().__init__(nome, cpf, telefone, endereco)
        self.comandas = comandas  # Lista de comandas do cliente

    def exibirComanda(self):
        if not self.comandas:
            print("Nenhuma comanda encontrada.")
            return

        for comanda in self.comandas:
            print('\n')
            print("-" * 60)
            print("\bCOMANDA")
            print(f"Funcionário: {comanda.funcionario().nome}") # Exibe o nome do funcionário
            print(f"Cliente: {self.nome}")
            print(f"CPF: {self.cpf}")
            
            comanda.imprimirComanda()
            print(f"Total: R${comanda.calcularTotal():.2f}")
            print("-" * 60)

# Classe Comanda
class Comanda:
    def __init__(self, cliente, funcionario):
        self.__itens = []  # Lista de itens na comanda
        self.__cliente = cliente  # Cliente associado à comanda
        self.__funcionario = funcionario  # Funcionário associado à comanda
    
    def cliente(self):
        return self.__cliente
    
    def funcionario(self):
        return self.__funcionario

    @property
    def itens(self):
        return self.__itens  # Getter para a lista de itens na comanda
    
    def calcularTotal(self):
        total = 0
        for item in self.__itens:
            total += (item.preco * item.quantidade) 
        return total

    def adicionarItem(self, item):
        self.__itens.append(item)

    def imprimirComanda(self):
        for item in self.__itens:
            print("Estação: "+ item.estacao.nome)
            print('Itens:')
            print(str(item.quantidade) +'x - '+ item.nome + ' - ' + item.volume + ' - R$' + str(item.preco))
    
# Classe Estacao
class Estacao:
    def __init__(self, nome):
        self.__nome = nome  # Nome da estação

    @property
    def nome(self):
        return self.__nome  # Getter para o nome da estação

# Classe Funcionario que herda de Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, cargo):
        super().__init__(nome, cpf, telefone, endereco)  # Chama o construtor da classe base
        self.__cargo = cargo          # Cargo do funcionário

    @property
    def cargo(self):
        return self.__cargo  # Getter para o cargo

    #exibir todas as comandas
    def exibirComanda(self):
      for c in comandasGeral:
        print('\n')
        print('\bCOMANDAS EM GERAL')
        print('-' * 60)
        print("Cliente: " + c.cliente.nome)
        c.imprimirComanda()
        print('-' * 60)
        
         
    # permiti ao funcionario gerencia o cliente
    def gerenciarCliente(self, clientes):
      # verifica se existe um cliente
        if not clientes:
          print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
          return

        try:
          cliente = pesquisar_cliente(clientes)

          if not cliente.comandas:
            print("Nenhuma comanda encontrada para o cliente.")
            return

          cliente.exibirComanda()

          print('\nQuitar conta do cliente:\n1 - sim\n2 - não')  #pergunta se deseja quitar a conta do cliente
          opcao =  int(input("\nSeleciono uma opcao: "))
          comanda = cliente.comandas[0]
          if opcao == 1:
            cliente.comandas.remove(comanda)
            print("\nConta quitada com sucesso")
          else:
            print("\n Não quitada")
        except ValueError:
          print("Opção inválida. Tente novamente.")
          return


# Classe base Bebida
class Bebida:
    def __init__(self, nome, preco, volume, estacao, quantidade):
        self.__nome = nome      # Nome da bebida
        self.__preco = preco    # Preço da bebida
        self.__volume = volume  # Volume da bebida
        self.__estacao = estacao   # Estação associada à bebida
        self.__quantidade = quantidade  # Quantidade da bebida

    @property
    def nome(self):
        return self.__nome  # Getter para o nome

    @property
    def preco(self):
        return self.__preco  # Getter para o preço

    @property
    def volume(self):
        return self.__volume  # Getter para o volume

# diferentes tipos de bebidas
class Chopp(Bebida):
    def __init__(self, nome, preco, volume, estacao, quantidade):
        super().__init__(nome, preco, volume, estacao, quantidade)  # Chama o construtor da classe base

class Vinho(Bebida):
    def __init__(self, nome, preco, volume, estacao, quantidade):
        super().__init__(nome, preco, volume, estacao, quantidade)  # Chama o construtor da classe base

class Refrigerante(Bebida):
    def __init__(self, nome, preco, volume, estacao, quantidade):
        super().__init__(nome, preco, volume, estacao, quantidade)  # Chama o construtor da classe base


#---------------------------------------- funções ----------------------------------------#        
# Função para inicializar estações com objetos
def estacoes():
    estacao_sul = Estacao(" Estação do Sul")  # Cria estação de chopp
    estacao_centro = Estacao(" Estação do Centro")  # Cria estação de vinho
    estacao_norte = Estacao(" Estação do Norte")  # Cria estação de refrigerante
    return [estacao_sul, estacao_centro, estacao_norte]  # Retorna lista de estações


# função para criar cliente
def criar_Cliente_teste(clientes):
  if not clientes:
    cliente = Cliente("Juca", "123.456.789-10", "99 99999999", "Rua maria knsksdsds", comandas= [])
    clientes.append(cliente)
    
# Função para criar administrador padrão
def criar_administrador_padrao(funcionarios):
    if not funcionarios:  # Verifica se a lista de funcionários está vazia
        administrador = Funcionario("Adm", "000.000.000-00", "99 9999999","Rua Maria asasasas","Administrador",)  # Cria funcionário padrão
        funcionarios.append(administrador)  # Adiciona o administrador à lista
        #print("Funcionário padrão (Admin) criado com sucesso!")  # Mensagem de sucesso
        
# Função para carregar bebidas
def carregar_bebidas():
    # Bebidas organizadas 
    
    bebidas = []

    chops = []
    chopp = Chopp('Chopp', 6.00, '300ml', None, 0)
    chops.append(chopp)
    chopp = Chopp('Chopp', 8.00, '400ml', None, 0)
    chops.append(chopp)
    chopp = Chopp('Chopp', 9.00, '500ml', None, 0)
    chops.append(chopp)

    bebidas.append(chops)

    vinhos = []
    vinho = Vinho('Vinho', 12.00, '300ml', None, 0)
    vinhos.append(vinho)
    vinho = Vinho('Vinho', 16.00, '400ml', None, 0)
    vinhos.append(vinho)
    vinho = Vinho('Vinho', 20.00, '500ml', None, 0)
    vinhos.append(vinho)

    bebidas.append(vinhos)

    refrigerantes = []
    refrigerante = Refrigerante('Refrigerante', 6.00, '300ml', None, 0)
    refrigerantes.append(refrigerante)
    refrigerante = Refrigerante('Refrigerante', 8.00, '400ml', None, 0)
    refrigerantes.append(refrigerante)
    refrigerante = Refrigerante('Refrigerante', 10.00, '500ml', None, 0)
    refrigerantes.append(refrigerante)

    bebidas.append(refrigerantes)
    return bebidas  # Retorna o a lista de bebidas

# Função para realizar nova venda
def nova_venda(clientes,funcionarios, estacoes):
    if not clientes:  # Verifica se a lista de clientes está vazia
        print("Nenhum cliente cadastrado. Crie um cliente primeiro.")  # Mensagem de erro
        return

    if not funcionarios:  # Verifica se a lista de funcionários está vazia
        print("Nenhum funcionário cadastrado. Crie um funcionário primeiro.")  # Mensagem de erro
        return

    if not estacoes:  # Verifica se a lista de estações está vazia
        print("Nenhuma estação cadastrada. Crie uma estação primeiro.")  # Mensagem de erro
        return

    print('\nNOVA VENDA')  # Início do processo de nova venda

    funcionario = pesquisar_funcionario(funcionarios)
    cliente = pesquisar_cliente(clientes)  # Pesquisa o cliente

    if not cliente:
        return

    estacao_escolhida = escolherEstacao(estacoes) # escolha de estação

    if not estacao_escolhida:
        return

    if not cliente.comandas:
      comanda = Comanda(cliente,funcionario)
      comanda.cliente = cliente
      comandasGeral.append(comanda)
      cliente.comandas.append(comanda)  # Cria uma nova comanda para o cliente
    else: 
      comanda = cliente.comandas[-1]  # Utiliza a última comanda do cliente

  
    print(f"\bEstação selecionada: {estacao_escolhida.nome}")  # Confirmação da estação selecionada
    bebida_escolhida = escolherBebida()
    
    print(f"Bebida selecionada: {bebida_escolhida.nome}")  # Confirmação da bebida selecionada
    bebida_escolhida.estacao = estacao_escolhida
    comanda.adicionarItem(bebida_escolhida)

    print(f"Total da comanda: R${comanda.calcularTotal()}")  # Exibe o total da comanda

#pesquisa e devolve o funcionario 
def pesquisar_funcionario(funcionarios):
  # Selecionar o vendedor
    print("Selecione o vendedor:")
    idx = 1 # Índice para listar os vendedores
    for funcionario in funcionarios: # Percorre a lista de funcionários
        print(f"{idx} - {funcionario.nome} (CPF: {funcionario.cpf})")  # Lista de vendedores
        idx += 1 # Incrementa o índice

    try: # Tratamento de exceção
        opcao_vendedor = int(input('Digite a opção desejada: '))  # Captura a opção do vendedor
        if opcao_vendedor < 1 or opcao_vendedor > len(funcionarios): # Verifica se a opção é válida
            print("Vendedor inválido. Tente novamente.")  # Mensagem de erro
            return 
        vendedor = funcionarios[opcao_vendedor - 1]  # Seleciona o vendedor
    except ValueError: # Tratamento de exceção
        print("Opção inválida. Tente novamente.")  # Mensagem de erro
        return

    print(f"Vendedor selecionado: {vendedor.nome} (CPF: {vendedor.cpf})")  # Confirmação do vendedor selecionado
    return vendedor  # Retorna o vendedor selecionado

# Função para pesquisar cliente
def pesquisar_cliente(clientes):
    print('\nPESQUISAR CLIENTE')
    print('1 - Buscar por Nome')
    print('2 - Buscar por CPF')
    print('3 - Listar clientes')
    print('4 - Voltar')
    opcao = int(input('Digite a opção desejada: ')) # Captura a opção do usuário

    if opcao == 1: # Buscar por nome
        nome = input('Digite o nome do cliente: ')
        for cliente in clientes: # Percorre a lista de clientes
            if cliente.nome == nome: # Verifica se o nome do cliente é igual ao nome pesquisado
                return cliente
    elif opcao == 2: # Buscar por CPF
        cpf = input('Digite o CPF do cliente: ')
        for cliente in clientes: # Percorre a lista de clientes
            if cliente.cpf == cpf: # Verifica se o CPF do cliente é igual ao CPF pesquisado
                return cliente
    elif opcao == 3: # Listar clientes
        listarClientes(clientes) # Chama a função para listar clientes
        voltar = input('Voltar? (s/n) ') # Pergunta se deseja voltar
        if voltar.lower() == 's': # Verifica se deseja voltar
            return pesquisar_cliente(clientes) # Chama a função para pesquisar cliente
        else:
            return pesquisar_cliente(clientes)
    elif opcao == 4: # Voltar
        return None # Retorna None
    else: # Opção inválida
        print('Opção inválida. Tente novamente.')
        return None

    print("Cliente não encontrado.") 
    return None

# funcao para escolher a bebida
def escolherBebida():
  bebidas = carregar_bebidas()
  try:
    # pergunta que tipo de bebida o cliente prefere
    print("\nEscolha a bebida: ")
    print("Bebidas: \n1 - Chopp \n2 - Vinho \n3 - Refrigerante")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
       opcao_volume = 1
       print("\nSelecione o tamanho: ")
       # mostra a opção de tamanhos para a bebida selecionada
       for c in bebidas[0]:
        print(str(opcao_volume)  +"-"+ c.volume + " - " + str(c.preco))
        opcao_volume += 1

        # pergunta a quantidade que será comprada
       opcao_escolhida_be = int(input("Digite a opção desejada: "))
       quantidade = int(input("Digite a quantidade: "))

       if quantidade < 1:
        print("Quantidade inválida. Tente novamente.")
        return
       
       #atribui o a quantidade de bebida comprada
       bebidas[0][opcao_escolhida_be -1].quantidade = quantidade
       return bebidas[0][opcao_escolhida_be -1]

    elif opcao == 2:
      opcao_volume = 1
      print("\nSelecione o tamanho: ")
       # mostra a opção de tamanhos para a bebida selecionada
      for c in bebidas[1]:
        print(str(opcao_volume)  +"-"+ c.volume + " - " + str(c.preco))
        opcao_volume += 1

      # pergunta a quantidade que será comprada
      opcao_escolhida_be = int(input("Digite a opção desejada: "))
      quantidade = int(input("Digite a quantidade: "))

      if quantidade < 1:
        print("Quantidade inválida. Tente novamente.")
        return
      
      #atribui o a quantidade de bebida comprada
      bebidas[1][opcao_escolhida_be -1].quantidade = quantidade
      return bebidas[1][opcao_escolhida_be -1]

    elif opcao == 3:
      opcao_volume = 1
      print("\nSelecione o tamanho: ")
      # mostra a opção de tamanhos para a bebida selecionada
      for c in bebidas[2]:
        print(str(opcao_volume)  +"-"+ c.volume + " - " + str(c.preco))
        opcao_volume += 1
      # pergunta a quantidade que será comprada
      opcao_escolhida_be = int(input("Digite a opção desejada: "))
      quantidade = int(input("Digite a quantidade: "))

      if quantidade < 1:
        print("Quantidade inválida. Tente novamente.")
        return
      
      #atribui o a quantidade de bebida comprada
      bebidas[2][opcao_escolhida_be -1].quantidade = quantidade
      return bebidas[2][opcao_escolhida_be -1]

  except ValueError:
    print("Opção inválida. Tente novamente.")  # Mensagem de erro
    return

# função para escolher uma estação
def escolherEstacao(estacoes):
  print("\nSelecione a estação:")
  opcao_estacao = 1
  for e in estacoes:
    print(str(opcao_estacao) + "-" +  e.nome)
    opcao_estacao += 1
  
  try:
    opcao = int(input('Digite a opção desejada: '))  # Captura a opção do vendedor
    if opcao < 1 or opcao > len(estacoes):
      print("Opção inválida. Tente novamente.")  # Mensagem de erro
      return
    
    return estacoes[opcao -1]

  except ValueError:
    print("Opção inválida. Tente novamente.")  # Mensagem de erro
    return

# funcao para auxiliar no gerenciamento de clientes
def gerenciarCliente(clientes, funcionarios):
    # verifica se existe um cliente
    if not clientes: 
        print("Nenhum cliente cadastrado. Crie um cliente primeiro.")
        return

    try: # tratamento de exceção
        cliente = pesquisar_cliente(clientes) # pesquisa o cliente

        if cliente is None: # verifica se o cliente é nulo
            print("Cliente não encontrado.") # mensagem de erro
            return

        if not cliente.comandas: # verifica se o cliente possui comandas
            print("Nenhuma comanda encontrada para o cliente.")
            return

        cliente.exibirComanda() # exibe a comanda do cliente

        print('\nQuitar conta do cliente:\n1 - sim\n2 - não')  # pergunta se deseja quitar a conta do cliente
        opcao = int(input("\nSelecione uma opcao: "))
        comanda = cliente.comandas[0] # seleciona a comanda do cliente
        if opcao == 1: # verifica se a opção é 1
            cliente.comandas.remove(comanda) # remove a comanda do cliente
            print("\nConta quitada com sucesso")
        else: # se não
            print("\nConta não quitada") 
    except ValueError: # tratamento de exceção
        print("Opção inválida. Tente novamente.")
        return

# função para listar clientes
def listarClientes(clientes):
    if not clientes: # Verifica se a lista de clientes está vazia
        print("Nenhum cliente cadastrado.")
        return

    print("Lista de clientes:")
    for cliente in clientes: # Percorre a lista de clientes
        if isinstance(cliente, Cliente):  # Verifica se o objeto é uma instância da classe Cliente
            print(f"Nome: {cliente.nome}")


#funcao para auxiliar a exibir todas as coimandas
def mostrarComandas(funcionarios):
  funcionario = pesquisar_funcionario(funcionarios)

  if not funcionario: # se não existir funcionario retornar
    return

  if not comandasGeral: # se não existir comandas retornar
    print("Nenhuma comanda encontrada.")
    return

  funcionario.exibirComanda() # exibir todas as comandas

# Menu principal
def menu():
    estacoesRef = estacoes()  # Carrega as estações
    bebidas = carregar_bebidas()  # Carrega as bebidas por estação
    clientes = []  # Inicializa lista de clientes
    funcionarios = []  # Inicializa lista de funcionários

    criar_administrador_padrao(funcionarios)  # Cria um administrador padrão
    criar_Cliente_teste(clientes)  # Cria um cliente teste
    while True:
        print('\nSISTEMA DRINKEASY')  # Título do sistema
        print('1 - Nova venda')  # Opção para nova venda
        print('2 - Cadastrar cliente')  # Opção para cadastrar cliente
        print('3 - Cadastrar funcionário')  # Opção para cadastrar funcionário
        print('4 - Criar nova estação')   # Opção para criar uma nova estação
        print('5 - Gerenciar cliente')  # Opção para gerenciar a situação do cliente
        print('6 - exibir comandas') # opcao para gerenciar todas as comandas
        print('0 - Sair')  # Opção para sair

        try:
            opcao = int(input('Digite a opção desejada: '))  # Captura a opção do usuário
        except ValueError:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro
            continue

        if opcao == 1:
            nova_venda(clientes,funcionarios, estacoesRef)  # Chama a função de nova venda

        elif opcao == 2:
            print('\nCADASTRO DE CLIENTE')  # Início do cadastro de cliente
            nome = input('Nome do cliente: ')  # Captura o nome do cliente
            cpf = input('CPF do cliente: ')  # Captura o CPF do cliente
            telefone = input('Telefone do cliente: ')  # Captura o telefone do cliente
            endereco = input('Endereço do cliente: ')  # Captura o endereço do cliente
            cliente = Cliente(nome, cpf, telefone, endereco, comandas = [])  # Cria um novo cliente
            clientes.append(cliente)  # Adiciona o cliente à lista
            print(f"Cliente {nome} cadastrado com sucesso!")  # Mensagem de sucesso

        elif opcao == 3:
            print('\nCADASTRO DE FUNCIONÁRIO')  # Início do cadastro de funcionário
            nome = input('Nome do funcionário: ')  # Captura o nome do funcionário
            cpf = input('CPF do funcionário: ')  # Captura o CPF do funcionário
            telefone = input('Telefone do funcionário: ')  # Captura o telefone do funcionário
            endereco = input('Endereço do funcionário: ')  # Captura o endereço do funcionário
            cargo = input('Cargo do funcionário: ')  # Captura o cargo do funcionário
            funcionario = Funcionario(nome, cpf, telefone, endereco, cargo)  # Cria um novo funcionário
            funcionarios.append(funcionario)  # Adiciona o funcionário à lista
            print(f"Funcionário {nome} cadastrado com sucesso!")  # Mensagem de sucesso
            
        elif opcao == 4:
            print('\nNOVA ESTACAO')  # Início do cadastro de nova estação
            nome = input('Nome da estação: ')  # Captura o nome da estação
            estacao = Estacao(nome)  # Cria uma nova estação
            estacoesRef.append(estacao)  # Adiciona a estação à lista
            print('Estação cadastrada com sucesso!')  # Mensagem de sucesso
        elif opcao == 5:
            print('\nGERENCIAR CLIENTE')  # Início do gerenciamento de cliente
            gerenciarCliente(clientes, funcionarios)

        elif opcao == 6:
            print('\nEXIBIR COMANDAS') # 
            mostrarComandas(funcionarios)

        elif opcao == 0:
            print('Saindo...')  # Mensagem de saída
            break  # Encerra o loop
        else:
            print('Opção inválida. Tente novamente.')  # Mensagem de erro

menu()