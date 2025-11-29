import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

# ==============================
# 1️⃣ Load Dataset
# ==============================
data_path = os.path.join("data", "Thyroid-Dataset-Updated.csv")
print("📂 Loading dataset...")
df = pd.read_csv(data_path)

print(f"✅ Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
print(f"🔍 Columns found: {list(df.columns)}")

# ==============================
# 2️⃣ Clean / Prepare Dataset
# ==============================
# Drop rows with missing target
df = df.dropna(subset=["level_of_hypothyroid"])

# Separate features and label
X = df.drop(columns=["level_of_hypothyroid"])
y = df["level_of_hypothyroid"]

# Identify feature types
categorical_cols = [
    "sex", "on thyroxine", "query on thyroxine", "on antithyroid medication",
    "sick", "pregnant", "thyroid surgery", "I131 treatment",
    "query hypothyroid", "query hyperthyroid", "lithium", "goitre",
    "tumor", "hypopituitary", "psych", "referral source"
]

numeric_cols = ["age", "TSH", "T3", "TT4", "T4U", "FTI"]

# ==============================
# 3️⃣ Preprocessing Pipelines
# ==============================
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", categorical_transformer, categorical_cols),
        ("num", numeric_transformer, numeric_cols)
    ]
)

# ==============================
# 4️⃣ Full Model Pipeline
# ==============================
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        random_state=42,
        n_estimators=200,
        max_depth=15,
        n_jobs=-1
    ))
])

# ==============================
# 5️⃣ Train-Test Split
# ==============================
print("🧠 Splitting dataset into train/test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 6️⃣ Train Model
# ==============================
print("🌳 Training RandomForestClassifier model...")
model.fit(X_train, y_train)
print("✅ Model training complete!")

# ==============================
# 7️⃣ Save Model
# ==============================
os.makedirs("models", exist_ok=True)
model_path = os.path.join("models", "thyroid_model.pkl")

joblib.dump(model, model_path)
print(f"💾 Model saved successfully at: {model_path}")

# ==============================
# 8️⃣ Evaluate (optional)
# ==============================
score = model.score(X_test, y_test)
print(f"📊 Model accuracy on test data: {score:.2f}")
