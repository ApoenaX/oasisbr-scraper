# oasisbr-scraper

Ferramenta para obter informações do Portal Brasileiro de Publicações e Dados Científicos em Acesso Aberto.

## Instalação

```sh
pip install git+https://github.com/AcademicAI/oasisbr-scraper.git

```

## Biblioteca Python

### Busca simples

Essa ferramenta permite passar parâmetros usados na chamada da API da Oasisbr. Abaixo um exemplo onde pedimos para retornar os 5 primeiros resultados de teses e dissertações ordenados por relevância.

```python
from oasisbr_scraper.api import oasis_api

data = oasis_api.access_endpoint(
    "search",
    {
        "type": "AllFields",
        "filter[]": ["~format:masterThesis", "~format:doctoralThesis"],
        "sort": "relevance",
        "page": 1,
        "limit": 5,
        "lng": "pt-br"
    }
)
print(data)
```
