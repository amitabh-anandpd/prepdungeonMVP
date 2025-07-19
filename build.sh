# exit on error
set -o errexit

# Tesseract
echo "---> Installing Tesseract OCR Engine..."
#apt-get update && apt-get install -y tesseract-ocr libtesseract-dev
apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-eng

echo "---> Installing Python requirements..."
pip install -r requirements.txt

echo "---> Collecting static files..."
python manage.py collectstatic --noinput

echo "---> Running Django database migrations..."
python manage.py makemigrations
python manage.py migrate
