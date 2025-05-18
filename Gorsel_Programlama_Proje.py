import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QMessageBox, QTabWidget, QListWidget, QRadioButton,
                             QHBoxLayout, QDialog, QTextEdit, QFrame, QSplitter, QGridLayout,)
from PyQt5.QtGui import  QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget

#DİKKAT: kullanıcı adı:ece  şifre:2222
# Ana tema renkleri ve stil tanımlamaları
ANA_TEMA = "#345f9b"  
ARA_RENK = "#4378c6"  
BG_COLOR = "#7c8dbf"  
YAZI_RENGİ = "#2c3e50"  
GİRİS_BUTONU= f"""
    QPushButton {{
        background-color: {ANA_TEMA};
        color: white;
        border-radius: 5px;
        padding: 8px;
        font-weight: bold;
    }}
    QPushButton:hover {{
        background-color: {ARA_RENK};
    }}
    QPushButton:pressed {{
        background-color: #1c6399;
    }}
"""

CİKİS_STİL = """
    QLineEdit {
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        padding: 8px;
        background-color: white;
    }
    QLineEdit:focus {
        border: 1px solid #3498db;
    }
"""

LIST_STYLE = """
    QListWidget {
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        padding: 5px;
        background-color: white;
    }
    QListWidget::item {
        padding: 8px;
        border-bottom: 1px solid #ecf0f1;
    }
    QListWidget::item:selected {
        background-color: #3498db;
        color: white;
    }
"""
TAB_STYLE = """
    QTabWidget::pane {
        border: 1px solid #bdc3c7;
        border-radius: 5px;
        background-color: white;
    }
    QTabBar::tab {
        background-color: #ecf0f1;
        padding: 10px 15px;
        margin-right: 2px;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
    }
    QTabBar::tab:selected {
        background-color: #7544e5;
        color: white;
        font-weight: bold;
    }
    QTabBar::tab:hover:!selected {
        background-color: #d0d0d0;
    }
"""
RADIO_STİLİ = """
    QRadioButton {
        padding: 5px;
        spacing: 5px;
    }
    QRadioButton::indicator {
        width: 15px;
        height: 15px;
    }
    QRadioButton::indicator:checked {
        background-color: #3498db;
        border: 2px solid white;
        border-radius: 8px;
    }
"""
# Kart çerçeve stili
STİL_2 = """
    QFrame {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1);
    }
"""

