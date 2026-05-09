# Automated Sales Report Generator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Automation](https://img.shields.io/badge/Project-Business%20Automation-success)

---

## Project Overview

This project is an end-to-end automated sales reporting pipeline built using Python.  
The system ingests raw sales CSV data, performs data cleaning and KPI analysis using Pandas, generates professionally formatted multi-sheet Excel reports using openpyxl, and supports automated email delivery using smtplib.

The project simulates a real-world business reporting workflow commonly used in analytics and data engineering teams.

---

## Features

- Automated sales CSV ingestion
- Data cleaning and preprocessing using Pandas
- KPI generation and business analytics
- Multi-sheet formatted Excel reporting
- Revenue analysis by product and region
- Automated email dispatch support
- Cron-schedulable weekly automation pipeline
- Modular and reusable Python codebase

---

## KPIs Generated

The pipeline automatically calculates:

- Total Revenue
- Total Orders
- Average Order Value
- Top Product by Revenue
- Top Performing Region
- Revenue by Product
- Revenue by Region

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data cleaning and analysis |
| NumPy | Randomized dataset generation |
| openpyxl | Excel report creation and formatting |
| smtplib | Automated email delivery |
| Git & GitHub | Version control |

---

## Project Structure

```text
automated-sales-report-generator/
│
├── generate_data.py
├── sales_report_generator.py
├── sales_data.csv
├── sales_report_YYYYMMDD.xlsx
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Workflow

```text
Generate Sales Data
        ↓
Load CSV Data
        ↓
Clean & Validate Data
        ↓
Generate KPIs
        ↓
Create Excel Report
        ↓
(Optional) Email Report
```

---

## Sample Dataset

The project generates synthetic transactional sales data including:

- Date
- Product
- Region
- Quantity
- Unit Price
- Revenue

The generated dataset simulates realistic business sales records for reporting and analytics purposes.

---

## Excel Report Sheets

The generated Excel report contains:

| Sheet Name | Description |
|---|---|
| KPI Summary | Business KPI overview |
| Revenue by Product | Product-wise revenue analysis |
| Revenue by Region | Regional revenue analysis |
| Raw Data | Full transaction dataset |

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/automated-sales-report-generator.git
```

---

### 2. Install Dependencies

```bash
pip install pandas numpy openpyxl
```

---

### 3. Generate Sample Sales Data

```bash
python generate_data.py
```

This creates:

```text
sales_data.csv
```

---

### 4. Run the Automated Report Generator

```bash
python sales_report_generator.py
```

This generates:

```text
sales_report_YYYYMMDD.xlsx
```

---

## Automation Support

The project supports weekly scheduling using cron jobs.

### Example Cron Schedule

```bash
0 8 * * 1 /usr/bin/python3 /path/to/sales_report_generator.py
```

This runs the pipeline automatically every Monday at 8:00 AM.

---

## Screenshots

### KPI Summary Report
_Add screenshots here_

### Revenue by Product
_Add screenshots here_

### Revenue by Region
_Add screenshots here_

---

## Key Learning Outcomes

- Python-based business automation
- Data cleaning and preprocessing
- KPI generation and reporting
- Excel automation with openpyxl
- ETL-style workflow development
- Modular Python project structuring
- Automated reporting pipelines

---

## Future Improvements

- Add interactive charts to Excel reports
- Connect to SQL databases
- Deploy using Airflow
- Add dashboard integration with Power BI
- Dockerize the reporting pipeline

---

## Author

**Viraj Patil**

```