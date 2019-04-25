from flask import Flask, request, jsonify
app= Flask (__name__)

@app.route('/')
def home():
    return 'welcome!'

#request argument.
#shopee.co.id/search?keyword=tamiya

karyawan=[
    {'id':1, 'nama':'andi', 'job':'sales'},
    {'id':2, 'nama':'budi', 'job':'marketing'},
    {'id':3, 'nama':'cici', 'job':'it'}
]

@app.route('/search')
def search():
    # print(request.args)
    # print(request.args['katakunci'])      #/search?katakunci=d...&lokasi=...
    # print(request.args['lokasi'])
    # return request.args['katakunci']+' '+request.args['lokasi']
    # if 'keyword' in request.args:           #/search?keyword=... selain keyword akan muncul data tidak ditemukan
    #     return request.args['keyword']
    # else:
    #     return 'Data tidak ditemukan.'
    if 'id' in request.args:                    #http://localhost:5000/search?id=1
        id=int(request.args['id'])
        if id<1 or id>len(karyawan):
            return 'maaf data tidak ditemukan'
        else:
            return jsonify(karyawan[id-1])
    else:
        return jsonify(karyawan)
    
if __name__ == '__main__':
    app.run(debug=True)
