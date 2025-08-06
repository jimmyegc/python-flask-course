from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexión MySQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "menikmati"
app.config["MYSQL_PASSWORD"] = "menikmati"
app.config["MYSQL_DB"] = "facturacion"

conexion = MySQL(app)

@app.route('/')
def index():
  courses = ["Python", "React", "AWS", "Next", "HTML", "CSS", "JavaScript"]
  data = {
      'title': 'Home',
      'welcome': 'Python course',
      'courses': courses,
      'coursesLength': len(courses)
  }
  return render_template('index.html', data=data)

@app.route('/ping')
def ping():
    return "Pong!"

@app.route('/contact')
def contact_page():
  return render_template('contact.html')

@app.route('/clientes')
def clientes():
  return render_template('clientes.html')

@app.route('/clients')
def getClientes():
  data={}
  try:
    cursor=conexion.connection.cursor() 
    sql="Select * from cliente"
    cursor.execute(sql)
    clientes = cursor.fetchall()
    print(clientes)
    data['clientes'] = clientes
    data['message'] = 'Exito'
  except Exception as ex: 
    data['message']='error...'
  return jsonify(data)

def query_string():
  print(request)
  print(request.args)
  print(request.args.get('message'))
  return "OK"

def pagina_no_encontrada(error):
  # return render_template('404.html'), 404
  return redirect(url_for('index'))

if __name__ == '__main__':    
  app.add_url_rule('/query_string', view_func=query_string)
  app.register_error_handler(404, pagina_no_encontrada)
  app.run(debug=True, host='0.0.0.0', port=3000)