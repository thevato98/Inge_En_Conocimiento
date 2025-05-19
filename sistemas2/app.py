from flask import Flask, render_template, request

app = Flask(__name__)  # CORREGIDO __name__

# Reglas para diagnóstico por síntoma
REGLAS_SINTOMA = {
    "apagado_motor": "Posible fallo en el sensor de ralentí o válvula IAC.",
    "humo_negro": "La mezcla de combustible es muy rica. Revisa el sensor de oxígeno o inyectores.",
    "arranque_lento": "La batería puede estar descargada o el motor de arranque tiene fallas.",
    "explosion_escape": "Puede haber una falla en la sincronización del encendido o mezcla pobre.",
    "vibracion": "Posibles bujías defectuosas o soportes de motor dañados.",
    "olor_gasolina": "Posible fuga de combustible o sistema EVAP con fallas.",
}

# Reglas para diagnóstico por código OBD-II
REGLAS_CODIGO = {
    "P0171": "Sistema demasiado pobre (Banco 1) – posible fuga de vacío o sensor MAF defectuoso.",
    "P0300": "Fallo de encendido aleatorio – revise bujías, bobinas o inyectores.",
    "P0420": "Eficiencia del catalizador por debajo del umbral – puede estar dañado.",
    "P0128": "Temperatura del refrigerante baja – posible termostato atascado.",
    "P0455": "Fuga grande en el sistema EVAP – revise tapa de gasolina o mangueras.",
}

def diagnostico_por_sintoma(sintoma):
    return REGLAS_SINTOMA.get(sintoma.lower().strip(), "Síntoma no reconocido. Intente con otro.")

def diagnostico_por_codigo(codigo):
    return REGLAS_CODIGO.get(codigo.upper().strip(), "Código OBD-II no reconocido. Verifique el formato.")

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        modo = request.form.get("modo")
        if modo == "sintoma":
            sintoma = request.form.get("sintoma", "").strip()
            resultado = diagnostico_por_sintoma(sintoma)
        elif modo == "codigo":
            codigo = request.form.get("codigo", "").strip()
            resultado = diagnostico_por_codigo(codigo)
        else:
            resultado = "Modo de diagnóstico no válido."

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":  # CORREGIDO __name__
    app.run(debug=True)
