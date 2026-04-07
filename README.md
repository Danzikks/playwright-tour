Это пет-проект playwright + pytest + allure

my_project_site - это тестирование моих пет-проектов на php.  
demosite - это открытый сайт для тренировок автотестов

Для запуска тестов с генерацией отчётов allure: pytest --alluredir=./allure-results ./tests  
Для запуска тестов без генерации отчёта: pytest ./tests  
Для просмотра отчётов теста allure: ⏺ allure serve ./allure-results  

Разворачиваение проекта:

1) Для установки зависимостей: pip install -r requirements.txt
2) Для установки веб-драйверов: playwright install
