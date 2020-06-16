from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name' : 'DMart',
        'items' : [{'name' : 'chair', 'price' : '900'}]
    },
    {
        'name': 'rMart',
        'items': [ ]
    }
]

@app.route('/getallstores')
def getall():
    return jsonify( {'output' : stores} )


@app.route('/addstore', methods = ['POST'])
def addstore():
    # No need to take parameter in input since we are taking json input using below line.
    store_data = request.get_json()

    for each_store in stores:
        if each_store['name'] == store_data['name']:
            return jsonify({'message' : 'Store Already Exists'})

    stores.append(store_data)
    return jsonify( {'message' : 'store added'} )


@app.route('/findstore/<string:store_name>')
def search_store(store_name):
    for each_store in stores:
        if each_store['name'] == store_name:
            return jsonify(each_store)  # each_store is already a dictionary. No need to convert that into a dictionary.

    return jsonify( {'message' : 'Store not found in records.'} )


@app.route('/additem/<string:store_name>', methods=['POST'])
def add_item(store_name):

    item_data = request.get_json()

    # for each_store in stores:
    #     if each_store['name'] == store_name:
    #         each_store['items'].append(item_data)
    #         return jsonify({'message': 'Item Added..!!!'})
    #
    # return jsonify({'message': 'Store not found in records, could not add item'})

    for each_store in stores:
        if each_store['name'] == store_name:
            for item in each_store['items']:
                if item['name'] == item_data['name']:
                    return jsonify( {'message' : 'Item Already Exists'} )

                each_store['items'].append(item_data)
                return jsonify( { 'message' : 'Item Added..!!!' } )

    return jsonify( {'message' : 'Store not found in records, could not add item' } )


app.run(port=5000)