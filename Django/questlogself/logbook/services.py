#import the os module so you can use stuff you shouldnt code directly and import the request library to use APIs:
import os,requests
from .models import Fgo 

#make a function that grabs the API keys for np,class,image:
def get_servant(request):
    #get the API url
    api_url = "https://api.atlasacademy.io/export/NA/nice_servant.json"
    #get the servant info from the url:
    response = request.get(api_url)
    #check the status code to make sure you get the right response:
    if response.status_code == 200:
        #convert the json servant info you got to python:
        servant = response.json()
        #store the servants information here:
        servant_info = {}
        #loop over each servant in the database:
        for s in servant:
             #check if the current servant matches what the user summoned:
            if s.get("name").lower() == request.lower():
                #extract the fields you care about:
                class_name = s.get("className")
                servant_info["class_name"] = class_name
                np = s.get("noblePhantasm")
                servant_info["np"] = np
                #extract the image key:
                image = s.get("face")
                servant_info["image"] = image
                #summon servants have multiple nps(uncomment if you only want to see one):      
                #np_name = s["noblePhantasms"][0]["name"] if s["noblePhantasms"] else None
        #update the servants info in the model:
        return servant_info
    else:
        return f"api call failed with the status code: {response.status_code}"
#end:create a logic that links my servant_detail.html to my API  then create a url for it (make it so if someone clicks their created servant they go to the detail template to see all that servants info)



    






