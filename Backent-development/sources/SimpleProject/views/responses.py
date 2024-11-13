# views/responses.py

from flask import jsonify

class Response:
    @staticmethod
    def success(data, message, status_code=200):
        return jsonify({"message": message, "data": data}), status_code

    @staticmethod
    def error(message, status_code=400):
        return jsonify({"error": message}), status_code

# Create an instance of Response for easy access
response = Response()
