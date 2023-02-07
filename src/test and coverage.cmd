del /q htmlcov
del coverage.xml
del out_report.xml
del report.html
del /q html-coverage
del /q coverage
mkdir coverage
mkdir coverage\pytest
mkdir coverage\behave
mkdir coverage\django

::pause
coverage run -m pytest  --junitxml=out_report.xml 
copy .coverage .\coverage\pytest\.coverage
coverage run -m behave --tags=@Application
copy .coverage .\coverage\behave\.coverage
coverage run manage.py test
copy .coverage .\coverage\django\.coverage
del .coverage

coverage combine coverage\pytest\.coverage coverage\behave\.coverage coverage\django\.coverage
REM coverage report -m
REM --html=report.html
coverage xml
coverage html
:: sonar-scanner