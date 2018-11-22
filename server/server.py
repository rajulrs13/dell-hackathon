import os
import json
from reg_product import reg_product
from reg_services import reg_services
from class_revenue import class_service
from flask import Flask , request
from flask_cors import CORS
import warnings

with warnings.catch_warnings():
	warnings.filterwarnings("ignore",category=FutureWarning)
	warnings.filterwarnings("ignore",category=DeprecationWarning)
	import imp

app = Flask(__name__)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})
@app.route( "/predict", methods=['POST'])
def apicall():
	test_json = request.get_json(force = True)
	print()
	print("Response Recieved")

	print()
	print(test_json)
	response = None
	if(test_json['code'] == 'reg'):
		if(test_json['type'] == 'product'):
			response = reg_product(test_json['product'], test_json['region'], test_json['year'])
		elif(test_json['type'] == 'service'):
			response = reg_services(test_json['service'], test_json['region'], test_json['year'])
	elif(test_json['code'] == 'class'):
		response = class_service(test_json['age'], test_json['year'], test_json['ram'], test_json['hdd'], test_json['location'], test_json['warranty'])

	X = json.dumps(response)
	
	print()
	print("Sending Back Processed Response")
	print("*******************************")
	return X