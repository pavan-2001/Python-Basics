import requests
import json
subscription_key="08a9927105msh7a58eb6f0030beap131464jsn31348648e853"
vision_service_address="https://microsoft-computer-vision3.p.rapidapi.com/areaOfInterest"
parameters={'visualfeatures':'description,color','language':'en'}
image_path="C:\\Users\\HP\\Downloads\\wp4190968-arashiyama-wallpapers.jpg"
image_data=open(image_path,"rb").read()
headers={"X-RapidAPI-Host":"microsoft-computer-vision3.p.rapidapi.com","X-RapidAPI-Key":subscription_key,"content-type": "application/json",
"accept": "application/json"}
response=requests.post(vision_service_address,data=image_data,headers=headers)
result=response.json()
print(json.dumps(result))
