# database-essentials

### cria projeto django, observar db.sqlite com DB Browser, criar superuser 
* cria projeto em Pycharm
* migra `py manage.py migrate
* abre com DB Browser o ficheiro .sqlite3
* observa a estrutura da base de dados
* cria `py manage.py createsuperuser`
* ve na base de dados que foi registado
* ve migrations
*
### criar aplicação e Model Simple, makemigratinos e migrate
* cria aplicação example
* cria modelo apenas com atributo text
* regista em settings a aplicação
* makemigrations, e observa instrução para criar modelo Simple
* se formos a migrations e abrirmos ficheiro 0001_initial.py, este tem instruções para modificar a base de dados. vemos instrução para criar modelo, com atributos/colunas id (pk) e text
* migrate executa
* observa em DB Browser nova tabela example_simple, example nome da app e simple da tabela
* se formos a INSTALLED_APPS vemos que existem várias apps, q teem algumas tabelas
* se abrirmos example_simple vemos q tem id e text

## adicionando campos ao Model
* na documentação do Django encontramos muitos Field types, https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
* IntegerField
* URLField (tipo n existe numa base de dados, mas permite que Django valide)
* se fizermos makemigrations, dá erro *database needs som
ething to populate existing rows.*! indica q temos linhas. Se inserirmos nova coluna, temos q dizer o valor defeito para esse campo

## argumentos dos campos (Fields)
* na base de dados os campos são integer e varchar(20)
* 
