# Dados Abertos do Banco Central do Brasil (APIs)

Serviços de Consulta a API dos Dados Abertos do Banco Central do Brasil, utilizando Python.

https://dadosabertos.bcb.gov.br/.

## Serviços

- Dólar Comercial (Venda e Compra) - Cotações Diárias (
[URL](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios) ,
[Recursos](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos) ,
[Swagger](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/swagger-ui3#/) ,
[Documentação](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao)
)

### Moedas (Currency Service)

##### Exemplo de Uso

```Python
currency_service = CurrencyService()
currencies = currency_service.get_all()
```

### Dólar Comercial - Venda e Compra (PTAX Service)

##### Exemplo de Uso

```Python
ptax_service = PTAXService()
ptax = ptax_service.get_ptax_rate(date(2024, 1, 2))
ptax_list = ptax_service.get_daily_ptax_rate_by_period(date(2024, 1, 2), date(2024, 1, 5))
```

### Taxas de Câmbio (Exchange Rate Service)

##### Exemplo de Uso

```Python
currency_code = "CAD"
exchange_rate_service = ExchangeRateService()
exchange_rate = exchange_rate_service.get_exchange_rate(currency_code, date(2024, 1, 1))
exchange_rates = exchange_rate_service.get_daily_exchange_rate_by_period(currency_code, date(2024, 8, 1), date(2024, 8, 2))
```
