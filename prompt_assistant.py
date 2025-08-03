#!/usr/bin/env python3
"""
Prompt Assistant - Gelişmiş Prompt Mühendisliği Asistanı
Türkçe Prompt Mühendisliği dokümantasyonuna dayalı tasarlanmıştır.

Özellikler:
- Meta-prompting yetenekleri
- Çoklu teknik seçimi ve optimizasyon
- TAG, BAB ve diğer framework'ler
- Performans takibi ve iteratif geliştirme
"""

from typing import Dict, List, Optional, Tuple, Any
from enum import Enum
from dataclasses import dataclass
import json
import re
from datetime import datetime

class PromptTechnique(Enum):
    """Prompt teknikleri"""
    ZERO_SHOT = "zero_shot"
    FEW_SHOT = "few_shot"
    CHAIN_OF_THOUGHT = "chain_of_thought"
    TREE_OF_THOUGHT = "tree_of_thought"
    SELF_ASK = "self_ask"
    ROLE_BASED = "role_based"
    META_PROMPT = "meta_prompt"
    RAG = "rag"
    TAG_FRAMEWORK = "tag_framework"
    BAB_FRAMEWORK = "bab_framework"

class TaskType(Enum):
    """Görev tipleri"""
    REASONING = "reasoning"
    CREATIVE = "creative"
    TECHNICAL = "technical"
    ANALYTICAL = "analytical"
    EDUCATIONAL = "educational"

class DifficultyLevel(Enum):
    """Zorluk seviyeleri"""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

@dataclass
class PromptMetrics:
    """Prompt performans metrikleri"""
    clarity_score: float
    effectiveness_score: float
    optimization_level: int
    iteration_count: int
    success_rate: float
    timestamp: datetime

@dataclass
class PromptTemplate:
    """Prompt şablonu"""
    name: str
    technique: PromptTechnique
    template: str
    variables: List[str]
    task_types: List[TaskType]
    difficulty: DifficultyLevel
    description: str
    example: str

