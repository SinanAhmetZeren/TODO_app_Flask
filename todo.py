from flask import Flask, render_template,redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/HP/OneDrive/Desktop/- Flask-Todo-App/todo.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    todos = todo.query.all()   # todo'ların tamamını tüm özellikleri ile, sözlük olarak dönüyor.
    return render_template("index.html", todos = todos)



@app.route("/update/<string:id>")
def updateTodo(id):
    todo1 = todo.query.filter_by(id=id).first()  #bu id'ye sahip ilk todo'yu getir.
    todo1.completed = not todo1.completed
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo2 = todo.query.filter_by(id=id).first()  #bu id'ye sahip ilk todo'yu getir.
    db.session.delete(todo2)
    db.session.commit()
    return redirect(url_for("index"))



@app.route("/add", methods = ["post"])
def addTodo():
    title = request.form.get("title")  # title name'ine sahip değeri form'dan alıyoruz.
    newTodo = todo(title = title, completed = False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))



class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    completed = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all()  # program çalışmaya başlarken tablolar oluşturuluyor, zaten varsa yeniden oluşturulmuyor.
    app.run(debug=True)
