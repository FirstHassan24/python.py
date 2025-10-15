#import the os module so you can use stuff you shouldnt code directly and import the request library to use APIs:
import os,requests
from .models import Fgo 

#make a function that grabs the API keys for np,class,image:
def get_servant(servant_name):
    # Import the requests library for HTTP calls
    import requests
    
    # Define the API URL to search for servants by name
    api_url = "https://api.atlasacademy.io/nice/NA/servant/search"
    # Specify the name of the servant to request as query parameters
    params = {"name": servant_name}
    
    # Send the GET request to the API with the parameters
    response = requests.get(api_url, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert the JSON response to a Python list
        servant_data = response.json()
        # Check if the list is not empty (servant found)
        if servant_data:
            # Take the first servant from the search results
            first_servant = servant_data[0]
            # Extract and store servant details in a dictionary
            servant_info = {
                # Get the class name of the servant
                "class_name": first_servant.get("className"),
                # Get the noble phantasm name (handle if array is empty)
                "np": first_servant.get("noblePhantasms", [{}])[0].get("name", "N/A"),
                # Get the image URL with fallbacks for missing keys
                "image": first_servant.get("extraAssets", {}).get("faces", {}).get("ascension", {}).get("1", "No image"),
                # Get the rarity of the servant
                "rarity": first_servant.get("rarity")
            }
            # Return the servant info dictionary
            return servant_info
        else:
            # Return default values if no servant was found
            return {"class_name": "Not Found", "np": "N/A", "image": "No image", "rarity": "Unknown"}
    else:
        # Return error info if the API call failed
        return {"class_name": "Error", "np": f"API failed with {response.status_code}", "image": "No image", "rarity": "Unknown"}