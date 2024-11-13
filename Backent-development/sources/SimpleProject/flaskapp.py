# app.py

from flask import Flask
from controllers.user_controller import user_controller

app = Flask(__name__)

# Register the user controller blueprint
app.register_blueprint(user_controller)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
