from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version="1.0", title="Book Application", description="A simple Book Application")

# Define a namespace for books
ns = api.namespace("books", description="Book operations")

# Define the book model
book_model = api.model("Book", {
    "id": fields.Integer(readOnly=True, description="The unique identifier of a book"),
    "title": fields.String(required=True, description="The title of the book"),
    "author": fields.String(required=True, description="The author of the book")
})

# In-memory storage for books
books = []
book_counter = 1

# Route for listing books (GET)
@api.route("/books/list")
class BookList(Resource):
    """Shows a list of all books"""
    
    @ns.doc("list_books")
    @ns.marshal_list_with(book_model)
    def get(self):
        """List all books"""
        return books

# Route for adding a new book (POST)
@api.route("/books/add")
class BookAdd(Resource):
    """Add a new book"""
    
    @ns.doc("create_book")
    @ns.expect(book_model)
    @ns.marshal_with(book_model, code=201)
    def post(self):
        """Create a new book"""
        global book_counter
        book = api.payload
        book["id"] = book_counter
        books.append(book)
        book_counter += 1
        return book, 201

# Route for getting a specific book (GET) and deleting a book (DELETE)
@api.route("/books/<int:id>")
@ns.param("id", "The book identifier")
class Book(Resource):
    """Show a single book item and lets you delete a book"""
    
    @ns.doc("get_book")
    @ns.marshal_with(book_model)
    def get(self, id):
        """Fetch a given book"""
        for book in books:
            if book["id"] == id:
                return book
        api.abort(404, "Book not found")

    @ns.doc("delete_book")
    @ns.response(204, "Book deleted")
    def delete(self, id):
        """Delete a book given its identifier"""
        global books
        books = [book for book in books if book["id"] != id]
        return "", 204

# Add the namespace to the API
api.add_namespace(ns)

if __name__ == "__main__":
    app.run(debug=True)
