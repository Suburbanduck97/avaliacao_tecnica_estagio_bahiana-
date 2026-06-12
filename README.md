# Avaliação Técnica — Parte 1 e Parte 2

## Descrição

Este repositório contém a solução desenvolvida para a avaliação técnica proposta.

O projeto está dividido em duas partes:

* **Parte 1:** Implementação da solução utilizando Python 3.
* **Parte 2:** Resolução das consultas SQL solicitadas.

---

## Estrutura do Projeto

```plaintext
AVALIACAOTECNICA/
├── avaliacaoInovate.sql
├── parte1.py
└── README.md
```

---

## Tecnologias Utilizadas

### Parte 1

* Python 3

### Parte 2

* SQL
* Banco testado: PostgreSQL

---

## Dependências

### Parte 1

Nenhuma dependência externa foi necessária.

---

## Como Executar

### Parte 1

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd AVALIACAOTECNICA
```

Execute:

```bash
python parte1.py
```

Para ambientes online, basta copiar o conteúdo do arquivo:

```plaintext
parte1.py
```

e executar no interpretador correspondente.

---

### Parte 2 — Banco de Dados

O arquivo SQL foi desenvolvido com foco em compatibilidade com ambientes SQL online.

Execute o script:

```plaintext
avaliacaoInovate.sql
```

Caso utilize bancos como MySQL ou SQL Server, opcionalmente crie o banco antes:

```sql
CREATE DATABASE IF NOT EXISTS avaliacaoInovate;

USE avaliacaoInovate;
```

Para PostgreSQL, crie o banco pela ferramenta utilizada e execute o script sem os comandos acima.

O script realiza:

* Criação das tabelas;
* Definição dos relacionamentos;
* Inserção dos dados;
* Execução das consultas solicitadas.

---

## Consultas Implementadas

### Questão 1

Retorna:

* ID da compra;
* Nome do produto;
* Quantidade;
* Preço unitário;
* Valor total da compra.

### Questão 2

Retorna:

* Produto mais vendido;
* Quantidade total comprada.

### Questão 3

Retorna:

* Todos os produtos cadastrados;
* Quantidade total comprada por produto;
* Inclusão de produtos sem compras registradas.

---

## Observações

* As consultas foram desenvolvidas utilizando SQL padrão.
* O projeto pode ser executado em ferramentas SQL online ou localmente.
