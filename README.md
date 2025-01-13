# FPFTechChallenge

Repositório dedicado ao upload de arquivos relacionados ao questionário FPF Tech Challenge.

## Questão 9: Automação de Testes Funcionais para Identificação de Triângulos com Selenium e Pytest
Crie os cenários de teste e implemente a automação de testes funcionais utilizando o **Selenium WebDriver** e algum framework de teste unitário em qualquer linguagem de programação para a aplicação triângulo disponível em [http://www.vanilton.net/triangulo/](http://www.vanilton.net/triangulo/). 

Os testes devem cobrir o seguinte requisito:
- Dado os três lados de um triângulo, o programa deve informar se o triângulo é **equilátero**, **isósceles** ou **escaleno**.
- Lados só formam um triângulo se o comprimento de um lado for sempre menor do que a soma dos outros dois. Caso essa propriedade não seja satisfeita, o programa deve exibir uma **mensagem de erro**.

### Requisitos e Ferramentas Utilizadas
- **Linguagem de Programação:** Python
- **Framework de Teste Unitário:** pytest
- **Automação de Testes:** Selenium WebDriver
- **Gerenciamento de Dependências:** pip

### Como Executar os Testes
1. **Clone este repositório em sua máquina local**:
   Abra um terminal e execute o comando abaixo para clonar o repositório:
   ```bash
   git clone https://github.com/gabriellvalle/FPFTechChallange.git
2. **Na pasta onde o repositório foi clonado, acesse a pasta 'question09'**.
3. **Certifique-se de ter o Python instalado na versão 3.8 ou superior**:
    ```bash
    python --version
4. **Crie e ative um ambiente virtual (opcional, mas recomendado para isolar as dependências do projeto)**:
    ```bash
   python -m venv venv
   venv\Scripts\activate # para Windows
   source venv/bin/activate # para Linux/MacOS
5. **Instale os pacotes necessários executando o comando abaixo**:
   ```bash
   pip install -r requirements.txt
6. **Execute o teste com o arquivo 'alltests.py'**:
   ```bash
   pytest alltests.py

### Abordagem da Aplicação

A aplicação foi abordada de forma a garantir a cobertura completa dos cenários de teste para a funcionalidade de identificação de triângulos, utilizando o Selenium WebDriver em conjunto com o framework de testes pytest. A solução automatizada abrange os seguintes pontos:

1. **Configuração Inicial**: Foi implementada uma fixture para configurar o ambiente de teste com o Selenium WebDriver. Essa fixture é executada uma vez por classe de teste, iniciando o navegador Chrome e acessando o site da aplicação para cada execução de teste.

2. **Cenários de Teste Parametrizados**:
   - **Triângulo Equilátero**: São testados triângulos com três lados iguais (por exemplo, 5, 5, 5), para garantir que a aplicação retorne a classificação "Equilátero".
   - **Triângulo Isósceles**: Triângulos com dois lados iguais (por exemplo, 5, 5, 8) são testados para garantir que a aplicação retorne "Isósceles".
   - **Triângulo Escaleno**: Testes para triângulos com todos os lados diferentes (por exemplo, 4, 5, 6) são realizados para validar a classificação "Escaleno".
   - **Validade dos Lados**: Um cenário de teste adicional verifica a validade dos lados do triângulo, assegurando que o comprimento de um lado seja sempre menor que a soma dos outros dois (propriedade fundamental dos triângulos). Caso os lados não formem um triângulo válido, o sistema não deve identificar nenhum tipo de triângulo e deve retornar uma mensagem de erro.

3. **Interação com a Aplicação**: Para cada teste, o código preenche os campos de entrada com os valores dos lados fornecidos, clica no botão "Identificar" e aguarda a resposta da aplicação. A validação é feita comparando o resultado obtido com o esperado, seja "Equilátero", "Isósceles", "Escaleno", ou uma indicação de erro para triângulos inválidos.

4. **Verificação de Erros**: O teste `test_triangulo_validade` verifica se o programa exibe corretamente uma mensagem de erro quando os lados fornecidos não formam um triângulo válido, aplicando as regras matemáticas de existência de triângulos (somatório dos lados).

5. **Execução do Teste**: Utilizando o pytest e o Selenium WebDriver, os testes são executados de forma automatizada. O código foi parametrizado para rodar múltiplos cenários com diferentes valores para os lados, testando tanto os casos válidos quanto os inválidos.

---

## Questão 10: Automação de Testes de API REST

Este repositório contém uma collection do Postman para testar a API fornecida.

**O que o script faz**:
1. Envia uma requisição POST à API para criar um novo produto ou recurso.
2. Extrai o ID do recurso criado, que é armazenado no banco de dados do Django.
3. Realiza uma requisição GET utilizando o ID retornado para validar a criação do recurso.
4. Fornece mensagens de erro claras caso algo não esteja de acordo com o esperado.

## Ferramentas Necessárias

Antes de começar, certifique-se de ter o Postman instalado:

**Postman**: Ferramenta para desenvolvimento, teste e automação de APIs.
   - [Baixe aqui](https://www.postman.com/downloads/)

### Como rodar os testes

1. **Suba o Serviço em Django Rest Framework para Teste (Containers Docker)**:
   Faça o clone do projeto:
   ```bash
   git clone https://github.com/Vanilton18/lojaapi.git
2. **Siga os passos descritos no arquivo README.md do repositório a partir da seção "Executar container API" para configurar e executar o serviço**.
3. **Clone este repositório em sua máquina local**:
   Abra um terminal e execute o comando abaixo para clonar o repositório:
   ```bash
   git clone https://github.com/gabriellvalle/FPFTechChallange.git.
3. **Abra o Postman e importe a collection `FPF Tech Challange.postman_collection`, localizada em na pasta 'question10'**.
4. No **Postman**, clique no ícone de configurações (⚙️) no canto superior direito e selecione **Manage Environments**. 
   Clique em **Add** para criar um novo ambiente e nomei-o como quiser.
   Adicione a seguinte variável ao ambiente:
   - **Key**: `product_id`
   - **Initial Value**: Deixe em branco.
   Torne o ambiente em ativo clicando em **Turn Active Environment**
5. Selecione a coleção **FPF Tech Challange** no painel esquerdo do Postman.
   Clique nos 3 pontos ao lado da coleção e selecione a opção **Run colletion**.
6. No **Collection Runner**, clique no botão **Run**.
   Acompanhe os resultados dos testes no painel de execução.

Os testes serão executados automaticamente para as requisições **POST** e **GET**.

### Testes Realizados

#### **POST /produtos/**
- **Objetivo**: Criar um produto e validar seu conteúdo.
- **Validações**:
  - A resposta contém os campos: `nome`, `preco`, `quantidade` e `categoria`.

#### **GET /produtos/{{product_id}}**
- **Objetivo**: Recuperar um produto específico utilizando o `ID`.
- **Validações**:
  - Os dados retornados correspondem aos dados enviados no **POST**.

### Observações
1. Certifique-se de que a API está rodando no mesmo ambiente e endpoint especificados na coleção.
2. Foi observado que a API não retorna o `ID` no método **POST**, pois esse campo não está especificado em fields do .ModelSerializer na aplicação Django. Uma opção seria adicionar o campo 'ID' para solucionar a interatividade e poder testar abrangemente os casos de teste no método GET.
3. Para contornar isto, foi utilizado um único caso de teste que determina estáticamente no script POST o valor do ID esperado pelo método GET.
4. Alterando-se os campos de Serializer, é possível recuperar o valor do ID do produto e adicionar este valor propriamente à variável 'product_id', que iterará corretamente na função GET.

---

## Questão 11: Script para Download, Descompactação e Organização de Arquivos

Este repositório contém o script completo para a **Questão 11** que realiza uma série de operações no Linux, como criar diretórios, baixar um arquivo, descompactá-lo e mover seu conteúdo para uma pasta específica. O objetivo é automatizar o processo de manipulação de arquivos comprimidos.

### O que o script faz:
1. Cria uma pasta com o seu nome (no caso, "gabrielvalle").
2. Dentro da pasta, cria outra pasta chamada "resultado".
3. Baixa o arquivo comprimido de um link fornecido ([https://vanilton.net/v1/download/zip.zip](https://vanilton.net/v1/download/zip.zip)).
4. Descompacta o arquivo na raiz da pasta com o seu nome.
5. Move o conteúdo descompactado para a pasta "resultado".
6. Exclui o arquivo comprimido após a descompactação e movimentação dos arquivos.

### Requisitos

Antes de executar o script, você precisa garantir que tem os seguintes requisitos no seu sistema:

- **Bash** (já vem com a maioria das distribuições Linux).
- **wget** (usado para fazer o download do arquivo).
- **unzip** (para descompactar o arquivo ZIP).

Para instalar as ferramentas necessárias (se não estiverem já instaladas), use os seguintes comandos:

```bash
sudo apt update
sudo apt install wget unzip
