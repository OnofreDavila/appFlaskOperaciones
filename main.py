from flask import Flask, render_template, request
app= Flask (__name__)

#usuarios registrados
usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidadTarros = int(request.form['cantidadTarros'])
        totalSinDesc: float = cantidadTarros * 9000
        totalConDesc: float = 0
        descuento: float = 0
        desc: float = 0
        if 18 <= edad <= 30:
            desc = 0.15
            descuento = totalSinDesc * desc
            totalConDesc = totalSinDesc - descuento
            return render_template('ejercicio1.html', nombre=nombre, totalSinDesc=totalSinDesc, descuento=descuento,
                                   totalConDesc=totalConDesc)
        elif edad > 30:
            desc = 0.25
            descuento = totalSinDesc * desc
            totalConDesc = totalSinDesc - descuento
            return render_template('ejercicio1.html', nombre=nombre, totalSinDesc=totalSinDesc, descuento=descuento,
                                   totalConDesc=totalConDesc)
        else:
            desc = 0
            return render_template('ejercicio1.html')

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        contraseña = str(request.form['contraseña'])
        resultado = ''

        if usuario in usuarios and usuarios[usuario] == contraseña:
            if usuario == 'juan':
                resultado = 'Bienvenido administrador ' + usuario
                return render_template('ejercicio2.html', resultado=resultado)
            elif usuario == 'pepe':
                resultado = 'Bienvenido Usuario ' + usuario
                return render_template('ejercicio2.html', resultado=resultado)
        resultado = 'Usuario o contraseña incorrecto.'
        return render_template('ejercicio2.html', resultado=resultado)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)