from flask import Flask, jsonify

APP_MESSAGE = "Projeto DevOps rodando com CI/CD + Docker!"


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return jsonify({"message": APP_MESSAGE, "status": "ok"})

    @app.get("/health")
    def health():
        return jsonify({"healthy": True})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
