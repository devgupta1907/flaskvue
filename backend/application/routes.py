from flask import current_app as app, jsonify, request, send_file
from flask_security import auth_required, verify_password, hash_password
from .models import db, User, Customer, Professional
from datetime import datetime
from application.celery.tasks import add, create_csv
from celery.result import AsyncResult

datastore = app.security.datastore
cache = app.cache


@app.route('/create_report')
def create_report():
    task = create_csv.delay()
    return {'task_id': task.id}, 200


@app.route('/get_report/<id>')
def get_report(id):
    result = AsyncResult(id)
    if result.ready():
        return send_file(f'./application/celery/downloads/{result.result}'), 200
    return jsonify({
        'message': 'Task not ready'
    }), 405


@app.route('/register', methods=["POST"])
def register():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    existing_user = datastore.find_user(email=email)
    if existing_user:
        return jsonify({
            'message': 'User with this email already exist'
        }), 409

    if not name or not email or not password or not role:
        return jsonify({
            'message': 'Payload not complete'
        }), 400
    
    try:        
        if role == 'customer':
            pincode = data.get('pincode')

            if not pincode:
                return jsonify({
                'message': 'Payload not complete. Pincode?'
            }), 400

            user = datastore.create_user(name=name, email=email, password=hash_password(password), roles=[role], active=True)
            db.session.commit()

            customer = Customer(user_id=user.id, pincode=pincode)
            db.session.add(customer)
        
        elif role == 'professional':
            work_exp = data.get('work_exp')
            service_id = data.get('service_id')

            if work_exp is None or service_id is None:
                return jsonify({
                'message': 'Payload not complete. WorkExp? Service?'
            }), 400

            user = datastore.create_user(name=name, email=email, password=hash_password(password), roles=[role], active=True)
            db.session.commit()

            professional = Professional(user_id=user.id, work_exp=work_exp, service_id=service_id)
            db.session.add(professional)

        else: return jsonify({
            'message': 'Invalid data passed'
        }), 400

        db.session.commit()

        return jsonify({
            'message': 'User created successfully!'
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'message': 'Error creating user'
        })



@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({
            'message': 'Invalid Inputs'
        }), 404
    
    user = datastore.find_user(email=email)
    if not user:
        return jsonify({
            'message': 'Email not registered'
        }), 404
    
    if verify_password(password, user.password):
        if user.isBlocked == 1:
            return jsonify({
                'message': 'Access Denied. You are blocked by admin.'
            }), 403
        
        response = {
            'token': user.get_auth_token(),
            'email': user.email,
            'role': user.roles[0].name
        }

        if user.roles[0].name == 'professional':
            response['details'] = user.professional.to_dict()
        elif user.roles[0].name == 'customer':
            response['details'] = user.customer.to_dict()

        return jsonify(response)
    
    return jsonify({
        'message': 'Password did not match'
    }), 409


@app.route('/time')
@cache.cached(timeout=5)
def get_time():
    return {'time': str(datetime.now())}