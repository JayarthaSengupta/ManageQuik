# ManageQuik — Management & Performance Tracking System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?logo=python&logoColor=white)
![python--dotenv](https://img.shields.io/badge/python--dotenv-1.x-ECD53F?logo=dotenv&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

**ManageQuik** is a Python-based management and performance-tracking system designed to simplify managerial workflows, review team-member performance, and provide structured insights that can help individuals understand their performance and improve going forward.

The current implementation uses an **esports organization as its domain-specific use case**, combining a MySQL-backed member database with CSV-based performance data for different games. The underlying system, however, is designed from a **management and performance-analysis perspective rather than a gaming-specific perspective**.

ManageQuik provides role-based access for Managers, In-Game Leaders (IGLs), and Gamers, allowing managers to oversee organizational data and team performance while enabling individuals to review their own performance records.

Version **2.0.0** significantly restructures the original application by separating database operations, authentication, validation, game-data management, and visualization into dedicated modules. It also introduces configurable environment-based settings, persistent performance-data updates, improved validation, stronger error handling, and fixes several correctness issues present in v1.0.0.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [What's New in v2.0.0](#whats-new-in-v200)
- [Current Use Case](#current-use-case)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Supported Games](#supported-games)
- [Setup](#setup)
- [Environment Configuration](#environment-configuration)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)
- [User Roles](#user-roles)
- [Authentication](#authentication)
- [Performance Data](#performance-data)
- [Application Flow](#application-flow)
- [Data Visualization](#data-visualization)
- [Project Structure](#project-structure)
- [Error Handling](#error-handling)
- [Security](#security)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [Version History](#version-history)
- [What I Learned](#what-i-learned)
- [License](#license)

---

## Overview

ManageQuik is built around a simple management workflow:

```
                    ┌─────────────────────┐
                    │      Manager       │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
        ┌──────────────────┐       ┌──────────────────┐
        │ Manage People    │       │ Review Performance│
        │ & Organizational │       │ & Work Data       │
        │ Information      │       │                   │
        └────────┬─────────┘       └─────────┬────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Performance Data    │
                    │ Analysis & Reports  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Individual Insights │
                    │ & Improvement       │
                    └─────────────────────┘
```

The system is intended to support three interconnected activities:

### 1. Manage

Managers can maintain organizational/member information and oversee the people they are responsible for.

### 2. Review

Performance data can be collected, viewed, and visualized to help managers evaluate work and identify areas that require attention.

### 3. Improve

Individuals can use their performance information to understand their results and identify how they can improve over time.

This makes the application more than a simple database or statistics viewer. Its broader purpose is to connect **management, performance review, and improvement** within a single workflow.

---

## Features

### Management

- MySQL-backed member database
- Manager access to organizational member records
- Add new members
- Role-based access control
- Centralized member-data management

### Performance Tracking

- Track individual/team performance
- Store performance records in structured CSV datasets
- Add new performance records
- Persist performance-data changes
- View historical performance data

### Performance Review

- Tabular performance-data review
- Graphical performance visualization
- Compare rounds won and lost
- Review historical performance trends
- Provide a foundation for identifying areas of improvement

### Application Architecture

- Modular Python architecture
- Dedicated database layer
- Dedicated authentication layer
- Centralized validation utilities
- Dedicated performance-data management
- Dedicated visualization module
- Environment-based configuration
- Configurable data directories

### Reliability

- Input validation
- User ID validation
- Date validation
- CSV file validation
- CSV schema validation
- Database error handling
- Transaction rollback
- Explicit database connection cleanup
- Global exception handling

---

## What's New in v2.0.0

Version 2.0.0 is a substantial architectural and reliability upgrade over v1.0.0.

| Area | v1.0.0 | v2.0.0 |
| --- | --- | --- |
| Architecture | Monolithic | Modular |
| Database credentials | Hardcoded | Environment variables |
| File paths | Absolute Windows paths | Configurable paths |
| Performance-data updates | In-memory only | Persisted |
| Pandas append | `DataFrame.append()` | `pd.concat()` |
| Input validation | Scattered | Centralized |
| User ID validation | Basic | Six-digit validation |
| Username matching | Partial | Exact, case-insensitive |
| User ID matching | Containment | Exact comparison |
| Game selection | Repeated logic | Central mapping |
| Database operations | Embedded in menus | Dedicated module |
| Authentication | Embedded in main | Dedicated module |
| Data processing | Repeated logic | Dedicated module |
| Visualization | Embedded in main | Dedicated module |
| Database errors | Limited | Error handling + rollback |
| CSV errors | Limited | File/schema validation |
| Connection cleanup | Not explicit | Explicit cleanup |
| Configuration | Machine-specific | Portable/configurable |
| Secret handling | Hardcoded | `.env` + `.gitignore` |
| Maintainability | Low | Significantly improved |

---

## Current Use Case

ManageQuik is currently implemented around an **esports management scenario**.

The application models an organization where:

- A Manager oversees members
- IGLs lead teams
- Gamers participate in games
- Game performance is recorded
- Managers can review performance data
- Individuals can access their associated performance data
- Performance can be visualized to identify trends

The gaming domain was selected as a practical implementation scenario because performance is naturally measurable through structured metrics.

For the current implementation, those metrics include:

```
Games Won
Games Lost
Rounds Won
Rounds Lost
```

The domain can therefore be viewed as:

```
ManageQuik
    │
    ▼
Management Framework
    │
    ▼
Performance Tracking
    │
    ▼
Current Domain: Esports
```

The same underlying management approach could be adapted to other environments where people perform measurable work, such as:

```
Sales Teams
Customer Support Teams
Project Teams
Operations Teams
Training Programs
Sports Organizations
Educational Teams
```

The current gaming implementation is therefore a **use case of the management system rather than the definition of the product itself**.

---

## Tech Stack

- **Python 3.x** — Application development
- **MySQL** — Member and organizational data
- **MySQL Connector/Python** — Database connectivity
- **Pandas** — Performance-data processing
- **Matplotlib** — Performance visualization
- **python-dotenv** — Environment-based configuration
- **CSV** — Performance-data storage

---

## System Architecture

Version 2.0.0 separates the application according to responsibility.

```
                         ┌──────────────────┐
                         │     main.py      │
                         │ Application Flow │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
     ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
     │ authentication  │ │    database     │ │   validation    │
     │      .py        │ │      .py        │ │      .py        │
     └─────────────────┘ └────────┬────────┘ └─────────────────┘
                                  │
                                  ▼
                           ┌──────────────┐
                           │    MySQL     │
                           │ Member Data  │
                           └──────────────┘

              ┌───────────────────┴───────────────────┐
              │                                       │
              ▼                                       ▼
     ┌─────────────────┐                     ┌─────────────────┐
     │   game_data.py  │                     │ visualization.py│
     │                 │                     │                 │
     │ Load / Add /    │                     │ Tables / Graphs │
     │ Save Performance│                     │                 │
     │ Data            │                     │                 │
     └────────┬────────┘                     └─────────────────┘
              │
              ▼
        ┌─────────────┐
        │    data/    │
        │ CSV Files   │
        └─────────────┘
```

### Module Responsibilities

| Module | Responsibility |
| --- | --- |
| `main.py` | Application entry point, menus, and control flow |
| `database.py` | MySQL connection and member database operations |
| `authentication.py` | Authentication and role identification |
| `validation.py` | Reusable input and data validation |
| `game_data.py` | Loading, validating, modifying, and saving performance data |
| `visualization.py` | Performance tables and graphical visualizations |

This separation allows the management logic, data layer, validation, and visualization components to evolve independently.

---

## Supported Games

The current esports implementation supports:

| Game | Dataset |
| --- | --- |
| Valorant | `ValorantData.csv` |
| CS | `CSGOData.csv` |
| BGMI | `BGMIData.csv` |

Each dataset currently contains:

- Date
- Games Won
- Games Lost
- Rounds Won
- Rounds Lost

These metrics represent the current implementation of ManageQuik's broader performance-tracking concept.

---

## Setup

### Prerequisites

- Python 3.x
- MySQL Server
- pip

Install the required dependencies:

```
pip install mysql-connector-python pandas matplotlib python-dotenv
```

---

## Environment Configuration

Database credentials and local configuration are externalized through environment variables.

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=outset
GAME_DATA_DIR=data
```

### Configuration Variables

| Variable | Description | Example |
| --- | --- | --- |
| `DB_HOST` | MySQL server host | `localhost` |
| `DB_USER` | MySQL username | `root` |
| `DB_PASSWORD` | MySQL password | `your_password` |
| `DB_NAME` | MySQL database | `outset` |
| `GAME_DATA_DIR` | Performance-data directory | `data` |

The `.env` file should never be committed to version control.

---

## Database Setup

The current implementation uses a MySQL database named:

```
outset
```

Member information is stored in:

```
emp
```

A compatible database can be initialized using:

```sql
CREATE DATABASE outset;

USE outset;

CREATE TABLE emp (
    name VARCHAR(100),
    designation VARCHAR(20),
    dob DATE,
    username VARCHAR(50) UNIQUE,
    user_id INT UNIQUE,
    game_name VARCHAR(50)
);
```

Expected member fields:

```
name
designation
dob
username
user_id
game_name
```

---

## Running the Project

Ensure MySQL is running and the database is configured.

Place the performance datasets inside the configured data directory:

```
data/
├── ValorantData.csv
├── CSGOData.csv
└── BGMIData.csv
```

Then run:

```
python main.py
```

The application prompts for:

```
ENTER USERNAME -
ENTER USER ID -
```

After successful authentication, the user is directed to the appropriate role-based interface.

---

## User Roles

| Role | Primary Responsibility |
| --- | --- |
| **Manager** | Manage organizational information and review performance |
| **IGL** | Lead a team and maintain associated performance data |
| **Gamer** | Review associated performance data |

### Manager

Managers can:

- View organizational member information
- Add new members
- Access game-performance datasets
- Review performance data
- Add performance records
- Visualize performance information

### IGL

IGLs can:

- Access their associated game
- Review performance statistics
- Add performance records

### Gamer

Gamers can:

- Access their associated game
- Review performance data

The role model reflects the current esports implementation while providing a foundation for broader managerial permission systems.

---

## Authentication

Authentication currently uses:

```
Username
User ID
```

The User ID must contain exactly six digits.

The authentication process is:

```
Username + User ID
        │
        ▼
Load member records
        │
        ▼
Exact username comparison
        │
        ▼
Exact User ID comparison
        │
        ▼
Identify designation
        │
        ▼
Open role-specific interface
```

Username matching is exact and case-insensitive.

For example:

```
jay
```

will match:

```
jay
```

but not:

```
jayartha
jay123
```

---

## Performance Data

Performance data is currently stored as CSV files and processed using Pandas.

The data-management workflow is:

```
CSV
 ↓
Load
 ↓
Validate
 ↓
Review / Modify
 ↓
Save
 ↓
Updated Performance Data
```

### Adding Performance Records

Authorized users can enter:

```
Date
Games Won
Games Lost
Rounds Won
Rounds Lost
```

Version 2.0.0 persists these changes back to the appropriate CSV file.

This means:

```
Session 1
   ↓
Record Added
   ↓
CSV Updated
   ↓
Application Closed

Session 2
   ↓
Updated Record Still Available
```

### Data Validation

The application validates:

- File existence
- Required CSV columns
- Dates
- Numeric input
- Menu selections
- User IDs
- Non-empty text fields

---

## Application Flow

```
                         START
                           │
                           ▼
                  Load Configuration
                           │
                           ▼
                    Connect to MySQL
                           │
                           ▼
                    Load Member Data
                           │
                           ▼
                   Authenticate User
                           │
                           ▼
                    Identify Role
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
       Manager            IGL             Gamer
          │                │                │
          ▼                ▼                ▼
    Manage Members    Review/Edit      Review
          │            Performance     Performance
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                  Performance Analysis
                           │
                           ▼
                    Table / Graph
                           │
                           ▼
                  Close DB Connection
                           │
                           ▼
                          END
```

---

## Data Visualization

Performance visualization is isolated in:

```
visualization.py
```

The module provides graphical analysis of performance data.

Current visualizations include:

- Rounds Won
- Rounds Lost
- Date-based performance trends

Graphs include:

- Date on the X-axis
- Number of rounds on the Y-axis
- Legend
- Grid
- `Rounds Won & Lost` title
- Rotated date labels
- Automatic layout adjustment

The visualization layer is intentionally separate from the management and data-processing logic, allowing additional analytical features to be introduced without restructuring the rest of the application.

---

## Project Structure

```
ManageQuik/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env
│
├── main.py
├── database.py
├── authentication.py
├── validation.py
├── game_data.py
├── visualization.py
│
├── data/
│   ├── ValorantData.csv
│   ├── CSGOData.csv
│   └── BGMIData.csv
│
└── docs/
    └── screenshots/
```

### Architecture at a Glance

```
main.py
│
├── authentication.py
│   └── Authentication + Role Identification
│
├── database.py
│   └── MySQL Operations
│
├── validation.py
│   └── Input + Data Validation
│
├── game_data.py
│   └── Performance Data Management
│
└── visualization.py
    └── Performance Visualization
```

---

## Error Handling

Version 2.0.0 introduces structured error handling throughout the application.

### Input

Reusable validation handles:

- Integer input
- User IDs
- Menu choices
- Dates
- Yes/No responses
- Non-empty strings

### Database

Database operations use error handling and transaction rollback:

```
Execute
  │
  ├── Success ──► Commit
  │
  └── Failure ──► Rollback
```

### CSV

Game-data files are validated for:

- Existence
- Required schema
- Expected columns

### Application

Unexpected application-level exceptions are handled at the main application boundary.

`KeyboardInterrupt` is also handled to provide cleaner command-line termination.

---

## Security

ManageQuik is an educational management application and is **not intended to be production-grade authentication software**.

### v2.0.0 Security Improvements

Database credentials are no longer hardcoded into Python source files.

Configuration is supplied through:

```
.env
```

and should be excluded from version control using:

```
.gitignore
```

### Remaining Security Limitations

The current authentication system uses:

```
Username + User ID
```

rather than password-based authentication.

A production implementation should additionally consider:

- Secure password hashing
- Session management
- Granular authorization
- Restricted database permissions
- Secure secrets management
- Audit logging
- Access monitoring

---

## Known Limitations

ManageQuik v2.0.0 remains a command-line educational implementation.

### Domain-Specific Data Model

The current implementation is built around esports metrics. Adapting it to other management environments would require changes to the performance-data model.

### CSV-Based Performance Storage

Performance information is currently stored in CSV files rather than a centralized database.

### Authentication

Authentication remains based on username and User ID rather than a full credential and session-management system.

### Console Interface

The application currently operates through a command-line interface.

### Automated Testing

A comprehensive automated test suite has not yet been implemented.

---

## Future Improvements

Future development can focus on expanding ManageQuik from the current esports implementation into a more general management platform.

Potential improvements include:

- Migrate performance data from CSV to MySQL
- Introduce configurable performance metrics
- Support multiple management domains
- Add password-based authentication
- Introduce secure password hashing
- Implement session management
- Add granular role and permission management
- Add automated unit and integration tests
- Introduce structured logging and audit trails
- Add performance reports
- Add individual improvement recommendations
- Add manager dashboards
- Add historical performance comparisons
- Add team-level analytics
- Build a graphical interface
- Build a web-based management dashboard
- Add multi-user support
- Add automated reporting and exports
- Containerize the application using Docker

---

## Version History

### v2.0.0 — Modularization & Reliability Upgrade

Major architectural and functional upgrade.

Key changes:

- Renamed and positioned the application as **ManageQuik**
- Refactored the monolithic application into dedicated modules
- Separated management, database, authentication, validation, data-processing, and visualization responsibilities
- Moved database credentials to environment variables
- Added configurable performance-data paths
- Added `.env` and `.gitignore` support
- Added persistent performance-data updates
- Replaced deprecated `DataFrame.append()` usage
- Added centralized input validation
- Added six-digit User ID validation
- Added date validation
- Added exact username matching
- Added exact User ID matching
- Added CSV file and schema validation
- Added database transaction rollback
- Added explicit database connection cleanup
- Added global exception handling
- Corrected CS and BGMI game-detection logic
- Separated visualization functionality
- Reduced duplicated role and game logic
- Improved portability and maintainability

### v1.0.0 — Initial Release

The original implementation established the core management workflow:

- MySQL member management
- Username/User ID authentication
- Manager, IGL, and Gamer roles
- CSV-based performance data
- Performance visualization
- Member creation
- Command-line management menus

v2.0.0 builds upon that foundation by restructuring the implementation and improving reliability, portability, and maintainability.

---

## What I Learned

Developing ManageQuik provided practical experience with:

- Designing management-oriented software
- Translating a real-world management workflow into software
- Python application architecture
- Modular programming
- Separation of concerns
- MySQL database integration
- SQL operations from Python
- Database transactions and rollback
- Environment-based configuration
- Secure handling of local configuration
- Pandas DataFrame manipulation
- CSV data processing and persistence
- Input and data validation
- Role-based application design
- Error and exception handling
- File-system path management
- Performance visualization with Matplotlib
- Refactoring a monolithic application into maintainable modules
- Designing software around a real-world use case

---

## License

This project is licensed under the **MIT License**.

See the `LICENSE` file for the complete license text.
