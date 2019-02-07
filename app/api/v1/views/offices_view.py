from flask import jsonify, request
from ...v1 import version_1 as v1
from ..schemas.offices_schema import OfficeSchema
from ..models.offices_model import Office

db = Office()

@v1.route('/office', methods=['POST'])
def post_office():
    """ Endpoint to post office """
    office_data = request.get_json()

  
    if not office_data:
        return jsonify({'status': 400, 'alert': 'No data provided'}), 400

  
    data, errors = OfficeSchema().load(office_data)
    if errors:
        return jsonify({'status': 400, 'message' : 'Invalid data. Please fill all required fields', 'errors': errors}), 400

    
    office = db.save(data)
    result = OfficeSchema().dump(office).data
    return jsonify({'status': 201, 'message': 'Office created successfully', 'data': result}), 201

@v1.route('/office', methods=['GET'])
def get_offices():
    all_offices = db.all()
    result = OfficeSchema(many=True).dump(all_offices).data
    return jsonify({'status':200, 'data':result}), 200


@v1.route('/office/<int:office_id>', methods=['GET'])
def specific_office(office_id):
   
    if not db.exists('id', office_id):
        return  jsonify({'status': 404, 'error': 'party not found'}), 404

    partiess = db.fetch_by_id(office_id)
    result = OfficeSchema(many=True).dump(partiess).data
    return jsonify({'status':200, 'data':result}), 200


