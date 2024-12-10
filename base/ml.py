import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Train a refined model with extensive data
def train_price_model():
    data = {
        "temperature": [
            50, 40, 30, 20, 35, 25, 60, 55, 45, 15, 10, 70, 65, 55, 30, 20, 25, 40, 50, 30,
            80, 75, 35, 28, 18, 12, 25, 32, 40, 50, 65, 55, 38, 22, 48, 70, 75, 68, 20, 10,
            25, 45, 33, 58, 48, 20, 5, 60, 40, 70, 80, 85, 30, 15, 50, 42, 27, 35, 60, 28
        ],
        "rain": [
            "mist", "moderate", "heavy", "snow", "mist", "moderate", "mist", "mist",
            "moderate", "snow", "heavy", "none", "none", "moderate", "snow", "moderate",
            "heavy", "none", "none", "snow", "none", "light", "moderate", "heavy", "snow",
            "msit", "light", "heavy", "mist", "moderate", "snow", "none", "light", "heavy",
            "moderate", "mist", "snow", "moderate", "light", "none", "snow", "mist", "light",
            "moderate", "mist", "heavy", "light", "none", "snow", "moderate", "mist", "mist",
            "light", "snow", "moderate", "mist", "heavy", "moderate", "snow", "mist"
        ],
        "busyness": [
            0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1,
            0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1,
            1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1
        ],
        "base_price": [
            5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 4.5, 4.5, 5.0, 6.0, 6.0, 4.0, 4.0, 5.0, 5.0, 6.0,
            5.5, 5.0, 5.0, 6.0, 4.5, 4.7, 5.3, 6.5, 6.7, 4.5, 5.0, 6.0, 4.8, 5.5, 6.0, 5.0,
            5.5, 5.0, 4.5, 6.0, 5.0, 4.5, 6.0, 5.0, 4.0, 6.0, 5.5, 5.0, 5.0, 5.3, 4.0, 6.5,
            5.0, 5.5, 5.3, 4.0, 6.0, 5.2, 5.0, 5.8, 4.9, 5.6, 5.5, 6.2
        ],
        "adjusted_price": [
            5.0, 5.5, 6.5, 7.0, 5.0, 6.0, 4.5, 4.7, 5.3, 7.5, 7.0, 4.0, 4.2, 5.6, 6.5, 7.2,
            6.7, 5.1, 5.0, 7.3, 4.6, 4.9, 5.5, 6.8, 7.4, 4.8, 5.2, 6.3, 4.9, 5.8, 6.5, 5.3,
            5.7, 5.2, 4.6, 6.2, 5.6, 4.9, 6.8, 5.4, 4.7, 6.3, 5.6, 5.3, 5.5, 5.8, 4.3, 6.6,
            5.3, 5.6, 5.5, 4.3, 6.2, 5.4, 5.1, 6.0, 5.0, 6.1, 5.6, 6.4
        ]
    }
    df = pd.DataFrame(data)
    
    # Encode categorical 'rain' feature into numerical values
    rain_encoder = LabelEncoder()
    df["rain_encoded"] = rain_encoder.fit_transform(df["rain"])
    
    # Define features and target variable
    X = df[["temperature", "rain_encoded", "busyness", "base_price"]]
    y = df["adjusted_price"]

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X, y)
    
    return model, rain_encoder


# Predict new prices based on the trained model
def predict_price(model, rain_encoder, temperature, rain, busyness, base_price):
    # Encode the rain condition (string to numeric)
    try:
        rain_encoded = rain_encoder.transform([rain])[0]
    except ValueError:
        # Handle unseen labels by assigning a default value (e.g., 0)
        print(f"Warning: Unseen rain condition '{rain}' encountered. Assigning default value.")
        rain_encoded = 0  # Or you can choose a default encoding for unknown labels
    
    # Use the trained model to predict the adjusted price
    predicted_price = model.predict([[temperature, rain_encoded, busyness, base_price]])[0]
    return predicted_price


# Example usage: Training the model and making predictions
if __name__ == "__main__":
    model, rain_encoder = train_price_model()

    # Predicting a price for a specific condition
    predicted_price = predict_price(
        model, rain_encoder, temperature=25, rain="mist", busyness=1, base_price=5.0
    )
    
    print(f"Predicted Price: ${predicted_price:.2f}")
