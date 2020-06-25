					PATIENT SECTION



LOGIN-SUCESSFUL (METHOD-POST)
	Request - /patient/login/

	Data to be send(json)
	{
			 "email": "sameer@gmail.com",
			 "password": "testpass1"
        } 
		
	Rsponse- 200
	{
	    "DATA OF PATIENT"
	}

LOGIN-UNSUCESSFUL (METHOD-POST)
	Request - /patient/login/
	
	Data to be send(json)
	{
			 "email": "sameer@gmail.com",
			 "password": "wongpass"
        } 
		
	Rsponse- 200
	{
	    "Invalid Credentials"
	}

REGISTER (METHOD-POST)
	Request - /patient/register/
	
	Data to be send(json)
	
	 {
			
			"first_name": "Sameer",
			"last_name": "Verma",
			"email": "sameer@gmail.com",
			"age": "20",
			"gender": "Male",
			"phone_no": "1234567890",
			"address": "lucknow,lucknow",
			"password": "testpass1"
			
			
         }
	
	Response-200
	{
	"OK"
	}
	
	IF EMAIL ALREADY REGISTERED
	
	Response-200
	{
	"EMAIL ALREADY REGISTERED"
	}
	











					APPOINTMENT SECTION

BOOK APPOINTMENT (METHOD-POST)
	REQUEST - /appointment/add/

 	Data to be send(json)
	
	 {
		
			"patient_id": 4,
			"problem": "testproblem",
			"existing_disease": "existing disease test",
			"appointment_date": "YYYY-MM-DD",
			"appointment_time": "HH:MM",
		
	
	
	 }


        Response-200
	{
	"OK"
	}
	IF PREVIOUS APPOINTMENT NOT REJECTED
	
        Response-200
	{
		"YOU CANNOT BOOK ANOTHER APPOINMENT UNTIL YOUR PREVIOUS APPOINTMENT IS NOT REJECTED"
	}


PENDING APPOINTMENTS FOR MANAGER  (METHOD-GET)
	
	REQUEST- /appointment/receptionpending/



	  Response-200
	[{"id": 1, "patient__email": "rgrgarg18@gmail.com", "patient__phone_no": "8218730916", "appointment_date": "2020-08-10", "appointment_time": "10:25:00", "problem": "testproblem1", "existing_disease": "existingdiseasetest12ndproblem", "patient__first_name": "Rishav", "patient__last_name": "Garg"}, {"id": 2, "patient__email": "sameer@gmail.com", "patient__phone_no": "1234567890", "appointment_date": "2020-08-12", "appointment_time": "11:25:00", "problem": "testproblem2", "existing_disease": "existingdiseasetest1,2ndproblem", "patient__first_name": "Sameer", "patient__last_name": "Verma"}, {"id": 4, "patient__email": "arjunkaushik810@gmail.com", "patient__phone_no": "902711372", "appointment_date": "2020-08-13", "appointment_time": "11:40:00", "problem": "testproblem3", "existing_disease": "existingdiseasetest1,2ndproblem", "patient__first_name": "arjun ", "patient__last_name": "kaushik"}, {"id": 5, "patient__email": "arjunkaushik810@gmail.com", "patient__phone_no": "902711372", "appointment_date": "2020-06-19", "appointment_time": "14:13:00", "problem": "Fever, Cold ", "existing_disease": "AIDS, Diabetes", "patient__first_name": "arjun ", "patient__last_name": "kaushik"}]




