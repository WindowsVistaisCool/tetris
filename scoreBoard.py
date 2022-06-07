from flask import Flask, jsonify, request, json
import os
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class color:
    end = "\033[0m"
    red = "\033[91m"
    green = "\033[92m"
    blue = "\033[94m"
    magenta = "\033[95m"
    white = "\033[37m"

app = Flask(__name__)
scores = []
names = []
@app.route('/')

def index():

    return ('AKZ server')

@app.route('/test', methods=['POST'])
def test():

    name = request.json['name'] ## take the username from the list post request

    if name in names: ## if the name has been recieved before
        scores[names.index(name)] += 1 ## add one to the scores list for name index
        
    else: ## if name is new, has not been recieved before
        names.append(name) ## add name to names list
        scores.append(1) ## add one value to scores list
    
    os.system('clear')
    print(color.red+'User: |Score:'+color.end)
    max = 0
    for i in range (len(names)):
        if scores[i] >= max:
            max = scores[i]
    for i in range(len(names)):
        if scores[i] == max:
            print(color.white)
        else:
            print(color.blue)
        print(names[i],"  ",scores[i])

    
     #   sg.window(title = ((str(names[i])+ str(scores[i]))),leyout=[[]], margins=(100,50)).read()
    return jsonify({"success": "true"}), 201
    
    

if __name__ == '__main__':
    app.run(debug=True,port=80,host='10.168.91.219')

