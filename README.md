# Projeto Aula1008

## Sobre
Este é um projeto Django de loja simples com uma página inicial e um carrinho. O projeto salva compras em um banco SQLite e mostra os itens do carrinho na interface.

## Estrutura principal
- `manage.py` - comando principal do Django.
- `loja2/` - configurações do projeto Django.
- `loja_inicial/` - app responsável pela página inicial da loja.
- `carrinho/` - app responsável por exibir o carrinho de compras.
- `db.sqlite3` - banco de dados SQLite usado em desenvolvimento.

## Funcionalidades
- Página inicial da loja (`/` ou `/home/`).
- Página do carrinho (`/carrinho/`) exibindo as compras salvas.
- Renderização de templates em `loja_inicial/templates/home/` e `carrinho` usando `Compras` do modelo.

## Requisitos
- Python 3.x
- Django 6.1

## Como executar
1. Ative o ambiente virtual se existir.
2. Instale dependências se necessário:
   ```bash
   pip install django
   ```
3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
4. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
5. Acesse no navegador:
   - `http://127.0.0.1:8000/` para a loja
   - `http://127.0.0.1:8000/carrinho/` para o carrinho

## Observações
- O projeto utiliza `sqlite3` para desenvolvimento.
- O `DEBUG` está ativado em `loja2/settings.py`, então não use em produção.
