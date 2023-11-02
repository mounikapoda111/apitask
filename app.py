from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (Make sure your MongoDB server is running)
client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']
print(db)
collection = db['test_collection']

# Create operation - Add a new document
@app.route('/items', methods=['POST'])
def create_item():
    item_data = request.get_json()
    result = collection.insert_one(item_data)
    print(result)
    return jsonify({'message': 'Item created', 'inserted_id': str(result.inserted_id)}), 201

# Read operation - Get all documents
@app.route('/items', methods=['GET'])
def get_all_items():
    items = list(collection.find())
    return jsonify({'items': items})

# Read operation - Get a specific document by ID
@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = collection.find_one({'_id': item_id})
    if item:
        return jsonify({'item': item})
    return jsonify({'message': 'Item not found'}, 404)

# Update operation - Update a specific document by ID
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.get_json()
    result = collection.update_one({'_id': item_id}, {'$set': item_data})
    if result.modified_count:
        return jsonify({'message': 'Item updated'})
    return jsonify({'message': 'Item not found'}, 404)

# Delete operation - Delete a specific document by ID
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    result = collection.delete_one({'_id': item_id})
    if result.deleted_count:
        return jsonify({'message': 'Item deleted'})
    return jsonify({'message': 'Item not found'}, 404)

if __name__ == '__main__':
    app.run(debug=True)
