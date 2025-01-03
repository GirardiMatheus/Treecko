# Treecko

Treecko is an expense management software developed in Python using FastAPI. It helps users manage balances, accounts, debts, and transactions, and generates monthly reports in spreadsheet format.

## Project Structure

```
Treecko/
├── backend/                  # Backend of the system
│   ├── app/
│   │   ├── api/              # FastAPI routes
│   │   ├── core/             # Core configurations
│   │   ├── models/           # ORM models definitions
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   ├── utils/            # Utilities (reports, helpers)
│   │   ├── main.py           # Application entry point
│   ├── tests/                # Automated tests
├── .gitignore                # Git ignore file
├── requirements.txt          # Project dependencies
└── README.md                 # Initial project documentation
```

## Main Features
- **Balance by Account:** Manage balances in accounts such as savings, emergency funds, and investments.
- **Debt Management:** Track platforms and amounts.
- **Transaction Registration:** Add income and expenses with descriptions.
- **Monthly Reports:** Export transactions to Excel format.

## Initial Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/youruser/treecko.git
   cd treecko/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Contribution
1. Fork the project.
2. Create a branch for your feature:
   ```bash
   git checkout -b feat-my-feature
   ```
3. Make clear and objective commits.
4. Open a Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
