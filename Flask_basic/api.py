###Put and delete_HTTP Verbs
### Working with API's--JSON
from flask import Flask, jsonify, request
app=Flask(__name__)
#initial data in my to-do list
items=[
    {'id':1,'task':'Do laundry',"name":'Item-1'},
    {'id':2,'task':'Read a book',"name":'Item-2'},
    
]

@app.route('/')
def home():
    return "Welcome to the Home Page of TO_DO APP"
#GET:retrieve all items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify({'items':items})
#GET:retrieve a specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'message':'Item not found'}),404
#POST:add a new item
@app.route('/items',methods=['POST'])
def add_item():
    new_item=request.get_json()
    items.append(new_item)
    return jsonify(new_item),201
#item=next((item for item in items if item['id']==item_id),None)
#if item is None:
#   return jsonify({'message':'Item not found'}),404
#return jsonify(item)
#PUT:update an existing item by id
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item:
        updated_data=request.get_json()
        item.update(updated_data)
        return jsonify(item)
    else:
        return jsonify({'message':'Item not found'}),404
#DELETE:remove an item by id
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({'message':'Item deleted'})

if__name__=='__main__':
app.run(debug=True)
#postman,post,raw-json