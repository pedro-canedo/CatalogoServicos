<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=200px src="https://portal.unila.edu.br/proagi/ctic/imagens-ctic/banner-catalogo-servicos-v2.png/@@images/a96dc99c-88d2-4ca8-9bdc-ac36bb8a9912.png" alt="Project logo"></a>
</p>

<h3 align="center">Catálogo de Serviços</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Projeto feito em Django com PostgresSQL para controle de cadastro de Serviços.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
python 3.10 > | Docker 
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pip install -r requirements.txt
```

start the server with docker-compose

```
docker compose -f "docker-compose.yml" up -d --build

```

if you want to access the admin panel, you will need to create an admin account, for this just access the docker cli and run the following command.

```bash
python manage.py createsuperuser
```

Now you need to run a migration with the following command in your docker cli

```bash 
python manage.py migrate
```

Good, now restart your container with name webAppCatalogoServicos frist

```bash
docker restart webAppCatalogoServicos
```

Ok now the server is running on http://localhost:8000

<!-- End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example -->
<!-- ```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Web Framework
- [PostgresSQL](https://www.postgresql.org/) - Database
- [Docker](https://www.docker.com/) - Container



## ✍️ Authors <a name = "Pedro Augusto Canedo Araujo Obalhe"></a>

- [@pedro-canedo](https://github.com/pedro-canedo) - Idea & Initial work

See also the list of [contributors](https://github.com/pedro-canedo) who participated in this project.


- Hat tip to anyone whose code was used
- Inspiration
- References
