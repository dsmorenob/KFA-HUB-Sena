from flask import Blueprint, render_template

classes_bp = Blueprint('classes', __name__)

@classes_bp.route('/form_classes')
def form_classes():
    return render_template('classes/form_classes.html')
