from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Load model kalian disini
model = tf.keras.models.load_model('linear.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Lakukan Preprocess data terlebih dahulu jika ada
    data_predict = int(data["data"])

    # Make predictions using the loaded model
    predictions = model.predict([[data_predict]])

    # Lakukan Postprocess data terlebih dahulu jika ada
    # ...

    # Return the predictions as a JSON response
    return jsonify(predictions.item())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
