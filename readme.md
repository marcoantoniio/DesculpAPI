<h1 align="center">DesculpAPI</h1>

<p align="center">
Esta aplicação utiliza o <a href="https://github.com/hotheadhacker/no-as-a-service">No-as-a-Service</a> para gerar desculpas engraçadas em português.
</p>

---

## Descrição

DesculpAPI foi desenvolvido com o intuito de gerar risadas com **desculpas esfarrapadas** em português de forma simples e divertida.  

## Como rodar o projeto

```bash
# Clone o repositório
git clone https://github.com/marcoantoniio/DesculpAPI.git
cd DesculpAPI

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # .venv\Scripts\activate se estiver utilizando Windows

# Instale as dependências
pip install -r requirements.txt

# Configure sua chave da OpenAI no ambiente
crie um .env e coloque a URL da API do no-as-a-service dentro desse arquivo
NAAS="URL_DA_API"

# Rode a aplicação
execute o main.py
```
## licença
GPL-3.0

Todos os créditos para [Salman Qureshi](https://github.com/hotheadhacker) e sua API.



