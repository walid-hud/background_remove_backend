from waitress import serve
from App import app

serve(app, host='0.0.0.0', port=8080)
