from flask import Flask, render_template
# captuando todo flask 
app = Flask(__name__)
# ruta raiz
@app.route('/')
def inicio():
  titulo = "Bienvenido"
  return render_template('inicio.html', titulo=titulo)

# ruta equipo
@app.route('/base')
def base():
    titulo = "Archivo Base"
    return render_template('base.html', titulo=titulo)
  


# bloque de prueba para flask 
if __name__ == "__main__":
  app.run(debug=True)