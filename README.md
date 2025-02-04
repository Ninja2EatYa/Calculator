# 🧮 Калькулятор на Python (Tkinter)

Простой графический калькулятор, написанный на Python с использованием Tkinter.

## 🚀 Возможности:
✔️ Базовые арифметические операции (+, -, *, /)  
✔️ Поддержка процентов (%)  
✔️ Функция памяти (MR+ / MR=)  
✔️ Ограничение длины чисел (до 13 символов)  
✔️ Автоматический переход в экспоненциальный формат для больших чисел  
✔️ Графический интерфейс (Tkinter)

---

## 📥 Установка и запуск

### 🔹 1. Запуск из исходного кода (Python)
Убедитесь, что у вас установлен Python 3.9+.

1. **Скачайте код**:
   ```bash
   git clone https://github.com/Ninja2EatYa/Calculator
   cd calculator
   ```
2. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Запустите калькулятор**:
   ```bash
   python Calculator_3_0.py
   ```
### 🔹 2. Как создать .exe (Windows)
Если хотите запустить калькулятор без Python, можно создать .exe.

1. **Установите pyinstaller**:
   ```bash
   pip install pyinstaller
   ```
2. **Создайте .exe**:
   ```bash
   pyinstaller --onefile --windowed Calculator_3.0.py
   ```
3. **Готовый .exe файл появится в dist/Calculator_3.0.exe.**

## 📌 Теперь можно запускать Calculator_3.0.exe без установки Python!

### 🔹 3. Как создать .app (macOS)
На macOS можно создать приложение .app:

1. **Установите pyinstaller**:
   ```bash
   pip install pyinstaller
   ```
2. **Соберите .app**:
```bash
pyinstaller --onefile --windowed --name Calculator Calculator_3.0.py
```
3. **Приложение появится в dist/Calculator.app.**

## 📌 Теперь можно запускать Calculator_3.0.app как обычное приложение!

# 🛠 Структура проекта
```bash
calculator/
│── Calculator_3.0.py  # Основной код калькулятора
│── README.md          # Этот файл
│── requirements.txt   # Зависимости (если есть)
│── .gitignore         # Игнорируемые файлы
└── dist/              # Сюда сохраняется скомпилированный `.exe` или `.app`
```
## 📌 Автор: Ninja2EatYa
