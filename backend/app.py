from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from flask_login import UserMixin
from flask_migrate import Migrate
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

app = Flask(__name__)
# app.secret_key = b'_5#y2LF4Q8z\ddfdgxec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskvueDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'N$gx[v?E[`qAJs4`/}fx9Hl:dxcnBaSe'

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    books = db.relationship('Book', backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"

    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"
    
class Customer(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    # status = db.Column(db.Enum(CustomerStatus), default=CustomerStatus.ACTIVE, nullable=False)
    # service_request = db.relationship('ServiceRequest', backref='customer', lazy=True)

    def __repr__(self):
        return f"<Customer {self.email}>"

class Professional(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    work_exp = db.Column(db.Integer, nullable=False)
    # service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    # service_requests = db.relationship('ServiceRequest', backref='professional', lazy=True)
    # status = db.Column(db.Enum(ProfessionalStatus), default=ProfessionalStatus.PENDING, nullable=False)
    
    def __repr__(self):
        return f'<Professional {self.name}>'

category_fields = {
    "id": fields.Integer,
    "name": fields.String
}

books_fields = {
    "title": fields.String,
    "price": fields.Integer,
    # "category": fields.Nested(category_fields)
}



class BookAlreadyExists(HTTPException):
    code = 409
    description = "A book with this title already exists."
    
    
class CategoryResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("name", required=True, help = "Category name is required")
        
    @marshal_with(category_fields)
    def get(self):
        categories = Category.query.all()
        return categories, 200
    
    @marshal_with(category_fields)
    def post(self):
        categoryArgs = self.parser.parse_args(strict=True)
        name = categoryArgs.get("name")
        
        existing_category = Category.query.filter_by(name=name).first()
        if existing_category:
            abort(409, "A category with this name already exists.")
            
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        
        return new_category, 201


class BooksResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", required=True, help = "Book title is required")
        self.parser.add_argument("price", required=True, help = "Book price is required")
        self.parser.add_argument("category_id", required=True, help = "Category ID is required")
    @marshal_with(books_fields)
    def get(self):
        books = Book.query.all()
        return books, 200
    
    @marshal_with(books_fields)
    def post(self):
        booksArgs =self.parser.parse_args(strict=True)
        title = booksArgs.get("title")
        price = booksArgs.get("price")
        category_id = booksArgs.get("category_id")
        
        existing_book = Book.query.filter_by(title=title).first()
        if existing_book:
            raise BookAlreadyExists
            
        new_book = Book(title=title, price=price, category_id=category_id)
        db.session.add(new_book)
        db.session.commit()
        
        return new_book, 201


class ProfessionalRegistration(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='Name cannot be blank.')
        self.parser.add_argument('email', required=True, help='Email cannot be blank.')
        self.parser.add_argument('password', required=True, help='Password cannot be blank.')
        self.parser.add_argument('work_exp', type=int, required=True, help='Work experience cannot be blank.')

    def post(self):
        args = self.parser.parse_args()
        
        existing_professional = Professional.query.filter_by(email=args['email']).first()
        if existing_professional:
            abort(409, "This email is already taken. Please use different email")
        
        if (int(args['work_exp']) < 0 or int(args['work_exp']) > 20):
            abort(400, "Work experience must be in range 0 to 20 (both inclusive)")
        
        hashed_password = generate_password_hash(args['password'])
        new_professional = Professional(
            name=args['name'],
            email=args['email'],
            password=hashed_password,
            work_exp=args['work_exp']
        )
        db.session.add(new_professional)
        db.session.commit()
        return {'message': 'Professional registered successfully.'}, 201


class CustomerRegistration(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help='Name cannot be blank.')
        self.parser.add_argument('email', required=True, help='Email cannot be blank.')
        self.parser.add_argument('password', required=True, help='Password cannot be blank.')
        self.parser.add_argument('pincode', type=int, required=True, help='Pincode cannot be blank.')

    def post(self):
        args = self.parser.parse_args()
        
        existing_customer = Customer.query.filter_by(email=args['email']).first()
        if existing_customer:
            abort(409, "This email is already taken. Please use different email")
            
        hashed_password = generate_password_hash(args['password'])
        new_customer = Customer(
            name=args['name'],
            email=args['email'],
            password=hashed_password,
            pincode=args['pincode']
        )
        db.session.add(new_customer)
        db.session.commit()
        return {'message': 'Customer registered successfully.'}, 201


class ProfessionalLogin(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', required=True, help='Email cannot be blank.')
        self.parser.add_argument('password', required=True, help='Password cannot be blank.')
        
    def post(self):
        args = self.parser.parse_args()
        email = args.get('email')
        password = args.get('password')
        
        professional = Professional.query.filter_by(email=email).first()
        if professional and check_password_hash(professional.password, password):
            access_token = create_access_token(identity={'usertype': "professional", 'email': professional.email})
            return {'message':'Login Successful', 'access_token': access_token}, 200
        abort(401, "Invalid Credentials")
        

api.add_resource(BooksResource, '/books')
api.add_resource(CategoryResource, '/categories')
api.add_resource(ProfessionalRegistration, '/register/professional')
api.add_resource(CustomerRegistration, '/register/customer')
api.add_resource(ProfessionalLogin, '/login/professional')



if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)