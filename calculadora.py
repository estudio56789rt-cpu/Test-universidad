from pyscript import window, display

dato1 = window.prompt("Ingresa el primer número:")
dato2 = window.prompt("Ingresa el segundo número:")

if dato1 is not None and dato2 is not None and dato1 != "" and dato2 != "":
    num1 = float(dato1)
    num2 = float(dato2)
    suma = num1 + num2
    display(f"La suma es: {num1} + {num2} = {suma}", target="resultado", append=True)
else:
    display("Presiona el botón 'Sumar números' para calcular.", target="resultado", append=False)