# 🐍 Python Meetup Stack v2 - Quick Start

## 🚀 One-Command Start
```bash
cd python-meetup-stack
docker-compose up -d
```

## 📋 What You Get
| Service | URL | Purpose |
|---------|-----|---------|
| **it-tools** | http://localhost:8080 | Developer utilities |
| **Jellyfin** | http://localhost:8096 | Media server |
| **Pi-hole** | http://localhost:8081/admin | DNS security |
| **Python Dev** | http://localhost:8888 | Jupyter Lab |

## 💾 Resource Requirements
- **RAM:** ~1GB (vs 8GB+ original)
- **Storage:** ~2GB (vs 20GB+ original)
- **Services:** 4 total (vs 16 original)

## 🎯 Perfect for Meetups
- ✅ Fast startup (< 1 minute)
- ✅ Low resource usage
- ✅ Simple port-based URLs
- ✅ Python-focused examples
- ✅ Production-ready patterns

## 🛠️ Management Commands
```bash
docker-compose up -d          # Start all services
docker-compose ps             # Check status
docker-compose logs [service] # View logs
docker-compose down           # Stop all services
```

## 📚 Demo Ideas
1. **Python Basics** - Jupyter Lab interactive coding
2. **Developer Tools** - it-tools utility exploration
3. **Media Processing** - Jellyfin API integration
4. **Network Security** - Pi-hole DNS blocking
5. **Container Concepts** - Docker orchestration

## 🐛 Troubleshooting
- **Port conflicts?** Change ports in docker-compose.yml
- **Services not starting?** Check `docker-compose logs`
- **Permission issues?** Fix volume permissions

Built for encouraging Python developers to embrace containers! 🐳