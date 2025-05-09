#!/usr/bin/env bash

echo "Testing..."
# В параметре alluredir указывается директория, куда будет складываться результат прогона тестов.
python3  -m pytest tests --alluredir=allure-results
# Генерируем отчет allure, который будет использован для визуального отображения.
allure generate ./logs/allure-results/ -o ./allure-report/ --clean
allure generate -c ./allure-results -o ./allure-report
echo "Saving..."
# Копируем папку history из отчета в результаты, чтобы сохранить историю прогонов.
cp -R ./allure-report/history/  ./logs/allure-results/
echo "Starting Allure..."
# Запуск приложения для отображения отчета.
allure serve -p 8580