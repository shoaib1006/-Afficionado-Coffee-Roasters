# Afficionado Coffee Roasters Sales Analysis & Forecasting

This project provides a comprehensive data-driven analysis for Afficionado Coffee Roasters, focusing on sales forecasting and peak demand detection for three locations: Astoria, Hell's Kitchen, and Lower Manhattan.

## Project Objectives
- **Timeline Reconstruction**: Inferred dates from 180 time-resets in transaction sequences (Jan - June 2025).
- **Daily Sales Forecasting**: Predicted revenue using Facebook Prophet with high accuracy (~$248 MAE).
- **Peak Demand Detection**: Identified consistent 'rush hour' windows (08:00 - 10:00 AM) to optimize staffing.
- **Interactive Dashboard**: A Streamlit application for real-time operational insights.

## Repository Structure
- `Afficionado Coffee Roasters.xlsx`: Raw transaction data.
- `app.py`: Streamlit dashboard source code.
- `requirements.txt`: Python dependencies.
- `Analysis_Notebook.ipynb`: Full data processing and modeling pipeline.

## How to Run the Dashboard
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```

## Key Insights
- **Staffing**: Prioritize shift coverage between 07:00 AM and 11:00 AM, especially in Lower Manhattan where demand surges early.
- **Inventory**: Leverage weekly seasonality trends to adjust stock levels for high-volume periods (weekends vs weekdays).