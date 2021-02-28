from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    complete=db.Column(db.Boolean)

@app.route('/')
def index():
    # show all todos
    todoList=Todo.query.all()
    
    return render_template("base.html",todoList=todoList)

@app.route("/add",methods=["Post"])
def add():
    # add new item
    title=request.form.get("title")
    newTodo=Todo(title=title, complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))
    
@app.route("/update/<int:todoId>")
def update(todoId):
    # update new item
    todo=Todo.query.filter_by(id=todoId).first()
    todo.complete=not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:todoId>")
def delete(todoId):
    # delete new item
    todo=Todo.query.filter_by(id=todoId).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)