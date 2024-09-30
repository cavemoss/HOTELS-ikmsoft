FROM python:3.9.19-slim

WORKDIR /HotelMariupol

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app"]