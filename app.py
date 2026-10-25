import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>CI/CD Cloud App</h1>
    <p>Версія застосунку розгортається автоматично.</p>
    <p>Варіант 7: СТО. Замовлення: <code>/api/orders</code></p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    }), 200


# Індивідуальний endpoint варіанта 7 (СТО): список замовлень
@app.route("/api/orders")
def orders():
    return jsonify([
        {"id": 1, "car": "Toyota Camry", "service": "Заміна масла", "status": "Виконано"},
        {"id": 2, "car": "Skoda Octavia", "service": "Діагностика ходової", "status": "В роботі"},
        {"id": 3, "car": "Renault Duster", "service": "Заміна гальмівних колодок", "status": "Очікує"}
    ])


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
