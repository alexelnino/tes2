from flask import Flask, send_from_directory, render_template, request, redirect, url_for   #redirect dan url_for untuk disaat memasukkan pass dan di submit akan ditembak ke route yg lain
app= Flask(__name__, static_url_path='')        #string kosong karena folder images selevel dengan 1.py

# data={
#     "nama"="andi",
#     "pwd"="12345"
# }

#home.route
@app.route('/')
def home():
    return '<h1>Welcome to my web server!</h1>'

#render template html
@app.route('/html')
def html():
    return render_template('html.html')

@app.route('/html2')
def html2():
    return render_template('html2.html')

#POST route
@app.route('/post', methods=['POST'])
def post():
    nam=request.form['nama']
    pwd=request.form['pass']
    print('nama : ',nam,'\nPass : ',pwd)
    #return 'nama : '+nam+'\nPass : '+pwd
    return redirect(url_for('sukses',nama=nam))

@app.route('/sukses<string:nama>')
def sukses(nama):
    return '<h1>Selamat datang '+nama+'</h1>'

    # data=request.json
    # print('anda ngePOST : ' + data['nama']+data['pass'])
    # return 'anda ngePOST : ' + data['nama']+data['pass']

#render static file=>localhost:5000/images/onepiece13.jpg
@app.route('/images/<path:path>')   #root nya
def staticfile(path):
    return send_from_directory ('images', path) #folder name

#404 route
@app.errorhandler(404)
def error404(error):
    return '<h1>Error: 404 Not Found!</h1>'

if __name__=='__main__':
    app.run(debug= True)

