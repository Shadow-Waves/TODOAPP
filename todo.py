from PyQt6.QtWidgets import QMainWindow,QLabel,QLineEdit,QApplication,QFrame,QScrollArea,QGroupBox,QFormLayout,QCheckBox
from PyQt6.QtGui import QIcon,QPixmap
from PyQt6.QtCore import QTimer,QDateTime
from PyQt6.QtSql import QSqlDatabase,QSqlQuery
from sys import argv

class ToDo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("C:\\Users\\Hafedh\\Desktop\\TODOAPP\\iconic.jpg"))
        self.setWindowTitle("TODO")
        self.setFixedSize(600,430)
        self.setStyleSheet("background-color:black;")
        self.setWindowOpacity(.8)

        self.input = QLineEdit(self)
        self.input.setGeometry(10,10,500,40)
        self.input.setPlaceholderText("Stuff To Do")
        self.input.setStyleSheet("border:1px groove red;background-color:transparent;color:cyan;font-size:16px;font-weight:bold;")

        self.add = QLabel(self)
        self.add.setGeometry(535,15,30,30)
        self.add.setPixmap(QPixmap("C:\\Users\\Hafedh\\Desktop\\TODOAPP\\add.png").scaled(30,30))
        self.add.mousePressEvent = self.addItem

        self.main_task = QFrame(self)
        self.main_task.setGeometry(10,60,580,330)
        self.main_task.setStyleSheet("background-color:rgba(255, 87, 51, 0.3);")

        self.datetime_timer = QTimer()
        self.datetime_timer.setInterval(1000)
        self.datetime_timer.timeout.connect(self.timer)
        self.datetime_timer.start()

        self.datetime = QLabel(QDateTime.currentDateTime().toString(),self)
        self.datetime.setGeometry(150,395,260,40)
        self.datetime.setStyleSheet("background-color:transparent;color:white;font-size:20px;font-weight:bold;")

        self.scrollarea = QScrollArea(self.main_task)
        self.scrollarea.setGeometry(0,0,580,330)
        self.scrollarea.setStyleSheet("border-width:0px;")
        self.scrollarea.verticalScrollBar().setStyleSheet("QScrollBar:vertical {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")
        self.scrollarea.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")

        self.item_list = []

        self.delete_checked_timer = QTimer()
        self.delete_checked_timer.setInterval(400)
        self.delete_checked_timer.timeout.connect(self.delete_item)
        self.delete_checked_timer.start()

        self.groupbox = QGroupBox()
        self.groupbox.setFixedWidth(578)
        self.main_layout = QFormLayout()
        self.main_layout.setSpacing(30)
        print(executer.exec("""
                        SELECT TODOSTR FROM TODO;
                     """))
        while executer.next():
            element_label = QLabel(executer.value(0))
            element_label.setFixedWidth(490)
            element_label.setStyleSheet("width:100px;color:white;background-color:transparent;font-size:16px;")
            element_checkbox = QCheckBox()
            element_checkbox.setStyleSheet("color:white;background-color:transparent;font-size:16px;")
            self.main_layout.addRow(element_label,element_checkbox)
            self.item_list.append((element_label,element_checkbox))

        self.groupbox.setLayout(self.main_layout)
        self.scrollarea.setWidget(self.groupbox)

        self.counter = QLabel(str(len(self.item_list)),self)
        self.counter.setGeometry(20,395,80,40)
        self.counter.setStyleSheet("background-color:transparent;color:white;font-size:20px;font-weight:bold;")

        self.show()

    def timer(self):
        self.datetime.setText(QDateTime.currentDateTime().toString())

    def addItem(self,e):
        if self.input.text():
            self.groupbox = QGroupBox()
            self.groupbox.setFixedWidth(578)
            self.main_layout = QFormLayout()
            self.main_layout.setSpacing(30)
            element_label = QLabel(self.input.text())
            element_label.setFixedWidth(490)
            element_label.setStyleSheet("width:100px;color:white;background-color:transparent;font-size:16px;")
            element_checkbox = QCheckBox()
            element_checkbox.setStyleSheet("color:white;background-color:transparent;font-size:16px;")
            self.item_list.append((element_label,element_checkbox))
            print(len(self.item_list))
            print(executer.exec(f"""
                                INSERT INTO TODO(ID,TODOSTR) VALUES({len(self.item_list) - 1},"{element_label.text()}");
                            """))
            self.counter.setText(str(len(self.item_list)))
            for nested_element in self.item_list:
                self.main_layout.addRow(nested_element[0],nested_element[1])
            self.groupbox.setLayout(self.main_layout)
            self.scrollarea.setWidget(self.groupbox)

    def delete_item(self):
        l = self.item_list.copy()
        self.groupbox = QGroupBox()
        self.groupbox.setFixedWidth(578)
        self.main_layout = QFormLayout()
        self.main_layout.setSpacing(30)
        for item in range(len(self.item_list)):
            if self.item_list[item][1].isChecked():
                print(executer.exec(f"""
                                DELETE FROM TODO
                                WHERE TODOSTR = "{self.item_list[item][0].text()}";
                            """))
                self.main_layout.removeRow(item)
                l.pop(item)
        self.item_list = l
        self.counter.setText(str(len(self.item_list)))
        for x,y in self.item_list:
            self.main_layout.addRow(x,y)
        self.groupbox.setLayout(self.main_layout)
        self.scrollarea.setWidget(self.groupbox)

if __name__ == "__main__":
    con = QSqlDatabase.addDatabase("QSQLITE","TODO")
    con.setDatabaseName("C:\\Users\\Hafedh\\Desktop\\TODOAPP\\todo.sql")
    con.open()
    create_to_do_table_query = """
                                    CREATE TABLE TODO
                                    (
                                        ID NUMBER PRIMARY KEY,
                                        TODOSTR VARCHAR
                                    );
                                """
    executer = QSqlQuery(con)
    #executer.exec(create_to_do_table_query)
    application = QApplication(argv)
    todo = ToDo()
    application.exec()
    con.close()