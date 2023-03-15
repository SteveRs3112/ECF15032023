import re

# Ouvrir le fichier texte en mode lecture
with open("input-emails.txt", "r") as f:
    # Lire le contenu du fichier
    content = f.read()
    # Trouver tous les emails français se terminant par ".fr"
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[fr|FR]{2,}\b'
    emails = re.findall(pattern, content)
    # Imprimer la liste des emails trouvés
    print(emails)
    
    
# A la base, j'avais fait le script depuis une liste
# import re
 
# def veriflisteadrmail(L):
#     """vérifie la syntaxe d'une liste d'adresses mail données sous forme de chaine"""
#     R = [] # future liste des adresses valides
#     E = [] # future liste des adresses invalides
#     reExt = re.compile(r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)")
#     reVerif = re.compile(r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[fr]{2,})$")
#     for ch in L:
#         # extraction de l'adresse même dans le cas 'yyyyy <xxxx@xxxx.xxx>' 
#         a = reExt.findall(ch.strip())
#         if len(a)>0:
#             adr = ''.join(a[0]).strip()
#         else:
#             adr = ''
#         # vérification de syntaxe de l'adresse mail extraite
#         if adr=='':
#             E.append(ch)
#         else:
#             if reVerif.match(adr)!=None:
#                 R.append(ch)
#             else:
#                 E.append(ch)
#     return [R]

# #ma liste test
# # L = ["jeanlouismichel@aol.fr",
# #      "robert.oui.xxx@xxx.xxx.fr",
# #      "toto <xxxx.xxx.xxx@xxx.xxx.fr>",
# #      "toto <xxxx.xxx.xxx@xxx.xxx.com",
# #      "toto xxxx.xxx.xxx@co.uk>",
# #      "to<to <xxxx.xxx.xxx@xxx.xxx.xxx>",
# #      "tot>o xxxx.xxx.xxx@xxx.xxx.xxx>",
# #      "toto <xxxx.xxx.xxxxxx.xxx.xxx>",
# #      "toto <xxxx..xxx.xxx@xxx.xxx.xxx>",
# #      ".xxxx@xxx.xxx",
# #      "xxxx.@xxx.xxx"
# #      ]

# #mon test
# #veriflisteadrmail(L)
# #si besoin d'afficher les adresses non valides, faire return[E]
