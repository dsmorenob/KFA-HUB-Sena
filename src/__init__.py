from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.controllers.home_controller import home_bp
    from src.controllers.schedules_controller import schedules_bp
    from src.controllers.classes_controller import classes_bp
    from src.controllers.enrollments_controller import enrollments_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(schedules_bp)
    app.register_blueprint(classes_bp)
    app.register_blueprint(enrollments_bp)

    return app
