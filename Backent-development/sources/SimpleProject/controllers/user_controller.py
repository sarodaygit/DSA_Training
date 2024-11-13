# controllers/user_controller.py

from flask import Blueprint, request
from models.user_model import UserModel
from views.responses import response

user_controller = Blueprint('user_controller', __name__)

# Create an instance of UserModel to interact with the database
user_model = UserModel()

@user_controller.route('/api/add_user', methods=['POST'])
def add_user():
    try:
        user_data = request.json
        user_id = user_model.add_user(user_data)
        return response.success({"user_id": user_id}, "User added successfully", 201)
    except Exception as e:
        return response.error(str(e), 400)

@user_controller.route('/api/users', methods=['GET'])
def get_all_users():
    try:
        users = user_model.get_all_users()
        return response.success(users, "Users retrieved successfully")
    except Exception as e:
        return response.error(str(e), 400)

@user_controller.route('/api/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = user_model.get_user_by_id(user_id)
        if user:
            return response.success(user, "User retrieved successfully")
        return response.error("User not found", 404)
    except Exception as e:
        return response.error(str(e), 400)


# http://127.0.0.1:5000/api/users?name=<user_name>
@user_controller.route('/api/users/name', methods=['GET'])
def get_user_by_name():
    try:
        name = request.args.get('name')  # Get 'name' from query parameters
        
        if not name:
            return response.error("Name is required", 400)
        
        # Call the method to retrieve the user by username
        user = user_model.get_user_by_name(name)
        
        if user:
            return response.success(user, "User retrieved successfully")
        return response.error("User not found", 404)
    except Exception as e:
        return response.error(str(e), 400)

@user_controller.route('/api/users/name', methods=['DELETE'])
def delete_user_by_name():
    try:
        name = request.args.get('name')  # Get 'name' from query parameters

        if not name:
            return response.error("Name is required", 400)

        # Call the method to delete the user by username
        success = user_model.delete_user_by_name(name)
        
        if success:
            return response.success({}, "User deleted successfully")
        return response.error("User not found", 404)
    
    except Exception as e:
        return response.error(str(e), 400)
    

@user_controller.route('/api/users/count', methods=['GET'])
def get_user_count():
    try:
        count = user_model.get_user_count()
        return response.success({"count": count}, "Total users retrieved successfully")
    except Exception as e:
        return response.error(str(e), 400)
    
@user_controller.route('/api/users/age', methods=['GET'])
def get_users_by_age():
    try:
        # You can pass the minimum age as a query parameter
        min_age = int(request.args.get('min_age', 25))  # Default to 25 if not provided
        users = user_model.get_users_by_age(min_age)
        
        if users:
            return response.success(users, f"Users with age >= {min_age} retrieved successfully")
        return response.error("No users found with the given age criteria", 404)
    except Exception as e:
        return response.error(str(e), 400)