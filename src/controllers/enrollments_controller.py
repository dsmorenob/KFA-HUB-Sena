from flask import Blueprint, render_template

enrollments_bp = Blueprint('enrollments', __name__)

@enrollments_bp.route('/form_enrollments')
def form_enrollments():
    return render_template('enrollments/form_enrollments.html')
