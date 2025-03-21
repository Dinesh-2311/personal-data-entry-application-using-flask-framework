# personal-data-entry-application-using-flask-framework

This is a Flask-based web application for managing personal data. It allows users to submit their personal information (name, surname, telephone, address, and age) through a form, which is then stored in a MySQL database. The application also displays all submitted data in a table.

## Features
- Submit personal data through a web form.
  ![image](https://github.com/user-attachments/assets/5d4efb12-2175-4aab-a9a5-c5a01237cead)

- Store data in a MySQL database.
  ![image](https://github.com/user-attachments/assets/5480a201-c6b2-4ee0-87b6-2d05c8da32ff)

- Display all stored data in a table.
  ![image](https://github.com/user-attachments/assets/3bad6408-e717-4dc5-855a-6a70c3d2473c)

- Responsive and clean user interface.
  
## Prerequisites
- Python 3.x
- MySQL Server
- Flask
- PyMySQL

## Installation

1. **Clone the repository:**
   git clone https://github.com/Dinesh-2311/personal-data-entry-application-using-flask-framework.git

 2. **Set up a virtual environment (optional but recommended):**
 python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **installation dependenices:**
pip install -r requirements.txt

4. **Set up the MySQL database:**
Create a database named personal_data.
Update the database configuration in app.py with your MySQL credentials:

db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'xxxxxxxxxxx',  # Replace with your MySQL password
    'database': 'personal_data'
}
![Uploading Screenshot 2025-03-22 000906.png…]()

5. **Run the application:**

Run application by clicking python file which is named as app.py

![image](https://github.com/user-attachments/assets/f19afc28-b9a0-4c0c-a88a-8b9ee4716336)


6. **Access the application:**
Open your browser and go to http://localhost:5000.
![image](https://github.com/user-attachments/assets/23c6ba71-0740-49bd-89b2-bf98ed056eec)


8. **project structure:**

![image](https://github.com/user-attachments/assets/6f9a043a-cf88-476f-9e49-02fd5117dfbb)




