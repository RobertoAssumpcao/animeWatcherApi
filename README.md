<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
  <h1 align="center">Anime Watcher</h1>
  <h2>Back End</h2>

  <p align="center">
    <a href="https://github.com/RobertoAssumpcao/animeWatcherApi/issues">Report Bug</a>
    ·
    <a href="https://github.com/RobertoAssumpcao/animeWatcherApi/issues">Request Feature</a>
  </p>
</div>

## About

O objetivo deste projeto é registrar **animes assistidos**, permitindo o gerenciamento pessoal de quais animes foram vistos, com dados como título, gênero, número de episódios e status de visualização (ex: "Assistido", "Assistindo", "Planejo ver").

Este projeto faz parte de um MVP que explora arquitetura baseada em componentes/microsserviços, utilizando Flask com banco de dados SQLite.

## Como usar

1. **Clone o repository:**

   ```bash
   git clone https://github.com/RobertoAssumpcao/animeWatcherApi.git
   ```

2. **Navegue até o diretório do projeto:**

   ```bash
   cd animeWatcherApi
   ```

> ⚠️ O desenvolvimento foi feito usando o sistema operacional WSL2 ubuntu. Dependendo do seu sistema operacional, a maneira de instalar e ativar o ambiente virtual pode mudar. Em caso de dúvida, consulte os [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

3. **Criar o ambiente virtual**

   ```bash
   python3 -m venv .venv
   ```

4. **Ativar o ambiente virtual**

   ```bash
   source .venv/bin/activate
   ```

5. **Instalar as dependências**

   ```bash
   pip install -r requirements.txt
   ```

6. **run a API:**

   ```bash
   flask run --host 0.0.0.0 --port 5000
   ```

   OR

   ```bash
   flask run --host 0.0.0.0 --port 5000 --reload
   ```

> Este segundo comando reiniciará automaticamente o servidor após uma alteração no código-fonte.

Para atualizar o requirements.txt

   ```bash
   pip freeze > requirements.txt
   ```

## Contribuição

Contribuições são o que fazem a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

Se você tiver uma sugestão que possa melhorar este projeto, por favor, faça um fork do repositório e crie um pull request. Você também pode simplesmente abrir uma issue. Não se esqueça de dar uma estrela ao projeto! Muito obrigado!

1. Faça um fork do projeto
2. Crie sua Branch de Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça o push da sua Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

<p align="right">(<a href="#top">voltar ao topo</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/RobertoAssumpcao/animeWatcherApi.svg?style=for-the-badge

[contributors-url]: https://github.com/RobertoAssumpcao/animeWatcherApi/graphs/contributors

[issues-shield]: https://img.shields.io/github/issues/RobertoAssumpcao/animeWatcherApi.svg?style=for-the-badge

[issues-url]: https://github.com/RobertoAssumpcao/animeWatcherApi/issues