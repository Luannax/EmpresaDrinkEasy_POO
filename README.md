# Gerenciador de Comandas - DrinkEasy

Este projeto foi desenvolvido em Python para a disciplina de **Programação Orientada a Objetos**. Ele implementa um sistema de gerenciamento de comandas para restaurantes ou bares, permitindo o controle de clientes, funcionários, bebidas e vendas.

## 📋 Funcionalidades

- **Cadastro de Clientes e Funcionários**:
  - Registre novos clientes e funcionários com informações como nome, CPF, telefone e endereço.
- **Criação e Gerenciamento de Comandas**:
  - Associe comandas a clientes e funcionários.
  - Adicione itens às comandas, como chopp, vinho e refrigerante, com preços e volumes personalizados.
- **Controle de Estações de Bebidas**:
  - Relacione bebidas às estações (ex.: Estação Sul, Centro e Norte).
- **Exibição Detalhada**:
  - Visualize as comandas em aberto, com detalhes de itens, valores e cliente responsável.
- **Encerramento de Comandas**:
  - Finalize comandas após pagamento, removendo-as da lista de abertas.

## 🛠️ Tecnologias Utilizadas

- **Python**
- Paradigmas de Programação Orientada a Objetos (POO)
- VsCode
- <a href="https://app.diagrams.net/">Draw.io</a>
- Canva (Usado para fazer a apresentação do código)

## 📂 Estrutura do Projeto

```plaintext
├── menu.py                               # Arquivo principal com todas as funcionalidades do sistema
├── Slides POO - EMPRESA DRINKEASY.pdf    # Apresentação do projeto
├── LICENSE                               # Licença do projeto
└── README.md                             # Documentação do projeto
```

### Como adicionar ao GitHub:

1. Crie um arquivo chamado `README.md` na raiz do projeto.
2. Copie e cole o código acima no arquivo.
3. Confirme as alterações com os seguintes comandos no terminal:
   ```bash
   git add README.md
   git commit -m "Adiciona README ao projeto"
   git push
   ```

## 🌟 Fluxo Básico de Uso

1. **Inicialize o Sistema**:
   - O menu apresenta as opções para gerenciar clientes, funcionários, estações e comandas.

2. **Cadastro de Clientes e Funcionários**:
   - Cadastre clientes e funcionários diretamente no sistema.

3. **Nova Venda**:
   - Associe uma comanda a um cliente, escolha a estação, adicione bebidas e visualize o total.

4. **Gerencie Comandas**:
   - Visualize as comandas em aberto e finalize-as após o pagamento.

5. **Personalize Estações e Bebidas**:
   - Adicione novas estações e configure bebidas personalizadas com volumes e preços variados.

## 🧩 Estrutura das Classes

- **Pessoa (Classe Base)**:
  - Representa uma pessoa genérica com atributos como nome, CPF, telefone e endereço.
- **Cliente e Funcionário**:
  - Herdam de Pessoa e incluem informações específicas, como comandas associadas ou cargo.
- **Comanda**:
  - Gerencia itens associados a um cliente e funcionário, permitindo cálculos e visualização do total.
- **Bebida e Subclasses (Chopp, Vinho, Refrigerante)**:
  - Representam os diferentes tipos de bebidas disponíveis para venda.
- **Estação**:
  - Representa estações específicas associadas às vendas.

## 📚 Aprendizados

Este projeto abordou:

- Encapsulamento, herança e polimorfismo na modelagem de classes.
- Estruturação de um sistema interativo utilizando Python.
- Práticas de design para facilitar a reutilização e manutenção do código.

## 👥 Equipe do Projeto

### Professor da Disciplina
- **<a href="http://buscatextual.cnpq.br/buscatextual/visualizacv.do;jsessionid=A2061DA0EA3802B15DF4BC68E83C9A91.buscatextual_0#ProjetosPesquisa">Frank</a>**

### Integrantes
- **<a href="https://github.com/Luannax">Luanna Bahia</a>**
- **<a href="https://github.com/Elismara04">Elismara Rodrigues</a>**
- **<a href="https://github.com/ApN-Jonas">Jonas Dantas</a>**
- **<a href="https://github.com/PedroHenrBarreto">Pedro Henrique Barreto</a>**


## 🤝 Contribuições

Contribuições são bem-vindas! Caso queira sugerir melhorias ou relatar problemas, sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

