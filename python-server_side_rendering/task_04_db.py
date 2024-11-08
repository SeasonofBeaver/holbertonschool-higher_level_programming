#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                row['id'] = int(row.get('id', 0))
                row['price'] = float(row.get('price', 0.0))
            except ValueError:
                row['id'] = 0
                row['price'] = 0.0

            row['name'] = row.get('name', 'N/A')
            row['category'] = row.get('category', 'N/A')
            products.append(row)
    return products

def fetch_data_from_sqlite():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        products = cursor.fetchall()
        conn.close()
        return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
    except sqlite3.Error as e:
        print(f"Database error: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    with open('items.json') as json_file:
        data = json.load(json_file)
        items_list = data.get("items", [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == "json":
        products = read_json_file('products.json')
    elif source == "csv":
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = fetch_data_from_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source. Please specify 'json' or 'csv'.")

    if product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
