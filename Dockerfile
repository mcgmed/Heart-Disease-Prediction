FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY notebook/best_rf_model.pkl notebook/best_rf_model.pkl

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]