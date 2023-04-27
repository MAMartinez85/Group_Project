import os
from extensions import db
from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "login.user_login"
    login_manager.init_app(app)

    from models.models import Person

    @login_manager.user_loader
    def load_user(user_id):
        return Person.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    from home.routes import home
    from schedule.routes import schedule
    from login.routes import login
    from logout.routes import logout
    from signup.routes import signup

    app.register_blueprint(home)
    app.register_blueprint(schedule)
    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(signup)

    return app

app = create_app()

#if __name__ == "__main__":
#   app.run()