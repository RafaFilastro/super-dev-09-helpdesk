# Entidade não existe
- model
- alembic
- repository
- schema
- service
- controller
- main.py

# Entidade existe adcionar método
- repository (opcional)
- schema (representação do que vem do front ou do que retornarnamos para o front)
- service
- controller


# Executar o projeto
- precisa estar na pasta api
- cd ./api
- `uvicorn app.main:app --reload`


# Ativar ambiente virtual
- `source .venv/bin/activate`

# Cria um projeto angular, -- directrory significa na propia pasta, --skip-git não inicializa um repo git, --style configura como scss, --routing deixa configurado para multiplas rotas
- `ng new helpdesk --directory . --skip-git --style=scss --routing`
- `N`
- `None`

# Para iniciar o projeto angular
- `ng serve`

# Gerar o componente listar
- `ng g c tickets/listar`

# Gerar o componente detalhes
- `ng g c tickets/detalhes`

# Gerar a navbar
- `ng g c navbar `

# Gerar o service do ticket
- `ng g s ticket.service`

# Passos para Front-end
- `Criar o componente`
- `Adcionar rota no app.route`
- `Adcionar link(routerlink) na lista para tela de criar`
- `Criar model`
- `Criar service`
- `Componente`
    `Implementar o ts`
    `Implementar o html`
