db = db.getSiblingDB("meal_menu");
db.createUser({
  user: "admin",
  pwd: "password",
  roles: [{ role: "readWrite", db: "meal_menu" }],
});
db.meals.insertOne({ name: "Spaghetti", description: "Delicious pasta with tomato sauce", price: 12 });
