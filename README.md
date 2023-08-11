# Automação: TDD, BDD, Github, CI, CD, Cucumber, Codecov e AWS S3 com Ambientes de Desenvolvimento (dev, prod)
O objetivo desse exemplo é utilizar as práticas já aprendidas de TDD e BDD (Cucumber) para automatizar ambientes de dev e produção (Github), levantar cobertura de testes (CI e codecov) e enviar, caso tudo esteja correto, para um ambiente de produção (CD e AWS S3).

## Passo 1 - Configuração de repositórios Github
Criar brachs de dev e prod fazendo as configurações de push necessárias.

## Passo 2 - Criar teste utilizando TDD e BDD: mesmo exemplo da calculadora.

## Passo 3 - Criação de pipeline CI com Cucumber
Na pasta "/.github/workflows" para reconhecimento do Github que a pipeline deve ser executada seguindo regras definidas a seguir:

```
    name: Testes Automatizados  # Nome do fluxo de trabalho
  
    on: [push]  # Disparar o fluxo de trabalho quando houver push no repositório
    
    jobs:
      testes:
        name: Testes BDD  # Nome da tarefa "testes"
    
        runs-on: ubuntu-latest  # Define o sistema operacional em que os testes serão executados
    
        steps:
        - name: Checkout do código  # Nome da etapa: Faz checkout do código do repositório
          uses: actions/checkout@v2  # Usa a ação de checkout da versão 2
    
        - name: Configurar ambiente Python  # Nome da etapa: Configura o ambiente Python
          uses: actions/setup-python@v2  # Usa a ação para configurar o Python
          with:
            python-version: '3.x'  # Especifica a versão do Python a ser usada
    
        - name: Instalar dependências  # Nome da etapa: Instala as dependências do projeto
          run: pip install behave  # Executa o comando para instalar o Behave
    
        - name: Executar testes com Behave  # Nome da etapa: Executa os testes com o Behave
          run: behave  # Comando para executar os testes com o Behave
```
Fazer testes de pull request no github mostrando como um CI deve funcionar usando o esquema de branchs criado.
Ok, garatimos que os testes estão passando e que esta tudo correto com eles mas como eu garanto que TODO meu código esta testado?

## Passo 4 - Cobertura de código (codecov)
O codecov é uma ferramenta que se integra ao Github para fornecer relatórios de cobertura de testes fornecendo insights sobre áreas do código que não estão bem testadas.
1. Entrar na plataforma com o github e autorizar o codecov: https://about.codecov.io
2. Encontrar o repositório do projeto dentro do codecov e configurar repositório.
3. Um código será fornecido pelo codecov. Esse código deve ser inserido dentro dos "secrets" do Github pois NÃO DEVE SER COMPARTILHADO.
4. Voltamos ao projeto e vamos configurar ele para que os testes sejam enviados ao codecov

  ```
  pip install coverage
  ```

O package coverage irá criar, com base nos testes do Cucumber (behave), um arquivo de cobertura de código:
  ```
  coverage report -> breve report no command line
  ```
  ```
  coverage html -> gera um html de cobertura de código para disponibilizar online
  ```
  ```
  coverage run -m behave -> comando que gera o arquivo com base no behave
  ```

Agora vamos atualizar nossa pipeline para enviar esse relatório para o codecov analisar:
  ```
  - name: Executar behave e criar relatório de cobertura
      run: coverage run -m behave

    - name: Upload relatório de cobertura para o Codecov
      uses: codecov/codecov-action@v3
      env:
        CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
  ```

Depois do teste rodar no Github Action, podemos visualizar a cobertura dele no site do codecov.

## Passo 5 - Pipeline de CD para AWS S3
1.  Criar um bucket no S3
2.  Criar access key (serve para acessarmos a AWS remotamente) na AWS: Serviço "IAM" -> Usuários -> Selecione seu usuário -> Credenciais de segurança -> Create access key
3.  Configurar secrets com a chave criada da AWS no Github: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION.
4.  Criar pipeline de CD:
   ```
   name: Deploy to S3  # Nome do fluxo de trabalho

    on:
      push:
        branches:
          - prod  # Disparar o fluxo de trabalho quando houver push na branch "prod"
    
    jobs:
      deploy:
        runs-on: ubuntu-latest  # Define o sistema operacional em que o deploy será executado
    
        steps:
          - name: Checkout code  # Nome da etapa: Faz checkout do código do repositório
            uses: actions/checkout@v2  # Usa a ação de checkout da versão 2
    
          - name: Configure AWS credentials  # Nome da etapa: Configura as credenciais da AWS
            uses: aws-actions/configure-aws-credentials@v1  # Usa a ação para configurar as credenciais da AWS
            with:
              aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}  # Configura a chave de acesso da AWS
              aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}  # Configura a chave secreta de acesso da AWS
              aws-region: ${{ secrets.AWS_REGION }}  # Configura a região da AWS
    
          - name: Sync files to S3  # Nome da etapa: Sincroniza arquivos com o S3
            run: aws s3 sync . s3://testeautomatizado1 --delete --exclude ".github/*"  # Comando para sincronizar arquivos com o S3, excluindo a pasta ".github"
   ```
Demonstração do CD funcionando apenas em PROD
