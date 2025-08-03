# 🤖 Gelişmiş Prompt Mühendisliği Asistanı

Türkçe prompt mühendisliği dokümantasyonuna dayalı olarak geliştirilmiş, gelişmiş meta-prompting yetenekleri ile donatılmış bir prompt asistanı.

## ✨ Özellikler

### 🎯 Çoklu Prompt Teknikleri
- **Zero-Shot Prompting**: Doğrudan talimat verme
- **Few-Shot Prompting**: Örneklerle öğrenme
- **Chain-of-Thought (CoT)**: Adım adım düşünce süreci
- **Tree-of-Thought (ToT)**: Çok yollu keşif
- **Self-Ask**: Kendi kendine sorgulama
- **Role-Based Prompting**: Uzman rolü atama
- **Meta-Prompting**: Kendini optimize eden promptlar

### 🏗️ Yapılandırılmış Çerçeveler
- **TAG Framework**: Görev-Aksiyon-Hedef
- **BAB Framework**: Önce-Sonra-Köprü narratif
- **RAG Entegrasyonu**: Bilgi kaynaklarıyla zenginleştirme
- **Progressive Enhancement**: İteratif geliştirme

### 🔍 Otomatik Analiz ve Optimizasyon
- Görev tipi tespiti (yaratıcı, teknik, analitik, mantıksal)
- Karmaşıklık seviyesi değerlendirmesi
- En uygun teknik önerisi
- Performans metrikleri takibi
- İteratif optimizasyon

### 📊 Performans Takibi
- Netlik skoru
- Etkinlik değerlendirmesi
- Optimizasyon seviyesi
- Kullanım istatistikleri
- Detaylı raporlama

## 🚀 Kurulum ve Kullanım

### Gereksinimler
```bash
Python 3.8+
tkinter (GUI için)
```

### Hızlı Başlangıç

#### 1. Komut Satırı Kullanımı
```python
from prompt_assistant import PromptAssistant

# Asistanı başlat
assistant = PromptAssistant()

# Görev analizi
task = "Bir e-ticaret sitesi için güvenlik açıklarını tespit eden bir araç tasarla"
analysis = assistant.analyze_task(task)
print(f"Önerilen teknik: {analysis['recommended_technique'].value}")

# Prompt oluştur
prompt, metrics = assistant.generate_prompt(
    task=task,
    context="E-ticaret güvenliği",
    expert_role="Siber Güvenlik Uzmanı",
    experience="10"
)

print(f"Oluşturulan prompt:\n{prompt}")
print(f"Etkinlik skoru: {metrics.effectiveness_score:.2f}")
```

#### 2. GUI Kullanımı
```bash
python prompt_assistant_gui.py
```

## 🎭 Prompt Şablonları

### Meta-Prompt Şablonu
Kendini optimize eden, evrensel meta-prompt:
```
Sen bir uzman prompt mühendisissin. Verilen görevi analiz et ve en etkili promotu oluştur.
GÖREV: {task}
HEDEF KİTLE: {audience}
BAĞLAM: {context}
...
```

### TAG Framework Şablonu
Yapılandırılmış görev çerçevesi:
```
GÖREV (Task): {task}
AKSİYON (Action): {action}
HEDEF (Goal): {goal}
...
```

### BAB Framework Şablonu
Narratif problem çözme:
```
ÖNCE (Before): {current_state}
SONRA (After): {desired_state}
KÖPRÜ (Bridge): {solution_path}
...
```

## 📈 Performans Metrikleri

### Netlik Skoru
- Prompt'un anlaşılabilirlik düzeyi
- 0.0 - 1.0 arası değer
- Kelime sayısı ve yapı analizi

### Etkinlik Skoru
- Template kalitesi ve zorluk seviyesi
- Teknik seçimi uygunluğu
- Geçmiş başarı oranları

### Optimizasyon Seviyesi
- Doldurulmuş parametr sayısı
- Template değişkenlerinin kullanımı
- Kişiselleştirme derecesi

## 🔧 Gelişmiş Kullanım

### Özel Template Ekleme
```python
from prompt_assistant import PromptTemplate, PromptTechnique, TaskType, DifficultyLevel

custom_template = PromptTemplate(
    name="Özel Şablon",
    technique=PromptTechnique.ZERO_SHOT,
    template="Sen bir {role} uzmanısın. {task} görevini tamamla.",
    variables=["role", "task"],
    task_types=[TaskType.TECHNICAL],
    difficulty=DifficultyLevel.INTERMEDIATE,
    description="Özel kullanım şablonu",
    example="Yazılım geliştirme görevleri"
)

assistant.templates["custom"] = custom_template
```

