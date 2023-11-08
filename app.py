from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from webforms.Userform import UserForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin@localhost/tabuleirodb' #INSERIR URI DO DATABASE
app.config['SECRET_KEY'] = 'essa é uma chave super secreta contra todo o mal do mundo!'
db = SQLAlchemy(app)


@app.route('/user', methods=['GET', 'POST'])
def add_user():
    from models.users import Users
    name = None
    form = UserForm()

    if form.validate_on_submit():
        user = Users(
            person_name=form.name.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password_hash.data),
        )

        db.session.add(user)
        db.session.commit()

        flash('Usuário adicionado com sucesso!')
        return redirect(url_for('add_user'))  # Redirecione para a mesma página após o sucesso

    
    return render_template('add_user.html', form=form, name=name)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
