def programa():

    lista = [("call","scan","Entre A","a"),
             ("=", "i", "0", None),
             ("label", "inicio", None, None),
             ("<", "TEMP", "i", "a"),
             ("if","TEMP",'verdadeiro','falsidade'),
             ("label",'verdadeiro',None,None),
             ("call","print","i",None),
             ("+","i","i","1"), 
             ("jump", "inicio", None, None),
             ("label",'falsidade',None,None),
             ("call","print","a",None)
            ]
    return lista


    # lista = [("call","scan","Entre A","a"),
    #          ("=", "i", "0", None),
    #          ("label", "inicio", None, None),
    #          ("<", "TEMP", "i", "a"),
    #          ("if","TEMP",'verdadeiro','falsidade'),
    #          ("label",'verdadeiro',None,None),
    #          ("call","print","i",None),
    #          ("+","i","i","1"), 
    #          ("jump", "inicio", None, None),
    #          ("label",'falsidade',None,None),
    #          ("call","print","a",None)
    #         ]

#  lista = [("call","scan","Entre A","a"),("call","scan","Entre B","b"),("+","c","a","b"),("/","c","c","2"),
#              ("call","print","Media =","c"), (">","TEMP","a","b"),("if","TEMP",'maior','menor'),
#              ("label",'maior',None,None),("call","print","A maior",None),("jump","fim",None,None), 
#              ("label",'menor',None,None),("call","print","B maior",None),("label","fim",None,None),
#              ("call","STOP",None, None)]

    # lista = [
    #     ("call", "scan", "Entre a", "a"), #scan -> escrita
    #     # ("call", "scan", "Entre b", "b"), #scan -> escrita
    #     ("<", "temp", "a", "10"), #acesso ou escrita
    #     # ("-", "temp", "a", "10"),
    #     ("if", "temp", "verdade", "falsidade"), 
    #     ("label", "verdade", None, None),
    #     ("call", "print", "Menor que 18", None), #print -> acesso
    #     ("jump", "fim", None, None),
    #     ("label", "falsidade", None, None),
    #     ("call", "print", "Maior==10", None),
    #     ("label", "fim", None, None)
    # ]
    # return lista

    # lista = [
    #     ("call", "scan", "Entre a", "a"), #scan -> escrita
    #     ("+", "temp", "a", "10"),
    #     ("!=", "a", "a", None),
    #     ("call", "print", "a", None)
    # ]
    # return lista

    # lista = [("call","scan","Entre A","a"),("call","scan","Entre B","b"),("+","c","a","b"),("/","c","c","2"),
    #          ("call","print","Media =","c"), (">","TEMP","a","b"),("if","TEMP",'maior','menor'),
    #          ("label",'maior',None,None),("call","print","A maior",None),("jump","fim",None,None), 
    #          ("label",'menor',None,None),("call","print","B maior",None),("label","fim",None,None),
    #          ("call","STOP",None, None)]
    # return lista

