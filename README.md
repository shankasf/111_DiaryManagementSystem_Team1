# Warehouse Management System (WMS) - TechBoys

> MSCS 542L-256-24F - Database Management System Project  
> Marist College, School of Computer Science and Mathematics  
> Instructor: Dr. Reza Sadeghi  

## Project Overview

This Warehouse Management System (WMS) is designed to streamline warehouse operations where multiple shopkeepers store and manage their inventory under the supervision of an administrator. The system provides a secure, organized, and user-friendly interface for effective warehouse management. It handles everything from inventory tracking to order processing, borrowing requests, and audits.

## Team Members

| Name | Email | Role |
|------|-------|------|
| Sumanth Kumar Katapally | SumanthKumar.Katapally1@marist.edu | Team Head |
| Abhijeet Cherungottil | Abhijeet.Cherungottil1@marist.edu | Team Member |
| Sagar Shankaran | Sagar.Shankaran1@marist.edu | Team Member |

## Project Objectives

- Secure login & access control for Admins and Shopkeepers
- Full CRUD operations on:
  - Shopkeepers
  - Products
  - Categories
  - Suppliers
  - Orders
  - Transactions
  - Borrow Requests
- Inventory tracking with:
  - Warehouse capacity management
  - Stock audits
  - Borrowing history
  - Shipment and transaction management
- Optimized SQL with:
  - Normalization
  - Indexing
  - Performance enhancements
- User-friendly interface (Admin & Shopkeeper POV)
- Data security with encryption and integrity constraints

## ER & EER Diagram Overview

The system models:
- Entities: Admin, Shopkeeper, Product, Warehouse, BorrowRequest, Category, Supplier, Order, Location, Transaction, StockAudit, Shipment
- Relationships: One-to-Many, Many-to-Many, Weak Entities, Derived Attributes

## Database Implementation

- Database: MySQL (Workbench used for EER diagram)
- Schema: `Warehouse_Management_System_DBMS_Project`
- Features:
  - Primary, Foreign, Composite Keys
  - Indexes for query optimization
  - Bulk data loading using CSVs
  - Sample data for testing

## Key Features

- Inventory threshold notifications
- Item location tracking down to aisle/bin
- Stock rotation to clear old stock first
- Sustainability tracking via Carbon Footprint
- Full borrowing and order processing pipeline
- Comprehensive audit and transaction management

## Tools & Technologies

- **Database**: MySQL
- **ER/EER Modeling**: MySQL Workbench
- **Languages**: SQL, JSON (for data handling)
- **Security**: Password encryption, access control
- **Optimization**: Indexing, Bulk Inserts, Normalization

## Project Structure

```
Warehouse Management System
├── SQL Scripts
│   ├── CREATE TABLE Statements.sql
│   ├── INSERT Sample Data.sql
│   └── Index Optimization.sql
├── CSV Data
│   ├── admin.csv
│   ├── shopkeeper.csv
│   ├── category.csv
│   ├── supplier.csv
│   └── ...
├── Diagrams
│   ├── ER_Diagram.png
│   ├── EER_Diagram.png
│   └── UX_Flow.png
├── README.md
└── Report.pdf
```

## Repository Link

[GitHub Repo](https://github.com/Sumanthkatapally/DBMS_PROJECT.git)

## Contributors Acknowledgement

This project was developed as part of the **MSCS 542L** course at Marist College, and we sincerely thank Dr. Reza Sadeghi for his guidance and support.

