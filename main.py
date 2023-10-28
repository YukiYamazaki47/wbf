from flask import Flask, render_template,abort
import json
from db.db import get_wlists_nams, get_wisches, get_wisch_ids, get_wisch, get_wisches_data

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "404 Error - Page not found", 404

@app.route('/',methods=['GET'])
def index()->str:

    return render_template('/index/html/index.html')

@app.route('/wisch/<int:wid>',methods=['GET'])
def wisch(wid:int)->str:
    if wid not in get_wisch_ids(): abort(404)
    return "NO"

@app.route('/wlist/<wlist>',methods=['GET'])
def wlist(wlist:str)->str:

    if wlist.upper() not in get_wlists_nams():abort(404)

    return render_template('/wlist/html/index.html')

@app.route('/api/wlists',methods=['GET'])
def api_wlits()->str:

    return json.dumps(get_wlists_nams())

@app.route('/api/wisches/data/<wlist>',methods=['GET'])
def apt_wisches_data(wlist:str)->str:
    if wlist.upper() not in get_wlists_nams(): abort(404)
    return json.dumps(get_wisches_data(wlist))

@app.route('/api/wisches/<wlist>',methods=['GET'])
def apt_wisches(wlist:str)->str:
    if wlist.upper() not in get_wlists_nams(): abort(404)
    return json.dumps(get_wisches(wlist))

@app.route('/api/wisch/<int:wid>',methods=['GET'])
def apt_wisch(wid:int)->str:
    if wid not in get_wisch_ids(): abort(404)
    return json.dumps(get_wisch(wid))

if __name__ == '__main__':
    app.run(debug=True)