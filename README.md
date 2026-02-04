# SMC Road Repair

A Smart Road Reporting web application for SMC (Smart Municipal Corporation) that allows citizens to report road damage using photos, AI analysis, and geolocation.

## Features

- 📷 Photo capture of road damage
- 🤖 AI-powered damage analysis (severity detection)
- 📍 Automatic geolocation capture
- 📝 User description input
- ✅ Report submission to SMC Dashboard

## Lightning.ai Deployment

This project is configured to deploy on [Lightning.ai](https://lightning.ai/).

### Prerequisites

1. Install the Lightning.ai CLI:
   ```bash
   pip install lightning
   ```

2. Login to Lightning.ai:
   ```bash
   lightning login
   ```

### Deploy to Lightning.ai

1. Clone this repository:
   ```bash
   git clone https://github.com/aadityav5/smc-road-repair.git
   cd smc-road-repair
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally (optional):
   ```bash
   lightning run app app.py
   ```

4. Deploy to Lightning.ai cloud:
   ```bash
   lightning run app app.py --cloud
   ```

### Project Structure

```
smc-road-repair/
├── app.py              # Lightning.ai application entry point
├── static/
│   └── index.html      # Main web application
├── requirements.txt    # Python dependencies
├── .lightning          # Lightning.ai configuration
└── README.md           # This file
```

## Local Development

To run the app locally without Lightning.ai:

1. Simply open `static/index.html` in a web browser, or
2. Use a local server:
   ```bash
   cd static
   python -m http.server 8080
   ```
   Then visit `http://localhost:8080`

## License

MIT License