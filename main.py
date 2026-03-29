from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import random

# إعدادات الشاشة السيادية
Window.clearcolor = (0, 0, 0, 1) # خلفية سوداء فخمة

class SinaShieldUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10)
        
        # عنوان البرنامج
        self.add_widget(Label(
            text="[ SINA SHIELD - V1.0 ]",
            font_size='30sp',
            color=(0, 1, 0, 1), # لون أخضر "نبض"
            bold=True
        ))
        
        self.add_widget(Label(
            text="Eng. Mohamed Hussein",
            font_size='18sp',
            color=(0.8, 0.8, 0.8, 1)
        ))

        # شاشة الرادار (النبض)
        self.status_label = Label(
            text="[SYSTEM ACTIVE - MONITORING]",
            font_size='15sp',
            color=(0, 1, 0, 1)
        )
        self.add_widget(self.status_label)

        # منطقة عرض التهديدات (المراية العاكسة)
        self.attack_log = Label(
            text="Waiting for threats...",
            font_size='12sp',
            color=(1, 0, 0, 1), # أحمر للهجمات
            halign='center'
        )
        self.add_widget(self.attack_log)

        # زر تفعيل الحماية
        self.btn = Button(
            text="ACTIVATE MIRROR SHIELD",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0, 1),
            font_size='20sp'
        )
        self.btn.bind(on_press=self.start_defense)
        self.add_widget(self.btn)

    def start_defense(self, instance):
        self.status_label.text = "[MIRROR SHIELD ACTIVE - 100%]"
        self.btn.text = "DEFENSE RUNNING..."
        self.btn.disabled = True
        # تشغيل محاكي كشف الهجمات
        Clock.schedule_interval(self.update_log, 2)

    def update_log(self, dt):
        fake_ips = ["192.168.1.50", "45.12.88.3", "102.166.1.1", "العدو رقم 21"]
        target = random.choice(fake_ips)
        self.attack_log.text = f"ATTACK DETECTED FROM: {target}\n[ACTION]: MIRROR REFLECTED - IP BLOCKED"

class SinaShieldApp(App):
    def build(self):
        return SinaShieldUI()

if __name__ == "__main__":
    SinaShieldApp().run()[app]
title = Sina Shield
package.name = sinashield
package.domain = org.mohamed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
