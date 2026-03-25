# Python Backend - CEP Service (FastAPI + TDD)

API para consulta de CEP usando ViaCEP, com validacao de entrada, tratamento de erros e testes automatizados.

## Objetivo

Este projeto demonstra:

- desenvolvimento de API com FastAPI
- arquitetura em camadas (rota, servico, excecoes, schema)
- TDD com pytest
- isolamento de chamadas externas com `unittest.mock`

## Stack

- Python 3.12+
- FastAPI
- Uvicorn
- Requests
- Pytest
- python-dotenv

## Estrutura

```text
app/
  api/
    handlers/cep_handler.py     # Handler global para CepServiceError
    routes/cep.py               # Endpoint /cep/{cep}
  core/config.py                # Config de ambiente
  exceptions/cep_service_error.py
  schemas/cep_data.py           # Tipagem do retorno
  services/api_service.py       # Regras de negocio e integracao ViaCEP
  main.py                       # App FastAPI
tests/
  test_api_service.py
  test_cep_route.py
  test_parse_cep_response.py
```

## Configuracao

1. Copie o arquivo de exemplo:

```powershell
Copy-Item .env.example .env
```

2. Defina no `.env`:

```env
VIA_CEP_BASE_URL=https://viacep.com.br/ws
```

## Como rodar

Com ambiente virtual ativo:

```bash
uvicorn app.main:app --reload
```

Documentacao interativa:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Endpoint

### `GET /cep/{cep}`

Exemplo:

```bash
curl http://127.0.0.1:8000/cep/01001000
```

Resposta de sucesso (`200`):

```json
{
  "cep": "01001-000",
  "logradouro": "Praca da Se"
}
```

Possiveis erros:

- `400`: CEP invalido (nao numerico ou diferente de 8 digitos)
- `504`: timeout ao consultar ViaCEP
- `502`: falha geral de integracao (status nao 200 ou resposta invalida)

## Testes

Rodar todos os testes:

```bash
pytest -q
```

Rodar apenas testes da rota:

```bash
pytest tests/test_cep_route.py -q
```

## Notas de qualidade

- validacao do CEP antes de chamar API externa
- logs para erros de timeout, resposta invalida e falha de integracao
- retorno padronizado de erro via handler global (`CepServiceError`)
