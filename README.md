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
	{
				  {
        "id": 1,
        "patient_id": 1,
        "doctor_id": null,
        "problem": "testproblem1",
        "existing_disease": "existingdiseasetest12ndproblem",
        "appointment_date": "2020-08-10",
        "appointment_time": "10:25:00",
        "status": "TO MANAGER",
        "add_date": "2020-06-13T08:57:53.887Z"
    },
    {
        "id": 2,
        "patient_id": 2,
        "doctor_id": null,
        "problem": "testproblem2",
        "existing_disease": "existingdiseasetest1,2ndproblem",
        "appointment_date": "2020-08-12",
        "appointment_time": "11:25:00",
        "status": "TO MANAGER",
        "add_date": "2020-06-13T08:59:11.800Z"
    },
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
	Request - /Doctor/login/
	
	Data to be send(json)
	{
		 "email": "sameer@gmail.com",
		 "password": "wongpass"
        } 
		
	Rsponse- 200
	{
	    "Invalid Credentials"
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
