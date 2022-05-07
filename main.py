import function

while True:
    op = function.cadastro(['Acessar CMD (usuario)', 'Rastrear dominio IP', 'Fechar o programa'])
    if op == 0:
        function.cmdcommand()
    elif op == 1:
        function.localizardominio()
    elif op == 2:
        print('\nPrograma finalizado.')
        break
