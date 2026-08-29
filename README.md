# Outset — Gaming Management System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

A Python-based command-line management system for **Outset**, an esports organization. The application combines a MySQL member database with CSV-based game performance data to provide role-based access for Managers, In-Game Leaders (IGLs), and Gamers.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Overview](#system-overview)
- [Supported Games](#supported-games)
- [Setup](#setup-one-time-only)
- [Running the Project](#running-the-project)
- [Database Setup](#database-setup)
- [User Roles](#user-roles)
- [Game Data](#game-data)
- [Project Structure](#project-structure)
- [Application Flow](#application-flow)
- [Data Visualization](#data-visualization)
- [Security Notes](#security-notes)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [What I Learned](#what-i-learned)
- [License](#license)

---

## Features

- MySQL-backed Outset member database
- Username and six-digit User ID authentication
- Role-based access for Managers, IGLs, and Gamers
- Manager access to the complete Outset member database
- Add new members to the organization
- Validation for usernames and User IDs
- Support for Valorant, CS:GO, and BGMI
- View game performance data in table format
- Visualize rounds won and lost using Matplotlib
- Add new game-performance records
- CSV-based game data management
- Interactive command-line menus
- Basic input validation and error handling through menu loops

## Tech Stack

- Python 3.x
- MySQL
- MySQL Connector/Python
- Pandas
- Matplotlib
- CSV

---

## System Overview

The application acts as a small management system for an esports organization.

Member information is stored in a MySQL database, while individual game statistics are maintained in CSV datasets. After logging in, the application identifies the user's designation and provides the functionality associated with that role.

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Username + User ID │
                    │    Authentication   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   MySQL Member DB   │
                    │    (emp table)      │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │   Manager   │       │ IGL / Gamer │
             └──────┬──────┘       └──────┬──────┘
                    │                     │
          ┌─────────┴─────────┐           │
          ▼                   ▼           ▼
   Member Database       Game Data    Game Data
   View / Add             View/Edit    View/Edit
          │                   │           │
          └───────────────────┴───────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Pandas + Matplotlib │
                    │ Table / Graph View  │
                    └─────────────────────┘
```

---

## Supported Games

The application currently supports three games:

| Game | Dataset |
|---|---|
| Valorant | `ValorantData.csv` |
| CS:GO | `CSGOData.csv` |
| BGMI | `BGMIData.csv` |

Game performance records contain:

- Date
- Games Won
- Games Lost
- Rounds Won
- Rounds Lost

---

## Setup (one time only)

### Prerequisites

Make sure the following are installed:

- Python 3.x
- MySQL Server
- pip

Install the required Python packages:

```bash
pip install mysql-connector-python pandas matplotlib
```

---

## Running the Project

### 1. Start MySQL

Make sure the MySQL server is running and the `outset` database has been created.

### 2. Configure the CSV files

The current implementation expects the game datasets at:

```text
C:\IP_Project_File\
```

with the following files:

```text
C:\IP_Project_File\ValorantData.csv
C:\IP_Project_File\CSGOData.csv
C:\IP_Project_File\BGMIData.csv
```

If you move the project to another computer, update these paths in the Python source.

### 3. Run the application

```bash
python <filename>.py
```

The application will prompt for:

```text
ENTER USERNAME -
ENTER USER ID -
```

After successful authentication, the appropriate role-based menu will be displayed.

---

## Database Setup

The application connects to a MySQL database named:

```text
outset
```

and reads member information from the:

```text
emp
```

table.

The application expects member records containing the following fields:

```text
name
designation
dob
username
user_id
game_name
```

A compatible database can be initialized with:

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

The Python application currently connects using credentials defined directly in the source code. Update them to match your local MySQL installation.

> **Security:** Do not commit real database credentials to a public repository.

---

## User Roles

The application supports three designations.

| Role | Capabilities |
|---|---|
| **Manager** | View/edit game data and access the Outset member database |
| **IGL** | View/edit the game data associated with the IGL |
| **Gamer** | View the game data associated with the Gamer |

### Manager

Managers have the highest level of access in the application.

They can:

- Access game datasets
- View game data
- Add game-performance records
- View the Outset member database
- Add new members to the database

### IGL

An IGL can access the game associated with their member record and:

- View game statistics
- Add new game-performance records

### Gamer

A Gamer can access the game associated with their member record and view its performance data.

---

## Authentication

The application uses two pieces of information for login:

```text
Username
User ID
```

The User ID is expected to contain exactly six digits.

The system:

1. Loads the member database from MySQL.
2. Searches for the supplied username.
3. Validates the corresponding User ID.
4. Identifies the user's designation.
5. Opens the appropriate role-specific interface.

Supported designations are case-sensitive:

```text
Manager
IGL
Gamer
```

---

## Game Data

Game datasets are loaded using Pandas.

For example:

```python
d3 = pd.read_csv("C:\\IP_Project_File\\ValorantData.csv")
d3 = d3.dropna()
```

The same approach is used for the CS:GO and BGMI datasets.

### Adding a Record

Authorized users can enter:

```text
Date
Games Won
Games Lost
Rounds Won
Rounds Lost
```

The information is added to the active Pandas DataFrame during the current program session.

---

## Application Flow

```text
Start
  │
  ▼
Connect to MySQL
  │
  ▼
Load emp table
  │
  ▼
Enter Username + User ID
  │
  ▼
Validate Login
  │
  ├── Invalid Username ──► Re-enter Details
  │
  ├── Invalid User ID ───► Re-enter Details
  │
  ▼
Identify Designation
  │
  ├── Manager
  │      ├── Game Data
  │      │     ├── View
  │      │     └── Edit
  │      │
  │      └── Member Database
  │            ├── View
  │            └── Add Member
  │
  ├── IGL
  │      └── Associated Game
  │            ├── View
  │            └── Edit
  │
  └── Gamer
         └── Associated Game
               └── View
```

---

## Data Visualization

The `view()` function provides two ways to inspect game statistics:

### Table Format

Prints the complete Pandas DataFrame to the terminal.

### Graph Format

Matplotlib is used to visualize:

- Rounds Won
- Rounds Lost
- Date

The graph includes:

- Date on the X-axis
- Number of rounds on the Y-axis
- Grid
- Legend
- `Rounds Won & Lost` title

The visualization is generated directly from the currently loaded game DataFrame.

---

## Project Structure

A recommended repository structure is:

```text
Outset/
├── README.md
├── LICENSE
├── main.py
├── data/
│   ├── ValorantData.csv
│   ├── CSGOData.csv
│   └── BGMIData.csv
└── docs/
    └── screenshots/
```

The original implementation currently references the CSV files through an absolute Windows path rather than the relative `data/` structure shown above.

---

## Security Notes

This project is primarily an educational implementation and is **not production-ready authentication software**.

Important considerations:

- MySQL credentials are currently stored directly in the source code.
- Authentication uses a username and User ID rather than a password.
- CSV files are accessed directly from the local filesystem.
- There is no dedicated authentication/session framework.
- Database permissions should be restricted in a production deployment.
- User input validation should be strengthened before production use.

For example, credentials should not be hard-coded like:

```python
passwd="1234"
```

Instead, production implementations should use environment variables or a secure secrets-management system.

---

## Known Limitations

The current source contains several implementation details that should be addressed before production use.

### CSV Changes Are Not Persisted

Game records are added to the Pandas DataFrame in memory. The current implementation does not write the modified DataFrame back to its CSV file.

As a result, newly added game records may be lost when the application exits.

### Absolute File Paths

The application uses paths such as:

```text
C:\IP_Project_File\ValorantData.csv
```

This makes the project dependent on a particular Windows directory structure.

### Deprecated Pandas API

The source uses:

```python
DataFrame.append()
```

This method has been removed from current Pandas versions. A modern implementation should use `pd.concat()` or another supported approach.

### Input Handling

Several values are directly converted using `int()`. Non-numeric input can therefore raise an exception instead of being handled gracefully.

### Authentication

The current authentication mechanism is based on username and User ID matching and should not be considered secure authentication for a real-world application.

### Source Compatibility

The supplied implementation contains some code-level issues that may require correction when running it with current Python/Pandas/Matplotlib versions. This README documents the intended functionality of the project rather than silently modifying the original implementation.

---

## Future Improvements

- Move database credentials to environment variables
- Replace absolute file paths with configurable relative paths
- Persist game-data changes back to CSV
- Consider migrating game statistics into MySQL
- Add password-based authentication with secure password hashing
- Add stronger input validation and exception handling
- Refactor repeated role/game logic into reusable functions
- Separate database, authentication, data-processing, and visualization modules
- Add automated tests
- Add logging for administrative operations
- Build a graphical or web-based interface
- Introduce more granular role and permission management
- Improve portability across operating systems

---

## What I Learned

- Connecting Python applications to MySQL databases
- Performing SQL operations from Python
- Working with Pandas DataFrames
- Reading and processing CSV datasets
- Implementing role-based application flows
- Validating user input
- Building interactive command-line applications
- Visualizing data using Matplotlib
- Combining database management with data analysis in a single application

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
