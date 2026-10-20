import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_TITLE = os.getenv("APP_TITLE", "Електронний журнал")
APP_MESSAGE = os.getenv("APP_MESSAGE", "Застосунок запущено локально")


@app.route("/")
def index():
    return f"""
    <!doctype html>
    <html lang="uk">
    <head>
        <meta charset="utf-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">
        <title>{APP_TITLE}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 760px;
                margin: 50px auto;
                padding: 24px;
                line-height: 1.5;
            }}
            .card {{
                border: 1px solid #ddd;
                border-radius: 14px;
                padding: 24px;
            }}
            code {{
                background: #f3f3f3;
                padding: 3px 6px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{APP_TITLE}</h1>
            <p>{APP_MESSAGE}</p>
            <p>Предмети: <code>/api/subjects</code></p>
            <p>API: <code>/api/info</code></p>
            <p>Health: <code>/health</code></p>
        </div>
    </body>
    </html>
    """


@app.route("/api/info")
def api_info():
    return jsonify({
        "application": APP_TITLE,
        "platform": "cloud",
        "runtime": "python-flask",
        "status": "running",
        "student": "Ремінний Владислав",
        "version": "1.1"
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/subjects")
def subjects():
    return jsonify([
        {"id": 1, "title": "Хмарні технології"},
        {"id": 2, "title": "Бази даних"},
        {"id": 3, "title": "Вебпрограмування"}
    ])


@app.route("/api/env")
def env_info():
    return jsonify({
        "app_title": APP_TITLE,
        "environment": "cloud"
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
