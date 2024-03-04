import sqlite3

conn = sqlite3.connect('recipe_finder_app.db')

cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Recipes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    instructions TEXT,
    nutritional_info TEXT,
    api_source TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES Recipes (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS SavedRecipes (
    user_id INTEGER,
    recipe_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users (id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes (id)
)
''')

conn.commit()

conn.close()
