import datetime
from flask import Flask


app = Flask(__name__)

@app.route('/auto-daily/api/update_today/<file_name>')
def update_today(file_name):
    today = datetime.date.today()
    with open('datas/' + file_name, 'a') as f:
        f.write(f'{today.year}-{today.month}-{today.day}\n')
    return 'OK'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