class PromptAssistant:
    """Ana Prompt Asistanı Sınıfı"""
    
    def __init__(self):
        self.templates = self._initialize_templates()
        self.optimization_history = []
        self.performance_metrics = {}
        
    def _initialize_templates(self) -> Dict[str, PromptTemplate]:
        """Prompt şablonlarını başlat"""
        templates = {
            "meta_prompt": PromptTemplate(
                name="Universal Meta-Prompt",
                technique=PromptTechnique.META_PROMPT,
                template="""Sen bir uzman prompt mühendisissin. Verilen görevi analiz et ve en etkili promotu oluştur.

GÖREV: {task}
HEDEF KİTLE: {audience}
BAĞLAM: {context}

ADIM 1: GÖREV ANALİZİ
- Görevin türünü belirle (yaratıcı, teknik, analitik)
- Gerekli uzmanlık alanlarını tanımla
- Çıktı formatını belirle

ADIM 2: TEKNİK SEÇİMİ
- En uygun prompt tekniğini seç
- Nedenini açıkla
- Optimizasyon stratejisini belirle

ADIM 3: PROMPT OLUŞTURMA
- Seçilen teknikle optimum promotu oluştur
- Açık ve spesifik talimatlar ver
- Başarı kriterlerini tanımla

ÇIKTI FORMATI:
[Optimized Prompt]
[Explanation of technique choice]
[Success criteria]""",
                variables=["task", "audience", "context"],
                task_types=[TaskType.REASONING, TaskType.TECHNICAL, TaskType.CREATIVE],
                difficulty=DifficultyLevel.EXPERT,
                description="Kendini optimize eden meta-prompt",
                example="Meta-prompt ile blog yazısı oluşturma görevi optimizasyonu"
            ),
            
            "tag_framework": PromptTemplate(
                name="TAG Framework",
                technique=PromptTechnique.TAG_FRAMEWORK,
                template="""GÖREV (Task): {task}
AKSİYON (Action): {action}
HEDEF (Goal): {goal}

BAĞLAM: {context}
KISITLAR: {constraints}
ÇIKTI FORMATI: {output_format}

Lütfen yukarıdaki görevı belirtilen aksiyon ve hedef doğrultusunda tamamla.""",
                variables=["task", "action", "goal", "context", "constraints", "output_format"],
                task_types=[TaskType.TECHNICAL, TaskType.ANALYTICAL],
                difficulty=DifficultyLevel.INTERMEDIATE,
                description="Görev-Aksiyon-Hedef çerçevesi",
                example="Yazılım geliştirme görevleri için yapılandırılmış prompt"
            ),
            
            "bab_framework": PromptTemplate(
                name="BAB Framework", 
                technique=PromptTechnique.BAB_FRAMEWORK,
                template="""ÖNCE (Before): {current_state}
Bu mevcut durumu analiz et ve sorunları belirle.

SONRA (After): {desired_state}  
Bu hedef durumu net bir şekilde tanımla.

KÖPRÜ (Bridge): {solution_path}
Mevcut durumdan hedef duruma nasıl ulaşılacağını adım adım açıkla.

BAĞLAM: {context}
BAŞARI KRİTERLERİ: {success_criteria}""",
                variables=["current_state", "desired_state", "solution_path", "context", "success_criteria"],
                task_types=[TaskType.ANALYTICAL, TaskType.REASONING],
                difficulty=DifficultyLevel.INTERMEDIATE,
                description="Problem çözme için narratif çerçeve",
                example="İş süreçlerini iyileştirme projelerinde kullanım"
            ),
            
            "chain_of_thought": PromptTemplate(
                name="Düşünce Zinciri",
                technique=PromptTechnique.CHAIN_OF_THOUGHT,
                template="""{task}

Bu problemi çözmek için adım adım düşünelim:

1. Önce sorunu tam olarak anlayalım
2. Mevcut bilgileri listeleyelim  
3. Çözüm yaklaşımlarını değerlendirelim
4. En uygun yaklaşımı seçelim
5. Adım adım uygulayalım
6. Sonucu doğrulayalım

Her adımda düşünce sürecini açıkça belirt.""",
                variables=["task"],
                task_types=[TaskType.REASONING, TaskType.ANALYTICAL],
                difficulty=DifficultyLevel.BASIC,
                description="Adım adım düşünme süreci",
                example="Matematik problemleri ve mantıksal çıkarımlar"
            ),
            
            "role_based": PromptTemplate(
                name="Rol Tabanlı",
                technique=PromptTechnique.ROLE_BASED,
                template="""Sen bir {expert_role} uzmanısın. {experience} yıllık deneyimin var.

UZMANLİK ALANLARIN:
{expertise_areas}

GÖREV: {task}

Bu görevi uzmanlık alanına uygun şekilde, pratik deneyimini kullanarak çöz. 
Sadece {expert_role} perspektifinden yaklaş ve bu alandaki en iyi pratikleri uygula.

ÇIKTI FORMATI: {output_format}""",
                variables=["expert_role", "experience", "expertise_areas", "task", "output_format"],
                task_types=[TaskType.TECHNICAL, TaskType.CREATIVE, TaskType.EDUCATIONAL],
                difficulty=DifficultyLevel.INTERMEDIATE,
                description="Uzman rolü atama ile performans artışı",
                example="Yazılım mimarı rolüyle sistem tasarımı"
            )
        }
        return templates
    
    def analyze_task(self, task: str, context: str = "") -> Dict[str, Any]:
        """Görevi analiz et ve en uygun tekniği öner"""
        
        # Basit NLP analizi (gerçek projede daha sofistike olabilir)
        analysis = {
            "task_type": self._detect_task_type(task),
            "complexity": self._assess_complexity(task),
            "recommended_technique": None,
            "confidence": 0.0
        }
        
        # Teknik önerisi
        task_type = analysis["task_type"]
        complexity = analysis["complexity"]
        
        if "adım" in task.lower() or "nasıl" in task.lower():
            analysis["recommended_technique"] = PromptTechnique.CHAIN_OF_THOUGHT
            analysis["confidence"] = 0.8
        elif "uzman" in task.lower() or "profesyonel" in task.lower():
            analysis["recommended_technique"] = PromptTechnique.ROLE_BASED
            analysis["confidence"] = 0.7
        elif complexity == DifficultyLevel.EXPERT:
            analysis["recommended_technique"] = PromptTechnique.META_PROMPT
            analysis["confidence"] = 0.9
        elif task_type == TaskType.ANALYTICAL:
            analysis["recommended_technique"] = PromptTechnique.TAG_FRAMEWORK
            analysis["confidence"] = 0.7
        else:
            analysis["recommended_technique"] = PromptTechnique.ZERO_SHOT
            analysis["confidence"] = 0.5
            
        return analysis
    
    def _detect_task_type(self, task: str) -> TaskType:
        """Görev tipini tespit et"""
        task_lower = task.lower()
        
        creative_keywords = ["yaz", "oluştur", "tasarla", "yaratıcı", "hikaye", "makale"]
        technical_keywords = ["kod", "program", "algoritma", "sistem", "teknik", "geliştir"]
        analytical_keywords = ["analiz", "değerlendir", "karşılaştır", "incelendiğinde", "araştır"]
        reasoning_keywords = ["çöz", "açıkla", "kanıtla", "mantık", "sonuç", "sebep"]
        
        if any(keyword in task_lower for keyword in creative_keywords):
            return TaskType.CREATIVE
        elif any(keyword in task_lower for keyword in technical_keywords):
            return TaskType.TECHNICAL
        elif any(keyword in task_lower for keyword in analytical_keywords):
            return TaskType.ANALYTICAL
        elif any(keyword in task_lower for keyword in reasoning_keywords):
            return TaskType.REASONING
        else:
            return TaskType.EDUCATIONAL
    
    def _assess_complexity(self, task: str) -> DifficultyLevel:
        """Görev karmaşıklığını değerlendir"""
        complexity_indicators = {
            DifficultyLevel.EXPERT: ["optimize", "meta", "gelişmiş", "karmaşık", "çok boyutlu"],
            DifficultyLevel.ADVANCED: ["detaylı", "kapsamlı", "ileri", "profesyonel"],
            DifficultyLevel.INTERMEDIATE: ["analiz", "değerlendir", "karşılaştır"],
            DifficultyLevel.BASIC: ["basit", "açıkla", "listele", "tanımla"]
        }
        
        task_lower = task.lower()
        
        for level, keywords in complexity_indicators.items():
            if any(keyword in task_lower for keyword in keywords):
                return level
        
        # Cümle uzunluğu ve teknik terim sayısına göre varsayılan değerlendirme
        if len(task.split()) > 20:
            return DifficultyLevel.ADVANCED
        elif len(task.split()) > 10:
            return DifficultyLevel.INTERMEDIATE
        else:
            return DifficultyLevel.BASIC
    
    def generate_prompt(self, task: str, technique: Optional[PromptTechnique] = None, 
                       **kwargs) -> Tuple[str, PromptMetrics]:
        """Optimum prompt oluştur"""
        
        if not technique:
            analysis = self.analyze_task(task, kwargs.get("context", ""))
            technique = analysis["recommended_technique"]
        
        template = self.templates.get(technique.value)
        if not template:
            # Fallback to basic template
            prompt = f"Görev: {task}\n\nBu görevi en iyi şekilde tamamla."
            metrics = PromptMetrics(0.5, 0.5, 1, 1, 0.0, datetime.now())
            return prompt, metrics
        
        # Template değişkenlerini doldur
        prompt = self._fill_template(template, task, **kwargs)
        
        # Metrikleri hesapla
        metrics = self._calculate_metrics(prompt, template, kwargs)
        
        # Geçmişe ekle
        self.optimization_history.append({
            "task": task,
            "technique": technique,
            "prompt": prompt,
            "metrics": metrics,
            "timestamp": datetime.now()
        })
        
        return prompt, metrics
    
    def _fill_template(self, template: PromptTemplate, task: str, **kwargs) -> str:
        """Template değişkenlerini doldur"""
        
        # Otomatik değişken dolguları
        variables = {
            "task": task,
            "context": kwargs.get("context", "Genel bağlam"),
            "audience": kwargs.get("audience", "Genel kullanıcı"),
            "output_format": kwargs.get("output_format", "Yapılandırılmış metin"),
            "constraints": kwargs.get("constraints", "Belirtilmemiş"),
            "success_criteria": kwargs.get("success_criteria", "Görevin başarıyla tamamlanması")
        }
        
        # Kullanıcı tarafından sağlanan değişkenler
        variables.update(kwargs)
        
        try:
            return template.template.format(**variables)
        except KeyError as e:
            # Eksik değişken için varsayılan değer
            missing_var = str(e).strip("'")
            variables[missing_var] = f"[{missing_var.upper()}_BELIRTILMEDI]"
            return template.template.format(**variables)
    
    def _calculate_metrics(self, prompt: str, template: PromptTemplate, 
                          kwargs: Dict) -> PromptMetrics:
        """Prompt metrikleri hesapla"""
        
        # Netlik skoru (basit analiz)
        clarity_score = min(1.0, len(prompt.split()) / 100)  # Kelime sayısına göre
        
        # Etkinlik skoru (template kalitesine göre)
        effectiveness_score = {
            DifficultyLevel.EXPERT: 0.9,
            DifficultyLevel.ADVANCED: 0.8,
            DifficultyLevel.INTERMEDIATE: 0.7,
            DifficultyLevel.BASIC: 0.6
        }.get(template.difficulty, 0.5)
        
        # Optimizasyon seviyesi
        optimization_level = len([k for k in kwargs.keys() if k in template.variables])
        
        return PromptMetrics(
            clarity_score=clarity_score,
            effectiveness_score=effectiveness_score,
            optimization_level=optimization_level,
            iteration_count=1,
            success_rate=0.0,  # Başlangıçta 0, kullanım sonrası güncellenir
            timestamp=datetime.now()
        )
    
    def optimize_prompt(self, prompt: str, feedback: str) -> str:
        """Geri bildirime göre promotu optimize et"""
        
        optimization_suggestions = []
        
        if "belirsiz" in feedback.lower():
            optimization_suggestions.append("Daha spesifik talimatlar ekle")
        if "eksik" in feedback.lower():
            optimization_suggestions.append("Eksik bilgileri tamamla")
        if "uzun" in feedback.lower():
            optimization_suggestions.append("Gereksiz kısımları çıkar")
        
        # Meta-prompt ile optimizasyon
        meta_optimization = f"""Aşağıdaki promptu optimize et:

MEVCUT PROMPT:
{prompt}

GERİ BİLDİRİM:
{feedback}

OPTİMİZASYON ÖNERİLERİ:
{chr(10).join(f"- {suggestion}" for suggestion in optimization_suggestions)}

İyileştirilmiş prompt çıktısı ver."""
        
        return meta_optimization
    
    def get_template_suggestions(self, task_type: TaskType, 
                               difficulty: DifficultyLevel) -> List[PromptTemplate]:
        """Görev tipine göre şablon önerileri"""
        
        suitable_templates = [
            template for template in self.templates.values()
            if (task_type in template.task_types and 
                template.difficulty.value <= difficulty.value)
        ]
        
        return sorted(suitable_templates, 
                     key=lambda x: x.difficulty.value, reverse=True)
    
    def export_optimization_report(self) -> Dict[str, Any]:
        """Optimizasyon raporu oluştur"""
        
        if not self.optimization_history:
            return {"message": "Henüz optimizasyon geçmişi bulunmuyor"}
        
        total_prompts = len(self.optimization_history)
        avg_effectiveness = sum(entry["metrics"].effectiveness_score 
                              for entry in self.optimization_history) / total_prompts
        
        technique_usage = {}
        for entry in self.optimization_history:
            technique = entry["technique"].value
            technique_usage[technique] = technique_usage.get(technique, 0) + 1
        
        return {
            "total_prompts_generated": total_prompts,
            "average_effectiveness_score": avg_effectiveness,
            "most_used_technique": max(technique_usage.items(), 
                                     key=lambda x: x[1])[0],
            "technique_distribution": technique_usage,
            "latest_optimization": self.optimization_history[-1]["timestamp"].isoformat(),
            "performance_trend": "Gelişen" if avg_effectiveness > 0.7 else "İyileştirme Gerekli"
        }

