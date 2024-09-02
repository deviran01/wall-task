FROM python:3.10-slim
WORKDIR /app
COPY ./pip/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest-playwright allure-pytest
RUN playwright install --with-deps
COPY . .
CMD ["pytest", "--alluredir=/app/allure-results"]
