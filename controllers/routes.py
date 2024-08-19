from flask import render_template, request
from datetime import date #usar pra inserir a data atual

def init_app(app):
    
    itensHome = [{"ID": 1, "Nome": "Pyke", "Origem": "League of Legends"}, {"ID": 2, "Nome": "Liu Kang", "Origem": "Mortal Kombat"}, {"ID": 3, "Nome": "Mario", "Origem": "Super Mario World"}, {"ID": 4, "Nome": "Homem Aranha", "Origem": "Homem Aranha"}]
    person = []
    
    @app.route("/", methods=["GET", "POST"])
    def home(): 
        
        if request.method == "POST":
            if request.form.get("nome") and request.form.get("origem"):
                itensHome.append({"ID": len(itensHome) + 1, "Nome": request.form.get("nome"), "Origem": request.form.get("origem")})
        
        return render_template("index.html", itensHome=itensHome)
    
    @app.route("/personagens", methods=["GET", "POST"])
    def personagens():
        tperson = len(person)
        if request.method == "POST":
            if request.form.get("lore"):
                person.append(request.form.get("lore"))
        
        return render_template("personagens.html", person=person, tperson=tperson)
    
    @app.route("/listarPersonagens")
    def novos():
        return render_template("listarPersonagens.html", itensHome=itensHome)