def main():
    """Demo kullanımı"""
    
    assistant = PromptAssistant()
    
    print("🤖 Gelişmiş Prompt Asistanı")
    print("=" * 50)
    
    # Örnek görev
    task = "Bir e-ticaret sitesi için güvenlik açıklarını tespit eden bir araç tasarla"
    
    print(f"\n📋 GÖREV: {task}")
    
    # Görev analizi
    analysis = assistant.analyze_task(task)
    print(f"\n🔍 ANALİZ:")
    print(f"   Görev Tipi: {analysis['task_type'].value}")
    print(f"   Karmaşıklık: {analysis['complexity'].value}")
    print(f"   Önerilen Teknik: {analysis['recommended_technique'].value}")
    print(f"   Güven Skoru: {analysis['confidence']:.1%}")
    
    # Prompt oluşturma
    prompt, metrics = assistant.generate_prompt(
        task=task,
        context="E-ticaret güvenliği",
        expert_role="Siber Güvenlik Uzmanı",
        experience="10",
        expertise_areas="Web Uygulama Güvenliği, Penetrasyon Testi, OWASP"
    )
    
    print(f"\n✨ OLUŞTURULAN PROMPT:")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    
    print(f"\n📊 METRİKLER:")
    print(f"   Netlik Skoru: {metrics.clarity_score:.2f}")
    print(f"   Etkinlik Skoru: {metrics.effectiveness_score:.2f}")
    print(f"   Optimizasyon Seviyesi: {metrics.optimization_level}")
    
    # Şablon önerileri
    suggestions = assistant.get_template_suggestions(
        TaskType.TECHNICAL, DifficultyLevel.ADVANCED
    )
    print(f"\n💡 DİĞER UYGUN ŞABLONLAR:")
    for template in suggestions[:3]:
        print(f"   - {template.name}: {template.description}")
    
    # Optimizasyon raporu
    report = assistant.export_optimization_report()
    print(f"\n📈 OPTİMİZASYON RAPORU:")
    for key, value in report.items():
        print(f"   {key}: {value}")

if __name__ == "__main__":
    main()