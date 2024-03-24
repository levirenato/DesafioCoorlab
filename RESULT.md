# Resultado - Desafio CoorLab

Olá a todos, primeiro, agradeço pela oportunidade. Estou ansioso pelas próximas etapas. Abaixo estão as ferramentas que utilizei para solucionar a problemática:

OBS: No arquivo `run.sh`, na linha 10, há o comando para instalar o ambiente virtual `virtualenv`. Entretanto, em sistemas Manjaro, como é o meu caso, existe um bug que impede a instalação usando o pip. Para contornar esse problema, é necessário adicionar a flag `--break-system-packages`. No entanto, como o sistema a ser utilizado é o Ubuntu, acredito que não haverá problemas, então removi a flag no último commit. Contudo, se ocorrer algum erro como "error: externally-managed-environment", basta utilizar a solução mencionada acima.

[Mais informações sobre o bug](https://forum.manjaro.org/t/managing-python-packages-on-manjaro-error-with-externally-managed-environment/144149)


### frontend: http://localhost:8080/
### backend:  http://localhost:3000/



## Considerações

- **Vue.js 3:** Utilizei o Vue.js 3 conforme solicitado, aproveitando os recursos avançados desta framework. Trabalhar com essa ferramenta é sempre surpreendente, pois é muito completa e tem excelente performance.

- **PrimeVue:** Optei pelo PrimeVue, uma biblioteca de componentes Vue.js open-source, devido ao estilo e flexibilidade dos componentes oferecidos.

- **SQLite:** Utilizei o banco de dados SQLite para a solução, devido à sua natureza leve e portátil. Populei o banco e utilizei a API para extrair os dados necessários.

- **FastAPI:** No backend, escolhi o FastAPI pela sua alta performance e facilidade de uso. Apesar de parecer contra intuitivo em alguns casos, como ganho de produtividade, o FastAPI pode ser uma escolha melhor em relação ao Django. Para atingir os objetivos da melhor forma, mantive as "RESTful API Best Practices".

- **SQLAlchemy:** Utilizei o SQLAlchemy como ORM (Object-Relational Mapper) para facilitar a interação com o banco de dados SQLite. Não há segredo aqui, o SQLAlchemy é a principal ORM quando se trata de Python. Apesar da excelente concorrente SQLModel, criada pelo mesmo desenvolvedor do FastAPI, o SQLAlchemy oferece muitos recursos que aumentam a produtividade.

A palavra-chave é *produtividade*. Essa combinação de ferramentas é uma excelente escolha em casos como este. Claro, tudo depende do contexto. Mesmo assim, acredito que até em casos de escalabilidade, possivelmente apenas a troca do banco de dados poderá ser necessária.
