from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__, template_folder="templates")

client = MongoClient(os.getenv("MONGO_URI"))
db = client.meal_menu
meals_collection = db.meals
orders_collection = db.orders
cart_collection = db.cart

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/menu")
def menu():
    meals = list(meals_collection.find())
    return render_template("menu.html", meals=meals)

@app.route("/add-meal", methods=["GET", "POST"])
def add_meal():
    if request.method == "POST":
        meal_name = request.form["name"]
        description = request.form["description"]
        price = float(request.form["price"])
        meals_collection.insert_one({"name": meal_name, "description": description, "price": price})
        return redirect(url_for("menu"))
    return render_template("add-meal.html")

@app.route("/cart")
def cart():
    cart_items = list(cart_collection.find())
    return render_template("cart.html", cart=cart_items)

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    meal_name = request.form["meal_name"]
    meal = meals_collection.find_one({"name": meal_name})
    if meal:
        cart_item = cart_collection.find_one({"name": meal_name})
        if cart_item:
            cart_collection.update_one({"name": meal_name}, {"$inc": {"quantity": 1}})
        else:
            meal["quantity"] = 1
            cart_collection.insert_one(meal)
    return redirect(url_for("menu"))

@app.route("/update-cart", methods=["POST"])
def update_cart():
    meal_name = request.form["meal_name"]
    action = request.form["action"]
    cart_item = cart_collection.find_one({"name": meal_name})
    if cart_item:
        if action == "increment":
            cart_collection.update_one({"name": meal_name}, {"$inc": {"quantity": 1}})
        elif action == "decrement":
            if cart_item["quantity"] > 1:
                cart_collection.update_one({"name": meal_name}, {"$inc": {"quantity": -1}})
            else:
                cart_collection.delete_one({"name": meal_name})
    return redirect(url_for("cart"))

@app.route("/place-order")
def place_order():
    cart_items = list(cart_collection.find())
    if cart_items:
        orders_collection.insert_one({"meals": cart_items})
        cart_collection.delete_many({})
    return render_template("place-order.html")

@app.route("/orders")
def orders():
    orders = list(orders_collection.find())
    return render_template("orders.html", orders=orders)

@app.route("/order-details/<order_id>")
def order_details(order_id):
    order = orders_collection.find_one({"_id": ObjectId(order_id)})
    return render_template("order-details.html", order=order)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
