from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    page = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anos Web</title>
      </head>
      <body>
        <h1>Anos Panel</h1>

        <form action="/" method="POST">
          <input name="pseudo" placeholder="Ton pseudo" required>
          <button type="submit">Envoyer</button>
        </form>
      </body>
    </html>
    """

    if request.method == "POST":
        pseudo = request.form["pseudo"]
        return render_template_string(f"Bienvenue : {pseudo}")

    return render_template_string(page)

if __name__ == "__main__":
    app.run(debug=True)
