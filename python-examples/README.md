# Python Demo Scripts for Meetup Stack v2

This directory contains example Python scripts that demonstrate integration with the simplified Docker applications in the meetup stack.

## 📁 Scripts Overview

### 🌐 Web API Examples
- `stack_integration_demo.py` - FastAPI dashboard for the entire stack
- `fastapi_demo.py` - Basic FastAPI server example
- `api_client.py` - HTTP client for service communication

### 📊 Data Processing Examples
- `media_processor.py` - Media file processing for Jellyfin integration
- `text_analyzer.py` - Text processing utilities
- `data_visualizer.py` - Data visualization with matplotlib

### 🔧 Utility Examples
- `service_checker.py` - Health check script for all services
- `dns_tools.py` - DNS manipulation examples (Pi-hole related)
- `file_tools.py` - File system utilities

### 🛠️ Integration Examples
- `caddy_api.py` - Examples of working with Caddy
- `container_tools.py` - Docker container management
- `network_tools.py` - Network analysis utilities

## 🚀 Getting Started

1. Start the Python development container:
```bash
docker-compose up python-dev caddy
```

2. Access Jupyter Lab at http://dev.localhost

3. Run the stack integration demo:
```bash
docker exec -it python-dev python /workspace/examples/stack_integration_demo.py
```

4. View the dashboard at http://dev.localhost:8000

## 🔗 Integration Points

### With Caddy (Reverse Proxy)
- Service discovery and routing
- URL manipulation examples
- WebSocket communication
- Health check endpoints

### With it-tools
- Text encoding/decoding
- JSON/YAML processing
- Hash generation utilities
- Regular expression testing

### With Jellyfin
- Media metadata processing
- API integration patterns
- Plugin development concepts
- Content management

### With Pi-hole
- DNS query analysis
- Security automation
- Network monitoring
- System administration

## 💡 Demo Ideas

1. **Live Coding**: Edit scripts in Jupyter Lab during presentation
2. **Service Dashboard**: Show the FastAPI dashboard with real-time status
3. **API Integration**: Demonstrate service communication
4. **Container Management**: Show Python controlling Docker containers

## 🎯 Presentation Flow

1. **Start Simple**: Basic Python in Jupyter Lab
2. **Add Services**: Show service integration examples
3. **Build Dashboard**: Demonstrate the FastAPI dashboard
4. **Real Integration**: Live service communication demo

## 📚 Learning Resources

Each script contains detailed comments explaining:
- Container-based development
- Service communication patterns
- API design principles
- Modern Python practices

## 🔧 Environment Setup

The Python dev container comes with:
- Python 3.12
- FastAPI & Uvicorn
- Requests & HTTP libraries
- Pandas & Matplotlib
- Jupyter Lab
- Docker SDK (if needed)