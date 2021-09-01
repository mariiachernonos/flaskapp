# from flask import Flask, Response, request, jsonify, make_response
# from models import Book
# from flask_mongoengine import MongoEngine
#
# app = Flask('__name__')
# app.config['DEBUG'] = True
# app.config['JSON_AS_ASCII'] = False
# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb+srv://mariia:gifikew8-@flaskapp.2zik6.mongodb.net/test'
# }
#
# client = app.test_client()
# db = MongoEngine(app)
#
#
# @app.route('/books', methods=['GET'])
# def get_books():
#     books = Book.objects()
#     print(books[0])
#     return make_response(jsonify(books), 200)
#
#
# @app.route('/books/add', methods=['POST'])
# def post_book():
#     book = Book(**request.form)
#     book.save()
#     return make_response(jsonify(book), 201)
#
#
# @app.route('/books/<id>/delete', methods=['DELETE'])
# def delete_book(id):
#     book = Book.objects().filter(id=id)
#     book.delete()
#     return make_response('{"message": "Object was successfully deleted"}', 204)
#
#
# @app.route('/books/<id>/edit', methods=['PUT'])
# def edit_book(id):
#     book = Book.objects().filter(id=id)
#     book.update(**request.form)
#     return make_response(jsonify(book), 204)
#
#
# @app.route('/books/<id>', methods=['GET'])
# def get_book(id):
#     book = Book.objects().filter(id=id)
#     return make_response(jsonify(book), 200)
#
#
# #unit tests
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

