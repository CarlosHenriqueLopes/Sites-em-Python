filmes = {
    'Drama': ['filme1', 'filme2', 'filme3'],
    'Comedia': ['filme1', 'filme2', 'filme3'],
    'Terror': ['filme1', 'filme2', 'filme3'],
    'Romance': ['filme1', 'filme2', 'filme3'],
    'Acao': ['filme1', 'filme2', 'filme3']
}

page = open('HTML-cm-Python/index003.html', 'w')

page.write('''
<html lang="pt-br">
<header>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Pagina html em Python</title>

</header>
<body>

<h1>Dicionario de filmes</h1>
''')

# Marcadores: %d -> int, %s -> str, %f -> float
for k, v in filmes.items():
    page.write('<h2>%s</h2>' % k)
    for c in v:
        page.write('<p>%s</p>' % c)
page.write('''
</body>
</hmtl>)
''')
page.close()