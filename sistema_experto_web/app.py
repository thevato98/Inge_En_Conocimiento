from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tarea', methods=['GET', 'POST'])
def tarea():
    if request.method == 'POST':
        total = 0

        if request.form.get('portada') == 'si':
            total += 2

        funcionamiento = request.form.get('funcionamiento')
        if funcionamiento == 'si':
            total += 4
        elif funcionamiento == 'errores':
            total += 2

        if request.form.get('documentacion') == 'si':
            total += 2

        if request.form.get('conclusion') == 'si':
            total += 2

        return render_template('resultado.html', tipo='Tarea Práctica', total=total)

    return render_template('tarea.html')

@app.route('/presentacion', methods=['GET', 'POST'])
def presentacion():
    if request.method == 'POST':
        total = 0

        if request.form.get('presentacion') == 'si':
            total += 3

        if request.form.get('muletillas') == 'si':
            total += 1

        programa = request.form.get('programa')
        if programa == 'si':
            total += 4
        elif programa == 'errores':
            total += 2

        return render_template('resultado.html', tipo='Presentación', total=total)

    return render_template('presentacion.html')

if __name__ == '__main__':
    app.run(debug=True)
