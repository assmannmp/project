1 - Instalação Necessárias e Configurações
	Algumas instalações e configurações que devem ser realizadas no sistema operacional para que seja necessário a execução do projeto. Estas estação são referentes ao sistema operacional Linux/Ubuntu.
Instalações:
  sudo apt-get install python3.6
  sudo apt-get install python3.6-dev
  sudo apt-get install python3.6-venv
	Foi usado a IDE Pycharm para depuração do sistema.
Configurações:
	Deve ser criado um diretório com o nome que desejar e para abri-lo com os seguintes comandos:
  mkdir nome
cd nome
	Tem que criar uma virtual venv nesta pasta e ativá-la com os seguintes comandos:
    python3 -m venv venv
    source venv/bin/activate
  Instalações do Python:
    pip install -r requirements-dev.txt

Execução do comando no Terminal da IDE Pycharm:
	Deve-se abrir a IDE Pycharm, ir em file/Open e buscar a pasta criada na seção: 1 -Instalação Necessárias e Configurações/Configurações, no terminal da IDE deve ser executado os comando da seção: 1 -Instalação Necessárias e Configurações/Configurações  da ativação da virtual venv. E agora deve-se ser executado o seguintes comando no terminal da IDE com a virtual venv ativada e dentro da pasta “project”:
	Para o execução no terminal:
    python server.py localhost:3000
