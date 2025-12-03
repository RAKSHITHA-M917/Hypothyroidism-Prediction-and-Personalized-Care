python -m venv .venv


.venv\Scripts\activate


pip install -r requirements.txt

python -m src.model_train


python run_report.py

python app.py
