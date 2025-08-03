#!/usr/bin/env python3
"""
Prompt Assistant GUI - Gelişmiş Prompt Mühendisliği Asistanı Arayüzü
prompt_assistant.py modülü ile çalışır.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
from datetime import datetime
from typing import Dict, Any, List

try:
    from prompt_assistant import PromptAssistant, PromptTechnique, TaskType, DifficultyLevel
except ImportError:
    messagebox.showerror("Hata", "prompt_assistant.py modülü bulunamadı!")
    exit(1)

class PromptAssistantGUI:
    """Prompt Asistanı GUI Sınıfı"""
    
    def __init__(self, root):
        self.root = root
        self.assistant = PromptAssistant()
        self.setup_ui()
        self.current_prompt = ""
        self.current_metrics = None
        
    def setup_ui(self):
        """Kullanıcı arayüzünü oluştur"""
        
        self.root.title("🤖 Gelişmiş Prompt Mühendisliği Asistanı")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f0f0")
        
        # Ana container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Grid yapılandırması
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Başlık
        title_label = ttk.Label(main_frame, text="🤖 Gelişmiş Prompt Mühendisliği Asistanı", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Sol panel - Giriş ve Kontroller
        self.setup_input_panel(main_frame)
        
        # Sağ panel - Çıkış ve Analiz
        self.setup_output_panel(main_frame)
        
        # Alt panel - Performans ve İstatistikler
        self.setup_stats_panel(main_frame)
        
    def setup_input_panel(self, parent):
        """Giriş panelini oluştur"""
        
        input_frame = ttk.LabelFrame(parent, text="📝 Görev Girişi ve Ayarlar", padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        input_frame.columnconfigure(0, weight=1)
        
        # Görev girişi
        ttk.Label(input_frame, text="Görev Açıklaması:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.task_text = scrolledtext.ScrolledText(input_frame, height=6, width=50, wrap=tk.WORD)
        self.task_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        self.task_text.insert(tk.END, "Bir e-ticaret sitesi için güvenlik açıklarını tespit eden bir araç tasarla")
        
        # Bağlam girişi
        ttk.Label(input_frame, text="Bağlam (İsteğe bağlı):").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        self.context_text = scrolledtext.ScrolledText(input_frame, height=3, width=50, wrap=tk.WORD)
        self.context_text.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Teknik seçimi
        technique_frame = ttk.Frame(input_frame)
        technique_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(technique_frame, text="Prompt Tekniği:").grid(row=0, column=0, sticky=tk.W)
        
        self.technique_var = tk.StringVar(value="auto")
        technique_combo = ttk.Combobox(technique_frame, textvariable=self.technique_var, 
                                     values=["auto"] + [t.value for t in PromptTechnique])
        technique_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        technique_frame.columnconfigure(1, weight=1)
        
        # Ek parametreler
        params_frame = ttk.LabelFrame(input_frame, text="📊 Ek Parametreler", padding="5")
        params_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        params_frame.columnconfigure(1, weight=1)
        
        # Hedef kitle
        ttk.Label(params_frame, text="Hedef Kitle:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.audience_entry = ttk.Entry(params_frame)
        self.audience_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.audience_entry.insert(0, "Teknik personel")
        
        # Uzman rolü
        ttk.Label(params_frame, text="Uzman Rolü:").grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
        self.role_entry = ttk.Entry(params_frame)
        self.role_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.role_entry.insert(0, "Siber Güvenlik Uzmanı")
        
        # Deneyim
        ttk.Label(params_frame, text="Deneyim (yıl):").grid(row=2, column=0, sticky=tk.W, padx=(0, 10))
        self.experience_entry = ttk.Entry(params_frame)
        self.experience_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2)
        self.experience_entry.insert(0, "10")
        
        # Çıktı formatı
        ttk.Label(params_frame, text="Çıktı Formatı:").grid(row=3, column=0, sticky=tk.W, padx=(0, 10))
        self.output_format_entry = ttk.Entry(params_frame)
        self.output_format_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=2)
        self.output_format_entry.insert(0, "Yapılandırılmış metin")
        
        # Butonlar
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=(20, 0))
        
        generate_btn = ttk.Button(button_frame, text="🚀 Prompt Oluştur", 
                                command=self.generate_prompt, style="Accent.TButton")
        generate_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        analyze_btn = ttk.Button(button_frame, text="🔍 Görev Analizi", 
                               command=self.analyze_task)
        analyze_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        optimize_btn = ttk.Button(button_frame, text="⚡ Optimize Et", 
                                command=self.show_optimization_dialog)
        optimize_btn.pack(side=tk.LEFT)
        
    def setup_output_panel(self, parent):
        """Çıkış panelini oluştur"""
        
        output_frame = ttk.LabelFrame(parent, text="✨ Oluşturulan Prompt ve Analiz", padding="10")
        output_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Notebook for tabs
        notebook = ttk.Notebook(output_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Prompt tab
        prompt_frame = ttk.Frame(notebook, padding="10")
        notebook.add(prompt_frame, text="📝 Prompt")
        
        self.prompt_text = scrolledtext.ScrolledText(prompt_frame, wrap=tk.WORD, 
                                                   font=("Consolas", 10))
        self.prompt_text.pack(fill=tk.BOTH, expand=True)
        
        # Copy button
        copy_btn = ttk.Button(prompt_frame, text="📋 Kopyala", 
                            command=self.copy_prompt)
        copy_btn.pack(pady=(10, 0))
        
        # Analiz tab
        analysis_frame = ttk.Frame(notebook, padding="10")
        notebook.add(analysis_frame, text="🔍 Analiz")
        
        self.analysis_text = scrolledtext.ScrolledText(analysis_frame, wrap=tk.WORD, 
                                                     font=("Arial", 10))
        self.analysis_text.pack(fill=tk.BOTH, expand=True)
        
        # Şablonlar tab
        templates_frame = ttk.Frame(notebook, padding="10")
        notebook.add(templates_frame, text="🎭 Şablonlar")
        
        self.templates_tree = ttk.Treeview(templates_frame, 
                                         columns=("technique", "difficulty", "description"))
        self.templates_tree.heading("#0", text="Şablon Adı")
        self.templates_tree.heading("technique", text="Teknik")
        self.templates_tree.heading("difficulty", text="Zorluk")
        self.templates_tree.heading("description", text="Açıklama")
        
        self.templates_tree.pack(fill=tk.BOTH, expand=True)
        
        # Şablonları yükle
        self.load_templates()
        
    def setup_stats_panel(self, parent):
        """İstatistik panelini oluştur"""
        
        stats_frame = ttk.LabelFrame(parent, text="📈 Performans İstatistikleri", padding="10")
        stats_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        stats_frame.columnconfigure((0, 1, 2, 3), weight=1)
        
        # Metrik etiketleri
        self.clarity_label = ttk.Label(stats_frame, text="Netlik: --", font=("Arial", 10, "bold"))
        self.clarity_label.grid(row=0, column=0, padx=10)
        
        self.effectiveness_label = ttk.Label(stats_frame, text="Etkinlik: --", font=("Arial", 10, "bold"))
        self.effectiveness_label.grid(row=0, column=1, padx=10)
        
        self.optimization_label = ttk.Label(stats_frame, text="Optimizasyon: --", font=("Arial", 10, "bold"))
        self.optimization_label.grid(row=0, column=2, padx=10)
        
        self.total_prompts_label = ttk.Label(stats_frame, text="Toplam: 0", font=("Arial", 10, "bold"))
        self.total_prompts_label.grid(row=0, column=3, padx=10)
        
        # Progress bars
        self.clarity_progress = ttk.Progressbar(stats_frame, length=100, mode='determinate')
        self.clarity_progress.grid(row=1, column=0, padx=10, pady=(5, 0))
        
        self.effectiveness_progress = ttk.Progressbar(stats_frame, length=100, mode='determinate')
        self.effectiveness_progress.grid(row=1, column=1, padx=10, pady=(5, 0))
        
        self.optimization_progress = ttk.Progressbar(stats_frame, length=100, mode='determinate')
        self.optimization_progress.grid(row=1, column=2, padx=10, pady=(5, 0))
        
        # Rapor butonu
        report_btn = ttk.Button(stats_frame, text="📊 Detaylı Rapor", 
                              command=self.show_detailed_report)
        report_btn.grid(row=1, column=3, padx=10, pady=(5, 0))
        
    def load_templates(self):
        """Şablonları ağaca yükle"""
        
        for name, template in self.assistant.templates.items():
            self.templates_tree.insert("", tk.END, text=template.name,
                                     values=(template.technique.value,
                                           template.difficulty.value,
                                           template.description))
    
    def generate_prompt(self):
        """Prompt oluştur"""
        
        task = self.task_text.get("1.0", tk.END).strip()
        if not task:
            messagebox.showwarning("Uyarı", "Lütfen bir görev açıklaması girin!")
            return
        
        # Parametreleri topla
        params = {
            "context": self.context_text.get("1.0", tk.END).strip(),
            "audience": self.audience_entry.get() or "Genel kullanıcı",
            "expert_role": self.role_entry.get() or "Uzman",
            "experience": self.experience_entry.get() or "5",
            "output_format": self.output_format_entry.get() or "Metin",
            "expertise_areas": "Belirlenmemiş"  # Bu alana GUI'da ekleme yapılabilir
        }
        
        # Teknik seçimi
        technique = None
        if self.technique_var.get() != "auto":
            technique = PromptTechnique(self.technique_var.get())
        
        try:
            # Prompt oluştur
            prompt, metrics = self.assistant.generate_prompt(task, technique, **params)
            
            # Sonuçları göster
            self.current_prompt = prompt
            self.current_metrics = metrics
            
            self.prompt_text.delete("1.0", tk.END)
            self.prompt_text.insert("1.0", prompt)
            
            # Metrikleri güncelle
            self.update_metrics(metrics)
            
            messagebox.showinfo("Başarı", "Prompt başarıyla oluşturuldu!")
            
        except Exception as e:
            messagebox.showerror("Hata", f"Prompt oluşturulurken hata oluştu: {str(e)}")
    
    def analyze_task(self):
        """Görev analizi yap"""
        
        task = self.task_text.get("1.0", tk.END).strip()
        if not task:
            messagebox.showwarning("Uyarı", "Lütfen bir görev açıklaması girin!")
            return
        
        try:
            analysis = self.assistant.analyze_task(task, self.context_text.get("1.0", tk.END).strip())
            
            # Analiz sonuçlarını göster
            analysis_text = f"""
