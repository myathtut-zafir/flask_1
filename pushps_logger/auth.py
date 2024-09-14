from flask import Blueprint,render_template

auth=Blueprint("auth",__name__)

@auth.route("/signup")
def signup():
    return "Sign up"

@auth.route("/login")
def login():
    return "Login"

def logout():
    return "Logout"