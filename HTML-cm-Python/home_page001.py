page = open('site_arquivo_py/index001.html', 'w')
page.write('<html lang="pt-br">\n')
page.write('<header>\n')
page.write('<meta charset="UTF-8">\n')
page.write('<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
page.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')

page.write('<title>Pagina html em Python</title>\n')

page.write('</header>\n')
page.write('<body>\n')

page.write('<p>Lista de contagem de 10 numeros</p>\n')

for c in range(10):
    page.write('<p>%d</p>\n' % c)
page.write('</body>\n')
page.write('</html>\n')
page.close()