FROM python:3.9-slim  # Use a slim base image for efficiency

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY notebook/best_rf_model.pkl notebook/best_rf_model.pkl  # Copy model file

EXPOSE 8501  # Port for Streamlit

ENTRYPOINT ["streamlit", "run", "app.py"]