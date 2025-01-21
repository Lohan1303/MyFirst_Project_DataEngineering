# Meu Primeiro Projeto em Engenharia de Dados

## Introdução

Este projeto foi desenvolvido como parte do curso de Engenharia de Dados da IBM na plataforma Coursera. É um dos meus primeiros projetos na área de engenharia de dados e utiliza Python para implementar uma pipeline ETL (Extract, Transform, Load).

## Descrição do Projeto

O script contém métodos para:

- **Extração de dados**: Processa arquivos nos formatos CSV, JSON e XML, combinando-os em um único DataFrame.
- **Transformação de dados**: Realiza um tratamento simples, convertendo:
  - Alturas de polegadas para metros (1 polegada = 0,0254 metros).
  - Pesos de libras para quilogramas (1 libra = 0,45359237 quilogramas).
- **Carregamento de dados**: Salva todos os dados transformados em um único arquivo CSV.
- **Logging**: Registra mensagens informando o progresso de cada etapa do processo ETL.

## Mensagens de Log

As mensagens de log acompanham o progresso da pipeline ETL e seguem o formato:
```
YYYY-MMM-DD-HH:MM:SS, Mensagem
```
Exemplo:
```
2025-Jan-21-10:45:00, ETL Job Started
2025-Jan-21-10:45:10, Extract phase Started
2025-Jan-21-10:45:20, Extract phase Ended
2025-Jan-21-10:45:30, Transform phase Started
2025-Jan-21-10:45:40, Transform phase Ended
2025-Jan-21-10:45:50, Load phase Started
2025-Jan-21-10:46:00, Load phase Ended
2025-Jan-21-10:46:10, ETL Job Ended
```

## Autor
Lohan Batista Moreira

---

# My First Data Engineering Project

## Introduction

This project was developed as part of the IBM Data Engineering course on the Coursera platform. It is one of my first projects in the data engineering field and uses Python to implement an ETL (Extract, Transform, Load) pipeline.

## Project Description

The script includes methods for:

- **Data Extraction**: Processes files in CSV, JSON, and XML formats, combining them into a single DataFrame.
- **Data Transformation**: Applies simple processing to convert:
  - Heights from inches to meters (1 inch = 0.0254 meters).
  - Weights from pounds to kilograms (1 pound = 0.45359237 kilograms).
- **Data Loading**: Saves all transformed data into a single CSV file.
- **Logging**: Logs messages to track the progress of each ETL phase.

## Log Messages

Log messages track the progress of the ETL pipeline and follow the format:
```
YYYY-MMM-DD-HH:MM:SS, Message
```
Example:
```
2025-Jan-21-10:45:00, ETL Job Started
2025-Jan-21-10:45:10, Extract phase Started
2025-Jan-21-10:45:20, Extract phase Ended
2025-Jan-21-10:45:30, Transform phase Started
2025-Jan-21-10:45:40, Transform phase Ended
2025-Jan-21-10:45:50, Load phase Started
2025-Jan-21-10:46:00, Load phase Ended
2025-Jan-21-10:46:10, ETL Job Ended
```

## Author
Lohan Batista Moreira
