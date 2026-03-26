# Workshop API

API em **FastAPI** com CRUD básico de **usuários**, persistindo dados em **PostgreSQL** via `psycopg2`.

## Stack

- **Python**: 3.12+ (ver `pyproject.toml`)
- **API**: FastAPI
- **Servidor ASGI**: Uvicorn
- **Banco**: PostgreSQL

## Estrutura do projeto (alto nível)

- `src/routes/user.py`: define a aplicação FastAPI (`app`) e as rotas
- `src/controller/user.py`: funções de acesso ao banco (CRUD)
- `src/models/user.py`: modelo `User` (Pydantic)
- `src/db/connection.py`: conexão e helpers para PostgreSQL (`psycopg2`)

## Como rodar localmente

### Pré-requisitos

- Python **3.12+**
- PostgreSQL rodando localmente (ou acessível pela rede)

### Instalação (Poetry)

Se você ainda não usa Poetry:

```bash
pip install poetry
```

Instale as dependências:

```bash
poetry install
```

### Executar a API

O `app` está definido em `src/routes/user.py`. Para subir com reload:

```bash
poetry run uvicorn src.routes.user:app --reload
```

Por padrão o Uvicorn sobe em `http://127.0.0.1:8000`.

### Swagger / OpenAPI

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Banco de dados

O acesso ao banco é feito em `src/controller/user.py` via `PostgreSQLConnection(...)`.

Atualmente, o código usa credenciais fixas:

- **dbname**: `postgres`
- **user**: `myuser`
- **password**: `mypassword`
- **host**: `localhost`
- **port**: `5432`

Para rodar sem erro, garanta que exista um usuário/banco compatível no seu Postgres, e que exista uma tabela `users`.

### Tabela esperada (referência)

Pelos campos usados nos inserts/updates, a tabela deve conter (no mínimo) estas colunas:

- `id` (int)
- `name` (text/varchar)
- `area` (text/varchar)
- `job_description` (text/varchar)
- `role` (int)
- `salary` (numeric/float)
- `is_active` (boolean)
- `last_evaluation` (text/varchar ou date/timestamp)

## Endpoints

As rotas estão em `src/routes/user.py`.

### Buscar usuário por id

`GET /users/{user_id}`

Exemplo:

```bash
curl -s http://127.0.0.1:8000/users/1
```

### Criar usuário

`POST /users/`

Body (exemplo):

```json
{
  "id": 1,
  "name": "Renan",
  "area": "Engenharia",
  "job_description": "Backend",
  "role": 1,
  "salary": 10000.0,
  "is_active": true,
  "last_evaluation": "2026-03-26"
}
```

Exemplo:

```bash
curl -s -X POST http://127.0.0.1:8000/users/ ^
  -H "Content-Type: application/json" ^
  -d "{\"id\":1,\"name\":\"Renan\",\"area\":\"Engenharia\",\"job_description\":\"Backend\",\"role\":1,\"salary\":10000.0,\"is_active\":true,\"last_evaluation\":\"2026-03-26\"}"
```

### Atualizar usuário

`PUT /users/{user_id}`

Exemplo:

```bash
curl -s -X PUT http://127.0.0.1:8000/users/1 ^
  -H "Content-Type: application/json" ^
  -d "{\"id\":1,\"name\":\"Renan Rodrigues\",\"area\":\"Engenharia\"}"
```

### Remover usuário

`DELETE /users/{user_id}`

Exemplo:

```bash
curl -s -X DELETE http://127.0.0.1:8000/users/1
```

## Notas

- Este repositório contém uma pasta `venv/` no workspace. Em geral, **não é recomendado versionar** ambiente virtual no GitHub. Considere adicionar `venv/` no `.gitignore` antes de publicar.
