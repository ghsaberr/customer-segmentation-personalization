from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)  # Initialize Swagger


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict API
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            EngagementScore:
              type: number
            Recency:
              type: integer
            Frequency:
              type: integer
            Monetary:
              type: number
            LTV:
              type: number
            TransactionStdDev:
              type: number
    
    responses:
      200:
        description: Successful prediction response
        schema:
          type: object
          properties:
            prediction:
              type: string
              example: "High Value Customer"
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No input provided"}), 400

    # Example mock logic (replace with actual model)
    prediction = "High Value Customer" if data["Monetary"] > 1000 else "Low Value Customer"

    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)
