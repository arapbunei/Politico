from flask import jsonify, request,abort,make_response
from ...v1 import version_1 as v1
from ..schemas.party_schema import PartySchema
from ..models.party_model import Party
from flask_jwt_extended import (jwt_required, get_jwt_identity)

db = Party()

@v1.route('/party', methods=['POST'])
def create_party():
    """ Function to create a party """
    json_data = request.get_json()

    # No data has been provided
    if not json_data:
        return jsonify({'status': 400, 'error': 'No data provided'}), 400

    # Check if request is valid
    data, errors = PartySchema().load(json_data)
    if errors:
        return jsonify({'status': 400, 'error' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400

    if db.exists('name', data['name']):
        return jsonify({'status': 409, 'message' : 'Party already does exists'}), 409

  
    # Save new party and return response
    new_party = db.save(data)
    result = PartySchema().dump(new_party).data
    return jsonify({'status': 201, 'message': 'Party created successfully', 'data': [result]}), 201

@v1.route('/party/<int:party_id>', methods=['GET'])
def fetch_party(party_id):
    """ Function to fetch specific party """
    # Check if party exists 
    if not db.exists('id', party_id):
        return  jsonify({'status': 404, 'error': 'party not found'}), 404

    # Get parties 
    partiess = db.fetch_by_id(party_id)
    result = PartySchema(many=True).dump(partiess).data
    return jsonify({'status':200, 'data':result}), 200



@v1.route('/parties', methods=['GET'])
def get():
    all_parties = db.all()
    result = PartySchema(many=True).dump(all_parties).data
    return jsonify({'status':200, 'data':result}), 200

  
@v1.route('/party/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
    if not db.exists('id', party_id):
        return  jsonify({'status': 404, 'error': 'party not found'}), 404

    #delete parties 
    db.delete(party_id)
    return jsonify({'status':200, 'message': 'Party deleted successfully'}), 200

@v1.route('/party/<int:party_id>', methods=['PUT'])
def put():
        """editing a single party based on id"""
        for party in parties:
            if party['id'] == id:
                req = request.get_json()
                party['name'] = req['name']
                party['hqaddress'] = req['hqaddress'],
                party['logourl']=req['logourl']
                
                return make_response(jsonify({
                    "msg": "ok",
                    "party": party
                }), 200)

            updated_party = {
                "id": id,
                "name": req['name'],
                "hqaddress": req['hqaddress'],
                "logourl":req['logourl']
               
            }
            parties.append(updated_party)

            return make_response(jsonify({
                "msg": "ok",
                "party": party
            }), 201)



