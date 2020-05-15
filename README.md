# JWTAuthCore

Este projeto é uma API para controle de usuários de uma aplicação, feito em Django.
A Autenticação é feita no modelo Central Authentication Service (CAS)

Na aplicação jwtauthcore tem o serviço de autenticação e cadastro de usuários.
Na aplicação test_application é apresentada uma aplicação de teste para a autenticação,
com um backend de autenticação que requisita a validação do usuário para a primeira aplicação


### Instalação:

1) instalar requirements.txt
```
pip install -r requirements.txt
```

2) Criar os arquivos .env em ambas as aplicações com os dados de conexão ao banco de dados

3) entrar na jwtauthcore e aplicação migrações
```
python manage.py migrate
```

Para testar abasta rodar runserver na jwtauthcore com a porta 5009 e test_application com a porta 5008


TODO: Tacar o Docker...
