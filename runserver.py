"""
This script runs the project2 application .
the server will running on http://localhost:5000/
"""
import platform
from os import environ
from project2 import create_app
app=create_app()
if __name__ == '__main__':
    if platform.system() == 'Windows' :
        HOST = environ.get('SERVER_HOST', 'localhost')
    else:
        HOST = environ.get('SERVER_HOST', '0.0.0.0')
    PORT = 5000
    app.run(HOST, PORT , debug=True)
