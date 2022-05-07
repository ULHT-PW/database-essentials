# database-essentials
[prettyprinted course](https://courses.prettyprinted.com/courses/django-database-essentials/lectures/4674919)


### cria projeto django, observar db.sqlite com Pycharm (DB Browser), ver impacto de criar superuser 
* cria projeto em Pycharm
* migra `py manage.py migrate
* abre com Pycharm (ou DB Browser) o ficheiro .sqlite3
* observa a estrutura da base de dados
* o nome das tabelas têm como prefixo o nome da aplicação, tudo em minuscula
* existem várias aplicações instaladas (ver em INSTALLED_APPS)
* criar `py manage.py createsuperuser`
* ver na base de dados, tabela auth_user, que foi registado
* ver migrations

### criar aplicação e modelo
* criar aplicação example
* criar modelo apenas com atributo text
* registar em settings a aplicação
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

https://courses.prettyprinted.com/courses/django-database-essentials/lectures/4674921

## admin
* abrir o admin
* admin dashboard, permite fazer de forma amigável
* podemos modificar email na base de dados do Pycham e vemos mudado no admin. Se mudarmos no admin, aparece mudado no Pycharm.
* mostra dois modelos, groups e users
* no meu nome vejo o mesmo que na base de dados
* se alterar as permissões no admin, podemos ver as alterações na base de dados 
* devemos registar modelo na aplicação admin
```python
from .models import Simple

admin.site.register(Simple)
```
* no admin aparece a classe
* se adicionarmos 
```python
def __str__(self):
   return self.url
```
* o admin deve ser userfriendly, deve poder ser usado por não-programadores

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
```python
Entry.objects.filter(pub_date__lte='2006-01-01')
```
traduz-se em SQL:
```sql
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

## Count
* podemos contar quantos resultados são retornados por uma query
* Simple.objects.filter(number=10).count()

## Date
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#date
* DateTimeField, ou DateField
* correspondem ao datetime do Python `from datetime import date, datetime`. Django converte estes objetos em informação na base de dados
* Field Lookups: date, time, year, month, day, hour, etc...
* exemplos:
```python
from example.models import Date
from datetime import datetime
new_date = datetime.now()
new_date
datetime.datetime(2022, 1, 22, 21, 19, 28, 54842)
my_date = Date(date=new_date)  # guarda objeto datetime no campo DateTimeField
my_date.save()
Date.objects.filter(date__date=new_date) # filtra objetos com a mesma datetime
# <QuerySet [# <Date: Date object (1)>]>
another_date = datetime.now()
Date.objects.filter(date__date=another_date) # como difere de alguns segundos, não há correspondecia
# <QuerySet [# <Date: Date object (1)>]>
Date.objects.filter(date__time=new_date) 
# <QuerySet [# <Date: Date object (1)>]>
Date.objects.filter(date__time=another_date)
# <QuerySet []>
Date.objects.filter(date__month=1) # filtra objetos com mes 1
# <QuerySet [# <Date: Date object (1)>]>
Date.objects.filter(date__day=22)  # filtra objetos com dia 22
# <QuerySet [# <Date: Date object (1)>]>
```

## Null and blank
* campo com `null = True` indica à **base de dados** que pode ser NULL
* campo com `blank = True` indica ao **Django** que  **não é obrigatório no formulário** 
* quando queremos `blank = True` devemos por `null = True` excepto em CharField e TextField, que em django são guardados como string vazia (`''`) pelo q não precisamos de por `null = True`
* criemos classe `NullExample` com campo `col` do tipo `CharField` 
```python
from example.models import NullExample
one = NullExample(col='one')
one.save()
two = NullExample(col=None)
two.save()
three= NullExample()
three.save()
NullExample.objects.filter(col__isnull=True)
# <QuerySet [<NullExample: NullExample object (2)>, <NullExample: NullExample object (3)>]>
NullExample.objects.filter(col__isnull=False)
# <QuerySet [<NullExample: NullExample object (1)>]>
```

## Relações One to Many
* Ao trabalhar com bases de dados relacionais, um aspecto importante é podermos ter relações entre duas ou mais tabelas
* relação **pai-filho**, relação one-to-many ou many-to-one:
   * um pai pode ter vários filhos
   * cada filho apenas tem um pai

```python
class Language(models.Model):
    name = models.CharField(max_length=10)     
        
class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE) # se apagamos o pai, apaga os filhos
```

Podemos criar alguns objetos, linguagem **Python** com frameworks *Django* e *Flask*, e **Java** com *Spring*:
```python
from example.models import Language, Framework
python = Language(name='Python')
python.save()
django = Framework(name='Django')
django.language = python
flask = Framework(name='Flask', language=python)
flask.save()
django.save()
java=Language(name='Java')
java.save()
spring = Framework(name='Spring', language=java)
spring.save()
Framework.objects.all()
# <QuerySet [<Framework: Flask>, <Framework: Django>, <Framework: Spring>]>
```

## Consultas de relações One To Many
Podemos consultar as frameworks que teem como linguagem Python
* usando a foreignkey language:
```python
Framework.objects.filter(language=1)
# <QuerySet [<Framework: Flask>, <Framework: Django>]>
```
* usando o nome da linguagem, com o fieldLookup `language__name`:
```python
Framework.objects.filter(language__name='Python') # filtrar Frameworks com linguagem Python
# <QuerySet [<Framework: Flask>, <Framework: Django>]>
```
Podemos também saber as linguagens que têm como framework Django, pois o Django disponibiliza um campo com nome da classe filho em minúsculas:
```python
Language.objects.filter(framework__name='Django')
# <QuerySet [<Language: Python>]>
Language.objects.filter(framework__name__startswith='Dj')  # podemos combinar com FieldLookups
# <QuerySet [<Language: Python>]>
```
Uma tabela pode ter múltiplos elementos da outra. E a outra múltiplos elementos da primeira.

## Relações Many To Many
* Podemos ter tabelas com várias instancias relacionadas: desportos e alunos.
  * um aluno pode praticar vários desportos
  * um desporto pode ser praticado por vários alunos
* A relação ManyToMany especifica-se apenas numa das classes, por convenção a de menor hierarquia (aluno neste caso) 
* Usa-se o **método add** para adicionar uma relação ManyToMany a um objeto
```python
class Desporto(models.Model):
    nome = models.CharField(max_length=30)

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    desportos = models.ManyToManyField(Desporto)
```
* fazemos makemigrations e migrate 
* abrimos tabelas e vemos que existe uma terceira tabela, que relaciona ambas
```python
from example.models import Desporto, Aluno

vela = Desporto(nome='vela')
vela.save()

tenis = Desporto(nome = 'tenis')
tenis.save()

luis = Aluno(nome='Luis')
luis.save()

ana = Aluno(nome ='Ana')
ana.save()

luis.desportos.add(futebol) # método add para adicionar relação ManyToMany
luis.desportos.add(vela)

ana.desportos.add(vela)
ana.desportos.create(nome='dança') # permite criar um novo desporto!
```

## Consultas de relações Many to Many
* semelhante a consultas de relações Many to One
```python
Aluno.objects.filter(desportos__nome='vela')  # alunos que praticam vela
# <QuerySet [<Aluno: Luis>, <Aluno: Ana>]>
Desporto.objects.filter(aluno__nome='Ana')  # desportos que a Ana pratica
# <QuerySet [<Desporto: vela>, <Desporto: dança>]>

ana = Aluno.objects.get(nome='Ana')
ana.desportos.all()
# <QuerySet [<Desporto: vela>, <Desporto: dança>]>
```

* a classe Desporto não tem campo *alunos*. Usa-se o nome da classe em minúscula (aluno) e o sufixo '__set' (aluno__set). Exemplo:
```python
vela = Desporto.objects.get(nome='vela')
vela.aluno_set.all()         # 
# <QuerySet [<Aluno: Luis>, <Aluno: Ana>]>
```


## USar outra base de dados
https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASES

* em settings.py, DATABASES especifica a base de dados usada
