from flask import Flask, render_template
import os
import time

app = Flask(__name__)

WATCH_FOLDER = "."

def get_files():
    file_data = []
    for file in os.listdir(WATCH_FOLDER):
        if os.path.isfile(file):
            size = os.path.getsize(file)
            modified = time.ctime(os.path.getmtime(file))
            file_data.append((file, size, modified))
    return file_data

@app.route("/")
def home():
    files = get_files()
    return render_template("index.html", files=files)

if __name__ == "__main__":
    app.run(debug=True)