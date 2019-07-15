url1 = "https://www.alura.com.br/cursos-online-tecnologia"
import requests
from lxml import html

file = open("cursos.csv", "w")
file.truncate()

colunas = "curso;horas;link"

file.write(colunas + "\n")

page = requests.get(url1)
tree = html.fromstring(page.content)

courses = tree.xpath("//a[@class='cursoCard']")
for c in courses:
    url  = c.get("href")
    name = c.xpath(".//div[@class='cursoCard-nome']/text()")
    hour = c.xpath(".//div[@class='cursoCard-infos-tempoEstimado']/p[1]/text()")

    print(name, hour, url);
    file.write(name[0] + ";" + hour[0] + ";alura.com.br" + url + "\n")

file.close()
