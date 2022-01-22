# database-essentials
[prettyprinted course](https://courses.prettyprinted.com/courses/django-database-essentials/lectures/4674919)
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
https://courses.prettyprinted.com/courses/django-database-essentials/lectures/4674921

## admin
estrutura da base de dados

## create update delete
* adicionar conteudos a base de dados com código, `py manage.py shell`
* from app.models import class 
* criar objeto (com nomes de atributos), obj = Simple(atributo='valor') 
* mostrar em DB Browser que não apareceu
* gravar
* mostrar em DB Browser que apareceu
* alterar um atributo e gravar
* mostrar em DB Browser que apareceu
* apagar obj.delete(), mostra qtas linhas apagou e o que apagou
* mostrar em DB Browser que apagou

## obter uma única linha
* numa app precisamos manipular objetos da BD, precisamos de os pesquisar. 
* é onde o django é forte, a fazer queries
* podemos querer um objeto, ou vários. vamos obter um só
* método get podemos especificar exatamente o que queremos. podemso inserir o id duma coluna, id/pk obj = Simple.objects.get(id=1)
* se não existir, lança erro. se existir multiplos objetos iguais, dá erro. usar try catch para prevenir erros

## obter todas as linhas
* obter multiplos resultados
* results =  Simple.objects.all() retorna tudo
* podemos iterar pelos objetos e seus atributos com ciclos for
* o QuerySet é indexável, results[0]

## Filter
* filter() para limitar resultados da base de dados, procurando apenas o que escrevemos em filter
* filter() retorna um QuerySet, lista
* Simple.objects.filter(number=10) retorna os que teem number = 10
* podemos incluir condições:
   * 'e': results = Simple.objects.filter(height=80, age=20) 
   * 'ou' results = Simple.objects.filter(number=10) | Simple.objects.filter((number=20)
   * '>': results = Simple.objects.filter(age__gt=18) 
   * '>=': results = Simple.objects.filter(age__gte=18) 
   * '<': results = Simple.objects.filter(age__lt=18) 
   * '<=': results = Simple.objects.filter(age__lte=18) 
 
## Exclude
* Simple.objects.filter(number=10)
* oposto/complemento de filter. retorna tudo o que não tenha o especificado no argumento de exclude
* se fizermos exclude do que pusemos filter, obtemos o complemento

## Encadeando filtros
* filter retorna um QuerySet, ao qual podemos apliar um filtro novamente 
* Simple.objects.filter(number=0).filter(url='www.yahoo.com')
* criemos 6 elementos

## Field Lookups [1](https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups) [detailed](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups)

* operadores que podemos usar em **get, filter, exclude** para especificar clausulas do SQL WHERE
* sintaxe: `class.objects.get/filter/exclude(field__lookuptype=value)`
* exemplo:
```
Entry.objects.filter(pub_date__lte='2006-01-01')

traduz-se em SQL:

SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
```
campos:
* **exact**, valor exato
* **iexact**, case-insensitive match (correspondência sem distinção entre maiúsculas e minúsculas). 
   * `Blog.objects.get(name__iexact="beatles blog")` corresponderia a um Blog cujo campo *name* fosse `Beatles Blog`, `beatles blog`, ou até `BeAtlES blOG`.
* **contains**
   * `Entry.objects.get(headline__contains='Lennon')` corresponderia ao headline com valor 'Today Lennon honored' mas não a 'today lennon honored'.
* **icontains**, sem distinção entre maiúsculas e minúsculas
* **in** identifica todos osobjetos cujo campo está numa lista (tuplo ou QuerySet)
   * `Simple.objects.filter(age__in=[6, 10])` retorna todos os que tiverem age 6 ou 10
* **gt** '>': results = Simple.objects.filter(age__gt=18) 
* **gte** '>=': results = Simple.objects.filter(age__gte=18) 
* **lt** '<': results = Simple.objects.filter(age__lt=18) 
* **lte** '<=': results = Simple.objects.filter(age__lte=18) 
* **startswith endswith**
* **range** identifica os que estão num intervalo
   * `Pessoa.objects.filter(idade__range=(8,14))`, pessoas com idades no intervalo [8, 14[ 
* **regex**

Fazer um exemplo:
* usar exact com um campo | por maiuscula no valor e ver q nao escolhe | usar iexact e ve que apanha 
* Simple.objects.filter(number__in=[1,10]) 
* exemplo de gt, gte
* startswith

## Limiting and offset - slices
* podemos usar slices 
* Simple.objects.all()[:3] retorna os 3 primeiros
* Simple.objects.all()[2:] retorna todos excepto os dois primeiros
* Simple.objects.all()[2:5] retorna 5-2=3 resultados

## Order by
* ordem natural é por inserção
* podemos ordenar em função de um atributo
   * `Simple.objects.order_by('id')`, crescentemente pelo id
   * `Simple.objects.order_by('-id')`, decrescentemente pelo id
   * `Simple.objects.order_by('nome', 'ápelido')`, ordena primeiro pelo nome, e para nomes iguais ordena pelo apelido
* podemos aplicar um filtro

# Count
* podemos contar qtos resultados reotrnados por uma query
* Simple.objects.filter(number=10).count()





see database on Pycharm: https://www.youtube.com/watch?v=_FlpiNno088
