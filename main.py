from flask import Flask, render_template
import pandas as pd

# df = pd.read_csv("BS.csv")
# print(df.to_html())

app = Flask(__name__)
@app.route("/")
def main():
   return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
  app.run(port=8080,debug=True)
