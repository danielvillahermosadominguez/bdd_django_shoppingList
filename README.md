# Kata shopping list avanzada
Se trata de un ejemplo de BDD que contiene llamadas a servicio DJANGO. Trata de enseñar el uso de BDD,
inyección de dependencias, ciclo BDD->TDD

También se puede generar la Kata desde 0 siguiendo las instrucciones en el Anexo I: Paso a paso desde 0
Esta Kata viene apoyada por un power point explicativo.

Para poder generar el entorno para ejecutar ver Anexo II: preparación de entorno.

## Kata 1: BDD
La idea es dado un servicio "Shopping List" poder testearlo con BDD a través de distintos escenarios.
Para realizar esta Kata debemos:
* Borrar o conservar en otro directorio las clases:
    - src/features/steps/shoppinglist_steps.py
    - src/features/shoppinglist.feature
    - src/features/environment.p
* Ir escribiendo escenario por escenario, generando estas clases borradas. 
    - Healthcheck => comprobación de que el servicio responde
* Debes poder añadir items. Además debe conservar la cantidad de items, de forma que si añades dos veces el mismo item, aumenta su cantidad en 2: Ejemplo Pan - 2, Leche - 4
* No puedes añadir items si el formato es incorrecto: 
    - No acepta items vacios
    - No pueden empezar por número
    - el nombre del item, tienen que ser más de 2 caracteres

* El usuario puede eliminar items de la lista de la compra. Indicando el item a eliminar
* El usuario puede eliminar todos los items de la lista de la compra
* El usuario puede cambiar un item por otro item diferente
* El usuario puede cambiar un item por otro existente, quedandose la suma de ambos
* Un usuario no puede cambiar un item que no existe

## Kata 2: Ciclo BDD->TDD
Partiendo el codigo completo de Kata 1. introducimos una nueva feature end to end. Para eso podemos localizarnos en la etiqueta:
```
git checkout 1.0.0
```
Debemos poder resetear la lista poniendo todos los items a cantidad 1. Esta es una feature end to end donde deberemos:
- Ciclo de BDD
  - Crear el escenario, implementar el escenario y las llamadas. Se sugiere hacer 
  una llamada del estilo:
  curl -X PUT -d '{"option":"reset"}' -H "Content-Type:application/json" http://localhost:8000/items/ 
  - Crear la recuperación del PUT en el lado del servidor. En las views.py
- Empezar el ciclo de TDD
    - Test unitarios haciendo TDD sobre la aplicación, siendo el SUT: application + dominio (decisión)
- Finalizar ciclo BDD
  - Hacer llamada a método creado en capa de aplicación
  - Refactorizar

## Kata 3: Test de aceptación y Test de aplicación
 Para eso podemos localizarnos en la etiqueta:
```
git checkout 1.1.0
```

Con BDD podemos hacer test de aceptación siendo nuestro SUT (System Under Test) el propio servicio. Estos test suelen ser más lentos y la fixture más dificil de gestionar. Sin embargo, podemos reducir el número de test de aceptación a los imprescindibles y probar más ejemplos relacionados con la capa de aplicación y dominio.

Estos tests son más rapidos, por lo que hay que buscar un balance. La kata consiste en crear este tipo de tests y ser capaces de examinar reglas más especificas que seguramente no era necesario probar en los de aceptación. Por ejemplo:
- Comprobacion del comportamiento de la aplicación cuando reponemos
  items en la lista de la compra. Algunos ejemplos:

``` Behave
Example: change items
|        Items        | Input          |      Result            |
| Bread               |  Bread:Milk    |        Milk:1          |
| Bread,Bread,Bread   |  Bread:Onion   |        Onion:3         |
| Bread, Milk, Bread  |  Bread:Milk    |         Milk:3         |
| Bread, Milk, Milk   |  Bread:Onion   |  Onion:1,Milk:2        | 
``` 

## Kata 3: Test de integración
Partiendo del codigo completo de Kata 1 o Kata 2. introducimos una Techcnical feature que es la creación de un repositorio para usar con SQLite y Model de DJANGO

opcional: Hacer lo mismo con SQLAlchemy.

Para eso podemos localizarnos en la etiqueta:
```
git checkout 1.1.1
```
Para DJANGO: https://docs.djangoproject.com/en/3.1/topics/db/models/
Para SQLAlchemy: To be developed

# Anexo I. Preparación de entorno

