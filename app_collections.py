from flask import Flask, Response, request, jsonify, make_response
from pymongo import MongoClient
from bson import json_util, ObjectId

app = Flask('__name__')
app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False

r_client = app.test_client()
client = MongoClient(host='mongodb+srv://mariia:gifikew8-@flaskapp.2zik6.mongodb.net/test')
db = client.test


@app.route('/books', methods=['GET'])
def get_books():
    books = db.book.find()
    return Response(json_util.dumps(books),
                    status=200,
                    content_type="application/json")


@app.route('/books/add', methods=['POST'])
def post_book():
    print(request.get_json())
    author = request.json['author']
    title = request.json['title']
    db.book.insert_one({
        "author": author,
        "title": title})

    return Response("Object was created",
                    status=201,
                    content_type="application/json")


@app.route('/books/<id>/delete', methods=['DELETE'])
def delete_book(id):
    db.book.delete_one({"_id": ObjectId(id)})

    return Response({"message": "Object was deleted"},
                    status=204,
                    content_type="application/json")


@app.route('/books/<id>/edit', methods=['PUT'])
def edit_book(id):
    data = request.get_json()
    # iterating through keys
    author = request.json['author']
    title = request.json['title']
    book = db.book.find_one({'_id': ObjectId(id)})
    result = db.book.update_one({'_id': book.get('_id')}, {"$set": data})
    book = db.book.find_one({'_id': ObjectId(id)})
    return Response(json_util.dumps(book),
                    status=200,
                    content_type="application/json")


@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = db.book.find_one({'_id': ObjectId(id)})
    print(book)
    return Response(json_util.dumps(book),
                    status=200,
                    content_type="application/json")

#unit tests


if __name__ == '__main__':
    app.run(debug=True)

