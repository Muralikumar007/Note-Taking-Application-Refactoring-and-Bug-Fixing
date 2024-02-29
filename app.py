from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask import jsonify

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notes.append({"content": note, "timestamp": timestamp})
            # Redirect to avoid form resubmission on page refresh
            return redirect(url_for('index'))
    return render_template("home.html", notes=notes)

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    if 0 <= index < len(notes):
        del notes[index]
    # Redirect to avoid form resubmission on page refresh
    return redirect(url_for('index'))

@app.route('/delete-all', methods=["POST"])
def delete_all():
    notes.clear()
    # Redirect to avoid form resubmission on page refresh
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)