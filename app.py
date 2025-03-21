from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Sabiha@231101',  # Replace with your MySQL password
    'database': 'personal_data'
}

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Create the persons table if it doesn't exist
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            telephone VARCHAR(15) NOT NULL,
            address VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Home route - Display form and table
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT name, surname, telephone, address, age FROM persons')
    persons = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', persons=persons)

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    surname = request.form['surname']
    telephone = request.form['telephone']
    address = request.form['address']
    age = request.form['age']

    # Validate data
    errors = []
    if not name:
        errors.append("Name is required.")
    if not surname:
        errors.append("Surname is required.")
    if not telephone or not telephone.isdigit() or len(telephone) != 8:
        errors.append("Telephone must be 8 digits.")
    if not address:
        errors.append("Address is required.")
    if not age or not age.isdigit():
        errors.append("Age must be a number.")

    if not errors:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO persons (name, surname, telephone, address, age)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, surname, telephone, address, age))
        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
