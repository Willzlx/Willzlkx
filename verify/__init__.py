def isint(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print("Valor não idetificado, Tente novamente.")
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return number
