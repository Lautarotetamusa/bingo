from bingo import carton_valido
from jinja2 import Template

template = Template(open('src/plantilla.j2').read())
#file = open("a.html", "w");
#file.write(template.render(tabla = carton_valido()))
#file.close()
print template.render(tabla = carton_valido())
