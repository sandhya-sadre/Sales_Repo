# Create a Flask API that reads sales_data.csv file and returns total revenue
# the API should have an endpoint /total_revenue that returns the total revenue as a JSON response
# the structure of the sales_data.csv file is as follows:
# order_id,product,region,sales,order_date
# 1001,Monitor,South,1306,2024-12-26
# the total revenue can be calculated by summing up the sales column
# convert the total revenue to an integer and return it as a JSON response.
# Additionally, create another endpoint /highest_region that returns the region 
# with the highest sales along with the total sales for that region as a JSON response.

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
@app.route('/total_revenue', methods=['GET'])
def total_revenue():
    # Read the sales_data.csv file
    sales_data = pd.read_csv('sales_data.csv')
    
    # Calculate total revenue by summing up the sales column
    total_revenue = sales_data['sales'].sum()
    
    # Return the total revenue as a JSON response
    return jsonify({'total_revenue': int(total_revenue)})

@app.route('/highest_region', methods=['GET'])
def highest_region():
    # Read the sales_data.csv file
    sales_data = pd.read_csv('sales_data.csv')
    
    # Group by region and sum the sales for each region
    region_sales = sales_data.groupby('region')['sales'].sum()
    
    # Find the region with the highest sales
    highest_region = region_sales.idxmax()
    highest_sales = region_sales.max()
    
    # Return the highest region and its total sales as a JSON response
    return jsonify({'highest_region': highest_region, 'total_sales': int(highest_sales)})
    
if __name__ == '__main__':
    app.run(debug=True)

