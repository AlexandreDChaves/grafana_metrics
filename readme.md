Guia de Configuração e Execução do Projeto com InfluxDB, Grafana e Python.

Introdução

Este guia explica como configurar e executar um projeto de monitoramento de métricas de sistema usando InfluxDB, Grafana, e um script Python que coleta informações como uso de CPU, memória, disco e rede. As métricas são gravadas no InfluxDB, e os dados são visualizados em dashboards no Grafana.

Ferramentas necessárias:

    InfluxDB: Um banco de dados de séries temporais.
    Grafana: Uma plataforma de visualização de métricas.
    Python: Usado para coletar e enviar métricas para o InfluxDB.
    Psutil: Biblioteca Python para coleta de métricas do sistema.
    
    1. Configuração no Ubuntu
Passo 1: Instalar o InfluxDB

    Adicione a chave GPG para o InfluxDB:
    curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -

Adicione o repositório:
echo "deb https://repos.influxdata.com/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

Instale o InfluxDB:
sudo apt update
sudo apt install influxdb

Inicie o serviço do InfluxDB:
sudo systemctl start influxdb
sudo systemctl enable influxdb

Verifique se o InfluxDB está rodando:
sudo systemctl status influxdb

Acesse o InfluxDB CLI:
influx

Dentro do CLI, crie o banco de dados:
CREATE DATABASE system_metrics;

Crie um usuário para o banco de dados:
CREATE USER metrics_user WITH PASSWORD 'your_password' WITH ALL PRIVILEGES;


Passo 2: Instalar o Grafana

Adicione o repositório Grafana:
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"

Instale o Grafana:
sudo apt update
sudo apt install grafana

Inicie o serviço do Grafana:
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

Acesse o Grafana no navegador em http://localhost:3000. O login padrão é admin/admin.


Passo 3: Configurar o Python

Instale o Python e as bibliotecas necessárias:
sudo apt install python3-pip
pip3 install psutil influxdb

Crie um arquivo Python chamado monitor_metrics.py e adicione o código fornecido.
Execute o script:
python3 monitor_metrics.py

O script coleta as métricas e envia para o InfluxDB.

