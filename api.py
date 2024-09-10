from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos
class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<SensorData {self.sensor_id} - {self.value}>'

# Rotas
@app.route('/data', methods=['POST'])
def collect_data():
    data = request.json
    new_data = SensorData(
        sensor_id=data['sensor_id'],
        timestamp=data['timestamp'],
        value=data['value']
    )
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'message': 'Data collected'}), 201

@app.route('/data', methods=['GET'])
def get_data():
    all_data = SensorData.query.all()
    output = []
    for data in all_data:
        output.append({
            'sensor_id': data.sensor_id,
            'timestamp': data.timestamp,
            'value': data.value
        })
    return jsonify({'data': output})

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'Server is running'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
