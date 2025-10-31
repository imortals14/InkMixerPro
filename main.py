from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#1e293b")

class InkMixerPro(App):
    def calculate(self, instance):
        try:
            weight = float(self.weight_input.text)
            manufacturer = self.manufacturer_spinner.text
            
            if weight > 0:
                # Формулы для производителей (реальные данные)
                formulas = {
                    "Санкемикалз": (0.267, 0.75, 0.25),
                    "Сико": (0.333, 0.4, 0.6),
                    "Китай": (0.25, 0.8, 0.2),
                    "Тампо Механика": (0.221, 0.333, 0.667)
                }
                
                percent, cf2000_ratio, cf3000_ratio = formulas[manufacturer]
                total_solvent = weight * percent
                cf2000 = total_solvent * cf2000_ratio
                cf3000 = total_solvent * cf3000_ratio
                
                self.result_label.text = f'''[b]📊 РЕЗУЛЬТАТ:[/b]

● CF2000: {cf2000:.0f} мл
● CF3000: {cf3000:.0f} мл  
● Всего: {total_solvent:.0f} мл

Для {weight}г {manufacturer}'''
                
        except ValueError:
            self.result_label.text = "[color=#ff6b6b]Ошибка: введите число[/color]"
        except Exception as e:
            self.result_label.text = f"[color=#ff6b6b]Ошибка расчета[/color]"

    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Заголовок
        title = Label(
            text='[b]🎯 INK MIXER PRO[/b]\nGREIF: Packaging success together',
            markup=True,
            font_size='24sp',
            size_hint=(1, 0.3),
            color=get_color_from_hex("#22c55e")
        )
        main_layout.add_widget(title)
        
        # Поле ввода веса
        self.weight_input = TextInput(
            hint_text='Вес чернил (г)',
            multiline=False,
            input_filter='float',
            size_hint=(1, 0.15),
            font_size='20sp',
            background_color=get_color_from_hex("#334155"),
            foreground_color=get_color_from_hex("#f8fafc")
        )
        main_layout.add_widget(self.weight_input)
        
        # Выбор производителя
        self.manufacturer_spinner = Spinner(
            text='Санкемикалз',
            values=('Санкемикалз', 'Сико', 'Китай', 'Тампо Механика'),
            size_hint=(1, 0.15),
            background_color=get_color_from_hex("#334155"),
            color=get_color_from_hex("#f8fafc")
        )
        main_layout.add_widget(self.manufacturer_spinner)
        
        # Кнопка расчета
        calc_btn = Button(
            text='🚀 РАССЧИТАТЬ ПРОПОРЦИИ',
            size_hint=(1, 0.2),
            background_color=get_color_from_hex("#6366f1"),
            color=get_color_from_hex("#ffffff"),
            font_size='18sp',
            bold=True
        )
        calc_btn.bind(on_press=self.calculate)
        main_layout.add_widget(calc_btn)
        
        # Результат
        self.result_label = Label(
            text='Введите вес чернил для расчета',
            markup=True,
            font_size='18sp',
            size_hint=(1, 0.4)
        )
        main_layout.add_widget(self.result_label)
        
        return main_layout

if __name__ == '__main__':
    InkMixerPro().run()