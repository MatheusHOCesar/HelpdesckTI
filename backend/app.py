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

@app.route('/api/chamados', methods=['POST'])
def abrir_chamado():
    dados = request.get_json()
    if not dados or not 'titulo' in dados or not 'descricao' in dados:
        return jsonify({"erro": "Dados imcompletos"}), 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO chamados (titulo, descricao, usuario_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (dados['titulo'], dados['descricao'], dados['usuario_id']))
        conn.commit()
        return jsonify({"mensagem": "Chamado aberto!"}), 201
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)