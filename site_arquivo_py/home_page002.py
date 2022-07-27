page = open('site_arquivo_py/index002.html', 'w')
page.write('''
<html lang="pt-br">
<header>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Pagina html em Python</title>

</header>
<body>

<p>Lista de contagem de 10 numeros</p>
''')

for c in range(10):
    page.write('<p>%d</p>\n' % c)
page.write('''
</body>
</html>
''')
page.close()