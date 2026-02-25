# Employee Cyber Risk Monitoring & Awareness Platform

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/your-repo/employee-cyber-risk)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.3.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Overview

A professional Security Operations Center (SOC) simulation dashboard designed to monitor and analyze file system activity for potential cyber security threats. This platform helps organizations detect unauthorized file modifications, suspicious file types, and insider threats in real-time.

## 🎯 Key Features

- **Real-time File Monitoring**: Continuous scanning of specified directories
- **Risk Classification**: Intelligent file risk assessment based on extensions and patterns
- **Professional Dashboard**: Modern, responsive web interface with statistics
- **Comprehensive Logging**: Detailed audit trails and error handling
- **Configurable Settings**: Environment-based configuration management
- **Error Handling**: Graceful error pages and exception management

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/employee-cyber-risk.git
   cd employee-cyber-risk
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## 🚀 Quick Demo

Experience the full functionality with sample data:

```bash
# Create demo files
python demo.py

# Run the application
python app.py

# Open in browser: http://localhost:5000
```

The demo creates files across all risk levels to showcase the classification system.

## 📊 Risk Classification

The system automatically classifies files based on their extensions:

### 🔴 High Risk
- Executables: `.exe`, `.bat`, `.cmd`, `.scr`, `.pif`, `.com`
- Scripts: `.vbs`, `.js`
- Libraries: `.jar`, `.dll`

### 🟡 Medium Risk
- Archives: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- Documents: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`

### 🟢 Low Risk
- Media: `.jpg`, `.png`, `.gif`, `.mp4`, `.mp3`
- Code: `.py`, `.html`, `.css`, `.md`
- Text: `.txt`

## 🏗️ Architecture

```
employee-cyber-risk/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment configuration
├── README.md             # This file
├── cyber_monitor.log     # Application logs
├── static/
│   └── style.css         # Professional styling
└── templates/
    ├── index.html        # Main dashboard
    ├── 404.html          # Error pages
    └── 500.html
```

## ⚙️ Configuration

Configure the application using environment variables in `.env`:

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
WATCH_FOLDER=.
APP_NAME=Employee Cyber Risk Monitor
APP_VERSION=2.0.0
SESSION_TIMEOUT=3600
MAX_FILE_SIZE_MB=100
```

## 🔧 API Endpoints

- `GET /` - Main dashboard with file monitoring data

## 📈 Monitoring & Logging

The application provides comprehensive logging:
- File system scan events
- Risk classification results
- Error conditions and exceptions
- Access patterns

Logs are written to `cyber_monitor.log` and console output.

## 🛡️ Security Features

- Input validation and sanitization
- Secure configuration management
- Error handling without information disclosure
- File permission checks
- Environment-based secret management

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Install test dependencies
pip install pytest

# Run all tests
python -m pytest tests.py -v

# Run with coverage
python -m pytest tests.py --cov=. --cov-report=html
```

## 🐳 Docker Deployment

### Build and run with Docker:

```bash
# Build the image
docker build -t cyber-risk-monitor .

# Run the container
docker run -p 5000:5000 cyber-risk-monitor
```

### Or use Docker Compose:

```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

For support, email support@company.com or create an issue in this repository.

## 🚀 Future Enhancements

- [ ] Database integration for historical data
- [ ] Real-time notifications and alerts
- [ ] User authentication and role-based access
- [ ] Advanced threat detection algorithms
- [ ] API endpoints for external integrations
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

---

**Built with ❤️ for cybersecurity professionals**