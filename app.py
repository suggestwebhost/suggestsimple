from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Define data you want to send to the HTML page
    user_name = "Suggest"
    favorite_languages = ["Python", "HTML", "JavaScript"]
    
    # Pass variables as keyword arguments into render_template
    return render_template("index.html", name=user_name, tech_stack=favorite_languages)

if __name__ == "__main__":
    app.run(debug=True)
