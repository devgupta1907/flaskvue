from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    fs_uniquifier = db.Column(db.String, unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    roles = db.relationship('Role', backref='bearer', secondary='users_roles')
    isBlocked = db.Column(db.Boolean, default=False, nullable=False)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)


class UsersRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_ur_user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', name='fk_r_user_id'))


class Customer(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_cust_user_id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('customer', uselist=False))
    pincode = db.Column(db.Integer, nullable=False)
    service_requests = db.relationship('ServiceRequest', backref='customer', lazy=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Professional(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_prof_user_id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('professional', uselist=False))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id', name='fk_service_id'), nullable=False)
    work_exp = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, default="PENDING", nullable=False)
    service_requests = db.relationship('ServiceRequest', backref='professional', lazy=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    @property
    def rating(self):
        total_services = 0
        total_ratings = 0
        for request in self.service_requests:
            if request.rating is not None and request.status != "REQUESTED":
                total_ratings += request.rating
                total_services += 1
                
        if total_services > 0:
            return round(total_ratings / total_services, 1)
        return 0

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    services = db.relationship('Service', backref='category', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    

class Service(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', name='fk_customers_id'), nullable=False)
    professionals = db.relationship('Professional', backref='service', lazy=True)
    service_requests = db.relationship('ServiceRequest', backref='service', lazy=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id', name='fk_servicer_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.user_id', name='fk_customer_id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professional.user_id', name='fk_professional_id'), nullable=False)
    status = db.Column(db.String, default="REQUESTED", nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
