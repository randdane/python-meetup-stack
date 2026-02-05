# Python Meetup Demo Stack v2

A lightweight, simplified collection of Docker applications perfect for demonstrating Python development with containers. Designed specifically for meetup presentations and educational purposes.

## 🚀 Quick Start

```bash
# Clone or download this repository
cd python-meetup-stack

# Start all services
docker-compose up -d

# Or use the setup script
./setup.sh start

# Check service status
docker-compose ps
```

## 📋 Applications Overview

| Application | Technology | Port | URL | Purpose | Python Relevance |
|-------------|------------|------|-----|---------|------------------|
| | **it-tools** | Vue.js + Node.js | 8080 | http://localhost:8080 | Developer utilities | Tool integration examples |
| | **Jellyfin** | .NET Media Server | 8096 | http://localhost:8096 | Media management | Python media processing APIs |
| | **Pi-hole** | DNS + Web Admin | 8081 | http://localhost:8081/admin | Network security | Security concepts |
| | **Python Dev** | Jupyter + FastAPI | 8888 | http://localhost:8888 | Development environment | Main Python workspace |

## 🎯 Demo Scenarios

### 1. Development Environment - Python Dev
**Access:** http://localhost:8888
**Purpose:** Main Python development workspace

**Key Python Concepts:**
- Jupyter Lab for interactive development
- FastAPI for web API creation
- Package management with pip
- Container-based development workflow

**Demo Points:**
- Live coding in Jupyter notebooks
- Creating simple FastAPI endpoints
- Installing and using Python packages
- Container file system exploration

### 2. Developer Tools - it-tools
**Access:** http://localhost:8080
**Purpose:** Developer utility collection

**Python Relevance:**
- Text encoding/decoding tools
- JSON/YAML processing
- Regular expression testing
- Hash generation and verification

**Demo Scenarios:**
- String manipulation examples
- Data format conversions
- Security hash demonstrations
- API testing utilities

### 3. Media Processing - Jellyfin
**Access:** http://localhost:8096
**Default Setup:** No login required for demo

**Python Integration Examples:**
- Media metadata processing with Python
- Plugin development concepts
- API integration patterns
- Content management systems

**Demo Features:**
- Upload and organize media files
- Explore Python media processing libraries
- API endpoint exploration
- Plugin architecture discussion

### 4. Network Security - Pi-hole
**Access:** http://localhost:8081/admin
**Default Login:** admin / pihole123

**Python Security Concepts:**
- DNS resolution and blocking
- Network traffic analysis
- Security automation scripts
- System administration

**Demo Features:**
- DNS query visualization
- Ad-blocking functionality
- Network statistics
- Security rule management

## 🛠️ Installation Requirements

### System Requirements
- **RAM:** 2GB+ recommended (vs 8GB+ previously)
- **Storage:** 5GB+ free space (vs 20GB+ previously)
- **Docker:** 20.10+ with Docker Compose
- **OS:** Linux, macOS, or Windows with WSL2

### Prerequisites
```bash
# Install Docker (if not already installed)
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose (if needed)
pip install docker-compose
```

## 📊 Resource Usage

| Service | RAM Usage | CPU | Storage |
|--------|-----------|-----|---------|
| | it-tools | ~100MB | Low | ~200MB |
| | Jellyfin | ~500MB | Medium | ~1GB |
| | Pi-hole | ~200MB | Low | ~500MB |
| | Python Dev | ~300MB | Low | ~500MB |

**Total:** ~1.1GB RAM, ~2.2GB Storage

## 🎓 Learning Paths

### For Python Beginners
1. Start with **Python Dev** container (Jupyter Lab)
2. Explore basic concepts and syntax
3. Use **it-tools** for data manipulation examples
4. Learn container concepts

### For Intermediate Developers
1. Study **Jellyfin** API integration
2. Explore **Pi-hole** security automation
3. Practice **Python Dev** advanced features
4. Build container orchestration skills

### For Advanced Users
1. Analyze service communication
2. Study network security patterns
3. Explore performance optimization
4. Practice DevOps workflows

## 🔧 Customization Guide

### Environment Variables
Edit the `docker-compose.yml` to customize:

```yaml
# Change Pi-hole password
WEBPASSWORD: your-secure-password

# Adjust timezone
TZ: Your/Timezone

# Modify Jellyfin settings
JELLYFIN_PublishedServerUrl: http://your-domain:8096
```

### Port Configuration
All services use distinct ports to avoid conflicts:
- **8080:** it-tools (developer utilities)
- **8081:** Pi-hole (DNS admin)
- **8096:** Jellyfin (media server)
- **8888:** Python Dev (Jupyter Lab)

### Selective Startup
Start only specific services:

```bash
# Start only development environment
docker-compose up python-dev

# Start only media stack
docker-compose up jellyfin

# Start minimal stack
docker-compose up python-dev it-tools
```

## 🐛 Troubleshooting

### Common Issues

**Port Conflicts:**
```bash
# Check what's using ports
netstat -tulpn | grep :8080
sudo lsof -i :8080
```

**Service Won't Start:**
```bash
# Check logs
docker-compose logs [service-name]

# Restart specific service
docker-compose restart [service-name]
```

**Permission Issues:**
```bash
# Fix volume permissions
sudo chown -R 1000:1000 ./python-examples
```

### Performance Tips

1. **Use SSD storage** for better performance
2. **Allocate sufficient RAM** (2GB+ recommended)
3. **Start services gradually** for better resource management
4. **Regular cleanup** of unused Docker images:
   ```bash
   docker system prune -a
   ```

## 📚 Additional Resources

### Documentation Links
- [Jellyfin Documentation](https://jellyfin.org/docs/)
- [it-tools Repository](https://github.com/CorentinTh/it-tools)
- [Pi-hole Documentation](https://docs.pi-hole.net/)
- [Jupyter Lab Documentation](https://jupyterlab.readthedocs.io/)

### Python Learning Resources
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker for Python Developers](https://docker.com/languages/python)
- [Real Python](https://realpython.com/)

## 🎯 Presentation Tips

### Demo Sequence (20-30 minutes)
1. **Introduction** (3 min): Overview of simplified stack
2. **Python Basics** (5 min): Jupyter Lab interactive demo
3. **Developer Tools** (5 min): it-tools exploration
4. **Media Processing** (5 min): Jellyfin API discussion
5. **Security Concepts** (5 min): Pi-hole DNS demo
6. **Q&A** (5-7 min)

### Key Talking Points
- **Lightweight containers** for development
- **Direct port access** for simplicity
- **Service communication** patterns
- **Network security** fundamentals
- **Python integration** possibilities

### Engagement Ideas
- Live coding in Jupyter Lab notebooks
- Interactive tool exploration with it-tools
- Real-time DNS blocking demonstration
- Container architecture discussion

## 🤝 Contributing

This stack is designed for educational purposes. Feel free to:
- Add new Python-friendly services
- Improve documentation and examples
- Share additional demo scripts
- Report issues or suggestions

## 📄 License

This project is provided for educational purposes. Individual applications maintain their respective licenses.

---

**Happy containerizing! 🐍🐳**

Built with ❤️ for the Python community. Perfect for meetups, workshops, and hands-on learning.