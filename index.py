from flask import Flask, jsonify, render_template, send_from_directory, request
import requests

app = Flask(__name__, template_folder="html", static_folder="assets")
app.url_map.strict_slashes = False

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.route('/about')
def about():
    return render_template('about.html')    
            
# AL-QURAN
###############
@app.route('/')
def ayat():
    url = 'https://equran.id/api/v2/surat/'
    response = requests.get(url)
    data = response.json()
    return render_template('alquran/index.html', data=data)
    
# For Loop untuk membuat halaman dengan nama angka secara otomatis
numbers = [i for i in range(1, 114)]
@app.route('/surat/<int:n>')
def isi(n):
    url = f'https://equran.id/api/v2/surat/{n}'
    response = requests.get(url)
    if response.status_code == 404:
        return render_template('404.html', error="Halaman tidak ditemukan")
    data = response.json()
    return render_template('alquran/ayat.html', data=data)

# DOA
##############
@app.route('/doa')
def Doa():
    url = 'https://equran.id/api/doa/'
    response = requests.get(url)
    data = response.json()
    return render_template('/doa/index.html', data=data)
    
numbers = [i for i in range(1, 114)]
@app.route('/doa/<int:n>')
def Doanya(n):
    url = f'https://equran.id/api/doa/{n}'
    response = requests.get(url)
    if response.status_code == 404:
        return render_template('404.html', error="Halaman tidak ditemukan")
    data = response.json()
    return render_template('doa/doa.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
