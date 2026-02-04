"""
SMC Road Repair - Lightning.ai Application

This app serves the SMC Smart Road Reporting web application
using Lightning.ai for cloud deployment and AI capabilities.
"""

import lightning as L
from flask import Flask, send_from_directory
import os

# Allowed file extensions for static files
ALLOWED_EXTENSIONS = {'.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico'}


class SMCRoadRepairServer(L.LightningWork):
    """Lightning Work component to serve the SMC Road Repair web app."""

    def __init__(self, **kwargs):
        super().__init__(parallel=True, **kwargs)
        self.host = "0.0.0.0"
        self.port = 8080

    def run(self):
        """Run the Flask server to serve the static HTML application."""
        static_dir = os.path.join(os.path.dirname(__file__), "static")
        app = Flask(__name__, static_folder=static_dir)

        @app.route("/")
        def index():
            return send_from_directory(static_dir, "index.html")

        @app.route("/<path:path>")
        def static_files(path):
            # Validate file extension for security
            ext = os.path.splitext(path)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                return "Forbidden", 403
            return send_from_directory(static_dir, path)

        app.run(host=self.host, port=self.port, debug=False)


class SMCRoadRepairApp(L.LightningFlow):
    """Main Lightning Flow for the SMC Road Repair application."""

    def __init__(self):
        super().__init__()
        self.server = SMCRoadRepairServer()

    def run(self):
        """Start the web server."""
        self.server.run()

    def configure_layout(self):
        """Configure the app layout for Lightning.ai UI."""
        return [
            {"name": "SMC Road Repair", "content": self.server}
        ]


# Entry point for Lightning.ai
app = L.LightningApp(SMCRoadRepairApp())
