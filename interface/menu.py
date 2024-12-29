import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit
)
from PyQt6.QtGui import QFont, QColor, QPalette, QCursor
from PyQt6.QtCore import Qt


from ParsingScripts.parsing_emulator import Parser


class OzonStyleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ozon Style App")
        self.setFixedSize(800, 600)  # Пропорции 4:3

        self.setup_ui()

    def setup_ui(self):
        # Настраиваем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной лейаут
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Заголовок
        title_label = QLabel("Добро пожаловать в Ozon Style App")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Поле ввода категории товаров
        input_label = QLabel("Введите категорию товаров:")
        input_label.setFont(QFont("Arial", 14))
        layout.addWidget(input_label)

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setPlaceholderText("Например, электроника")
        layout.addWidget(self.input_field)

        # Кнопка подтверждения
        submit_button = QPushButton("Добавить категорию")
        submit_button.setFont(QFont("Arial", 14))
        submit_button.clicked.connect(self.on_submit)
        layout.addWidget(submit_button)

        # Поле для вывода результата
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        # Поле для вывода ссылок
        self.link_output = QTextEdit()
        self.link_output.setFont(QFont("Arial", 12))
        self.link_output.setReadOnly(True)
        layout.addWidget(self.link_output)

        # Применение Ozon-стиля
        self.apply_style()

    def apply_style(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#F6F9FC"))  # Светло-голубой фон
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#002B5C"))  # Темно-синий текст
        self.setPalette(palette)

        self.setStyleSheet(
            "QLabel { color: #002B5C; }"
            "QLineEdit { border: 2px solid #005B96; border-radius: 5px; padding: 5px; }"
            "QPushButton { background-color: #005B96; color: white; border-radius: 5px; padding: 10px; }"
            "QPushButton:hover { background-color: #0078D7; }"
            "QTextEdit { border: 2px solid #005B96; border-radius: 5px; padding: 5px; background-color: #FFFFFF; }"
        )

    def on_submit(self):
        category = self.input_field.text().strip()
        if category:
            self.result_label.setText(f"Категория \"{category}\" добавлена!")
            self.display_links(category)
        else:
            self.result_label.setText("Пожалуйста, введите категорию.")

    def simulate_loading(self):
        # Меняем курсор на "загрузка"
        QApplication.setOverrideCursor(QCursor(Qt.CursorShape.WaitCursor))


    def end_loading(self):
        # Возвращаем обычный курсор
        QApplication.restoreOverrideCursor()

    def display_links(self, category):
        print("YES")
        self.simulate_loading()
        slow = Parser(category)
        links: list = slow.products
        self.link_output.clear()
        self.link_output.append("Сгенерированные ссылки:")
        for link in links:
            self.link_output.append(f"<span style=\"color: black;\">{category}</span>: <a href=\"{link}\" style=\"color: #005B96;\">{link}</a>\n\n")
        print("READY")
        self.end_loading()


def open_app():
    app = QApplication(sys.argv)
    window = OzonStyleApp()
    window.show()
    sys.exit(app.exec())

