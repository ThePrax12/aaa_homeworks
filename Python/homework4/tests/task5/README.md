# task5

Этот проект содержит функцию, которая получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год. А также  тесты для проверки её работы.

## Инструкции по запуску тестов

1. Установите coverage, если у вас его нет
   ```bash
   pip install coverage
2. Запустите тесты командой
    ``` bash
   coverage run -m unittest -v  task5.py
3. Получите отчёт по покрытию кода тестами 
    ``` bash
   coverage report
