from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host= '10.20.30.3',
            database= 'helpdesck_db',
            user= 'user_api',
            password= 'j1j2m3'
        )
        return conn
    except Error as e:
        print(f"Erro de banco: {e}")
        return None
    
@app.route('/api/chamados', methods=['GET'])
def listar_chamados():
    conn = get_db_connection()
    if not conn:
        return jsonify({"erro": "Banco indisponivel"}), 500

    try:
        cursor = conn.cursor(dictionary= True)
        cursor.execute("SELECT FROM chamados ORDER BY data_criacao DESC")
        chamados = cursor.fetchall()
        return jsonify(chamados), 200
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)