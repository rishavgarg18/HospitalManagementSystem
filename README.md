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
	    "ID OF PATIENT"
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

BOOK APPOINTMENT (METHOD-POST)
	REQUEST - /appointment/add/

 	Data to be send(json)
	
	 {

	

	 }


        Response-200
	{
	"OK"
	}

