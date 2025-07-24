

python3 -m pip install -r requirements.txt
echo "🔧 Creating database..."
flask db init
flask db migrate -m "Initial migration"
flask db upgrade