🔍 GÖREV ANALİZİ
{'='*50}

📋 Görev Tipi: {analysis['task_type'].value.upper()}
📊 Karmaşıklık Seviyesi: {analysis['complexity'].value.upper()}
🎯 Önerilen Teknik: {analysis['recommended_technique'].value.upper()}
💯 Güven Skoru: %{analysis['confidence']*100:.1f}

📝 AÇIKLAMA:
{self.get_task_type_description(analysis['task_type'])}

⚡ TEKNİK ÖNERİSİ:
{self.get_technique_description(analysis['recommended_technique'])}

🎭 UYGUN ŞABLONLAR:
"""
            
            # Uygun şablonları bul
            suggestions = self.assistant.get_template_suggestions(
                analysis['task_type'], analysis['complexity']
            )
            
            for i, template in enumerate(suggestions[:5], 1):
                analysis_text += f"{i}. {template.name} - {template.description}\n"
            
            self.analysis_text.delete("1.0", tk.END)
            self.analysis_text.insert("1.0", analysis_text)
            
            # Otomatik teknik seçimi
            self.technique_var.set(analysis['recommended_technique'].value)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Analiz yapılırken hata oluştu: {str(e)}")
    
    def get_task_type_description(self, task_type: TaskType) -> str:
        """Görev tipi açıklaması"""
        descriptions = {
            TaskType.CREATIVE: "Yaratıcı içerik üretimi gerektiren görevler",
            TaskType.TECHNICAL: "Teknik bilgi ve uygulama gerektiren görevler",
            TaskType.ANALYTICAL: "Analiz ve değerlendirme gerektiren görevler",
            TaskType.REASONING: "Mantıksal çıkarım ve akıl yürütme gerektiren görevler",
            TaskType.EDUCATIONAL: "Öğretim ve eğitim amaçlı görevler"
        }
        return descriptions.get(task_type, "Genel amaçlı görev")
    
    def get_technique_description(self, technique: PromptTechnique) -> str:
        """Teknik açıklaması"""
        descriptions = {
            PromptTechnique.ZERO_SHOT: "Doğrudan talimat verme yaklaşımı",
            PromptTechnique.FEW_SHOT: "Örneklerle öğrenme yaklaşımı",
            PromptTechnique.CHAIN_OF_THOUGHT: "Adım adım düşünce süreci",
            PromptTechnique.META_PROMPT: "Kendini optimize eden meta-prompt",
            PromptTechnique.ROLE_BASED: "Uzman rolü atama yaklaşımı",
            PromptTechnique.TAG_FRAMEWORK: "Görev-Aksiyon-Hedef çerçevesi",
            PromptTechnique.BAB_FRAMEWORK: "Önce-Sonra-Köprü narratif çerçevesi"
        }
        return descriptions.get(technique, "Genel teknik")
    
    def copy_prompt(self):
        """Promptu panoya kopyala"""
        if self.current_prompt:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_prompt)
            messagebox.showinfo("Başarı", "Prompt panoya kopyalandı!")
        else:
            messagebox.showwarning("Uyarı", "Kopyalanacak prompt bulunamadı!")
    
    def update_metrics(self, metrics):
        """Metrikleri güncelle"""
        
        clarity_pct = int(metrics.clarity_score * 100)
        effectiveness_pct = int(metrics.effectiveness_score * 100)
        optimization_pct = min(100, metrics.optimization_level * 20)
        
        self.clarity_label.config(text=f"Netlik: %{clarity_pct}")
        self.effectiveness_label.config(text=f"Etkinlik: %{effectiveness_pct}")
        self.optimization_label.config(text=f"Optimizasyon: Seviye {metrics.optimization_level}")
        self.total_prompts_label.config(text=f"Toplam: {len(self.assistant.optimization_history)}")
        
        self.clarity_progress['value'] = clarity_pct
        self.effectiveness_progress['value'] = effectiveness_pct
        self.optimization_progress['value'] = optimization_pct
    
    def show_optimization_dialog(self):
        """Optimizasyon dialogunu göster"""
        
        if not self.current_prompt:
            messagebox.showwarning("Uyarı", "Önce bir prompt oluşturun!")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("⚡ Prompt Optimizasyonu")
        dialog.geometry("600x400")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Feedback girişi
        ttk.Label(dialog, text="Geri Bildirim:").pack(pady=(10, 5))
        feedback_text = scrolledtext.ScrolledText(dialog, height=6, wrap=tk.WORD)
        feedback_text.pack(fill=tk.BOTH, expand=True, padx=10)
        feedback_text.insert("1.0", "Prompt daha spesifik olmalı ve daha net talimatlar içermeli.")
        
        # Optimize butonu
        def optimize():
            feedback = feedback_text.get("1.0", tk.END).strip()
            if feedback:
                optimized_prompt = self.assistant.optimize_prompt(self.current_prompt, feedback)
                
                # Sonucu göster
                result_window = tk.Toplevel(dialog)
                result_window.title("✨ Optimize Edilmiş Prompt")
                result_window.geometry("700x500")
                
                result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
                result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                result_text.insert("1.0", optimized_prompt)
                
                ttk.Button(result_window, text="Kapat", 
                          command=result_window.destroy).pack(pady=(0, 10))
        
        ttk.Button(dialog, text="⚡ Optimize Et", command=optimize).pack(pady=10)
        ttk.Button(dialog, text="İptal", command=dialog.destroy).pack()
    
    def show_detailed_report(self):
        """Detaylı raporu göster"""
        
        try:
            report = self.assistant.export_optimization_report()
            
            dialog = tk.Toplevel(self.root)
            dialog.title("📊 Detaylı Performans Raporu")
            dialog.geometry("600x500")
            dialog.transient(self.root)
            
            report_text = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, font=("Consolas", 10))
            report_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Raporu formatla
            formatted_report = f"""
📊 PROMPT ASİSTANI PERFORMANS RAPORU
{'='*60}
📅 Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📈 GENEL İSTATİSTİKLER:
"""
            
            for key, value in report.items():
                if key == "technique_distribution":
                    formatted_report += f"\n📊 TEKNİK DAĞILIMI:\n"
                    for tech, count in value.items():
                        formatted_report += f"   • {tech}: {count} kez\n"
                else:
                    formatted_report += f"   • {key.replace('_', ' ').title()}: {value}\n"
            
            report_text.insert("1.0", formatted_report)
            
            ttk.Button(dialog, text="Kapat", command=dialog.destroy).pack(pady=(0, 10))
            
        except Exception as e:
            messagebox.showerror("Hata", f"Rapor oluşturulurken hata oluştu: {str(e)}")

def main():
    """Ana uygulama"""
    
    root = tk.Tk()
    
    # Stil ayarları
    style = ttk.Style()
    style.theme_use('clam')
    
    # Özel stiller
    style.configure('Accent.TButton', foreground='white', background='#007ACC')
    
    app = PromptAssistantGUI(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()