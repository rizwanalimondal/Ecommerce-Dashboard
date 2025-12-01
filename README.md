# Ecommerce Dashboard

This project is a simple ecommerce sales dashboard built using Python, Pandas and Streamlit.  
The goal is to demonstrate basic data analysis and interactive visualization using a small sample dataset.

The dashboard provides a quick overview of sales trends, category performance and key summary metrics.

## Features

- Sales trend over time
- Category-wise sales comparison
- Basic KPIs including total sales, number of orders and average order value
- Filters for category and region
- Interactive data table

## Project Structure

```
Ecommerce-Dashboard/
│
├── data/
│   └── sales_data.csv
│
├── src/
│   └── dashboard.py
│
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository:
   git clone https://github.com/rizwanalimondal/Ecommerce-Dashboard.git

2. Navigate into the project directory:
   cd Ecommerce-Dashboard

3. Install dependencies:
   python -m pip install -r requirements.txt

4. Run the Streamlit app:
   python -m streamlit run src/dashboard.py

5. Open the browser at:
   http://localhost:8501

## Tech Stack

- Python
- Pandas
- Streamlit
- Matplotlib

## Future Improvements

- Add date range filters
- Add more detailed charts and comparisons
- Use a larger dataset for deeper analysis
- Deploy the dashboard online

## Author

Rizwan Ali Mondal
