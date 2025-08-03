# 🎯 Prompt Mühendisliği Uygulaması

Modern, full-stack prompt engineering web uygulaması. AI modelleriniz için optimize edilmiş promptlar oluşturun, analiz edin ve yönetin.

## ✨ Özellikler

- **🤖 Çoklu AI Model Desteği**: Claude 4, GPT-4.1, GPT-4o, Gemini 2.5 Pro, DeepSeek R1 ve daha fazlası
- **⚡ Gelişmiş Teknikler**: Chain of Thought, Tree of Thought, Meta-prompting, Role-based prompts
- **📊 Gerçek Zamanlı Analitik**: Performans metrikleri, kullanım istatistikleri ve optimizasyon raporları
- **📚 Prompt Kütüphanesi**: Hazır şablonlar ve geçmiş promptlarınızın yönetimi
- **🎨 Modern UI/UX**: React 18 ve Tailwind CSS ile responsive tasarım
- **🔍 Akıllı Analiz**: Otomatik görev analizi ve teknik önerisi
- **💾 Veritabanı Entegrasyonu**: SQLAlchemy ile güçlü veri yönetimi

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Node.js (16.x veya üzeri)
- Python 3.8+
- npm veya yarn

### Kurulum

1. **Projeyi klonlayın**
   ```bash
   git clone <repository-url>
   cd ANALİZ
   ```

2. **Backend bağımlılıklarını yükleyin**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Frontend bağımlılıklarını yükleyin**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Ana dizindeki bağımlılıkları yükleyin**
   ```bash
   cd ..
   npm install
   ```

### Çalıştırma

#### Geliştirme Ortamı (Tam Stack)
```bash
npm run dev
```
Bu komut hem backend (Flask) hem de frontend (React) sunucularını eş zamanlı olarak başlatır.

#### Ayrı Ayrı Çalıştırma

**Backend:**
```bash
cd backend
python app.py
```
Backend http://localhost:5000 adresinde çalışacak.

**Frontend:**
```bash
cd frontend
npm start
```
Frontend http://localhost:3000 adresinde çalışacak.

## 📋 API Endpoints

### Temel Endpoints
- `GET /api/health` - Sistem durumu kontrolü
- `POST /api/analyze-task` - Görev analizi
- `POST /api/generate-prompt` - Prompt oluşturma
- `POST /api/optimize-prompt` - Prompt optimizasyonu

### Veri Endpoints
- `GET /api/templates` - Mevcut şablonlar
- `GET /api/techniques` - Kullanılabilir teknikler
- `GET /api/statistics` - Kullanım istatistikleri
- `GET /api/prompts` - Prompt geçmişi (sayfalama ile)
- `GET /api/prompts/{id}` - Belirli prompt detayları

## 🏗️ Proje Yapısı

```
ANALİZ/
├── backend/                 # Flask API Backend
│   ├── app.py              # Ana Flask uygulaması
│   ├── requirements.txt    # Python bağımlılıkları
│   └── prompt_engineering.db # SQLite veritabanı
├── frontend/               # React Frontend
│   ├── src/
│   │   ├── components/     # React bileşenleri
│   │   ├── services/       # API servis katmanı
│   │   └── App.js         # Ana React uygulaması
│   ├── public/
│   └── package.json
├── prompt_assistant.py     # Orijinal prompt asistan sınıfı
├── prompt_assistant_gui.py # Tkinter GUI (legacy)
├── package.json           # Ana proje bağımlılıkları
└── README.md
```

## 🎯 Kullanım Kılavuzu

### 1. Dashboard
- Sistem durumunu ve genel istatistikleri görüntüleyin
- Hızlı erişim aksiyonlarını kullanın
- Son aktiviteleri takip edin

### 2. Prompt Oluşturucu
- Görevinizi detaylı olarak tanımlayın
- AI modelinizi seçin (Claude 4, GPT-4.1, vb.)
- Uygun tekniği seçin veya otomatik analiz kullanın
- Gelişmiş parametreleri ayarlayın
- Optimize edilmiş prompt oluşturun

### 3. Analitik
- Performans metriklerinizi inceleyin
- Teknik kullanım dağılımını görüntüleyin
- Optimizasyon önerilerini değerlendirin

### 4. Geçmiş
- Oluşturduğunuz promptları görüntüleyin
- Arama ve filtreleme yapın
- Prompt detaylarını inceleyin

### 5. Şablonlar
- Hazır prompt şablonlarını keşfedin
- Kategorilere göre filtreleyin
- Şablonları kullanın veya kopyalayın

## 🔧 Yapılandırma

### Ortam Değişkenleri

**Backend (.env)**
```env
FLASK_APP=backend/app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///prompt_engineering.db
```

**Frontend (frontend/.env)**
```env
REACT_APP_API_URL=http://localhost:5000/api
GENERATE_SOURCEMAP=false
```

## 🧪 Test Etme

### Backend Testleri
```bash
cd backend
python -m pytest
```

### Frontend Testleri
```bash
cd frontend
npm test
```

### Tüm Testler
```bash
npm run test
```

## 📊 Desteklenen AI Modeller

| Model | Context | Features | Cost |
|-------|---------|----------|------|
| Claude 4 Opus/Sonnet | 200K token | XML tags, Ethical AI, Thinking mode | $15/$75 |
| GPT-4.1 | 1.05M token | Function calling, Diff output | $3.50/M token |
| GPT-4o | 128K token | Real-time multimodal | Variable |
| Gemini 2.5 Pro | 1.05M token | Scientific reasoning | $3.44/M token |
| DeepSeek R1 | 164K token | Open source, Transparent reasoning | $0.55/$2.19/M |

## 🎭 Prompt Teknikleri

- **Zero-shot**: Doğrudan talimat
- **Few-shot**: Örneklerle öğrenme
- **Chain of Thought**: Adım adım düşünce
- **Tree of Thought**: Çoklu yaklaşım değerlendirmesi
- **Meta-prompting**: Kendini optimize eden promptlar
- **Role-based**: Uzman rolü atama
- **TAG Framework**: Task-Action-Goal
- **BAB Framework**: Before-After-Bridge

## 🛠️ Geliştirme

### Yeni Özellik Ekleme
1. Backend API endpoint'i oluşturun
2. Frontend servis fonksiyonu ekleyin
3. UI bileşenini geliştirin
4. Test yazın

### Veritabanı Değişiklikleri
1. Model sınıfını güncelleyin
2. Migration scriptini çalıştırın
3. API endpoint'lerini güncelleyin

## 🚀 Dağıtım

### Production Build
```bash
npm run build
```

### Docker ile Dağıtım
```bash
# Dockerfile oluşturun ve:
docker build -t prompt-engineering-app .
docker run -p 3000:3000 -p 5000:5000 prompt-engineering-app
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🆘 Destek

Herhangi bir sorun yaşıyorsanız:

1. **Backend Bağlantı Sorunları**: Backend sunucusunun çalıştığından emin olun
2. **CORS Hataları**: Proxy ayarlarını kontrol edin
3. **Veritabanı Sorunları**: SQLite dosya izinlerini kontrol edin
4. **Frontend Hataları**: Browser console'u kontrol edin

## 🔮 Gelecek Planları

- [ ] Real-time prompt collaboration
- [ ] Advanced analytics with charts
- [ ] Template marketplace
- [ ] API rate limiting
- [ ] User authentication
- [ ] Prompt versioning
- [ ] Export/Import functionality
- [ ] Mobile app