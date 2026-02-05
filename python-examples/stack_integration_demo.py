"""
FastAPI Demo for Python Meetup Stack v2
Integrates with the simplified container stack
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import json
from datetime import datetime
import uvicorn

app = FastAPI(title="Python Meetup Stack API", version="2.0")

# Service URLs (through Caddy reverse proxy)
SERVICES = {
    "it_tools": "http://localhost",
    "jellyfin": "http://media.localhost",
    "pihole": "http://dns.localhost",
    "caddy_health": "http://health.localhost",
}


@app.get("/", response_class=HTMLResponse)
async def root():
    """Main dashboard showing stack status"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Meetup Stack v2</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #333; text-align: center; }
            .services { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 30px; }
            .service { padding: 20px; border: 1px solid #ddd; border-radius: 8px; background: #fafafa; }
            .service h3 { color: #007bff; margin-top: 0; }
            .service a { color: #007bff; text-decoration: none; }
            .service a:hover { text-decoration: underline; }
            .status { padding: 5px 10px; border-radius: 5px; font-size: 12px; font-weight: bold; }
            .status.up { background: #d4edda; color: #155724; }
            .status.down { background: #f8d7da; color: #721c24; }
            .python-section { margin-top: 40px; padding: 20px; background: #e8f5e8; border-radius: 8px; }
            .code { background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: monospace; margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐍 Python Meetup Stack v2</h1>
            <p>Lightweight container stack for Python development demonstrations</p>
            
            <div class="services">
    """

    # Check service status
    for name, url in SERVICES.items():
        try:
            response = requests.get(url, timeout=5)
            status = "UP" if response.status_code < 400 else "DOWN"
            status_class = "up" if response.status_code < 400 else "down"
        except:
            status = "DOWN"
            status_class = "down"

        if name == "it_tools":
            html += f"""
            <div class="service">
                <h3>🛠️ it-tools</h3>
                <p>Developer utilities and tools</p>
                <p><span class="status {status_class}">{status}</span></p>
                <a href="{url}" target="_blank">Open it-tools</a>
            </div>
            """
        elif name == "jellyfin":
            html += f"""
            <div class="service">
                <h3>🎬 Jellyfin</h3>
                <p>Media server with Python API support</p>
                <p><span class="status {status_class}">{status}</span></p>
                <a href="{url}" target="_blank">Open Jellyfin</a>
            </div>
            """
        elif name == "pihole":
            html += f"""
            <div class="service">
                <h3>🛡️ Pi-hole</h3>
                <p>DNS ad-blocker and network security</p>
                <p><span class="status {status_class}">{status}</span></p>
                <a href="{url}/admin" target="_blank">Open Pi-hole Admin</a>
            </div>
            """
        elif name == "caddy_health":
            html += f"""
            <div class="service">
                <h3>🌐 Caddy</h3>
                <p>Reverse proxy handling all routing</p>
                <p><span class="status {status_class}">{status}</span></p>
                <a href="{url}" target="_blank">Health Check</a>
            </div>
            """

    html += """
            </div>
            
            <div class="python-section">
                <h2>🐍 Python Integration Examples</h2>
                <p>Try these API endpoints:</p>
                <div class="code">
                    GET /api/services - Service status<br>
                    GET /api/time - Current server time<br>
                    GET /api/containers - Container information<br>
                    POST /api/echo - Echo back your data
                </div>
                <p><a href="/docs" target="_blank">📚 View API Documentation</a></p>
            </div>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html)


@app.get("/api/services")
async def get_services():
    """Get status of all services"""
    status = {}
    for name, url in SERVICES.items():
        try:
            response = requests.get(url, timeout=5)
            status[name] = {
                "url": url,
                "status_code": response.status_code,
                "status": "up" if response.status_code < 400 else "down",
            }
        except Exception as e:
            status[name] = {"url": url, "error": str(e), "status": "down"}
    return {"services": status, "timestamp": datetime.now().isoformat()}


@app.get("/api/time")
async def get_time():
    """Get current server time"""
    return {
        "current_time": datetime.now().isoformat(),
        "timezone": "UTC",
        "python_version": "3.12+",
        "fastapi_version": "0.104+",
    }


@app.get("/api/containers")
async def get_containers():
    """Get information about running containers"""
    # This is a demo - in real implementation you'd use Docker SDK
    containers = [
        {"name": "python-dev", "image": "python:3.12-slim", "status": "running"},
        {"name": "caddy", "image": "caddy:2-alpine", "status": "running"},
        {
            "name": "it-tools",
            "image": "corentinth/it-tools:latest",
            "status": "running",
        },
        {"name": "jellyfin", "image": "jellyfin/jellyfin:latest", "status": "running"},
        {"name": "pihole", "image": "pihole/pihole:latest", "status": "running"},
    ]
    return {"containers": containers, "total": len(containers)}


@app.post("/api/echo")
async def echo_data(request: Request):
    """Echo back the received data"""
    data = await request.json()
    return {
        "received": data,
        "timestamp": datetime.now().isoformat(),
        "message": "Python FastAPI received your data!",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
