import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data
def load_data():
    # Replace with actual paths for Canadian data
    gdp_data = pd.read_csv('data/canadian_gdp_data.csv')
    unemployment_data = pd.read_csv('data/canadian_unemployment_data.csv')
    inflation_data = pd.read_csv('data/canadian_inflation_data.csv')
    interest_rate_data = pd.read_csv('data/canadian_interest_rate_data.csv')
    trade_balance_data = pd.read_csv('data/canadian_trade_balance_data.csv')
    consumer_confidence_data = pd.read_csv('data/canadian_consumer_confidence_data.csv')
    stock_market_data = pd.read_csv('data/canadian_stock_market_data.csv')
    housing_data = pd.read_csv('data/canadian_housing_market_data.csv')
    debt_gdp_data = pd.read_csv('data/canadian_debt_to_gdp_data.csv')
    business_investment_data = pd.read_csv('data/canadian_business_investment_data.csv')
    retail_sales_data = pd.read_csv('data/canadian_retail_sales_data.csv')
    manufacturing_data = pd.read_csv('data/canadian_manufacturing_data.csv')
    labor_force_data = pd.read_csv('data/canadian_labor_force_participation_data.csv')
    forex_data = pd.read_csv('data/canadian_forex_data.csv')

    return (gdp_data, unemployment_data, inflation_data, interest_rate_data, trade_balance_data, 
            consumer_confidence_data, stock_market_data, housing_data, debt_gdp_data, 
            business_investment_data, retail_sales_data, manufacturing_data, labor_force_data, forex_data)

# Function to plot data
def plot_kpi(data, title, ylabel):
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Value'], marker='o')
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Streamlit app layout
def main():
    st.title("Canadian Economic KPIs Dashboard")

    st.sidebar.header("Select KPI")
    kpi = st.sidebar.selectbox("KPI", (
        "GDP", 
        "Unemployment Rate", 
        "Inflation Rate", 
        "Interest Rates", 
        "Balance of Trade", 
        "Consumer Confidence Index", 
        "Stock Market Performance", 
        "Housing Market Indicators", 
        "Government Debt-to-GDP Ratio", 
        "Business Investment", 
        "Retail Sales", 
        "Manufacturing and Industrial Production", 
        "Labor Force Participation Rate", 
        "Foreign Exchange Rates"
    ))

    (gdp_data, unemployment_data, inflation_data, interest_rate_data, trade_balance_data, 
    consumer_confidence_data, stock_market_data, housing_data, debt_gdp_data, 
    business_investment_data, retail_sales_data, manufacturing_data, labor_force_data, forex_data) = load_data()

    if kpi == "GDP":
        st.header("Gross Domestic Product (GDP) of Canada")
        plot_kpi(gdp_data, "GDP Over Time", "GDP (in billions CAD)")
    
    elif kpi == "Unemployment Rate":
        st.header("Unemployment Rate in Canada")
        plot_kpi(unemployment_data, "Unemployment Rate Over Time", "Unemployment Rate (%)")
    
    elif kpi == "Inflation Rate":
        st.header("Inflation Rate (CPI) in Canada")
        plot_kpi(inflation_data, "Inflation Rate Over Time", "Inflation Rate (%)")
    
    elif kpi == "Interest Rates":
        st.header("Interest Rates in Canada")
        plot_kpi(interest_rate_data, "Interest Rates Over Time", "Interest Rate (%)")
    
    elif kpi == "Balance of Trade":
        st.header("Balance of Trade in Canada")
        plot_kpi(trade_balance_data, "Trade Balance Over Time", "Balance (in millions CAD)")
    
    elif kpi == "Consumer Confidence Index":
        st.header("Consumer Confidence Index in Canada")
        plot_kpi(consumer_confidence_data, "Consumer Confidence Over Time", "Index")
    
    elif kpi == "Stock Market Performance":
        st.header("Stock Market Performance (S&P/TSX Composite Index)")
        plot_kpi(stock_market_data, "S&P/TSX Composite Index Over Time", "Index Value")
    
    elif kpi == "Housing Market Indicators":
        st.header("Housing Market Indicators in Canada")
        plot_kpi(housing_data, "Housing Market Indicators Over Time", "Price (in thousands CAD)")
    
    elif kpi == "Government Debt-to-GDP Ratio":
        st.header("Government Debt-to-GDP Ratio in Canada")
        plot_kpi(debt_gdp_data, "Debt-to-GDP Ratio Over Time", "Debt-to-GDP Ratio (%)")
    
    elif kpi == "Business Investment":
        st.header("Business Investment in Canada")
        plot_kpi(business_investment_data, "Business Investment Over Time", "Investment (in billions CAD)")
    
    elif kpi == "Retail Sales":
        st.header("Retail Sales in Canada")
        plot_kpi(retail_sales_data, "Retail Sales Over Time", "Sales (in millions CAD)")
    
    elif kpi == "Manufacturing and Industrial Production":
        st.header("Manufacturing and Industrial Production in Canada")
        plot_kpi(manufacturing_data, "Manufacturing and Industrial Production Over Time", "Index")
    
    elif kpi == "Labor Force Participation Rate":
        st.header("Labor Force Participation Rate in Canada")
        plot_kpi(labor_force_data, "Labor Force Participation Rate Over Time", "Participation Rate (%)")
    
    elif kpi == "Foreign Exchange Rates":
        st.header("Foreign Exchange Rates (CAD to USD)")
        plot_kpi(forex_data, "Foreign Exchange Rates Over Time", "Exchange Rate (CAD/USD)")

if __name__ == "__main__":
    main()
