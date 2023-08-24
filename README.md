# oasisbr-scraper



## Uso

### Realizando consulta na API

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
