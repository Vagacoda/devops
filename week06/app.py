from flask import Flask, request, render_template_string

app = Flask(__name__)
messages = []

html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>방명록</title>
</head>
<body>
    <h1>방명록</h1>

    <form method="post">
        <input type="text" name="name" placeholder="이름" required>
        <input type="text" name="message" placeholder="메시지" required>
        <button type="submit">등록</button>
    </form>

    <hr>

    {% for name, message in messages %}
        <p><b>{{ name }}</b> : {{ message }}</p>
    {% endfor %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def guestbook():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        messages.append((name, message))

    return render_template_string(html, messages=messages)

app.run(host="0.0.0.0", port=5000)
