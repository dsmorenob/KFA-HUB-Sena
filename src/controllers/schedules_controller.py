from flask import Blueprint, render_template

schedules_bp = Blueprint('schedules', __name__)

@schedules_bp.route('/list_schedules')
def list_schedules():
    return render_template('schedules/list_schedules.html')
