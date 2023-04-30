import requests 
import json 

url = 'http://127.0.0.1:8000/doctors/create_data'
def create_data():
    data = {
        'username':'varun1',
        'company_name':'testcompany',
        'company_designation':'testdes',
        'insurance':'partial'
    }
    json_data = json.dumps(data)
    r = requests.post(url = url, data = json_data)
    response = r.json()
    print(response)
url2 = 'http://127.0.0.1:8000/doctors/delete_data'
def delete_data(username = None):
    data = {
        'username':None
    }
    if username is not None:
        data = {
            'username':username
        }
    json_data = json.dumps(data)
    r = requests.delete(url = url2, data = json_data)
    response = r.json()
    print(response)

url3 = "http://127.0.0.1:8000/doctors/delete_doctor"
def delete_doctors(name = None):
    data = {'name':None}
    if name is not None:
        data = {'name':name}
    json_data = json.dumps(data)
    r = requests.delete(url = url3, data = json_data)
    response = r.json()
    print(response)
url4 = "http://127.0.0.1:8000/doctors/test_route"
def test_route():
    r = requests.get(url = url4)
    response = r.json()
    print(response)
url5 = "http://127.0.0.1:8000/doctors/get_doctor"
def get_doctor(name = None):
    data = {}
    if name is not None:
        data = {'name':name}
    json_data = json.dumps(data)
    r = requests.get(url = url5, data = json_data)
    response = r.json()
    print(response)

def create_appointment():
    data = {
        'DoctorName':'Varun',
        'PatientName':'Varun2',
        'DateOfAppointment':'2023-04-24T14:30'
    }
    json_data = json.dumps(data)
    r = requests.post(url = "http://127.0.0.1:8000/doctors/create_appointment", data = json_data)
    response = r.json()
    print(response)

def delete_appointment(doc_name = None, patient_name = None):
    data = {
            }
    if doc_name is not None and patient_name is not None:
        data = {
            'doc_name':doc_name,
            'patient_name':patient_name
        }
    json_data = json.dumps(data)
    r = requests.delete(url = 'http://127.0.0.1:8000/doctors/delete_appointment', data = json_data)
    response = r.json()
    print(response)

# delete_appointment()
def get_confirmed_appointments(patient_name = None):
    data = {'patient_name':patient_name}
    json_data = json.dumps(data)
    r = requests.get(url = 'http://127.0.0.1:8000/doctors/get_confirmed_appointments', data = json_data)
    response = r.json()
    print(response)

def create_bill():
    data = {
      'PatientName':'testpatient',
      'insurance':'None'
    }
    json_data = json.dumps(data)
    r = requests.post(url = 'http://127.0.0.1:8000/doctors/create_bill', data = json_data)
    response = r.json()
    print(response)

def get_bill(patient_name = None):
    data = {'PatientName':None}
    if patient_name is not None:
        data = {'patient_name':patient_name}
    json_data = json.dumps(data)
    r = requests.get(url = 'http://127.0.0.1:8000/doctors/get_bill', data = json_data)
    response = r.json()
    print(response)

def get_data(username = None):
    data = {
        'username':None
    }
    if username is not None:
        data = {
            'username':username
        }
    json_data = json.dumps(data)
    r = requests.get(url = 'http://127.0.0.1:8000/doctors/get_data', data = json_data)
    response = r.json()
    print(response)

# get_confirmed_appointments('varun1')
# create_data()
# create_bill()
# get_bill()
get_data()
# delete_data('mrunal')

    