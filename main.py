import os
import sys
import requests

from geocoder import *
from search_organization import *
from distance import *

from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QButtonGroup
from PyQt5.QtCore import Qt

from ui_file import Ui_MainWindow


class YandexMap(QMainWindow, Ui_MainWindow):
    def __init__(self, address, delta):
        super().__init__()

        self.setupUi(self)

        self.address = address
        self.delta = delta
        self.type_of_map = 'map'
        # храним список координат меток найденных объектов
        self.mark = ()
        self.bool_index = False
        self.previous_address = ''
        self.text_index = ''
        self.coords = self.get_coordinates(address)
        self.map_file = self.get_image()

        self.RB_1.setChecked(True)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.RB_1)
        self.button_group.addButton(self.RB_2)
        self.button_group.addButton(self.RB_3)

        self.button_group.buttonClicked.connect(self.set_map)
        self.index.clicked.connect(self.change_index)
        self.search.clicked.connect(self.search_object)
        self.flip.clicked.connect(self.reset)

        self.init_ui()

    def set_map(self, button):
        btn = button.text()
        if btn == 'схема':
            self.type_of_map = 'map'
        elif btn == 'спутник':
            self.type_of_map = 'sat'
        elif btn == 'гибрид':
            self.type_of_map = 'sat,skl'
        self.map_file = self.get_image()
        pixmap = QPixmap(self.map_file)
        self.image.setPixmap(pixmap)
        self.update()

    def get_coordinates(self, address):
        try:
            coords = get_coordinates(address)
            return coords
        except Exception as e:
            print(f"Could not find coordinates for address: {address}")

    def get_image(self):
        '''Сохраняем карту в файл по заданному address с масштабом delta'''
        address = self.address
        delta = self.delta
        toponym_longitude, toponym_latitude = self.coords

        map_params = {
            "ll": f"{toponym_longitude},{toponym_latitude}",
            "spn": f"{delta},{delta}",
            "l": f"{self.type_of_map}"
        }
        if self.mark:
            map_params["pt"] = ','.join([str(self.mark[0]), str(self.mark[1]), "pm2wtm"])

        map_api_server = "http://static-maps.yandex.ru/1.x/"

        response = requests.get(map_api_server, params=map_params)

        if not response.ok:
            response.raise_for_status()

        # Записываем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        return map_file

    def init_ui(self):
        ## Изображение
        pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(200, 0)
        self.image.resize(600, 600)
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)

    def closeEvent(self, event):
        os.remove(self.map_file)

    def moving(self, direction):
        x, y = self.coords
        if direction == 'UP':
            return (x, y + 0.0005)
        elif direction == 'DOWN':
            return (x, y - 0.0005)
        elif direction == 'LEFT':
            return (x - 0.0005, y)
        elif direction == 'RIGHT':
            return (x + 0.0005, y)

    def keyPressEvent(self, event):
        key = event.key()
        super().keyPressEvent(event)

        if key == Qt.Key_PageUp:  # PGUP
            print("PGUP")
            self.delta += 0.004
        elif key == Qt.Key_PageDown:  # PGDN
            print("PGDN")
            self.delta -= 0.004 if self.delta - 0.004 >= 0 else 0
        elif key == Qt.Key_Up:  # UP
            print("UP")
            self.coords = self.moving('UP')
        elif key == Qt.Key_Down:  # DOWN
            print("DOWN")
            self.coords = self.moving('DOWN')
        elif key == Qt.Key_Left:  # LEFT
            print("LEFT")
            self.coords = self.moving('LEFT')
        elif key == Qt.Key_Right:  # RIGHT
            print("RIGHT")
            self.coords = self.moving('RIGHT')

        self.do_refactor()

    def search_object(self):
        if self.object.text():
            temporary = get_coordinates(self.object.text())
            if temporary:
                self.coords = temporary
                self.mark = temporary
                self.previous_address = get_address(self.object.text())
                self.text_index = get_index(self.object.text())
                self.change_information()
                self.do_refactor()

    def reset(self):
        self.information.setText('')
        self.mark = ()
        self.object.setText('')
        self.text_index = ''
        self.previous_address = ''
        self.do_refactor()

    def change_index(self):
        self.bool_index = not self.bool_index
        if self.bool_index:
            self.index.setText('Убрать индекс')
        else:
            self.index.setText('Показать индекс')
        self.change_information()

    def change_information(self):
        if self.previous_address:
            if self.bool_index:
                if self.text_index:
                    self.information.setText(self.previous_address + '\nИндекс: ' + self.text_index)
                else:
                    self.information.setText(self.previous_address + '\nИндекс: не найден')
            else:
                self.information.setText(self.previous_address)

    def do_refactor(self):
        self.map_file = self.get_image()
        pixmap = QPixmap(self.map_file)
        self.image.setPixmap(pixmap)
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            if 200 <= event.x() <= 800 and 0 <= event.y() <= 600:
                delta_x_y = ((event.x() - 500) * 2.5, -event.y() + 300)
                new_coords = tuple(map(lambda x: self.coords[x] + self.delta * delta_x_y[x] / 600, range(2)))
                self.mark = new_coords
                self.previous_address = reversed_geocode(new_coords)
                self.text_index = get_index(self.previous_address)
                self.change_information()
                self.do_refactor()
        elif event.buttons() == Qt.RightButton:
            if 200 <= event.x() <= 800 and 0 <= event.y() <= 600:
                delta_x_y = ((event.x() - 500) * 2.5, -event.y() + 300)
                new_coords = tuple(map(lambda x: self.coords[x] + self.delta * delta_x_y[x] / 600, range(2)))
                organization = search_by_coords(new_coords, reversed_geocode(new_coords))
                if organization:
                    temporary = tuple(organization['geometry']['coordinates'])
                    if lonlat_distance(temporary, new_coords) <= 50:
                        self.mark = temporary
                        data = organization["properties"]["CompanyMetaData"]
                        row = 'name: ' + data['name'] + '\n' + 'address: ' + data['address']
                        self.previous_address = row
                        self.text_index = get_index(data['address'])
                        self.change_information()
                        self.do_refactor()


def main():
    address = 'Москва, ул. Ак. Королева, 12'
    delta = 0.005

    app = QApplication(sys.argv)
    mywindow = YandexMap(address=address, delta=delta)
    mywindow.setStyleSheet('background-color: rgb(255, 238, 194)')
    mywindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
