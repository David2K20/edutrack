# Django-Student-Management-System 
The **Student Management System** is a web-based application designed to streamline student data management for educational institutions. Built using Django, Bootstrap, and JavaScript, the system provides intuitive interfaces for administrators, and students to manage and access key information.  

## Features  

### Administrator Features  
- Add, update, and delete student details.  
- View detailed student profiles, including:  
  - Matric number  
  - Image  
  - CGPA  
  - Department  
  - Email   

### Student Features  
- Sign up, login, and logout functionality.  

## Technology Stack  

### Backend  
- **Django** (v5.1.1): Python-based web framework for rapid development and clean, pragmatic design.  

### Frontend  
- **HTML5**  
- **CSS3**  
- **Bootstrap**: For responsive and visually appealing design.  
- **JavaScript**  

### Database  
- Initially **SQLite**, now migrated to **MySQL** (Database Name: `sql_edutrack`).  

---

## Prerequisites  

Before setting up the application, ensure you have the following tools and technologies installed on your system:  
- **Python** (v3.8 or higher): Download and install it from [python.org](https://www.python.org/downloads/).  
- **MySQL**: Install and configure MySQL, ensuring a database named `sql_edutrack` is created.  
- **pip**: Python's package manager, included with Python installations.  
- **Virtual Environment Manager** (e.g., `venv` or `virtualenv`): Optional but recommended for dependency isolation.  
- **Git**: For cloning the project repository.  

---

# Installation

### 1. Create a Folder for Your Project  
### 2. Create a Virtual Environment and Activate It

### Install Virtual Environment

```bash
$ pip install virtualenv
```

### Create Virtual Environment

#### For Windows 

```bash
$ python -m venv venv
```

#### For Mac 

```bash
$ python3 -m venv venv
```

### Acivate Virtual Environment

#### For Windows 

```bash
$ source venv\scripts\activate
```

#### For Mac 

```bash
$ source venv\bin\activate
```

### 3. Clone this project

```bash
$ git clone https://github.com/David2K20/Django-Student-Management-System.git
```

#### Then, Enter the project

```bash
$ cd Django-Student-Mangement-System
```

### 4. Configure the Database
- Go to the settings.py file
- Ensure the database named **sql_edutrack** is created in MySQL. Modify the DATABASES section as follows:

```bash
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'sql_edutrack',  
        'USER': 'your-mysql-username',  
        'PASSWORD': 'your-mysql-password',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
    }  
}  
```

### 5. Apply Migrations

```bash
$ python manage.py makemigrations  
```

```bash
$ python manage.py migrate  
```

### 6. Create a Superuser

```bash
$ python manage.py createsuperuser  
```

### 7. Run the Development server

```bash
$ python manage.py runserver
```

---

## Sponsor

This project is open for sponsorship! If you're interested in sponsoring the development or further enhancements of this project, please contact us via the email below.

Email: [oreoluwadavid08@gmail.com](mailto:oreoluwadavid08@gmail.com)

---

## Project Enquiries

For any questions, suggestions, or collaboration opportunities, feel free to reach out.

Email: [oreoluwadavid08@gmail.com](mailto:oreoluwadavid08@gmail.com)

---

Thank you for your support!
