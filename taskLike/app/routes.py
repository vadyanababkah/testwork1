import re
from app import app

from flask import request, jsonify

@app.route('/likes', methods=['GET'])
def likes():

    error = False
    error_message = None
    data = None

    names = request.args.get("names", default="", type=str)

    names = names.split(',')
    names = list(map(str.strip, names))
    names = [x for x in names if len(x) > 0]

    if validate(names) == True:

        cou_names = len(names)

        if cou_names == 0:
            data = 'Это никому не нравится'
        elif cou_names == 1:
            data = f'{names[0]} лайкнул это.'
        elif cou_names == 2:
            data = f'{names[0]} и {names[1]} лайкнули это.'
        elif cou_names == 3:
            data = f'{names[0]}, {names[1]} и {names[2]} лайкнули это.'
        else: # cou_names > 3:
            data = f'{names[0]}, {names[1]} и ещё {cou_names-2} человека лайкнули это.'
    else:
        error = True
        error_message = 'Плохие имена'

    return jsonify({'error': error,
                    'data': data,
                    'error_message': error_message})

def validate(names: list) -> bool:
    for name in names:
        if len(name) > 10 or re.search(r'[\W|_]', name):
            return False
    return True

#set FLASK_DEBUG=1

#flask run --port=8000

#http//127.0.0.1:8000/likes?names=Петя,Evgen