PENDING APPOINTMENTS FOR DOCTOR  (METHOD-POST)
	
	REQUEST- /appointment/doctorpending/

	Data to be send Json

	{
	"doctor_id":"2"
	}


	  Response-200
	[id','patient__email','patient__phone_no','appointment_date','appointment_time','problem','existing_disease','patient__first_name','patient__last_name']

 
FORWARD AND EDIT APPOINTMENT(METHOD - POST)
	REQUEST -/appointment/editappointment/

	Data to be send (json)
	{

			"id":2,
			"appointment_date":"YYYY-MM-DD",
			"appointment_time":"HH-MM",
			"doctor_id""2"



	}
	
	  Response-200
	{
		"OK"
	}



REJECT APPOINTMENT(METHOD-POST)

		request-/appointment/rejectappointment/

	Data to be send Json

	{
	"appointment_id":
	}
	
	Response-200
	{
	"OK"
	}

PATIENT APPROVE APPOINTMENT(METHOD-POST)

		request-/appointment/patientapproveappointment/

	Data to be send Json

	{
	"appointment_id":
	}
	
	Response-200
	{
	"OK"
	}

DOCTOR APPROVE APPOINTMENT(METHOD-POST)

		request-/appointment/doctorapproveappointment/

	Data to be send Json

	{
	"appointment_id":
	}
	
	Response-200
	{
	"OK"
	}






SEND DOCTOR LIST BY DEPARTMENT(METHOD-POST)

		request-/appointment/senddoctorlist/

	Data to be send Json

	{
	"department":
	}
	
	Response-200
	{
	"doctor_id"
	"first_name"
	"last_name"
	}

PATIENT NOTIFICATION SECTION OF APPOINTMENT(LATEST APPOINTMENT)(METHOD-POST)

		request-/appointment/patientview/

	Data to be send Json

	{
	"patient_id":
	}
	
	Response-200
	{
	status of appointment ,appointment details
	}




					DOCTOR SECTION


  REGISTER (METHOD-POST)
	Request - /doctor/register/
	
	Data to be send(json)
	
	 {	

		"deparment":"EYE",
		"first_name":"Anuj",
		"last_name":"Chaturvedi",
		"email":"anuj@gmail.com",
		"age":"36",
		"gender":"Male",
		"phone_no":"1234567899",
		"address":"agra",
		"password":"test",
		"degree":"MBBS,B.PHARM",
		"previous_exp":7
    


	}

     		
        
         }
	
	Response-200
	{
		"OK"
	}
	
	IF EMAIL ALREADY REGISTERED
	
	Response-200
	{
		"EMAIL ALREADY REGISTERED"
	}

LOGIN-SUCESSFUL (METHOD-POST)
	Request - /doctor/login/

	Data to be send(json)
	{
		 "email": "anuj@gmail.com",
		 "password": "test"
        } 
		
	Rsponse- 200
	{
	    " Basic DATA OF Doctor"
	}

LOGIN-UNSUCESSFUL (METHOD-POST)
	Request - /doctor/login/
	
	Data to be send(json)
	{
		 "email": "sameer@gmail.com",
		 "password": "wongpass"
        } 
		
	Rsponse- 200
	{
	    "Invalid Credentials"
	}

ALL APPROVED APPOINTMENT OF DOCTOR(METHOD-POST)

	Request - /doctor/allapprovedappointment/
	
	Data to be send(json)
	{
		"doctor_id"
        } 
		
	Rsponse- 200
	{
	    
"'id','patient__email','patient__phone_no','appointment_date','appointment_time','problem','existing_disease','patient__first_name','patient__last_name'"
	}




					RECEPTION SECTION


LOGIN-SUCESSFUL (METHOD-POST)
	Request - /reception/login/

	Data to be send(json)
	{
			 "username": "admin",
			 "password": "admin"
        } 
		
	Rsponse- 200
	{
	    "OK"
	}

LOGIN-UNSUCESSFUL (METHOD-POST)
	Request -  /reception/login/
	
	Data to be send(json)
	{
			 "email": "admin",
			 "password": "wongpass"
        } 
		
	Rsponse- 200
	{
	    "Invalid Credentials"
	}

