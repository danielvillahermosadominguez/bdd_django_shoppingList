Feature: Capital

#CIBGBPANA-99: Método de ingesta de capita 
# Cargar todos los datos de capital necesarios para el reporting de RWAs
# 5 ficheros
@Aceptation
Scenario Outline: Cargar todos los datos de capital necesarios para el reporting de RWAs
Given la aplicacion operativa 
When los datos de RWAs son cargados provenientes del fichero <input>
Then se puede obtener el reporting de métricas de capital
And el output de la herramienta cuadra con el fichero de métricas de capital <input>

Example: Ficheros
|    input           |
|    bdr             |
|    bdr 1798        |
|    bdr ajustes     |
|    bdr titus NYB   |


#CIBGBPANA-99: Método de ingesta de capita 
@Aceptation
# En la base de datos de MISCO buscar el product de SCIB
Scenario: En la base de datos de MISCO buscar el product de SCIB
Given la aplicacion operativa 
When conectamos con la base de datos de "MISCO"
Then existe el producto SCIB 

#
@Application

# Revenues
# Para costes, ingresos y provisiones: incluir NYB y Continental Europe Branches