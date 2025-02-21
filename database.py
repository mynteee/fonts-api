'''
entry explanations

{
"id": 0,                                the "id" of the font; for this case it is in the sequential order that i decided to add them
"name": "sample font",                  the name of the font in css (if not applicable use googleapis; if still not applicable use file name)
"family": "sample family",              one of the 5 generic font families in css (serif, sans-serif, monospace, cursive, fantasy)
"projects": ["project1", "project2"],   list of the projects ive used the font in
"serif": True                           if the font is serif (this is only sometimes redundant)
}
'''

data = [
    {"id": 0, "name": "sample font",    "family": "sample family",  "projects": ["project1", "project2", "project3"],                           "serif": None}, # sample entry
    {"id": 1, "name": "Bebas Neue",     "family": "sans-serif",     "projects": ["da-poster"],                                                  "serif": False},
    {"id": 2, "name": "Magilio",        "family": "serif",          "projects": ["cards", "check-please-program", "check-please-shirt"],        "serif": True},
    {"id": 3, "name": "Copperplate",    "family": "serif",          "projects": ["da-program"],                                                 "serif": True},
]