En el raiz del directorio:
``` bash 
pip install virtualenv
python -m venv .\venv
```
y luego 
``` bash
pip install -r requirements.txt
``` 
(asegurate que lo ejecutas en el enviroment. Esto se sabe porque en la consola pone
(venv) c:\....\ . Si no tienes esto, prueba a cerrar el terminar y abrir otro en VSCode)
En el Visual Studio Code Ctrl+Shift+P y seleccionar Python Discover Test y seleccionar el directorio src con test de tipo pytests

En relación a las configuraciones para correr la aplicación Run->Add configuration y 
poner lo siguiente (launch.json):
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [


        {
            "name": "Python: Archivo actual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Run server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/manage.py",
            "console": "integratedTerminal",
            "args": [
                "runserver"
            ],
            "django": true
        },
        {
            "name": "BDD execution",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/venv/Scripts/Behave.exe",
            "console": "integratedTerminal",
            "args": [
                "--tags=~@Skip"
            ],
            "cwd": "${workspaceFolder}/src"
        },
        {
            "name": "Unit Test execution",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/venv/Scripts/pytest.exe",
            "console": "integratedTerminal"
        },
    ]
}
``` 
Y además debes configurar la base de datos de django ycrear el superusuario:
``` bash
python manage.py migrate
```
Además creamos un superusuario (admin/admin)
``` bash
python manage.py createsuperuser
```

y para que funcionen los reportes allure:
```
pip install allure-behave
```

y para que funcione el reporte de covertura
```
pip install pytest-html
```
# Anexo II. Paso a paso desde 0 y notas. A quien pueda interesar.

Adverencia. Con Python, hay  un problema bastante grande con respecto a los environments Tienes que tener mucho cuidado cuando instalas ya que se te puede instalar en local. Para eso es importante que si usas visual studio code, cuando abres la consola sepas en que environment estas.

1. Crea el virtual environment in the folder "bdd_django_shoppingList". Con el terminal escribe:

``` bash
   pip install virtualenv
   python -m venv .\venv
```
Además debemos vincular el Visual studio code al environment. Cerramos la consola antes ya que esta no está vinculada al environment todavía.

Pulsa Ctl+Shift+P => Python Select interpreter y seleccionamos el de la carpeta.

En nuestro caso, hemos creado un folder src donde meteremos el codigo y fuera estará el enviroment. Es mejor tener fuera el environment.

1. Crea un fichero main.py and escribe en el fichero:
``` python
   print("Hello World"); and execute in the terminal "python main.py"
``` 
2.  Creamos la estructura de directorios:
3. Vamos a crear un servicio REST por lo que instalamos djangorestframework: https://www.django-rest-framework.org/
``` bash
pip install django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
4.  Creamos un proyecto django. Para eso salimos fuera del directorio BDD KATA 2 - SHOPPING LIST 
```bash
django-admin startproject shoppinglist_project
```
y lo copiamos en BDD Kata 2 - Shopping List

5. Probamos a levantar django con

```bash 
python manage.py runserver
```
http://localhost:8000

Metemos tambien en visual studio code para poder arrancarlo

6. Debemos preparar para entrar como administrador:

http://localhost:8000/admin ==> administración

Pero antes debemos crear el superusuario y preparar la base de datos:
``` bash
python manage.py migrate
```

Además creamos un superusuario
``` bash
python manage.py createsuperuser
```
7. Creamos una aplicación en el proyecto django
```bash
   django-admin startapp shoppinglistapi
```
8. Ahora la idea es irse al proyecto e incluir en settings.py
https://levipy.com/crear-api-rest-con-django-rest-framework

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', <-
    'shopping_list_server_app
]
```
Además al settings.py debes añadir
``` python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

*NOTA-1: Encontramos problemas con los environments. Si no está activado no encuentra las referencias.
Para activar el environment por consola: {{your environment name}}/Scripts/activate.bat
Y en linux {{your environment name}}/bin/activate*

*Desde Visual Studio code: Pulsar Ctrl+shift+P y seleccionar python: Python interpreter y luego te dejará seleccionar el environment. En el ordenador del banco como tenemos limitados los permisos, el environment no se ejecuta bien, pero si llamamos manualmente al mismo archivo pero en lugar de ser activate.ps1 ponemos activate o activate.bat (no me queda clara la diferencia) funciona correctamente... o eso parece.*

*A veces cuando no encuentra ciertas librerias el servicio da errores que no tienen nada que ver con lo que está pasando. Es mejor crearse un main.py e ir probando a importar los módulos para  que te den los errores concretos. Seguramente depurando tambien se vea.*

