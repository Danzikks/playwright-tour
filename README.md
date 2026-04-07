Это пет-проект playwright + pytest + allure

my_project_site - это тестирование моих пет-проектов на php, которые развёрнуты на моём self-hosted NAS сервере.   
demosite - это открытый сайт для тренировок автотестов

Для запуска тестов с генерацией отчётов allure: make tests-allure  
Для запуска тестов без генерации отчёта: make tests
Для просмотра отчётов теста allure: make allure-serve 

Разворачиваение проекта:

1) Для установки зависимостей: make install
2) Для установки веб-драйверов: playwright install
