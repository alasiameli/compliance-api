from datetime import datetime
import json

from flask import Flask, jsonify, request, abort, Response, make_response

app = Flask(__name__)


@app.route('/api/v1/compliance/system_info/<string:event_name>', methods=['GET'])
def get_system_info_event(event_name):
    try:
        with open("static/" + event_name + '.json', "r+") as f:
            data = f.read()
        return Response(data, content_type='application/json; charset=utf-8')
    except Exception as e:
        return custom_error("Event not found", 404)


@app.route('/api/v1/compliance/system_info', methods=['POST'])
def create_system_info_event():
    jsonBody = request.json
    destination_path = 'static/'
    file_name = jsonBody['server_ip'] + datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_extension = '.json'

    file_name = get_destination(destination_path, file_name, file_extension)

    try:
        with open(file_name, 'w') as json_file:
            json.dump(jsonBody, json_file)
        return jsonify({'status': "OK"}), 201
    except Exception as e:
        return custom_error("File not created", 500)


def get_destination(path, file_name, extension):
    destination = path + file_name + extension
    return destination


def custom_error(message, status_code):
    return make_response(jsonify({'status_code': status_code, 'message': message}), status_code)


if __name__ == '__main__':
    app.run()
