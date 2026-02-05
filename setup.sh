#!/bin/bash

# Python Meetup Stack Setup Script
# This script helps set up and manage the Python meetup demo stack

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}[SETUP]${NC} $1"
}

# Check if Docker is installed
check_docker() {
    print_header "Checking Docker installation..."
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        echo "Visit: https://docs.docker.com/get-docker/"
        exit 1
    fi
    
    print_status "Docker is installed ✓"
}

# Check system resources
check_resources() {
    print_header "Checking system resources..."
    
    # Check available memory (Linux/Mac)
    if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
        TOTAL_MEM=$(free -m | awk '/^Mem:/{print $2}' 2>/dev/null || echo "Unknown")
        if [[ "$OSTYPE" == "darwin"* ]]; then
            TOTAL_MEM=$(sysctl -n hw.memsize | awk '{print $1/1024/1024}')
        fi
        
        if [[ "$TOTAL_MEM" != "Unknown" ]] && [[ $(echo "$TOTAL_MEM < 8000" | bc -l 2>/dev/null || echo "0") == "1" ]]; then
            print_warning "System has less than 8GB RAM. Some services may be slow."
        else
            print_status "System has sufficient RAM (${TOTAL_MEM}MB) ✓"
        fi
    fi
    
    # Check available disk space
    if command -v df &> /dev/null; then
        AVAILABLE_SPACE=$(df -BG . | awk 'NR==2 {print $4}' | sed 's/G//')
        if [[ $AVAILABLE_SPACE -lt 20 ]]; then
            print_warning "Less than 20GB disk space available. Consider freeing up space."
        else
            print_status "Sufficient disk space available (${AVAILABLE_SPACE}GB) ✓"
        fi
    fi
}

# Create necessary directories
create_directories() {
    print_header "Creating necessary directories..."
    
    mkdir -p python-examples
    mkdir -p logs
    mkdir -p data/{jellyfin,it-tools,pihole}
    
    print_status "Directories created ✓"
}

# Download example files if they don't exist
setup_examples() {
    print_header "Setting up example files..."
    
    # Create requirements.txt for Python dev container
    cat > python-examples/requirements.txt << EOF
fastapi
uvicorn
requests
pandas
matplotlib
seaborn
jupyter
beautifulsoup4
pydantic
python-multipart
aiofiles
prometheus-client
psutil
EOF

    # Create environment file
    cat > .env << EOF
# Python Meetup Stack v2 Environment Variables

# Pi-hole
WEBPASSWORD=pihole123
PIHOLE_DNS_=1.1.1.1;8.8.8.8

# Timezone
TZ=America/New_York

# Jellyfin
JELLYFIN_PublishedServerUrl=http://localhost:8096
EOF

    print_status "Example files created ✓"
}

# Quick start services
start_services() {
    print_header "Starting Python meetup stack v2..."
    
    # Start all services
    print_status "Starting all services..."
    docker-compose up -d
    
    # Wait for services to be ready
    sleep 10
    
    print_status "All services started! ✓"
}

# Show service URLs
show_urls() {
    print_header "Service URLs:"
    
    echo ""
    echo "🛠️  Developer Tools:"
    echo "   it-tools: http://localhost:8080"
    echo ""
    echo "🐍 Python Development:"
    echo "   Jupyter Lab: http://localhost:8888"
    echo ""
    echo "🎬 Media Server:"
    echo "   Jellyfin: http://localhost:8096"
    echo ""
    echo "🛡️  DNS & Security:"
    echo "   Pi-hole Admin: http://localhost:8081/admin"
    echo "   Login: admin / pihole123"
    echo ""
}

# Check service health
check_health() {
    print_header "Checking service health..."
    
    # Check services directly
    services=("8080:it-tools" "8888:python-dev" "8096:jellyfin" "8081:pihole")
    
    for service in "${services[@]}"; do
        port=$(echo $service | cut -d':' -f1)
        service_name=$(echo $service | cut -d':' -f2)
        
        if curl -s -o /dev/null -w "%{http_code}" "http://localhost:$port" | grep -q "200\|302"; then
            print_status "$service_name is healthy ✓"
        else
            print_warning "$service_name may still be starting..."
        fi
    done
}

# Stop all services
stop_services() {
    print_header "Stopping all services..."
    docker compose down
    print_status "All services stopped ✓"
}

# Cleanup
cleanup() {
    print_header "Cleaning up..."
    
    read -p "This will remove all containers, networks, and volumes. Continue? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        docker compose down -v --remove-orphans
        docker system prune -f
        print_status "Cleanup completed ✓"
    else
        print_status "Cleanup cancelled."
    fi
}

# Show logs
show_logs() {
    print_header "Showing logs (Ctrl+C to exit)..."
    docker compose logs -f
}

# Main menu
show_menu() {
    echo ""
    echo "🐍 Python Meetup Stack Management Menu"
    echo "======================================"
    echo "1. Start all services"
    echo "2. Stop all services"
    echo "3. Check service health"
    echo "4. Show service URLs"
    echo "5. Show logs"
    echo "6. Full setup (first time)"
    echo "7. Cleanup everything"
    echo "8. Exit"
    echo ""
}

# Full setup for first time users
full_setup() {
    print_header "Running full setup..."
    check_docker
    check_resources
    create_directories
    setup_examples
    start_services
    sleep 15
    check_health
    show_urls
    
    echo ""
    print_status "Setup complete! 🎉"
    print_status "Save this script for future management of your stack."
}

# Main execution
main() {
    if [[ "$1" == "setup" ]]; then
        full_setup
        exit 0
    elif [[ "$1" == "start" ]]; then
        start_services
        show_urls
        exit 0
    elif [[ "$1" == "stop" ]]; then
        stop_services
        exit 0
    elif [[ "$1" == "health" ]]; then
        check_health
        exit 0
    elif [[ "$1" == "logs" ]]; then
        show_logs
        exit 0
    elif [[ "$1" == "cleanup" ]]; then
        cleanup
        exit 0
    fi
    
    # Interactive menu
    while true; do
        show_menu
        read -p "Choose an option (1-8): " choice
        case $choice in
            1) start_services; show_urls ;;
            2) stop_services ;;
            3) check_health ;;
            4) show_urls ;;
            5) show_logs ;;
            6) full_setup ;;
            7) cleanup ;;
            8) echo "Goodbye! 👋"; exit 0 ;;
            *) print_error "Invalid option. Please choose 1-8." ;;
        esac
        echo ""
        read -p "Press Enter to continue..."
    done
}

# Run main function with all arguments
main "$@"
