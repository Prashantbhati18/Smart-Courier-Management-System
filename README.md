# 📦 Smart Courier Management System

A console-based Courier Management System developed using **Python** and **MySQL**. The application manages courier shipments through CRUD operations and generates business reports using SQL queries. Realistic test data is generated using the **Faker** library.

---

## 🚀 Features

### Shipment Management
- View all shipments
- Search shipment by Shipment ID
- Add a new shipment
- Update shipment status
- Delete shipment

### Business Reports
- Total Shipments
- Shipment Status Report
- Branch-wise Shipment Report
- Revenue Report
- Top 5 Customers
- Monthly Shipment Trend

### Data Generation
- Generate realistic customer records using Faker
- Generate branch records
- Generate shipment records with realistic dates and statuses

---

## 🛠 Tech Stack

- Python
- MySQL
- SQL
- Faker
- mysql-connector-python
- Tabulate

---

## 📂 Project Structure

```text
Smart-Courier-Management-System
│
├── SQL/
│   └── courier_database.sql
│
├── config.py
├── database.py
├── generate_branches.py
├── generate_customers.py
├── generate_shipments.py
├── shipment.py
├── reports.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🗄 Database Schema

The project consists of three relational tables:

### Customers
- customer_id
- customer_name
- phone
- email
- city

### Branches
- branch_id
- branch_name
- city
- manager_name

### Shipments
- shipment_id
- customer_id
- branch_id
- origin
- destination
- weight
- booking_date
- expected_delivery
- actual_delivery
- status
- shipping_cost

---

## 📊 SQL Concepts Used

- SELECT
- INSERT
- UPDATE
- DELETE
- JOIN
- GROUP BY
- ORDER BY
- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()
- LIMIT
- DATE_FORMAT()

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Smart-Courier-Management-System.git
```

### 2. Move into the project

```bash
cd Smart-Courier-Management-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

Run:

```
SQL/courier_database.sql
```

using MySQL Workbench.

### 5. Configure database credentials

Open `config.py` and update:

- Host
- Username
- Password
- Database Name

### 6. Generate sample data

```bash
python generate_customers.py
python generate_branches.py
python generate_shipments.py
```

### 7. Run the application

```bash
python main.py
```

---

## 📈 Sample Reports

The application generates reports such as:

- Shipment Status Distribution
- Branch-wise Shipment Count
- Revenue Analysis
- Top Customers
- Monthly Shipment Trend

---

## 🎯 Learning Outcomes

This project helped me gain practical experience with:

- Python programming
- MySQL database design
- CRUD operations
- SQL joins and aggregate functions
- Business report generation
- Faker for realistic data generation
- Modular Python programming

---

## 🔮 Future Enhancements

- User authentication
- Export reports to Excel/PDF
- Power BI dashboard integration
- GUI using Tkinter
- Shipment tracking using Tracking ID

---

## 👨‍💻 Author

**Prashant Bhati**

Final Year B.E. Computer Science Student

Panjab University, Chandigarh