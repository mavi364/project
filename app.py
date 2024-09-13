from flask import Flask, jsonify,request
from datetime import datetime
from model.connection import collection
from model.crud import Crud

app=Flask(__name__)
crud=Crud()

@app.route('/admins', methods=['GET'])
def get_all_data():
    documents = collection.find()
    result = []
    for doc in documents:
        doc['_id'] = str(doc['_id'])  # BSON ObjectId ni str çevirmək üçün
        result.append(doc)
    return jsonify(result)            # resulti JSON formatına dönüştürür ve HTTP yanıtı olarak geri döner.


@app.route('/admins/<int:id>',methods=['GET'])
def get_one_item(id):
    doc=collection.find_one({"id":id})
    if doc:
        doc['_id']=str(doc['_id'])
        return jsonify(doc)
    else:
        return jsonify({"error":"Missing required fields"}),404

@app.route('/admins',methods=['POST'])
def create_data():
    data=request.get_json()
    required_fields=["id", "name", "surname", "birthday", "last_login", "sign_out_time", "info"]
    if not all(field in data for field in required_fields):
        return jsonify({"error":"Missing required fields"}),400
    
    try:
        data["birthday"]=datetime.strptime(data["birthday"],'%Y-%m-%d')
        data["last_login"]=datetime.strptime(data["last_login"],'%Y-%m-%d')
    except ValueError:
        return jsonify({"error":"Invalid data format"}),400
    
    result=collection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return jsonify(data),201


@app.route('/admins/<int:id>',methods=['PUT'])
def update_data(id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"No data provided"}),400
    
    result=collection.update_one({"id":id},{"$set":data})
    if result.matched_count:
        return jsonify({"message":"Document updated"})
    else:
        return jsonify({"error":"Document not found"}),404


@app.route('/admins/<int:id>',methods=['DELETE'])
def delete_data(id):
    result=collection.delete_one({'id':id})
    if result.deleted_count:
        return jsonify({"message":"Document deleted"})
    else:
        return jsonify({"error":"Document not found"}),404


@app.route('/admins',methods=['DELETE'])
def delete_all():
    a=collection.delete_many({})
    return jsonify({"message": f"{a.deleted_count} document(s) deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)