# Giriş ekranı sınıfı
class GirisEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Film & Dizi Takip Uygulaması - Giriş")
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet(f"background-color: {BG_COLOR};")

        #Başlık alanı
        self.logo_label = QLabel(" ✮࣪⋆✧♡Film & Dizi Takip Uygulaması♡✧⋆✮")
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #004587;
            margin: 20px;
        """)

        # Giriş kartı çerçevesi
        self.login_card = QFrame()
        self.login_card.setStyleSheet(STİL_2)
        
        # Kullanıcı adı giriş alanı
        self.label_user = QLabel("Kullanıcı Adı:")
        self.label_user.setStyleSheet("font-weight: bold; color: #55729b;")
        self.input_user = QLineEdit()
        self.input_user.setStyleSheet(CİKİS_STİL)
        self.input_user.setPlaceholderText("Kullanıcı adınızı girin")
        
        # Şifre giriş alanı
        self.label_pass = QLabel("Şifre:")
        self.label_pass.setStyleSheet("font-weight: bold; color: #55729b;")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass.setStyleSheet(CİKİS_STİL)
        self.input_pass.setPlaceholderText("Şifrenizi girin")
        
        # Giriş butonu
        self.login_button = QPushButton("Giriş Yap")
        self.login_button.setStyleSheet(GİRİS_BUTONU)
        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.setMinimumHeight(40)
        self.login_button.clicked.connect(self.check_login)
        
        # Kart düzeni
        card_layout = QVBoxLayout(self.login_card)
        card_layout.addWidget(self.label_user)
        card_layout.addWidget(self.input_user)
        card_layout.addWidget(self.label_pass)
        card_layout.addWidget(self.input_pass)
        card_layout.addWidget(self.login_button)
        card_layout.setContentsMargins(20, 20, 20, 20)
        card_layout.setSpacing(15)

        # Ana düzen
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.logo_label)
        main_layout.addWidget(self.login_card)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        self.setLayout(main_layout)

    # Kullanıcı adı ve şifre doğrulama
    def check_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        if username == "ece" and password == "2222":  # Kendi verdiğim bilgiler
            self.accept_login()  
        else:#hatalı giriş olursa
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Warning)
            error_box.setWindowTitle("Giriş Hatası")
            error_box.setText("Kullanıcı adı veya şifre hatalı!")
            error_box.setStyleSheet("QMessageBox {background-color: #f5f5f5;}")
            error_box.exec_()

    # giriş başarılıysa ana ekrana gidiyor
    def accept_login(self):
        self.close()  # giriş başarılıysa pencereyi kapatıyor
        self.main_screen() 

    def main_screen(self):
        self.main_window = AnaEkran(self)  # ana ekranı LoginScreenle bağlıyoruz
        self.main_window.show()

# ana ekran sınıfı
class AnaEkran(QWidget):
    def __init__(self, login_screen):
        super().__init__()
        self.login_screen = login_screen
        self.init_ui()
        self.watched_comments = {}  #yorumları tutmak için bir sözlük
        self.watched_items = []  #izlenen öğeleri saklamak için bir liste

    def init_ui(self):
        self.setWindowTitle("Film & Dizi Takip - Ana Ekran")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet(f"background-color: #7c8dbf;")
        ana_stil = QHBoxLayout()
        
        # sol panel (Menü kısmı
        sol_panel = QFrame()
        sol_panel.setStyleSheet("""
            background-color: #4846a0;
            border-radius: 10px;
            padding: 20px;
        """)
        sol_panel.setFixedWidth(250)
        
        #Menü başlığı
        self.app_title = QLabel("˚.⋆Menü⋆.˚")
        self.app_title.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            margin-bottom: 20px;
        """)
        self.app_title.setAlignment(Qt.AlignCenter)
        
        # Menü butonları
        self.btn_wishlist = QPushButton(" İstek Listesi        🗒️")
        self.btn_watched = QPushButton(" İzlediklerim         📽")
        self.btn_comment = QPushButton(" Yorum Yaz           🖊")
        self.btn_show_comment = QPushButton(" Yorum Göster     🔎")
        self.btn_settings = QPushButton(" Ayarlar                ⚙️")
        
        # Buton şeilleri ve butona basıldığı zaman oluşacak görüntü(tek bir yerde tanımlayıp bütün butonlar için uyguluyoruz)
        buton_stil = """
            QPushButton {
                background-color: transparent;
                color: white;
                text-align: left;
                padding: 12px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #2980b9;
            }
        """
        
        self.btn_wishlist.setStyleSheet(buton_stil)
        self.btn_watched.setStyleSheet(buton_stil)
        self.btn_comment.setStyleSheet(buton_stil)
        self.btn_show_comment.setStyleSheet(buton_stil)
        self.btn_settings.setStyleSheet(buton_stil)
        
        # Butonları sol panel içine yerleştirme
        left_taraf = QVBoxLayout(sol_panel)
        left_taraf.addWidget(self.app_title)
        left_taraf.addWidget(self.btn_wishlist)
        left_taraf.addWidget(self.btn_watched)
        left_taraf.addWidget(self.btn_comment)
        left_taraf.addWidget(self.btn_show_comment)
        left_taraf.addWidget(self.btn_settings)
        left_taraf.addStretch()
        
        # Sağ panel
        sag_panel = QFrame()
        sag_panel.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            padding: 20px;
        """)
        
        # üstte bulunan Film ve Dizi sekmeleri
        self.top_tabs = QTabWidget()
        self.top_tabs.setStyleSheet(TAB_STYLE)
        
        # Film ve Dizi Listeleri
        self.film_list = QListWidget()
        self.series_list = QListWidget()
        
        self.film_list.setStyleSheet(LIST_STYLE)
        self.series_list.setStyleSheet(LIST_STYLE)
        
        
        self.top_tabs.addTab(self.film_list, "Film")
        self.top_tabs.addTab(self.series_list, "Dizi")
        
        # ana menü başığı
        content_title = QLabel("Filmler & Diziler˙✧˖°🎥 ༘ ⋆｡🎞️˚")
        content_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #670087;
            margin-bottom: 10px;
        """)
        
        #sağ panel içeriğini düzenleme
        right_layout = QVBoxLayout(sag_panel)
        right_layout.addWidget(content_title)
        right_layout.addWidget(self.top_tabs)
        
        #ana düzene panel ekleme
        ana_stil.addWidget(sol_panel)
        ana_stil.addWidget(sag_panel)
        self.setLayout(ana_stil)

        # Butonlara tıklanınca işlemleri bağlama
        self.btn_wishlist.clicked.connect(self.open_wishlist)
        self.btn_watched.clicked.connect(self.open_watched)
        self.btn_comment.clicked.connect(self.open_comment)
        self.btn_show_comment.clicked.connect(self.show_comment)
        self.btn_settings.clicked.connect(self.open_settings)

    # istek listesi ekranını açma
    def open_wishlist(self):
        self.wishlist_window = İstekListesi()
        self.wishlist_window.show()

    # izlediklerim ekranını açma
    def open_watched(self):
        self.watched_window = izlediklerim(self.film_list, self.series_list, self.watched_items)
        self.watched_window.show()

    # kullanıcının yorum yazmasını sağlama
    def open_comment(self):
        selected_item = self.top_tabs.currentWidget().currentItem()
        if selected_item:
            item_name = selected_item.text()
            if item_name in self.watched_comments:
                self.show_comment(item_name)
            else:
                self.add_comment(item_name)
        else:
            QMessageBox.information(self, "Seçim Yapın", "Lütfen yorum yapmak istediğiniz film veya diziyi seçin.")

    # Kullanıcının yorumlarını gösterme
    def show_comment(self):
        yorum = self.top_tabs.currentWidget().currentItem()
        if yorum:
            item_name = yorum.text()
            if item_name in self.watched_comments:
                comment = self.watched_comments[item_name]
                
                message_box = QMessageBox(self)
                message_box.setWindowTitle(f"{item_name} Yorumu")
                message_box.setText(comment)
                message_box.setStyleSheet("""
                    QMessageBox {
                        background-color: white;
                    }
                    QMessageBox QLabel {
                        color: #2c3e50;
                        min-width: 300px;
                    }
                """)
                message_box.exec_()
            else:
                QMessageBox.information(self, "Yorum Bulunamadı", f"{item_name} için henüz bir yorum yazılmamış.")
        else:
            QMessageBox.information(self, "Seçim Yapın", "Lütfen yorum görmek için bir film veya dizi seçin.")

    #yeni yorum ekleme penceresini açma
    def add_comment(self, item_name):
        dialog = YorumYaz(item_name, self)
        dialog.exec_()

    # ayarlar ekranını açma
    def open_settings(self):
        self.settings_window = Ayarlar(self)
        self.settings_window.show()

