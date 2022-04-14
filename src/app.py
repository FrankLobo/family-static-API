"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#---------------------------------------------------- GET ALL MEMBERS -----------------------------#
@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200
    
#---------------------------------------------------- POST A MEMBER -------------------------------#
@app.route('/member', methods=['POST'])
def create_member():
    adding_member = jackson_family.add_member({})
    return jsonify(adding_member), 200
   
#---------------------------------------------------- GET A MEMBER BY ID --------------------------#
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_id(member_id):
    member = jackson_family.get_member(member_id)
    response_body = {
        "id": member,
        "first_name": "Tommy",
        "last_name": member,
        "age": member,
        "lucky_numbers": member
    }

    return jsonify(response_body), 200

#------------------------------------------ DELETE A MEMBER BY ID ------------------#
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member_id(member_id):
    # deleted_member = jackson_family.get_member(member_id)
    # return jsonify(deleted_member), 200

    deleted_member = jackson_family.get_member(member_id)
    response_body = {
        "id": deleted_member,
        "first_name": deleted_member,
        "last_name": deleted_member,
        "age": deleted_member,
        "lucky_numbers": deleted_member
    }

    return jsonify({"done": True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
