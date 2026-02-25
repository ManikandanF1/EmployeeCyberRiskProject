from flask import Flask, render_template, request, jsonify
import os
import time
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration from environment
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
WATCH_FOLDER = os.getenv('WATCH_FOLDER', '.')
APP_NAME = os.getenv('APP_NAME', 'Employee Cyber Risk Monitor')
APP_VERSION = os.getenv('APP_VERSION', '2.0.0')

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('cyber_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Risk classification based on file extensions
HIGH_RISK_EXTENSIONS = {'.exe', '.bat', '.cmd', '.scr', '.pif', '.com', '.vbs', '.js', '.jar', '.dll'}
MEDIUM_RISK_EXTENSIONS = {'.zip', '.rar', '.7z', '.tar', '.gz', '.pdf', '.doc', '.docx', '.xls', '.xlsx'}
LOW_RISK_EXTENSIONS = {'.txt', '.jpg', '.png', '.gif', '.mp4', '.mp3', '.html', '.css', '.py', '.md'}

def classify_risk(filename):
    """Classify file risk based on extension"""
    _, ext = os.path.splitext(filename.lower())

    if ext in HIGH_RISK_EXTENSIONS:
        return 'high'
    elif ext in MEDIUM_RISK_EXTENSIONS:
        return 'medium'
    else:
        return 'low'

def get_files():
    """Get file data with risk classification"""
    file_data = []
    try:
        logger.info(f"Scanning directory: {WATCH_FOLDER}")
        for file in os.listdir(WATCH_FOLDER):
            if os.path.isfile(file):
                size = os.path.getsize(file)
                modified_timestamp = os.path.getmtime(file)
                modified = time.ctime(modified_timestamp)
                risk = classify_risk(file)
                file_data.append((file, size, modified, risk))

        logger.info(f"Found {len(file_data)} files")
    except PermissionError as e:
        logger.error(f"Permission error accessing directory: {e}")
    except Exception as e:
        logger.error(f"Error scanning directory: {e}")

    return file_data

def get_risk_counts(files):
    """Calculate risk statistics"""
    high = sum(1 for _, _, _, risk in files if risk == 'high')
    medium = sum(1 for _, _, _, risk in files if risk == 'medium')
    low = sum(1 for _, _, _, risk in files if risk == 'low')
    return high, medium, low

@app.route("/")
def home():
    try:
        files = get_files()
        suspicious_count, medium_risk_count, low_risk_count = get_risk_counts(files)
        last_scan = datetime.now().strftime("%H:%M:%S")

        return render_template("index.html",
                             files=files,
                             suspicious_count=suspicious_count,
                             medium_risk_count=medium_risk_count,
                             low_risk_count=low_risk_count,
                             last_scan=last_scan,
                             app_name=APP_NAME,
                             app_version=APP_VERSION)
    except Exception as e:
        logger.error(f"Error rendering home page: {e}")
        return render_template('500.html'), 500

@app.route('/api/files', methods=['GET'])
def api_get_files():
    """REST API endpoint to get file data"""
    try:
        files = get_files()
        suspicious_count, medium_risk_count, low_risk_count = get_risk_counts(files)

        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'data': {
                'files': files,
                'statistics': {
                    'total_files': len(files),
                    'high_risk': suspicious_count,
                    'medium_risk': medium_risk_count,
                    'low_risk': low_risk_count
                }
            }
        })
    except Exception as e:
        logger.error(f"API error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/risk-assessment', methods=['POST'])
def api_risk_assessment():
    """API endpoint for risk assessment of file extensions"""
    try:
        data = request.get_json()
        filename = data.get('filename', '')

        if not filename:
            return jsonify({'error': 'Filename required'}), 400

        risk_level = classify_risk(filename)

        return jsonify({
            'filename': filename,
            'risk_level': risk_level,
            'assessment_time': datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Risk assessment API error: {e}")
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def page_not_found(e):
    logger.warning("404 error occurred")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    logger.error(f"500 error occurred: {e}")
    return render_template('500.html'), 500

@app.context_processor
def inject_globals():
    """Inject global variables into all templates"""
    return {
        'app_name': APP_NAME,
        'app_version': APP_VERSION,
        'current_year': datetime.now().year
    }

if __name__ == "__main__":
    logger.info(f"Starting {APP_NAME} v{APP_VERSION}")
    app.run(
        debug=os.getenv('FLASK_DEBUG', 'True').lower() == 'true',
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000))
    )