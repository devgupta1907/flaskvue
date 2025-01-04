from flask import jsonify, abort, request
from flask_restful import Api, Resource, fields, reqparse, marshal_with
from flask_security import auth_required, roles_required
from .models import db, User, Category, Customer, Professional, Service

api = Api(prefix='/api')


class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()

        return [
            {
                **category.to_dict(),
                'service_count': Service.query.filter_by(category_id=category.id).count()
            }
            for category in categories
        ], 200
        
    @roles_required('admin')
    @auth_required('token')
    def post(self):
        data = request.get_json()
        name = data.get("name")

        if not name:
            abort(404, "Category name is required")
        
        existing_category = Category.query.filter_by(name=name).first()
        if existing_category:
            abort(409, "A category with this name already exists.")
            
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        
        return {
            **new_category.to_dict(),
            'service_count': 0
        }, 201
    
    @roles_required('admin')
    @auth_required('token')
    def put(self):
        data = request.get_json()
        existing_category_id = data.get("existingCategoryId")
        new_category_name = data.get("newCategoryName")

        if not existing_category_id or not new_category_name:
            abort(404, "Payload not complete.")

        category_to_update = Category.query.get(existing_category_id)
        if not category_to_update:
            abort(404, "Category not found.")

        existing_category = Category.query.filter(Category.name == new_category_name, Category.id != existing_category_id).first()
        if existing_category:
            abort(409, "A category with this name already exists.")

        category_to_update.name = new_category_name
        db.session.commit()

        return {
            **category_to_update.to_dict(),
            'service_count': Service.query.filter_by(category_id=existing_category_id).count()
        }, 200
    
    @roles_required('admin')
    @auth_required('token')
    def delete(self):
        data = request.get_json()
        category_id = data.get('id')

        if not category_id:
            abort(409, 'Payload not complete')

        existing_category = Category.query.get(category_id)
        if not existing_category:
            abort(404, 'Category not found')

        if Service.query.filter_by(category_id=category_id).count() > 0:
            abort(400, 'Cannot delete this category. Category has associated services.')
        
        db.session.delete(existing_category)
        db.session.commit()
        return {
            'message': 'Category deleted successfully'
        }


class ServiceResource(Resource):
    def get(self):
        services = Service.query.all()
        return [
            {
                **service.to_dict(),
                'professional_count': Professional.query.filter_by(service_id=service.id).count()
            }
            for service in services
        ], 200
    
    @roles_required('admin')
    @auth_required('token')
    def post(self):
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        category_id = data.get("category_id")

        if not name or not price or not description or not category_id:
            abort(404, "Payload not complete")
        
        existing_service = Service.query.filter_by(name=name).first()
        if existing_service:
            abort(409, "A service with this name already exists.")
            
        new_service = Service(name=name, price=price, description=description, category_id=category_id)
        db.session.add(new_service)
        db.session.commit()

        return {
            **new_service.to_dict(),
            'professional_count': 0
        }, 201

    @roles_required('admin')
    @auth_required('token')
    def put(self):
        data = request.get_json()
        existing_service_id = data.get("existingServiceId")
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        category_id = data.get("category_id")

        if not name or not price or not description or not category_id:
            abort(404, "Payload not complete")
        
        service_to_update = Service.query.get(existing_service_id)
        if not service_to_update:
            abort(404, "Service not found.")
        
        existing_service = Service.query.filter(Service.name == name, Service.id != existing_service_id).first()
        if existing_service:
            abort(409, "A service with this name already exists.")

        service_to_update.name = name
        service_to_update.price = price
        service_to_update.description = description
        service_to_update.category_id = category_id
        db.session.commit()

        return {
            **service_to_update.to_dict(),
            'professional_count': Service.query.filter_by(category_id=existing_service_id).count()
        }, 200
    

    @roles_required('admin')
    @auth_required('token')
    def delete(self):
        data = request.get_json()
        service_id = data.get('id')

        if not service_id:
            abort(409, 'Payload not complete')

        existing_service = Service.query.get(service_id)
        if not existing_service:
            abort(404, 'Service not found')

        if Professional.query.filter_by(service_id=service_id).count() > 0:
            abort(400, 'Cannot delete this service. Service has associated professionals.')
        
        db.session.delete(existing_service)
        db.session.commit()
        return {
            'message': 'Service deleted successfully'
        }


class CustomerResource(Resource):
    @roles_required('admin')
    @auth_required()
    def get(self):
        customers = Customer.query.all()
        return [
            {
                'name': customer.user.name,
                'email': customer.user.email,
                'isBlocked': customer.user.isBlocked,
                **customer.to_dict()
            }
            for customer in customers
        ], 200


class ProfessionalResource(Resource):
    @roles_required('admin')
    @auth_required()
    def get(self):
        professionals = Professional.query.all()
        return [
            {
                'name': professional.user.name,
                'email': professional.user.email,
                'isBlocked': professional.user.isBlocked,
                **professional.to_dict()
            }
            for professional in professionals
        ], 200


class ProfessionalsByServiceResource(Resource):
    @roles_required('customer')
    @auth_required()
    def get(self, service_id):
        professionals = Professional.query.filter(
            Professional.service_id == service_id
        ).all()

        unblocked_professionals = [
            {
                'id': professional.user_id,
                'name': professional.user.name
            }
            for professional in professionals
            if professional.user and not professional.user.isBlocked
        ]

        return unblocked_professionals, 200
   


class BlockUserResource(Resource):
    @roles_required('admin')
    @auth_required()
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        if not user_id:
            abort(400, 'User ID is not provided')
        user = User.query.get(user_id)
        if not user:
            abort(404, 'User not found')
        user.isBlocked = 1
        db.session.commit()
        return {
            'message': 'User blocked successfully!'
        }
    
class UnblockUserResource(Resource):
    @roles_required('admin')
    @auth_required()
    def post(self):
        data = request.get_json()
        user_id = data.get('user_id')
        if not user_id:
            abort(400, 'User ID is not provided')
        user = User.query.get(user_id)
        if not user:
            abort(404, 'User not found')
        user.isBlocked = 0
        db.session.commit()
        return {
            'message': 'User unblocked successfully!'
        }

api.add_resource(CategoryResource, '/categories')
api.add_resource(ServiceResource, '/services')

api.add_resource(CustomerResource, '/customers')
api.add_resource(ProfessionalResource, '/professionals')

api.add_resource(ProfessionalsByServiceResource, '/services/<int:service_id>/service_professionals')

api.add_resource(BlockUserResource, '/block_user')
api.add_resource(UnblockUserResource, '/unblock_user')