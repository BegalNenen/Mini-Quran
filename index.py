from flask import Flask, jsonify, render_template, send_from_directory, request
import requests

app = Flask(__name__, template_folder="html", static_folder="assets")
app.url_map.strict_slashes = False

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def ayat():
    url = 'https://equran.id/api/v2/surat/'
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')
    
# buat bikin page custom untuk ayat
pages = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114']
@app.route('/surat/<page>')
def surat(page):
    if page not in pages:
        return render_template('404.html'), 404
    url = f'https://equran.id/api/v2/surat/{page}'
    response = requests.get(url)
    data = response.json()
    return render_template('ayat.html', data=data)

@app.route('/surat/<path:filename>')
def custom_static(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
