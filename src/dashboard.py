import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sales_data.csv", parse_dates=["Date"])

st.title("📊 E-Commerce Sales Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Category", df["Category"].unique())
region_filter = st.sidebar.multiselect("Select Region", df["Region"].unique())

filtered_df = df.copy()

if category_filter:
    filtered_df = filtered_df[filtered_df["Category"].isin(category_filter)]

if region_filter:
    filtered_df = filtered_df[filtered_df["Region"].isin(region_filter)]

# KPI Cards
total_sales = (filtered_df["Quantity"] * filtered_df["Price"]).sum()
total_orders = len(filtered_df)
avg_order_value = total_sales / total_orders if total_orders > 0 else 0

st.metric("Total Sales (₹)", f"{total_sales:,.0f}")
st.metric("Total Orders", total_orders)
st.metric("Avg Order Value (₹)", f"{avg_order_value:,.0f}")

# Sales Trend
st.subheader("Sales Over Time")
filtered_df["Sales"] = filtered_df["Quantity"] * filtered_df["Price"]

sales_by_date = filtered_df.groupby("Date")["Sales"].sum()

fig, ax = plt.subplots()
sales_by_date.plot(ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Sales (₹)")
st.pyplot(fig)

# Category Breakdown
st.subheader("Sales by Category")

category_sales = filtered_df.groupby("Category")["Sales"].sum()

fig2, ax2 = plt.subplots()
category_sales.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Sales (₹)")
st.pyplot(fig2)

st.write("### Data Table")
st.dataframe(filtered_df)
