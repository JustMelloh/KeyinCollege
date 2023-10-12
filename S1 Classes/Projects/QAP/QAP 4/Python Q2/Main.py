# Generate a program that will allow the user to input the amount of sales for each month from Jan - Dec
# Written by: Austin R
# Created on July 20/2023


# Libraries needed.

import math
import calendar
import matplotlib.pyplot as plt
import Functions


sales_by_month = []

for month in range(1, 13):
        month_name = calendar.month_name[month]
        try:
            sales = float(input(f"Enter total sales for {month_name} (Enter 0 if not available): "))
            sales_by_month.append(sales)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        for month, sales in enumerate(sales_by_month, start=1):

            month_name = calendar.month_name[month]
            
Functions.create_sales_graph(sales_by_month)

