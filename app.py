from flask import Flask, jsonify
import api, translate

app = Flask(__name__)

@app.route("/desculpa", methods=["GET"])
def desculpa_traduzida():
    NoAsAService_API = api.get_api_key("NAAS")
    excuse = api.get_excuse(NoAsAService_API)
    if excuse is None:
        return jsonify({"error": "Sem resposta da API externa"}), 502
    if isinstance(excuse, str) and (excuse.startswith("Request error:") or excuse.startswith("Error") or excuse.startswith("Field")):
        return jsonify({"error": excuse}), 502
    translated_excuse = translate.translate_text(excuse, target_language="pt")
    return jsonify({"desculpa": translated_excuse})
