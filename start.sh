#!/bin/bash

echo "🎯 Prompt Mühendisliği Uygulaması Başlatılıyor..."
echo "==========================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 bulunamadı. Lütfen Python 3.8+ yükleyin."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js bulunamadı. Lütfen Node.js 16+ yükleyin."
    exit 1
fi

# Install backend dependencies
echo "📦 Backend bağımlılıkları yükleniyor..."
cd backend
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Python virtual environment oluşturuldu"
fi

source venv/bin/activate || . venv/Scripts/activate
pip install -r requirements.txt
echo "✅ Backend bağımlılıkları yüklendi"

# Go back to root directory
cd ..

# Install frontend dependencies (if not installed)
if [ ! -d "frontend/node_modules" ]; then
    echo "📦 Frontend bağımlılıkları yükleniyor..."
    cd frontend
    npm install
    echo "✅ Frontend bağımlılıkları yüklendi"
    cd ..
fi

# Install root dependencies (if not installed)
if [ ! -d "node_modules" ]; then
    echo "📦 Ana proje bağımlılıkları yükleniyor..."
    npm install
    echo "✅ Ana proje bağımlılıkları yüklendi"
fi

echo ""
echo "🚀 Uygulama başlatılıyor..."
echo ""
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:3000"
echo ""
echo "Durdurmak için Ctrl+C tuşlarına basın"
echo ""

# Start the application
npm run dev