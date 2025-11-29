import joblib
import pandas as pd
import os

# Load model and encoder
model_path = os.path.join("models", "thyroid_model.pkl")
encoder_path = os.path.join("models", "encoder.pkl")  # optional if you saved it
model = joblib.load(model_path)

# If encoder exists, load it; otherwise handle encoding manually
encoder = None
if os.path.exists(encoder_path):
    encoder = joblib.load(encoder_path)

def predict_thyroid(name, age, gender, pregnant, location, sugar_level, systolic, diastolic, TSH, T3, TT4):
    # Prepare a single-row DataFrame with input features
    data = {
        'age': [age],
        'sex': [gender.capitalize()],
        'pregnant': [pregnant.capitalize()],
        'location': [location.capitalize()],
        'sugar_level': [sugar_level],
        'systolic_bp': [systolic],
        'diastolic_bp': [diastolic],
        'TSH': [TSH],
        'T3': [T3],
        'TT4': [TT4]
    }
    df = pd.DataFrame(data)

    # Encode categorical values the same way as in training
    if encoder:
        df_encoded = encoder.transform(df)
    else:
        # Fallback: manually one-hot encode categorical columns (for safety)
        df_encoded = pd.get_dummies(df, columns=['sex', 'pregnant', 'location'], drop_first=True)

        # Ensure same columns as training
        model_features = model.feature_names_in_
        for col in model_features:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        df_encoded = df_encoded[model_features]

    # Predict thyroid class
    pred = model.predict(df_encoded)[0]

    # Optional: get probability/confidence
    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(df_encoded).max()
    else:
        confidence = None

    return {
        "Name": name,
        "Predicted_Level": pred,
        "Confidence": f"{confidence*100:.2f}%" if confidence else "N/A"
    }
