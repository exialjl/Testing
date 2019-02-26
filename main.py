from flask import Flask
import pandas as pd

# df = pd.read_csv("BS.csv")
# print(df.to_html())

app = Flask(__name__)
@app.route("/")
def main():
   return app.send_static_file("index.html")

@app.route("/about/")
def about():
    return app.send_static_file("about.html")

if __name__ == "__main__":
  app.run()
