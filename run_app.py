"""
STAQA Mini-Project: Application Launcher
Starts the local Flask web application server for manual exploration or automated testing.
"""

import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"[*] Starting STAQA Flask Application on http://127.0.0.1:{port}")
    print(f"[*] Project Dashboard available at: http://127.0.0.1:{port}/")
    print(f"[*] Press CTRL+C to terminate the server.")
    app.run(host="127.0.0.1", port=port, debug=False)
