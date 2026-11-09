from flask import request
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <div style="text-align: center; margin-top: 50px;">
        <h1>АЯТО</h1>
        <img src="https://avatars.mds.yandex.net/i?id=9e93fa88421eed9ac94c06478d4e567c_l-6301299-images-thumbs&n=13" style="max-width: 100%;"> 
    </div>   
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=15000)
