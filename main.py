import chromedriver_autoinstaller
from res.scripts.get_jwt import get_jwt
from res.scripts.generate_images import get_image_batch
from res.SaveConfig import SaveConfig

from flask import Flask, request, jsonify

#get email and password
email = ""
password = ""

with open('account.txt', 'r') as file:
    email = file.readline().replace('\n', '')
    password = file.readline().replace('\n', '')
    

#get jtw
chromedriver_autoinstaller.install()
_jwt = get_jwt(email, password)

print("Got jwt:", _jwt)

#prepare saveconfig
save_config = SaveConfig(
    save_dir="output/images",
    save_name="image",
    force_mkdir=True,
    additional_return_mode=True,
    separator="-"
)

#run flask
app = Flask("lol")

@app.route('/sdapi/v1/options')
def apiOptions():
    return 'ok'

@app.route('/sdapi/v1/sd-models')
def apiModels():
    return 'ok'

@app.route('/sdapi/v1/txt2img', methods=['POST'])
def text2Image() :
    data = request.get_json()
    prompt = data['prompt']
    negative_prompt = data["negative_prompt"]
    width = data["width"]
    height = data["height"]
    
    images = get_image_batch(
        prompt=prompt,
        negative_prompt=negative_prompt,
        size=(width, height),
        _n=1,
        __jwt=_jwt,
        _saveConfig=save_config
    )
    
    data = {"format" : 'png', "images" : images}
    return jsonify(data)

app.run(debug=False)