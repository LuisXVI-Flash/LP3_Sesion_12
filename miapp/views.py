from django.shortcuts import render, HttpResponse

layaout="""<h1>ProyectoWeb(LP3) | Luis Angel IZquierdo rojas</h1>
<hr>
<ul>
    <li>
    <a href="/inicio">Inicio</a>
    </li>
      <li>
    <a href="/saludo">Mensaje de  saludo</a>
    </li>
      <li>
    <a href="/rango">Mostrar números [a,b]</a>
    </li>
    </ul>
    </hr>
    """

def inicio(request):
    return render(request, 'index.html')

def saludo(request):
    mensaje="""
        <h1>Bienvenidos</h1>
        <h2>Luis Angel Izquierdo Rojas</h2>
        <h3>Lenguaje de Programacion III</h3>
        """
    return HttpResponse(mensaje)

def saludo2(request):
    return render(request, 'saludo.html')

def rango(request):
    a=10
    b=20
    resultado=f"""
    <h2>Numeros de[{a},{b}]</h2>
    Resultado: <br>
    <ul>
    """
    while a<=b:
        resultado+=f"<li>{a}</li>"
        a+=1
    resultado+= "</ul>"
    return HttpResponse(layaout + resultado)

def rango2(request,a=0,b=100):
    
    resultado=f"""
            <h2>Numeros de[{a},{b}]</h2>
            Resultado: <br>
            <ul>
        """
    while a<=b:
        resultado+=f"<li>{a}</li>"
        a+=1
    resultado+= "</ul>"
    return HttpResponse(layaout + resultado)