from flask import Flask, render_template

from controllers.books import books

# App Factory Pattern: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
def create_app():
    app = Flask(__name__)

    # https://stackoverflow.com/questions/46944596/is-autoescape-default-in-jinja2-flask
    app.jinja_options["autoescape"] = lambda _: True

    @app.errorhandler(404)
    def page_not_found(e):
        return """<!DOCTYPE html>
<html>
<head><title>404 Not Found</title></head>
<body><p><img src="https://http.cat/404.jpg"></p></body>
</html>
"""

    @app.route("/")
    def index():
        return render_template("base.html.j2", title="Welcome")

    app.register_blueprint(books)

    return app

if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)
    app.run()
