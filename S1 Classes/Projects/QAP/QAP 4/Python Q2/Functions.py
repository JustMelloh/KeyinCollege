
# Create sales graph
import matplotlib
import matplotlib.pyplot as plt


def create_sales_graph(sales_by_month):
    monthsLst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Check if the length of sales_by_month is 12. If not, fill the remaining months with 0.
    if len(sales_by_month) < 12:
        sales_by_month += [0] * (12 - len(sales_by_month))

    # Plot the graph
    fig, ax = plt.subplots()
    x = monthsLst
    y = sales_by_month
    ax.bar(x,y, align ='center')
    
    plt.title("Total Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()

    # Display the graph
    plt.show()