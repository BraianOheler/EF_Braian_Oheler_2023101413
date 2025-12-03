from flask import Flask, render_template, request, redirect, url_for
from db_connection import get_db_connection
import pymysql

app = Flask(__name__)

LOTES = [
    {
        'lote': 1,
        'tipo': 'Ternero',
        'descripcion': 'Bovino joven, generalmente al pie de la madre.',
        'cantidad': 100,
        'precio': 'USD 250',
        'imagen': 'terneroEF.jpg'
    },
    {
        'lote': 2,
        'tipo': 'Novillito',
        'descripcion': 'Macho castrado de destete hasta aprox. 2 años.',
        'cantidad': 80,
        'precio': 'USD 450',
        'imagen': 'novillitoEF.jpg'
    },
    {
        'lote': 3,
        'tipo': 'Novillo',
        'descripcion': 'Macho castrado de más de 2 años.',
        'cantidad': 225,
        'precio': 'USD 700',
        'imagen': 'NovilloEF.jpg'
    },
    {
        'lote': 4,
        'tipo': 'Vaquillona',
        'descripcion': 'Hembra desde destete hasta su primera parición.',
        'cantidad': 25,
        'precio': 'USD 600',
        'imagen': 'VaquillonaEF.jpg'
    },
    {
        'lote': 5,
        'tipo': 'Vaca',
        'descripcion': 'Hembra adulta.',
        'cantidad': 70,
        'precio': 'USD 850',
        'imagen': 'VacaEF.jpg'
    },
    {
        'lote': 6,
        'tipo': 'Toro',
        'descripcion': 'Macho entero (no castrado).',
        'cantidad': 20,
        'precio': 'USD 1200',
        'imagen': 'toroEF.jpg'
    },
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', lotes=LOTES)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular']
        horario = request.form['horario']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO contactos (nombre_apellido, correo, celular, horario_contacto)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (nombre, correo, celular, horario))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('gracias'))

    return render_template('contacto.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

if __name__ == '__main__':
    # host 0.0.0.0 para que sea accesible desde cualquier IPv4 del equipo
    app.run(debug=True, host='0.0.0.0', port=5000)
