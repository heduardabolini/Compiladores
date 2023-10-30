def programa():
    lista = [
        ("call", "scan", "Entre a", "a"), #scan -> escrita
        ("<", "temp", "a", "10"), #acesso ou escrita
        ("if", "temp", "verdade", "falsidade"), 
        ("label", "verdade", None, None),
        ("call", "print", "Menor que 18", None), #print -> acesso
        ("jump", "fim", None, None),
        ("label", "falsidade", None, None),
        ("call", "print", "Maior==10", None),
        ("label", "fim", None, None)
    ]
    return lista