*En lugar de c:/workspace/python/BDD_Kata_2_Shopping_List/venv/Scripts/Activate.ps1
c:/workspace/python/BDD_Kata_2_Shopping_List/venv/Scripts/Activate*

*NOTA 2: Si usamos vistas de modelo, en ese caso esto nos vale pero si usamos otro tipo de vistas como el APIView debemos usar *
``` python
'rest_framework.permissions.IsAuthenticated'
o 'rest_framework.permissions.AllowAny' para que lo pueda usar cualquiera
```
9.   Creamos el servicio y lo levantamos con un healthcheck. Basicamente seguimos los siguientes pasos:

- Creamos en el modulo de vistas esto
``` python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HealthSerializer

class HealthCheck(APIView):
    def get(self, request, format=None):
        return Response("OK", status.HTTP_200_OK)
```

Los codigos de estados los tenemos en el framework:
https://www.django-rest-framework.org/api-guide/status-codes/

Con esto hemos garantizado que tenemos un servicio que podemos levantar.

10.  Behaviour Driven Development Framework
 https://github.com/behave/behave
- Instalamos behave: https://behave.readthedocs.io/en/stable/install.html
``` 
    pip install -U behave
    Esto instalará el plugin de gherkin
``` 
creamos directorio llamado features
```
    root/features
```
Evidentemente, para mejor leer el gherkin debemos instalar gherkin como plugin. Metemos el Healthckeck:

shoppinglist.feature
``` Gherkin
Feature: Manage the shopping list
    
    # User story:Healthcheck 
    Scenario: The shopping list is alive
        Given a shopping list
        When ask if the shopping list is alive
        Then the shopping list is alive
```
y creamos los steps
```
    root/features/steps
```
y el codigo behind shoppinglist_steps.py

Una vez lo tenemos listo, llamamos a behave.
```
behave
```

llamamos a "behave" en al consola y nos dirá que nos falta. Como vemos no son clases, pero
hay un modulo que si te permite usar clases.

https://github.com/spyoungtech/behave-classy

Por ahora avanzamos con behave sin más

Metemos el codigo behind
``` python
from behave import given, when, Then

@given(u'a shopping list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a shopping list')


@when(u'ask if the shopping list is alive')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ask if the shopping list is alive')


@then(u'the shopping list is alive')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the shopping list is alive')
```
11.  Crear el primer test, levantar el servicio y llamar a la función

https://behave.readthedocs.io/en/stable/
https://behave.readthedocs.io/en/stable/gherkin.html#given-when-then-and-but

Es interesante comentar que en behave no tendremos el tipico setup que se ejecuta antes de un escenario. Aqui lo llama directamente fixtures. Este concepto se provee para simplificar
el setup y el cleanup.

La fixture, al crearse podrias decir de ejecutarla a nivel de feature, o a nivel de escenario

NOTA: para levantar comandos:
pip install os_sys (tarda un rato y por algún motivo da un error al final)
```python
import os
```
Deberiamos meter lo de BDD para que pueda ejecutarse. Ponemos lo siguiente en el launch:
 {
            "name": "BDD execution",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/venv/lib/site-packages/behave/__main__.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/src"
        },

Ahora para los requests:
https://www.testaddict.space/using-pythons-requests-to-make-rest-api-calls/
``` bash
pip install requests (plural)
```
Podemos instalar el behave test explorer (el cual no he conseguido hacer funcionar)

Instalamos para generar un html
``` bash
pip install allure-behave
```
Necesitamos allure para jenkins y podemos ejecutar el server o generar el reporte
``` bash
behave -f allure_behave.formatter:AllureFormatter -o report ./features
D:\automation\api\reports>allure generate D:\automation\api\reports
allure serve %allure_result_folder%
```
Para matar los procesos no funciona muy bien el kill del proceso, sin embargo con
las psutils (hay que instalarlas) se puede matar el proceso por el pid. Ver codigo
12.  Tenemos ya el happy path y construido el servicio con un healtcheck. Ahora la idea es
ir construyendo. Siguientes pasos:
- Refactorizar
- Escribir los Escenarios en gherkin y dejarlos skip
- IR escenario pro escenario haciendo BDD -> TDD
- Inicialmente plantear que el shopping list puede ir por usuario y que se guarda como un fichero xml
- Una vez terminada la especificación pasamos sonar, subimos los tes
- Al final nos piden guardarlo en base de datos, usando django
- LA shopping list deberá conectarse a un servidor en busca de su traduccion en ingles (google)
- Necesitaremos un iOC
- ¿Que pasaria si quisieramos no usar django  quisieramos usar

