from flask import Flask, jsonify, request, json
import os ## used to close screen
import logging ## import lgging

log = logging.getLogger('werkzeug') # remove debug mode
log.setLevel(logging.ERROR) ## remove error mesages

class color: ##  define colors to be used in Fake GUI
    end = "\033[0m"
    red = "\033[91m"
    green = "\033[92m"
    blue = "\033[94m"
    magenta = "\033[95m"
    white = "\033[37m"

app = Flask(__name__) ## start flask name funciton
scores = [] ## list to store user scores in order
names = [] ## list to hold user names in order
@app.route('/') ## start server

def index(): ## when recieved a post request

    return ('AKZ server') ## when web browser is started

@app.route('/test', methods=['POST'])
def test(): ## test method for post request

    name = request.json['name'] ## take the username from the list post request

    if name in names: ## if the name has been recieved before
        scores[names.index(name)] += 1 ## add one to the scores list for name index
       
    else: ## if name is new, has not been recieved before
        names.append(name) ## add name to names list
        scores.append(1) ## add one value to scores list
   
    os.system('clear') ## clear screen
    print(color.red+'User: |Score:'+color.end)
    max = 0 ## largest number
    for i in range (len(names)): ## for each name
        if scores[i] >= max: ## if names score is larger than max score
            max = scores[i] ## set max to names scores
    for i in range(len(names)): ## for each name
        if scores[i] == max: ## if the score is the max
            print(color.white) ## set color to white
        else: ## if score is not max
            print(color.blue) ## set color to blue
        print(names[i],"  ",scores[i]) ## print name and its scores

   
     #   sg.window(title = ((str(names[i])+ str(scores[i]))),leyout=[[]], margins=(100,50)).read() ## reset screen
    return jsonify({"success": "true"}), 201 ## return success value to pc
   
   

if __name__ == '__main__': ## when ip is pinged
    app.run(debug=True,port=80,host='10.168.91.219') ## ip of server, GET FROM IFCONFIG
