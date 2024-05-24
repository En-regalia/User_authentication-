# User Authentication Web Page

This project is a user authentication web page built using Flask. It provides functionalities for user registration, login, and logout, along with basic session management. This README file will guide you through setting up, running, and understanding the structure of the project.

## Features
User Registration
User Login
User Logout
Password Hashing

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your machine
- pip (Python package installer) installed
- virtualenv installed (optional but recommended)

## Installation

### Clone the Repository


```
git clone https://github.com/yourusername/User_authentication-](https://github.com/En-regalia/User_authentication-.git
cd your-repo-name
```

### Create a Virtual Environment

```python -m venv venv```

### Activate the Virtual Environment

On Windows:

```venv\Scripts\activate```

On macOS and Linux:

```source venv/bin/activate```

### Install Dependencies

```pip install -r requirements.txt```


## Running the Application

Initialize the Database
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
### Run the Flask Application

``` Python app.py ```

The application will be available at http://127.0.0.1:5000.

## Project Structure
_Currently Projected. Still Work in progress_
```
User_authentication-
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       └── home.html
│
├── migrations/
│
├── static/
│
├── .env
├── .gitignore
├── run.py
├── config.py
├── requirements.txt
└── README.md
```
## Usage

### Register
Navigate to /register to create a new user account.

### Login
Navigate to /login to log in with your credentials.

### Logout
Navigate to /logout to log out of the application.

## Contributing

If you would like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Make your changes.
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
If you have any questions or feedback, feel free to contact us at mike.ranner1@gmail.com
