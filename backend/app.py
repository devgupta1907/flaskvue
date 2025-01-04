from flask import Flask
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_cors import CORS
from application.config import LocalDevelopmentConfig
from application.models import db, User, Role
from application.resources import api


app = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, datastore=datastore, register_blueprint=False)
    app.app_context().push()
    return app

app = create_app()

with app.app_context():
    db.create_all() 

import application.routes
# db = SQLAlchemy(app)
# jwt = JWTManager(app)
# migrate = Migrate(app, db)
# api = Api(app)





    
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String, nullable=False, unique=True)
#     price = db.Column(db.Integer, nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

#     def __repr__(self):
#         return f"<Category {self.title}>"
    
# class Customer(UserMixin, db.Model):
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     name = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     pincode = db.Column(db.Integer, nullable=False)
#     # status = db.Column(db.Enum(CustomerStatus), default=CustomerStatus.ACTIVE, nullable=False)
#     # service_request = db.relationship('ServiceRequest', backref='customer', lazy=True)

#     def __repr__(self):
#         return f"<Customer {self.email}>"

# class Professional(UserMixin, db.Model):
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     name = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String, nullable=False)
#     work_exp = db.Column(db.Integer, nullable=False)
#     # service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
#     # service_requests = db.relationship('ServiceRequest', backref='professional', lazy=True)
#     # status = db.Column(db.Enum(ProfessionalStatus), default=ProfessionalStatus.PENDING, nullable=False)
    
#     def __repr__(self):
#         return f'<Professional {self.name}>'



# book_fields = {
#     "id": fields.Integer,
#     "title": fields.String,
#     "price": fields.Integer,
#     "category_id": fields.Integer
# }
    
    



# class BooksResource(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument("title", required=True, help = "Book title is required")
#         self.parser.add_argument("price", required=True, help = "Book price is required")
#         self.parser.add_argument("category", required=True, help = "Category ID is required")
    
#     @marshal_with(book_fields)
#     def get(self):
#         books = Book.query.all()
#         return books, 200
    
#     @marshal_with(book_fields)
#     def post(self):
#         booksArgs = self.parser.parse_args(strict=True)
#         title = booksArgs.get("title").strip()
#         price = booksArgs.get("price")
#         category_id = booksArgs.get("category")
        
#         category = Category.query.get_or_404(category_id)
#         if not category:
#             abort(404, "Category not found.")
        
#         existing_book = Book.query.filter_by(title=title).first()
#         if existing_book:
#             abort(409, "A book with this title already exists.")
            
#         new_book = Book(title=title, price=price, category_id=category.id)
#         db.session.add(new_book)
#         db.session.commit()
        
#         return new_book, 201


# class ProfessionalRegistration(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('name', required=True, help='Name cannot be blank.')
#         self.parser.add_argument('email', required=True, help='Email cannot be blank.')
#         self.parser.add_argument('password', required=True, help='Password cannot be blank.')
#         self.parser.add_argument('work_exp', type=int, required=True, help='Work experience cannot be blank.')

#     def post(self):
#         args = self.parser.parse_args()
        
#         existing_professional = Professional.query.filter_by(email=args['email']).first()
#         if existing_professional:
#             abort(409, "This email is already taken. Please use different email")
        
#         if (int(args['work_exp']) < 0 or int(args['work_exp']) > 20):
#             abort(400, "Work experience must be in range 0 to 20 (both inclusive)")
        
#         hashed_password = generate_password_hash(args['password'])
#         new_professional = Professional(
#             name=args['name'],
#             email=args['email'],
#             password=hashed_password,
#             work_exp=args['work_exp']
#         )
#         db.session.add(new_professional)
#         db.session.commit()
#         return {'message': 'Professional registered successfully.'}, 201


# class CustomerRegistration(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('name', required=True, help='Name cannot be blank.')
#         self.parser.add_argument('email', required=True, help='Email cannot be blank.')
#         self.parser.add_argument('password', required=True, help='Password cannot be blank.')
#         self.parser.add_argument('pincode', type=int, required=True, help='Pincode cannot be blank.')

#     def post(self):
#         args = self.parser.parse_args()
        
#         existing_customer = Customer.query.filter_by(email=args['email']).first()
#         if existing_customer:
#             abort(409, "This email is already taken. Please use different email")
            
#         hashed_password = generate_password_hash(args['password'])
#         new_customer = Customer(
#             name=args['name'],
#             email=args['email'],
#             password=hashed_password,
#             pincode=args['pincode']
#         )
#         db.session.add(new_customer)
#         db.session.commit()
#         return {'message': 'Customer registered successfully.'}, 201


# class ProfessionalLogin(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('email', required=True, help='Email cannot be blank.')
#         self.parser.add_argument('password', required=True, help='Password cannot be blank.')
        
#     def post(self):
#         args = self.parser.parse_args()
#         email = args.get('email')
#         password = args.get('password')
        
#         professional = Professional.query.filter_by(email=email).first()
#         if professional and check_password_hash(professional.password, password):
#             access_token = create_access_token(identity={'usertype': "professional", 'email': professional.email})
#             return {'message':'Login Successful', 'access_token': access_token, 'usertype': 'professional'}, 200
#         abort(401, "Invalid Credentials")
        

# api.add_resource(BooksResource, '/books')
# api.add_resource(ProfessionalRegistration, '/register/professional')
# api.add_resource(CustomerRegistration, '/register/customer')
# api.add_resource(ProfessionalLogin, '/login/professional')



if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run()