### Batch İşleme
```python
tasks = [
    "Veri analizi raporu hazırla",
    "API dokümantasyonu oluştur",
    "Test senaryoları yaz"
]

results = []
for task in tasks:
    prompt, metrics = assistant.generate_prompt(task)
    results.append((task, prompt, metrics))
```

### Optimizasyon Döngüsü
```python
# İlk prompt
initial_prompt, metrics = assistant.generate_prompt(task)

# Geri bildirim ile optimizasyon
feedback = "Daha spesifik örnekler gerekli"
optimized_prompt = assistant.optimize_prompt(initial_prompt, feedback)

# Performans karşılaştırması
report = assistant.export_optimization_report()
```

## 📊 GUI Özellikleri

### Ana Paneller
1. **Görev Girişi**: Task tanımlama ve parametre ayarları
2. **Çıkış ve Analiz**: Oluşturulan prompt ve analiz sonuçları
3. **Performans İstatistikleri**: Metrik görselleştirme ve raporlama

### Özellikler
- ✅ Gerçek zamanlı görev analizi
- ✅ Otomatik teknik önerisi
- ✅ Interaktif parametre ayarları
- ✅ Prompt kopyalama ve dışa aktarma
- ✅ Performans grafikleri
- ✅ Optimizasyon dialogları
- ✅ Şablon gezgini

## 🎯 Kullanım Senaryoları

### 1. İçerik Üretimi
```python
# Blog yazısı için prompt
prompt, _ = assistant.generate_prompt(
    task="SEO uyumlu bir teknoloji blog yazısı yaz",
    context="Yapay zeka ve gelecek",
    audience="Teknoloji meraklıları",
    expert_role="İçerik Pazarlama Uzmanı"
)
```

### 2. Kod Geliştirme
```python
# Yazılım geliştirme için prompt
prompt, _ = assistant.generate_prompt(
    task="Python ile RESTful API geliştir",
    context="E-ticaret sistemi",
    expert_role="Backend Developer",
    experience="8",
    technique=PromptTechnique.CHAIN_OF_THOUGHT
)
```

### 3. Eğitim ve Öğretim
```python
# Eğitim materyali için prompt
prompt, _ = assistant.generate_prompt(
    task="Makine öğrenmesi kavramlarını açıkla",
    audience="Üniversite öğrencileri",
    expert_role="Akademisyen",
    output_format="İnteraktif sunum"
)
```

### 4. İş Analizi
```python
# İş süreç optimizasyonu
prompt, _ = assistant.generate_prompt(
    task="Müşteri hizmetleri süreçlerini iyileştir",
    technique=PromptTechnique.BAB_FRAMEWORK,
    current_state="Uzun yanıt süreleri",
    desired_state="30 saniyede yanıt",
    expert_role="İş Analisti"
)
```

## 📚 Teknik Detaylar

### Sınıf Yapısı
- `PromptAssistant`: Ana koordinatör sınıf
- `PromptTemplate`: Şablon tanımlama
- `PromptMetrics`: Performans metrikleri
- `PromptTechnique`: Teknik enum'ları
- `TaskType`: Görev tipi tanımlamaları

### Algoritma Akışı
1. **Görev Analizi**: NLP tabanlı kategorizasyon
2. **Teknik Seçimi**: Kural tabanlı öneri sistemi
3. **Template Matching**: Uygun şablon seçimi
4. **Parametre Doldurma**: Dinamik değişken atama
5. **Metrik Hesaplama**: Performans değerlendirme
6. **Optimizasyon**: İteratif iyileştirme

### Veri Yapıları
- Template library: Dictionary-based storage
- Optimization history: List-based tracking
- Metrics calculation: Mathematical scoring
- GUI state management: Tkinter variables

## 🔮 Gelecek Planları

- [ ] GPT/Claude API entegrasyonu
- [ ] Çoklu dil desteği
- [ ] Makine öğrenmesi tabanlı optimizasyon
- [ ] Topluluk şablon paylaşımı
- [ ] Web tabanlı arayüz
- [ ] Batch processing API
- [ ] A/B testing framework

## 📄 Lisans

Bu proje MIT lisansı altında sunulmaktadır.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen:
1. Fork yapın
2. Feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Pull request gönderin

## 📞 İletişim

Sorularınız için issue açabilir veya doğrudan iletişime geçebilirsiniz.

---

*Bu prompt asistanı, Türkçe prompt mühendisliği araştırmalarına dayalı olarak geliştirilmiş, gelişmiş meta-prompting yetenekleri ile donatılmış bir araçtır. Sürekli öğrenen ve gelişen yapısıyla prompt kalitesini artırmayı hedefler.*