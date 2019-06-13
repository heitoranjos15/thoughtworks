#Guide Galaxy

### Descrição Funcional

    Esse script tem como finalidade fazer anotações das conversões dos sistemas unitarios Galaxy e o Romano, e as transações já realizadas. Sendo possível prever novas transações.

### Arquitetura
    .
    ├── src            
        ├──errors      # Guarda as exceções customizadas do script.
        ├──logic       # Recebe a mensagem do usuário, e faz todo o fluxo necessário para executar/obter a resposta.
        ├──numeral     # Todas as tratativas de conversão para os sistemas unitários ficam nesta pasta.
        └──materials   # Faz a trativas do material que é usado para obter credits.
    ├──tests           # Testes Unitários de toda a aplicação
    ├──guide_galaxy    # Inicializador do script, nele possui todos os fluxos de acordo com a mensagem recebida, e as mensagem                         de inicialização.
    └──requirements    # Todas as bibliotecas utilizadas.

### Executar o Script

    - 1º Passo
        Abra o cmd, indique o caminho que está a pasta do script.
    
    - 2º Passo
        Dentro do cmd, digite a seguinte mensagem.
        ```bash
            python guide_galaxy.py
        ```
        O script será incializado.

### Tests

    - 1º Passo
        Abra o cmd, indique o caminho que está a pasta do script.

    - 2º Passo
        Dentro do cmd, digite a seguinte mensagem.
        ```bash
            pip install virtualenvwrapper-win
            mkvirtualenv guide_galaxy
            workon guide_galaxy
            pip install -r requirements.txt
            pytest
        ```

