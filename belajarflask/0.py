#pip install flask
#mempelajari flask
from flask import Flask, render_template, jsonify, abort, make_response,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

karyawan=[
    {'id':1,'nama':'andi','usia':22},
    {'id':2,'nama':'budi','usia':23},
    {'id':3,'nama':'caca','usia':24}
]

@app.route('/data')
def data():
    return jsonify(karyawan)

@app.route('/data/<int:id>')
def dataSatuan(id):
    if id<1 or id>len(karyawan):
        abort(404)
    else:
        return jsonify(karyawan[id-1])

@app.errorhandler(404)
def tidakFound(error):
    return make_response(
        render_template('error.html')
    )

profilku={
    'nama':'el nino',
    'usia':27
}
@app.route('/about')
def about():
    return render_template(
        'about.html',
        profil=profilku        
    )

@app.route('/tes',methods=['GET','POST','PUT','DELETE'])
def tes():
    if request.method=='GET':
        return 'anda nge-GET'
    elif request.method=='POST':
        pesanBody=request.json
        print(pesanBody['nama'])
        return 'pesan yang anda kirim = '+pesanBody['nama']
    else:
        return 'anda tidak nge-GET atau nge_POST'

if __name__=='__main__':
    app.run(debug=True)


#postman
# get = mengambil data
# post=mengirim data. misalnya log up
# delete=menghapus data
# cara ngepost=>post;body;raw;json

