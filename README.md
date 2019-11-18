
![radartona](https://github.com/guica/api_dados_radar/blob/master/media/admin-interface/logo/75125107_2420153768241552_3174633533629005824_o.png?raw=true)
# API para Dados de Radares

## Apresentação

### API Swagger
![apresentacao](https://github.com/guica/api_dados_radar/blob/master/media/Swagger-UI.gif)

#### Funcionalidades
- Saídas em JSON, XML e CSV
- Versionamentode API (v1,v2,...)
- Autenticação com Token
- Log de controle de armazenamento
- Paginação
- Throttle/Rate Limiting
- Filtros e ordenação
- Cache
- API das bases: radares, contagem, trajetos

### Interface Frontend Dashboard
![dash](https://github.com/guica/api_dados_radar/blob/master/media/Dash.gif)

#### Funcionalidades
- Navegação com Mapa
- Interação com mapa para saber endereços e fluxo de contagem de veículos ao longo do dia
- Filtros dinâmicos de Lote, quantidade de faixasm velocidade
- Saiba pontos de congestionamento, vias com maior fluxo e radares com maiores e menores índices de infração

### Interface Frontend CRUD
- Cadastramento de usuário
- Permissões e Grupos de acesso (administrador, outros)
- Auto Cadastramento

### DevOps
- Protocolo HTTPS
- Agnóstica a plataforma, multiplataforma, roda em windows, linux e Mac
- Serviço funciona em banco SQL (postgres, mysql ou sqlite) ou NoSQL (mongoDB)


Slides - https://docs.google.com/presentation/d/1Wh3uLDF66x8tkwyF42uuZY1rVi9e6LFNCizsGW94UvQ/edit?usp=sharing


## Acesso para o Ambiente de homologação

API - http://radartona.portalretina.com/docs/

Front CRUD - http://radartona.portalretina.com/admin/

Front Dashboard - http://radartona.portalretina.com:8050/

`Usuário`: admin
`Senha`: admin

## Começando

Essas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste. Consulte implantação para obter notas sobre como implantar o projeto em um sistema em ambiente de produção.

### Pré-requisitos

-   Docker
-   docker-compose

Install  [Docker](https://docs.docker.com/engine/installation/)  and  [Docker compose](https://docs.docker.com/compose/install/)

### Instalando
Clone o repositório e entre no seu diretório

`git clone https://github.com/guica/api_dados_radar.git`

`cd api_dados_radar`

Crie um arquivo .env:

`touch .env`

Construa a imagem em Docker, suba o container e entre nele

`sudo docker-compose build`

`sudo docker-compose up -d`

`sudo docker-compose exec web bash`

Crie um super-usuário:

`python manage.py createsuperuser`

Entre em http://localhost/admin e faça seu login. 
Você pode usar essa interface para navegar e explorar os dados. 

API - http://localhost/docs/

Front CRUD - http://localhost/admin/

Front Dashboard - http://localhost:8050/


## Arquitetura

### [MTV](https://towardsdatascience.com/working-structure-of-django-mtv-architecture-a741c8c64082) (Model, View e Template) estrutura de componentização no framework Django
![mvt](https://miro.medium.com/max/1200/0*8ZFh-CsrMi7bQG0O.jpg)

### UML do Banco de Dados
![apresentacao](https://github.com/guica/api_dados_radar/blob/master/media/uml.png)


## TODO

- Melhorar Segurança (integrar OAuth 2.0, HTTPS, Logs de uso e Throttle)
    - Logs (check)
    - throttle (check)
    - OAuth 2.0
    - HTTPS
- Testes Automáticos
- Melhorar Escalabilidade (testes de estresse na solução)
- Estruturação de dados (descrições dos parâmetros, rever estrutura de dados e sanity checks)

## Contruido com

* Python 2.7
* [Django](https://www.djangoproject.com/) 1.11.8
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Docker](https://www.docker.com/)
* Docker-Compose
* Celery
* Nginx
* Postgres
* Sqlite3
* Redis
* Dash

## Autores

* **Guilherme Camargo**  - [LinkedIn](https://www.linkedin.com/in/guilherme-camargo-82029b142/)

* **Paulo Henrique da Silveira** - [LinkedIn](https://www.linkedin.com/in/phsilveira/)

## License

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