13.  Refactorizar.

- Creamos una clase de utilidades
``` bash
features/
features/signup.feature
features/login.feature
features/account_details.feature
features/environment.py
features/steps/
features/steps/website.py
features/steps/utils.py
```
14. Una vez refactorizado empezamos a crear el shopping list. Ponemos todos los
    escenarios y los ponemos en modo Skip.
    - ponemos el tag @Skip
    behave --tags ~@Skip

    y hacemos que funcione con el visual code.

15. Siguiente historia de usuario. La idea es implementarlo de forma que nuestro repositorio
sea un fichero XML y es por usuario, es decir que si tenemos varios usuarios deberiamos poder
arrancar

16. Por eso hacemos la llamada desde BDD a nuestro shoppinglist y vamos directos a la api.
- Implementamos los endpoints, tanto de listado como de añadir
- Comprobamos que funciona con un curl
- Comprobamos que funciona con el propio test de BDD

https://www.django-rest-framework.org/tutorial/3-class-based-views/

17. Hacemos TDD con shopping list. Dominio y aplicacion son nuestro sut (system under test)
    En esta ocasion usaremos pytests
    Para pytest hay varios layouts. Usaremos el normal
``` bash 
    setup.py
    src/mypckg
    src/tests
        __init__.py
        shoppinglist
            __init__.py
            test_shoppinglis.py
```
Así que instalamos pytest
``` bash
pip install pytest
```
y ya con poner pytest en la consola, ya los ejecuta

Si queremos hacerlo desde visual studio code, creamos un pytest.ini en el directorio raiz donde:
``` ini
# pytest.ini
[pytest]
testpaths =
    src/tests
    src/integration (este no hace falta)
```
Con esto podriamos ejecutar desde el raiz

Para visual studio code tenemos que ejecutar Ctrl+Shift+P y elegir Python:Discover Tests. Ahi elegiras pytest y el directorios. 

Para inyeccion de dependencias:
https://github.com/google/pinject


- Metemos todos los escenarios y hacemos BDD -> TDD

18. Imaginemos que ahora queremos ver que cobertura tenemos. Coverage.py.
- Instalamos pip install coverage
- Esto vale para pytest y para unittest
- Desde consola:
- con pytest solo sería pytest arg1 arg2 arg3 (ficheros)
- con unittest seria algo asi como python -m unittest discover - con coverage sería cubrirlo, por ejemplo coverage run -m unittest discover
``` bash
    coverage run -m pytest arg1 , arg2
```    
Esto te generará un fichero .coverage
- ahora pon coverage report y saldrá la cobertura por consola
- si pones coverage html te generará un html

Para tema de cobertura puedes generar un fichero .coveragerc donde puedes escribir cosas como:
``` ini
    [html]
    directory = html-coverage
    [run]
    omit = 
        shopping/__init__.py
        test_shoppinglist.py
```
19. Con respecto a crear nuevos repositorios. Veamos los pasos para DJANGO.

- Creamos un repositorio para DJANGO que cumpla el interface de ShoppingListRepository
- Creamos el modelo de DJANGO. En principio algo sencillo como dos entiendades:
    - ShoppingListDB. Solo contiene el nombre de usuario. Tendremos una por usuario. Y es primary key.
    - ShoppingListDetailDB. Contiene el nombre de usuario como foreing key y con opción de borrado en cascada. Cada entrada tiene una descripción y una cantidad.
- Aplicamos los cambios a la base de datos. Para eso debemos:
    - Abrimos settings. py y en INSTALLED_APPS añadimos shoppinglistapi (podriamos tener el modelo en otro sitio)
``` 
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'shoppinglistapi'
]
``` 
  - Hacemos las migraciones
``` 
    python manage.py makemigrations
``` 

mostrará lo siguiente:
``` 
  shoppinglistapi\migrations\0001_initial.py
    - Create model ShoppingListDB
    - Create model ShoppingListDetailDB
``` 

Esto te creará en shoppinglistapi/migrations/0001_initial.py

Con este comando, veremos que está deschequeada:
``` 
    python manage.py showmigrations
``` 
Y con esto crearemos la migración:
``` 
python manage.py sqlmigrate shoppinglistapi 0001_initial
``` 

Y con esto la aplicaremos y se crearán las tablas:
``` 
python manage.py migrate
20. En cuanto a frameworks de doblado (mock) podemos usar el de pytest-mock
https://pypi.org/project/pytest-mock/

``` 