NOT APPROVED DOCTOR LIST (METHOD-GET)

	Request - /reception/notapproveddoctorlist/
	
		
	Rsponse- 200
	{
	    


		"deparment":"EYE",
		"first_name":"Anuj",
		"last_name":"Chaturvedi",
		"email":"anuj@gmail.com",
		"age":"36",
		"gender":"Male",
		"phone_no":"1234567899",
		"address":"agra",
		"password":"test",
		"degree":"MBBS,B.PHARM",
		"previous_exp":7,
		"status":"NOT APPROVED"
    


	}

APPROVED DOCTOR LIST (METHOD-GET)

	Request - /reception/approveddoctorlist/
	
		
	Rsponse- 200
	{
	    


		"deparment":"EYE",
		"first_name":"Anuj",
		"last_name":"Chaturvedi",
		"email":"anuj@gmail.com",
		"age":"36",
		"gender":"Male",
		"phone_no":"1234567899",
		"address":"agra",
		"password":"test",
		"degree":"MBBS,B.PHARM",
		"previous_exp":7,
		"status":"APPROVED"
    

	}

REJECTED DOCTOR LIST (METHOD-GET)

	Request - /reception/rejecteddoctorlist/
	
		
	Rsponse- 200
	{
	    


		"deparment":"EYE",
		"first_name":"Anuj",
		"last_name":"Chaturvedi",
		"email":"anuj@gmail.com",
		"age":"36",
		"gender":"Male",
		"phone_no":"1234567899",
		"address":"agra",
		"password":"test",
		"degree":"MBBS,B.PHARM",
		"previous_exp":7,
		"status":"REJECTED"
    

	}



APPROVE DOCTOR  (METHOD-POST)

	Request - /reception/approvedoctor/
	
		DATA TO BE SEND JSON

	{
	"doctor_id"
	}
	Rsponse- 200
	{
		"OK"	    

	
	}


REJECT DOCTOR  (METHOD-POST)

	Request - /reception/rejectdoctor/
	
		DATA TO BE SEND JSON

	{
	"doctor_id"
	}
	Rsponse- 200
	{
		"OK"	    

	}


APPROVE DOCTOR  (METHOD-POST)

	Request - /reception/approvedoctor/
	
		DATA TO BE SEND JSON

	{
	"doctor_id"
	}
	Rsponse- 200
	{
		"OK"	    

	
	}

ALL PATIENT LIST (METHOD-GET)

	REQUEST- /reception/allpatients/


Response-200
	{
	
			"first_name": "Sameer",
			"last_name": "Verma",
			"email": "sameer@gmail.com",
			"age": "20",
			"gender": "Male",
			"phone_no": "1234567890",
			"address": "lucknow,lucknow",
			"password": "testpass1"
			
	}


PATIENTS UNDER DOCTOR(METHOD-POST)

	REQUEST- /reception/patientunderdoctor/

	
	DATA TO BE SEND JSON

	{
	"doctor_id"
	}



	RESPONSE-200
	{		'patient_id','patient__first_name','patient__last_name','patient__email','patient__phone_no','patient__address'

	}







							MEDICAL REPORT SECTION



MEDICAL REPORT ADD BY DOCTOR(METHOD-POST)

	REQUEST- /medicalhistory/add/

	Data to be send (JSON)

	{
	"appointment_id_id"
	"height"
	"Weight"
	"blood_group"
	"prescribed_medicine"
	"report_message"

	}

	Response-200
	{
	"OK"
	}


MEDICAL REPORT ADD BY DOCTOR(METHOD-POST)

	REQUEST- /medicalhistory/viewpatient/

	Data to be send (JSON)

	{
	"patient_id"

	}

	Response-200
	{
	'id','appointment_id_id','height','Weight','prescribed_medicine','blood_group','report_message','appointment_id__doctor_id__first_name','appointment_id__doctor_id__last_name','appointment_id__doctor_id__email','appointment_id__doctor_id__phone_no','appointment_id__problem','appointment_id__existing_disease','appointment_id__appointment_date','appointment_id__appointment_time'
	}
