# 🐍 Python Backend — CEP Service (TDD + Clean Architecture)

Projeto desenvolvido com foco em **boas práticas de backend profissional**, utilizando **TDD (Test Driven Development)** desde o início.

Este serviço implementa a consulta de CEP utilizando a API do ViaCEP, com tratamento de erros, validação de entrada e isolamento de dependências externas.

---

## 🚀 Objetivo

Demonstrar habilidades em:

- Desenvolvimento backend com Python
- Testes automatizados com TDD
- Integração com APIs externas
- Tratamento de erros e resiliência
- Organização de código em camadas
- Boas práticas utilizadas em ambientes corporativos

---

## 🧱 Tecnologias e ferramentas

- Python 3.12+
- pytest (testes)
- requests (HTTP client)
- python-dotenv (.env)
- unittest.mock (mock de dependências externas)

---

## 📁 Estrutura do projeto

```
app/
├── core/
│   └── config.py          # Configurações via .env
├── exceptions/
│   └── cep_service_error.py  # Exceções customizadas
├── services/
│   └── api_service.py     # Lógica principal de negócio

tests/
└── test_api_service.py    # Testes automatizados
```

---

## 🧠 Abordagem: TDD (Test Driven Development)

O projeto foi desenvolvido seguindo o ciclo:

1. Escrever o teste (falhando)
2. Implementar o mínimo para passar
3. Refatorar com segurança

### Exemplos de cenários testados:

- ✅ Montagem correta da URL
- ✅ Resposta de sucesso da API
- ✅ Erro HTTP (status != 200)
- ✅ Timeout da requisição
- ✅ Validação de CEP inválido
- ✅ Garantia de que a API não é chamada com input inválido

---

## 🔐 Validação e Resiliência

O serviço valida o CEP antes de qualquer chamada externa:

- Apenas números
- Exatamente 8 dígitos

Isso evita chamadas desnecessárias e aumenta a robustez do sistema.

---

## ⚠️ Tratamento de erros

O projeto utiliza exceções customizadas:

```python
class CepServiceError(Exception):
    pass
```

Casos tratados:

- Timeout da API
- Resposta inválida
- CEP inválido

---

## 🧪 Testes

Para rodar os testes:

```bash
pytest
```

O projeto utiliza mocks para evitar dependência de API externa:

```python
@patch("app.services.api_service.requests.get")
```

---

## 🌍 Variáveis de ambiente

Crie um arquivo `.env`:

```
VIA_CEP_BASE_URL=https://viacep.com.br/ws
```

---

## 📌 Exemplo de uso

```python
from app.services.api_service import get_cep

result = get_cep("01001000")
print(result)
```

---

## 💡 Diferenciais do projeto

- TDD aplicado desde o início
- Mock de dependências externas (testes isolados)
- Validação de entrada antes de integração
- Exceções customizadas (evita uso de Exception genérica)
- Código organizado em camadas
- Pronto para evoluir para FastAPI

---

## 🚀 Próximos passos (em evolução)

- [x] Implementar FastAPI
- [x] Adicionar tipagem com Pydantic/TypeDict
- [x] Logging estruturado
- [ ] Dockerização
- [ ] CI/CD com GitHub Actions

---

## 👨‍💻 Autor

Alexandre Pellegrino
Fullstack Developer (React | Flutter | Python em evolução)

---

## 🧠 Observação

Este projeto faz parte de um roadmap focado em backend Python moderno, com ênfase em:

- Integrações
- Automação
- Arquitetura limpa
- APIs robustas
- Engenharia de software aplicada

---