#istek listesi classı
class İstekListesi(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("İstek Listesi")
        self.setGeometry(150, 150, 500, 500)
        self.setStyleSheet(f"background-color: {BG_COLOR};")

        ana_tasarim = QFrame()
        ana_tasarim.setStyleSheet(STİL_2)
        
        # Başlık
        self.label_title = QLabel("İstek Listesi🎞️✨")
        self.label_title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
        """)
        self.label_title.setAlignment(Qt.AlignCenter)
        
        # Alt başlık
        self.label_subtitle = QLabel("İzlemek istediğiniz film ve dizileri buraya ekleyebilirsiniz🎥")
        self.label_subtitle.setStyleSheet("color: #7f8c8d; margin-bottom: 20px;")
        self.label_subtitle.setAlignment(Qt.AlignCenter)

        # Film/Dizi Ekleme Alanı
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Film/Dizi Adı Girin")
        self.input_name.setStyleSheet(CİKİS_STİL)

        # Film ve Dizi için yuvarlak seçim kutuları((radio butonlar)
        radio_buton = QFrame()
        radio_buton.setStyleSheet("background-color: transparent;")
        
        self.radio_film = QRadioButton("Film")
        self.radio_series = QRadioButton("Dizi")
        self.radio_film.setChecked(True)
        
        self.radio_film.setStyleSheet(RADIO_STİLİ)
        self.radio_series.setStyleSheet(RADIO_STİLİ)

        # Ekle ve Çıkar Butonları
        self.btn_add = QPushButton("Ekle")
        self.btn_remove = QPushButton("Çıkar")
        
        self.btn_add.setStyleSheet(GİRİS_BUTONU)
        self.btn_remove.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        self.btn_add.setCursor(Qt.PointingHandCursor)
        self.btn_remove.setCursor(Qt.PointingHandCursor)

        # Film/Dizi Listesi
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet(LIST_STYLE)
        self.list_widget.setMinimumHeight(250)

        radio_layout = QHBoxLayout(radio_buton)
        radio_layout.addWidget(self.radio_film)
        radio_layout.addWidget(self.radio_series)
        radio_layout.setContentsMargins(0, 0, 0, 0)

        add_frame = QFrame()
        add_frame.setStyleSheet("""
            background-color: #ecf0f1;
            border-radius: 8px;
            padding: 15px;
        """)
        
        add_layout = QVBoxLayout(add_frame)
        add_layout.addWidget(QLabel("Yeni Ekle:"))
        add_layout.addWidget(self.input_name)
        add_layout.addWidget(radio_buton)
        add_layout.addWidget(self.btn_add)
        
        # Liste çerçevesi
        list_frame = QFrame()
        list_frame.setStyleSheet("""
            background-color: #ecf0f1;
            border-radius: 8px;
            padding: 15px;
        """)
        
        list_layout = QVBoxLayout(list_frame)
        list_layout.addWidget(QLabel("İzleme Listesi:"))
        list_layout.addWidget(self.list_widget)
        list_layout.addWidget(self.btn_remove)

        # Kart içi düzen
        card_layout = QVBoxLayout(ana_tasarim)
        card_layout.addWidget(self.label_title)
        card_layout.addWidget(self.label_subtitle)
        card_layout.addWidget(add_frame)
        card_layout.addWidget(list_frame)

        # Ana düzen
        main_layout = QVBoxLayout()
        main_layout.addWidget(ana_tasarim)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        self.setLayout(main_layout)

        #butonlara tıklanınca işlemleri bağlama
        self.btn_add.clicked.connect(self.add_item)
        self.btn_remove.clicked.connect(self.remove_item)

    def add_item(self):
        item_name = self.input_name.text().strip()
        if not item_name:
            QMessageBox.warning(self, "Hata", "Lütfen bir isim girin!")
            return

        #Film veya dizi olduğunu belirten metni ekliyoruz
        if self.radio_film.isChecked():
            item_name = f"Film: {item_name}"
        elif self.radio_series.isChecked():
            item_name = f"Dizi: {item_name}"

        # Film/Dizi listesine ekliyoruz
        self.list_widget.addItem(item_name)
        self.input_name.clear()

        #ekleme işlemi renk değişimi
        self.list_widget.item(self.list_widget.count() - 1).setBackground(QColor("#dff0d8"))

    def remove_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            # silme onayı kutucuğu
            confirm = QMessageBox()
            confirm.setIcon(QMessageBox.Question)
            confirm.setWindowTitle("Onay")
            confirm.setText(f"{selected_item.text()} öğesini silmek istediğinize emin misiniz?")
            confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm.setDefaultButton(QMessageBox.No)
            confirm.setStyleSheet("QMessageBox {background-color: #f5f5f5;}")
            
            if confirm.exec_() == QMessageBox.Yes:
                self.list_widget.takeItem(self.list_widget.row(selected_item))
        else:
            QMessageBox.information(self, "Seçim Yapın", "Lütfen çıkarmak istediğiniz bir öğe seçin.")


class izlediklerim(QWidget):
    def veritabani_baglan(self):
        self.conn = sqlite3.connect("veritabani.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS izlediklerim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT,
            yayin_tarihi TEXT,
            yonetmen TEXT,
            puan TEXT
        )
        """)
        self.conn.commit()
        
    def __init__(self, film_list, series_list, watched_items):
        super().__init__()
        self.setWindowTitle("İzlediklerim")
        self.film_list = film_list
        self.series_list = series_list
        self.watched_items = watched_items
        self.watched_details = {}  # Film/dizi detaylarını saklamak için sözlük
        
        # Veritabanı bağlantısını başlat
        self.veritabani_baglan()
        
        # UI'yı oluştur
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("İzlediklerim")
        self.setGeometry(150, 150, 800, 650)
        self.setStyleSheet(f"background-color: {BG_COLOR};")

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        main_card = QFrame()
        main_card.setStyleSheet(STİL_2)
        
        # başlık
        self.label_title = QLabel("İzlediklerim🍿🎟️🎬")
        self.label_title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
        """)
        self.label_title.setAlignment(Qt.AlignCenter)
        
        # Alt başlık
        self.label_subtitle = QLabel("İzlediğiniz film ve dizileri ekleyin🎥🌃")
        self.label_subtitle.setStyleSheet("color: #7f8c8d; margin-bottom: 20px;")
        self.label_subtitle.setAlignment(Qt.AlignCenter)

        # Ana içerik düzeni için splitter (ayırıcı) oluşturma
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.setStyleSheet("QSplitter::handle { background-color: #d0d0d0; width: 2px; }")
        
        # Sol panel - Form alanı
        left_panel = QFrame()
        left_panel.setStyleSheet("""
            background-color: #ecf0f1;
            border-radius: 8px;
            padding: 15px;
        """)
        
        form_layout = QGridLayout(left_panel)
        
        # Form başlığı
        form_title = QLabel("Film/Dizi Ekle veya Düzenle")
        form_title.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #345f9b;
            margin-bottom: 10px;
        """)
        form_layout.addWidget(form_title, 0, 0, 1, 2)
        
        # Film/Dizi Adı
        self.label_name = QLabel("Film/Dizi Adı:")
        self.label_name.setStyleSheet("font-weight: bold; color: #55729b;")
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Film/Dizi Adı Girin")
        self.input_name.setStyleSheet(CİKİS_STİL)
        
        # Yönetmen ekleme
        self.label_director = QLabel("Yönetmen:")
        self.label_director.setStyleSheet("font-weight: bold; color: #55729b;")
        self.input_director = QLineEdit()
        self.input_director.setPlaceholderText("Yönetmen Adı")
        self.input_director.setStyleSheet(CİKİS_STİL)
        
        # Yayın Tarihi ekleme
        self.label_release_date = QLabel("Yayın Tarihi:")
        self.label_release_date.setStyleSheet("font-weight: bold; color: #55729b;")
        self.input_release_date = QLineEdit()
        self.input_release_date.setPlaceholderText("YYYY-AA-GG")
        self.input_release_date.setStyleSheet(CİKİS_STİL)
        
        # Puan ekleme
        self.label_rating = QLabel("Puanım:")
        self.label_rating.setStyleSheet("font-weight: bold; color: #55729b;")
        self.input_rating = QLineEdit()
        self.input_rating.setPlaceholderText("1-10 arası")
        self.input_rating.setStyleSheet(CİKİS_STİL)

        # Film ve Dizi için seçim kutusu
        radio_frame = QFrame()
        radio_frame.setStyleSheet("background-color: transparent;")
        
        self.radio_film = QRadioButton("Film")
        self.radio_series = QRadioButton("Dizi")
        self.radio_film.setChecked(True)
        
        self.radio_film.setStyleSheet(RADIO_STİLİ)
        self.radio_series.setStyleSheet(RADIO_STİLİ)
        
        radio_layout = QHBoxLayout(radio_frame)
        radio_layout.addWidget(self.radio_film)
        radio_layout.addWidget(self.radio_series)
        radio_layout.setContentsMargins(0, 0, 0, 0)

        # Form düzenine alanları ekle
        form_layout.addWidget(self.label_name, 1, 0)
        form_layout.addWidget(self.input_name, 1, 1)
        form_layout.addWidget(self.label_director, 2, 0)
        form_layout.addWidget(self.input_director, 2, 1)
        form_layout.addWidget(self.label_release_date, 3, 0)
        form_layout.addWidget(self.input_release_date, 3, 1)
        form_layout.addWidget(self.label_rating, 4, 0)
        form_layout.addWidget(self.input_rating, 4, 1)
        form_layout.addWidget(QLabel("Tür:"), 5, 0)
        form_layout.addWidget(radio_frame, 5, 1)

        # Kaydet ve Sil Butonları
        self.btn_save = QPushButton("Kaydet")
        self.btn_delete = QPushButton("Seçileni Sil")
        self.btn_edit = QPushButton("Seçileni Düzenle")
        
        self.btn_save.setStyleSheet(GİRİS_BUTONU)
        self.btn_delete.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        self.btn_edit.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
        """)
        
        self.btn_save.setCursor(Qt.PointingHandCursor)
        self.btn_delete.setCursor(Qt.PointingHandCursor)
        self.btn_edit.setCursor(Qt.PointingHandCursor)
        
        # Buton düzeni
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.btn_save)
        button_layout.addWidget(self.btn_edit)
        button_layout.addWidget(self.btn_delete)
        self.btn_veritabani = QPushButton("Veri Tabanı")
        self.btn_veritabani.setStyleSheet(GİRİS_BUTONU)
        self.btn_veritabani.setCursor(Qt.PointingHandCursor)
        button_layout.addWidget(self.btn_veritabani)
        self.btn_veritabani.clicked.connect(self.veritabani_penceresini_ac)

        form_layout.addLayout(button_layout, 6, 0, 1, 2)
        
        # Sağ panel - Liste ve detay alanı
        right_panel = QFrame()
        right_panel.setStyleSheet("""
            background-color: #ecf0f1;
            border-radius: 8px;
            padding: 15px;
        """)
        
        right_layout = QVBoxLayout(right_panel)
        
        # Liste başlığı
        list_title = QLabel("İzlenen Film ve Dizilerim")
        list_title.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #345f9b;
            margin-bottom: 10px;
        """)
        right_layout.addWidget(list_title)
        
        # Liste ve detay alanını ayıran bir splitter
        list_detail_splitter = QSplitter(Qt.Vertical)
        list_detail_splitter.setStyleSheet("QSplitter::handle { background-color: #d0d0d0; height: 2px; }")
        
        # İzlenenler listesi
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet(LIST_STYLE + """
            QListWidget::item {
                padding: 12px;
                font-size: 14px;
            }
            QListWidget::item:selected {
                background-color: #345f9b;
                color: white;
            }
        """)
        self.list_widget.setMinimumHeight(250)
        
        detail_frame = QFrame()
        detail_frame.setStyleSheet("""
            background-color: white;
            border-radius: 8px;
            padding: 15px;
        """)
        detail_layout = QVBoxLayout(detail_frame)
        
        # Detay başlığı
        self.detail_label = QLabel("Seçilen İçerik Detayları")
        self.detail_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold; 
            color: #345f9b;
            margin-bottom: 10px;
        """)
        self.detail_text = QTextEdit()
        self.detail_text.setReadOnly(True)
        self.detail_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 15px;
                background-color: white;
                font-size: 14px;
                line-height: 1.5;
            }
        """)
        self.detail_text.setMinimumHeight(180)  # Yükseklik arttı
        
        detail_layout.addWidget(self.detail_label)
        detail_layout.addWidget(self.detail_text)
        
        list_detail_splitter.addWidget(self.list_widget)
        list_detail_splitter.addWidget(detail_frame)
        list_detail_splitter.setSizes([400, 250])  # başlangıç boyutları
        
        right_layout.addWidget(list_detail_splitter)
        
        main_splitter.addWidget(left_panel)
        main_splitter.addWidget(right_panel)
        main_splitter.setSizes([300, 500])  #sol ve sağ panel başlangıç boyutları
        
        # var olan izlenen öğeleri listeye ekleyelim
        for item in self.watched_items:
            self.list_widget.addItem(item)
        #kart içi düzen
        card_layout = QVBoxLayout(main_card)
        card_layout.addWidget(self.label_title)
        card_layout.addWidget(self.label_subtitle)
        card_layout.addWidget(main_splitter)

        # Ana düzen
        main_layout.addWidget(main_card)
        
        # Bu tek bir layout atamasıdır!
        self.setLayout(main_layout)

        # Butonlara tıklanınca işlemleri bağlama
        self.btn_save.clicked.connect(self.save_item)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_edit.clicked.connect(self.edit_item)
        self.list_widget.itemClicked.connect(self.show_details)
    
    def veritabani_penceresini_ac(self):
        self.vt_pencere = VeritabaniPenceresi()
        self.vt_pencere.show()

    def save_item(self):
        item_name = self.input_name.text().strip()
        director = self.input_director.text().strip()
        release_date = self.input_release_date.text().strip()
        rating = self.input_rating.text().strip()

        if not item_name:
            QMessageBox.warning(self, "Hata", "Lütfen bir isim girin!")
            return

        try:
            if rating:
                rating_value = float(rating)
                if rating_value < 1 or rating_value > 10:
                    QMessageBox.warning(self, "Hata", "Puan 1-10 arasında olmalıdır!")
                    return
        except ValueError:
            QMessageBox.warning(self, "Hata", "Lütfen geçerli bir puan girin (1-10 arası)!")
            return

        if self.radio_film.isChecked():
            item_name_full = f"Film: {item_name}"
        else:
            item_name_full = f"Dizi: {item_name}"

        if item_name_full not in self.watched_items:
            self.watched_items.append(item_name_full)

        self.watched_details[item_name_full] = {
            "director": director,
            "release_date": release_date,
            "rating": rating
        }

        if self.radio_film.isChecked():
            if not self.film_list.findItems(item_name_full, Qt.MatchExactly):
                self.film_list.addItem(item_name_full)
        else:
            if not self.series_list.findItems(item_name_full, Qt.MatchExactly):
                self.series_list.addItem(item_name_full)

        if not self.list_widget.findItems(item_name_full, Qt.MatchExactly):
            self.list_widget.addItem(item_name_full)

    # ✅ BURASI: Veritabanına ekleme
        try:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO izlediklerim (ad, yayin_tarihi, yonetmen, puan)
                VALUES (?, ?, ?, ?)
            """, (item_name, release_date, director, rating))
            conn.commit()
            conn.close()
        except Exception as e:
            QMessageBox.warning(self, "Veritabanı Hatası", str(e))

        self.clear_form()
        QMessageBox.information(self, "Başarılı", f"{item_name_full} başarıyla kaydedildi.")

    def clear_form(self):
        # Tüm form alanlarını temizle
        self.input_name.clear()
        self.input_director.clear()
        self.input_release_date.clear()
        self.input_rating.clear()
        self.radio_film.setChecked(True)

    def delete_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            item_name = selected_item.text()
            # Silme onayı soralım
            confirm = QMessageBox()
            confirm.setIcon(QMessageBox.Question)
            confirm.setWindowTitle("Onay")
            confirm.setText(f"{item_name} öğesini silmek istediğinize emin misiniz?")
            confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            confirm.setDefaultButton(QMessageBox.No)
            confirm.setStyleSheet("QMessageBox {background-color: #f5f5f5;}")
            
            if confirm.exec_() == QMessageBox.Yes:
                # İzlenen öğeler listesinden kaldıralım
                if item_name in self.watched_items:
                    self.watched_items.remove(item_name)
                
                # Detay bilgilerini de silelim
                if item_name in self.watched_details:
                    del self.watched_details[item_name]
                
                # Ana ekrandaki listelerden de kaldıralım
                if item_name.startswith("Film:"):
                    items = self.film_list.findItems(item_name, Qt.MatchExactly)
                    if items:
                        self.film_list.takeItem(self.film_list.row(items[0]))
                elif item_name.startswith("Dizi:"):
                    items = self.series_list.findItems(item_name, Qt.MatchExactly)
                    if items:
                        self.series_list.takeItem(self.series_list.row(items[0]))
                
                # Listeden kaldıralım
                self.list_widget.takeItem(self.list_widget.row(selected_item))
                
                # Detay metnini temizleyelim
                self.detail_text.clear()
        else:
            QMessageBox.information(self, "Seçim Yapın", "Lütfen silmek istediğiniz bir öğe seçin.")

    def edit_item(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            item_name = selected_item.text()
            # Mevcut bilgileri forma yükle
            if item_name in self.watched_details:
                details = self.watched_details[item_name]
                
                # Film/Dizi tipini ayarla
                if item_name.startswith("Film:"):
                    self.radio_film.setChecked(True)
                    self.input_name.setText(item_name[6:].strip())  # "Film: " kısmını kaldır
                elif item_name.startswith("Dizi:"):
                    self.radio_series.setChecked(True)
                    self.input_name.setText(item_name[6:].strip())  # "Dizi: " kısmını kaldır
                
                # Diğer detayları yükle
                self.input_director.setText(details.get("director", ""))
                self.input_release_date.setText(details.get("release_date", ""))
                self.input_rating.setText(details.get("rating", ""))
                
                # Öğeyi silip, düzenlenmiş yeni versiyonu kaydetme mesajı
                QMessageBox.information(self, "Düzenleme", 
                    "Bilgileri düzenlendikten sonra 'Kaydet' butonuna basın. Eski kayıt güncellenecektir.")
                
                # Eski öğeyi listeden kaldıralım
                self.list_widget.takeItem(self.list_widget.row(selected_item))
                
                # İzlenen öğeler listesinden de kaldıralım (yeni kayıtla değiştirilecek)
                if item_name in self.watched_items:
                    self.watched_items.remove(item_name)
                
                # Ana ekrandaki listelerden de kaldıralım
                if item_name.startswith("Film:"):
                    items = self.film_list.findItems(item_name, Qt.MatchExactly)
                    if items:
                        self.film_list.takeItem(self.film_list.row(items[0]))
                elif item_name.startswith("Dizi:"):
                    items = self.series_list.findItems(item_name, Qt.MatchExactly)
                    if items:
                        self.series_list.takeItem(self.series_list.row(items[0]))
            else:
                QMessageBox.warning(self, "Hata", "Bu öğe için detay bilgisi bulunamadı.")
        else:
            QMessageBox.information(self, "Seçim Yapın", "Lütfen düzenlemek istediğiniz bir öğe seçin.")

    def show_details(self, item):
        # Seçilen öğenin detaylarını göster
        item_name = item.text()
        if item_name in self.watched_details:
            details = self.watched_details[item_name]
            
            # Daha güzel bir HTML formatı ile detayları gösterelim
            html_content = f"""
            <div style="font-family: Arial, sans-serif; padding: 10px;">
                <h2 style="color: #345f9b; margin-bottom: 15px;">{item_name}</h2>
                <p><strong style="color: #2c3e50;">Yönetmen:</strong> {details.get('director', 'Belirtilmemiş')}</p>
                <p><strong style="color: #2c3e50;">Yayın Tarihi:</strong> {details.get('release_date', 'Belirtilmemiş')}</p>
                <p><strong style="color: #2c3e50;">Puanım:</strong> <span style="font-size: 16px; color: #e67e22; font-weight: bold;">{details.get('rating', 'Belirtilmemiş')}/10</span></p>
            </div>
            """
            self.detail_text.setHtml(html_content)
        else:
            self.detail_text.setHtml("""
            <div style="font-family: Arial, sans-serif; padding: 10px;">
                <p style="color: #7f8c8d; font-style: italic;">Bu içerik için detay bilgisi bulunmuyor.</p>
                <p>İçerik eklemek veya düzenlemek için sol taraftaki formu kullanabilirsiniz.</p>
            </div>
            """)
            
    def ekleButonunaTikla(self):
        print("Ekle butonuna tıklandı")  # ← TEST satırı
        ad = self.lineEdit.text()
        yayin_tarihi = self.dateEdit.date().toString("yyyy-MM-dd")
        yonetmen = self.lineEdit_3.text()
        puan = self.lineEdit_2.text()

        if ad and yonetmen and puan:
            try:
                self.cursor.execute("""
                    INSERT INTO izlediklerim (ad, yayin_tarihi, yonetmen, puan)
                    VALUES (?, ?, ?, ?)
                """, (ad, yayin_tarihi, yonetmen, puan))
                self.conn.commit()
                print(f"Veritabanına eklendi: {ad}, {yayin_tarihi}, {yonetmen}, {puan}")
                
                # Formu temizle
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()

                # Verileri yeniden yükle
                self.verileri_yukle()
                
                QMessageBox.information(self, "Başarılı", "Kayıt başarıyla eklendi.")
            except sqlite3.Error as e:
                print(f"SQLite hatası: {e}")
                QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {e}")
        else:
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen tüm alanları doldurun!")
        

class YorumYaz(QDialog):
    def __init__(self, item_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{item_name} için Yorum Yaz")
        self.setGeometry(200, 200, 500, 400)
        self.setStyleSheet(f"background-color: {BG_COLOR};")
        self.parent = parent
        self.item_name = item_name
        self.init_ui()

    def init_ui(self):
        # Ana kart çerçevesi
        main_card = QFrame()
        main_card.setStyleSheet(STİL_2)
        
        # Başlık
        self.label_title = QLabel(f"{self.item_name} için Yorum")
        self.label_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
        """)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.label_comment = QLabel("Düşüncelerinizi buraya yazın:")
        self.label_comment.setStyleSheet("color: #2c3e50; font-weight: bold;")
        
        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("""
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 10px;
                background-color: white;
            }
            QTextEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        self.text_edit.setMinimumHeight(200)

        # Butonlar
        button_layout = QHBoxLayout()
        
        self.btn_save = QPushButton("Kaydet")
        self.btn_save.clicked.connect(self.save_comment)
        self.btn_save.setStyleSheet(GİRİS_BUTONU)
        self.btn_save.setCursor(Qt.PointingHandCursor)
        
        self.btn_cancel = QPushButton("İptal")
        self.btn_cancel.clicked.connect(self.close)
        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        self.btn_cancel.setCursor(Qt.PointingHandCursor)
        
        button_layout.addWidget(self.btn_save)
        button_layout.addWidget(self.btn_cancel)

        # Kart içi düzen
        card_layout = QVBoxLayout(main_card)
        card_layout.addWidget(self.label_title)
        card_layout.addWidget(self.label_comment)
        card_layout.addWidget(self.text_edit)
        card_layout.addLayout(button_layout)
        card_layout.setContentsMargins(20, 20, 20, 20)

        # Ana düzen
        main_layout = QVBoxLayout()
        main_layout.addWidget(main_card)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        self.setLayout(main_layout)

    def save_comment(self):
        comment = self.text_edit.toPlainText()
        if not comment.strip():
            QMessageBox.warning(self, "Uyarı", "Lütfen bir yorum yazın!")
            return
            
        self.parent.watched_comments[self.item_name] = comment
        
        # Kayıt başarılı mesajı
        QMessageBox.information(self, "Başarılı", f"{self.item_name} için yorumunuz kaydedilmiştir.")
        self.close()

# Ayarlar ekranı sınıfı
import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QMessageBox, QTabWidget, QListWidget, QRadioButton,
                             QHBoxLayout, QDialog, QTextEdit, QFrame, QSplitter, QGridLayout,
                             QListWidgetItem, QScrollArea)
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette, QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateEdit
from PyQt5.QtCore import QDate

# Ayarlar ekranı sınıfı
class Ayarlar(QWidget):
    def __init__(self, main_screen):
        super().__init__()
        self.main_screen = main_screen
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ayarlar")
        self.setGeometry(200, 200, 450, 500)
        self.setStyleSheet(f"background-color: #ffffff;")

        main_card = QFrame()
        main_card.setStyleSheet("background-color: #f0f0f0; border-radius: 8px; padding: 15px;")

        self.label_title = QLabel("Uygulama Ayarları")
        self.label_title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            padding: 10px;
        """)
        self.label_title.setAlignment(Qt.AlignCenter)

        button_style = """
            QPushButton {
                background-color: #5061fc;
                color: white;
                border-radius: 5px;
                padding: 12px;
                font-weight: bold;
                margin-top: 20px;
                min-height: 45px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #160d54;
            }
        """

        self.btn_change_theme = QPushButton("Yazı Rengi Değiştir")
        self.btn_change_theme.setCursor(Qt.PointingHandCursor)
        self.btn_change_theme.setStyleSheet(button_style)
        self.btn_change_theme.clicked.connect(self.temayi_degistir)

        self.btn_change_language = QPushButton("Dil Değiştir")
        self.btn_change_language.setCursor(Qt.PointingHandCursor)
        self.btn_change_language.setStyleSheet(button_style)
        self.btn_change_language.clicked.connect(self.change_language)

        self.btn_change_password = QPushButton("Şifre Değiştir")
        self.btn_change_password.setCursor(Qt.PointingHandCursor)
        self.btn_change_password.setStyleSheet(button_style)
        self.btn_change_password.clicked.connect(self.change_password)

        self.btn_logout = QPushButton("Çıkış Yap")
        self.btn_logout.setCursor(Qt.PointingHandCursor)
        self.btn_logout.setStyleSheet(button_style)
        self.btn_logout.clicked.connect(self.logout)

        settings_grid = QGridLayout()
        settings_grid.addWidget(self.btn_change_theme, 0, 0, 1, 2, Qt.AlignCenter)
        settings_grid.addWidget(self.btn_change_language, 1, 0, 1, 2, Qt.AlignCenter)
        settings_grid.addWidget(self.btn_change_password, 2, 0, 1, 2, Qt.AlignCenter)
        settings_grid.setVerticalSpacing(20)

        settings_frame = QFrame()
        settings_frame.setStyleSheet("""
            background-color: #a8ccff;
            border-radius: 8px;
            padding: 20px;
        """)
        settings_frame.setLayout(settings_grid)

        card_layout = QVBoxLayout(main_card)
        card_layout.addWidget(self.label_title)
        card_layout.addWidget(settings_frame)
        card_layout.addWidget(self.btn_logout, 0, Qt.AlignCenter)
        card_layout.addStretch()
        card_layout.setContentsMargins(20, 20, 20, 20)

        main_layout = QVBoxLayout()
        main_layout.addWidget(main_card)
        main_layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(main_layout)
    def temayi_degistir(self):
    # Yeni tema rengi
        yeni_tema_rengi = "#2596be"
        yeni_yazi_rengi = "#1693bc"

    # Ana pencere ve alt elemanlara uygulanacak stil
        yeni_stil = f"""
        QWidget {{
            background-color: {yeni_tema_rengi};
            color: {yeni_yazi_rengi};
        }}
        QPushButton {{
            background-color: #9fb6ce;
            color: #80adbc;
            border-radius: 5px;
            padding: 8px;
        }}
        QPushButton:hover {{
            background-color: #155d9d;
        }}
        QLabel {{
            color: {yeni_yazi_rengi};
        }}
    """
    
        # Uygulamanın stilini değiştir
        QApplication.instance().setStyleSheet(yeni_stil)


    def change_language(self):
        QMessageBox.information(self, "Dil Değiştir", "Uygulamamızda şimdilik tek dil seçeneği mevcuttur. Güncellemelerimizi takip etmeyi unutmayın..")

    def change_password(self):
        from PyQt5.QtWidgets import QInputDialog

        mevcut_sifre = "2222"

    # Eski şifreyi al
        eski, ok1 = QInputDialog.getText(self, "Mevcut Şifre", "Eski şifrenizi girin:", QLineEdit.Password)
        if not ok1 or eski != mevcut_sifre:
            QMessageBox.warning(self, "Hatalı", "Mevcut şifre yanlış!")
            return

    # Yeni şifreyi al
        yeni, ok2 = QInputDialog.getText(self, "Yeni Şifre", "Yeni şifre girin:", QLineEdit.Password)
        if not ok2 or not yeni:
            QMessageBox.warning(self, "Hatalı", "Yeni şifre boş olamaz!")
            return

    # Yeni şifre tekrar
        tekrar, ok3 = QInputDialog.getText(self, "Yeni Şifre Tekrar", "Yeni şifreyi tekrar girin:", QLineEdit.Password)
        if not ok3 or yeni != tekrar:
            QMessageBox.warning(self, "Hatalı", "Şifreler uyuşmuyor!")
            return

    # Şifre değişti mesajı
        QMessageBox.information(self, "Başarılı", "Şifreniz başarıyla değiştirildi.")


    def logout(self):
        confirm = QMessageBox()
        confirm.setIcon(QMessageBox.Question)
        confirm.setWindowTitle("Çıkış Yap")
        confirm.setText("Çıkış yapmak istediğinize emin misiniz?")
        confirm.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm.setDefaultButton(QMessageBox.No)
        confirm.setStyleSheet("QMessageBox {background-color: white;}")

        if confirm.exec_() == QMessageBox.Yes:
            self.main_screen.close()
            self.close()
            self.open_login_screen()
        else:
            self.close()
            self.main_screen.show()

    def open_login_screen(self):
        self.login_screen = GirisEkrani()
        self.login_screen.show()

class VeritabaniPenceresi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Veri Tabanı Kayıtları")
        self.setGeometry(300, 300, 600, 400)
        self.setStyleSheet("background-color: #ecf0f1;")

        self.conn = sqlite3.connect("veritabani.db")
        self.cursor = self.conn.cursor()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Ad", "Yayın Tarihi", "Yönetmen", "Puan"])

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.verileri_yukle()

    def verileri_yukle(self):
        self.cursor.execute("SELECT ad, yayin_tarihi, yonetmen, puan FROM izlediklerim")
        veriler = self.cursor.fetchall()

        self.table.setRowCount(len(veriler))
        for i, satir in enumerate(veriler):
            for j, veri in enumerate(satir):
                self.table.setItem(i, j, QTableWidgetItem(str(veri)))
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_screen =GirisEkrani()
    login_screen.show()
    sys.exit(app.exec_())
    
