from PyQt5 import QtCore, QtGui, QtWidgets
from Reports.TaskManager import TaskManager
from Reports.DatabaseManager import DatabaseManager as dbm
import json
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.table_name = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_layout = QtWidgets.QVBoxLayout()
        self.side_menu_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.side_menu_layout.setSpacing(0)
        self.side_menu_layout.setObjectName("side_menu_layout")
        self.side_menu_button_guild_players = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu_button_guild_players.sizePolicy().hasHeightForWidth())
        self.side_menu_button_guild_players.setSizePolicy(sizePolicy)
        self.side_menu_button_guild_players.setMaximumSize(QtCore.QSize(200, 25))
        self.side_menu_button_guild_players.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.side_menu_button_guild_players.setObjectName("side_menu_button_guild_players")
        self.side_menu_layout.addWidget(self.side_menu_button_guild_players, 0, QtCore.Qt.AlignLeft)
        self.side_menu_button_player_roster = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu_button_player_roster.sizePolicy().hasHeightForWidth())
        self.side_menu_button_player_roster.setSizePolicy(sizePolicy)
        self.side_menu_button_player_roster.setMaximumSize(QtCore.QSize(200, 25))
        self.side_menu_button_player_roster.setObjectName("side_menu_button_player_roster")
        self.side_menu_layout.addWidget(self.side_menu_button_player_roster, 0, QtCore.Qt.AlignLeft)
        self.side_menu_button_sql_editor = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu_button_sql_editor.sizePolicy().hasHeightForWidth())
        self.side_menu_button_sql_editor.setSizePolicy(sizePolicy)
        self.side_menu_button_sql_editor.setMaximumSize(QtCore.QSize(200, 25))
        self.side_menu_button_sql_editor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.side_menu_button_sql_editor.setObjectName("side_menu_button_sql_editor")
        self.side_menu_layout.addWidget(self.side_menu_button_sql_editor, 0, QtCore.Qt.AlignLeft)
        self.side_menu_dummy_frame = QtWidgets.QFrame(self.centralwidget)
        self.side_menu_dummy_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_dummy_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_dummy_frame.setObjectName("side_menu_dummy_frame")
        self.side_menu_layout.addWidget(self.side_menu_dummy_frame)
        self.horizontalLayout.addLayout(self.side_menu_layout)
        self.main_body_layout = QtWidgets.QVBoxLayout()
        self.main_body_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.main_body_layout.setSpacing(0)
        self.main_body_layout.setObjectName("main_body_layout")
        self.header_main_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_main_frame.setObjectName("header_main_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_main_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.allycode_line_edit = QtWidgets.QLineEdit(self.header_main_frame)
        self.allycode_line_edit.setObjectName("allycode_line_edit")
        self.horizontalLayout_2.addWidget(self.allycode_line_edit, 0, QtCore.Qt.AlignLeft)
        self.request_data_button = QtWidgets.QPushButton(self.header_main_frame)
        self.request_data_button.setObjectName("request_data_button")
        self.horizontalLayout_2.addWidget(self.request_data_button, 0, QtCore.Qt.AlignRight)
        self.main_body_layout.addWidget(self.header_main_frame)
        self.guild_players_main_frame = QtWidgets.QFrame(self.centralwidget)
        self.guild_players_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guild_players_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guild_players_main_frame.setObjectName("guild_players_main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.guild_players_main_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.guild_players_table_widget = QtWidgets.QTableWidget(self.guild_players_main_frame)
        self.guild_players_table_widget.setObjectName("guild_players_table_widget")
        self.guild_players_table_widget.setColumnCount(0)
        self.guild_players_table_widget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.guild_players_table_widget)
        self.main_body_layout.addWidget(self.guild_players_main_frame)
        self.player_roster_main_frame = QtWidgets.QFrame(self.centralwidget)
        self.player_roster_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player_roster_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_roster_main_frame.setObjectName("player_roster_main_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.player_roster_main_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.player_roster_table_widget = QtWidgets.QTableWidget(self.player_roster_main_frame)
        self.player_roster_table_widget.setObjectName("player_roster_table_widget")
        self.player_roster_table_widget.setColumnCount(0)
        self.player_roster_table_widget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.player_roster_table_widget)
        self.main_body_layout.addWidget(self.player_roster_main_frame)
        self.sql_editor_main_frame = QtWidgets.QFrame(self.centralwidget)
        self.sql_editor_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_editor_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sql_editor_main_frame.setObjectName("sql_editor_main_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sql_editor_main_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sql_editor_side_menu_frame = QtWidgets.QFrame(self.sql_editor_main_frame)
        self.sql_editor_side_menu_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sql_editor_side_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_editor_side_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sql_editor_side_menu_frame.setObjectName("sql_editor_side_menu_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.sql_editor_side_menu_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sql_editor_side_menu_table_widget = QtWidgets.QTableWidget(self.sql_editor_side_menu_frame)
        self.sql_editor_side_menu_table_widget.setObjectName("sql_editor_side_menu_table_widget")
        self.sql_editor_side_menu_table_widget.setColumnCount(0)
        self.sql_editor_side_menu_table_widget.setRowCount(0)
        self.verticalLayout_6.addWidget(self.sql_editor_side_menu_table_widget)
        self.horizontalLayout_3.addWidget(self.sql_editor_side_menu_frame)
        self.sql_editor_body_main_frame = QtWidgets.QFrame(self.sql_editor_main_frame)
        self.sql_editor_body_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_editor_body_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sql_editor_body_main_frame.setObjectName("sql_editor_body_main_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sql_editor_body_main_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sql_editor_text_edit = QtWidgets.QTextEdit(self.sql_editor_body_main_frame)
        self.sql_editor_text_edit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sql_editor_text_edit.setObjectName("sql_editor_text_edit")
        self.verticalLayout_5.addWidget(self.sql_editor_text_edit)
        self.sql_editor_error_execute_frame = QtWidgets.QFrame(self.sql_editor_body_main_frame)
        self.sql_editor_error_execute_frame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.sql_editor_error_execute_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_editor_error_execute_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sql_editor_error_execute_frame.setObjectName("sql_editor_error_execute_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.sql_editor_error_execute_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sql_editor_error_message_label = QtWidgets.QLabel(self.sql_editor_error_execute_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sql_editor_error_message_label.sizePolicy().hasHeightForWidth())
        self.sql_editor_error_message_label.setSizePolicy(sizePolicy)
        self.sql_editor_error_message_label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.sql_editor_error_message_label.setFont(font)
        self.sql_editor_error_message_label.setAutoFillBackground(True)
        self.sql_editor_error_message_label.setText("")
        self.sql_editor_error_message_label.setObjectName("sql_editor_error_message_label")
        self.horizontalLayout_4.addWidget(self.sql_editor_error_message_label)
        self.sql_editor_execute_button = QtWidgets.QPushButton(self.sql_editor_error_execute_frame)
        self.sql_editor_execute_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sql_editor_execute_button.setObjectName("sql_editor_execute_button")
        self.horizontalLayout_4.addWidget(self.sql_editor_execute_button, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.sql_editor_error_execute_frame)
        self.sql_editor_table_widget = QtWidgets.QTableWidget(self.sql_editor_body_main_frame)
        self.sql_editor_table_widget.setObjectName("sql_editor_table_widget")
        self.sql_editor_table_widget.setColumnCount(0)
        self.sql_editor_table_widget.setRowCount(0)
        self.verticalLayout_5.addWidget(self.sql_editor_table_widget)
        self.horizontalLayout_3.addWidget(self.sql_editor_body_main_frame)
        self.main_body_layout.addWidget(self.sql_editor_main_frame)
        self.horizontalLayout.addLayout(self.main_body_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.side_menu_button_guild_players.clicked.connect(self.open_guild_players_tab)
        self.side_menu_button_player_roster.clicked.connect(self.open_player_roster_tab)
        self.side_menu_button_sql_editor.clicked.connect(self.open_sql_editor_tab)
        self.request_data_button.clicked.connect(self.load_data)
        self.sql_editor_execute_button.clicked.connect(self.sql_editor_execute_query)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.open_guild_players_tab()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Swgoh Data App"))
        self.side_menu_button_guild_players.setText(_translate("MainWindow", "Guild Players"))
        self.side_menu_button_player_roster.setText(_translate("MainWindow", "Player Roster"))
        self.side_menu_button_sql_editor.setText(_translate("MainWindow", "SQL editor"))
        self.allycode_line_edit.setPlaceholderText(_translate("MainWindow", "Allycode"))
        self.request_data_button.setText(_translate("MainWindow", "Request Data"))
        self.sql_editor_execute_button.setText(_translate("MainWindow", "Execute"))

    def collapse_all_tabs(self):
        body_frames = {
            self.guild_players_main_frame: "guild_players",
            self.player_roster_main_frame: "player_roster",
            self.sql_editor_main_frame: ""
        }
        for frame in body_frames:
            frame.setMaximumSize(QtCore.QSize(16777215, 0))

    def refresh_swgoh_units_table(self):
        self.table_name = 'swgoh_units'
        drm = TaskManager(self.table_name)
        drm.refresh_data_if_needed()

    def open_guild_players_tab(self):
        self.collapse_all_tabs()
        self.guild_players_main_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.refresh_swgoh_units_table()
        self.table_name = 'guild_players'

    def open_player_roster_tab(self):
        self.collapse_all_tabs()
        self.player_roster_main_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.refresh_swgoh_units_table()
        self.table_name = 'player_roster'

    def open_sql_editor_tab(self):
        self.collapse_all_tabs()
        self.sql_editor_main_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.table_name = ''
        self.fill_side_menu_with_tables_names()

    def fill_side_menu_with_tables_names(self):
        table_names = dbm.get_all_tables_names()
        table_widget = self.sql_editor_side_menu_table_widget
        self.populate_table_widget_with_query_results(table_widget, table_names)

    def sql_editor_execute_query(self):
        sql_query = self.sql_editor_text_edit.toPlainText()
        try:
            sql_query_result = dbm.execute_sql_query(sql_query, need_sql_result=True)
            self.populate_table_widget_with_query_results(self.sql_editor_table_widget, sql_query_result)
        except Exception as exc:
            self.sql_editor_error_message_label.setText(str(exc))
        else:
            self.sql_editor_error_message_label.setText('')

    def load_data(self):
        if self.table_name:
            table_name_table_widget_dict = {
                'guild_players': self.guild_players_table_widget,
                'player_roster': self.player_roster_table_widget
            }
            with open('settings.json') as inf:
                cred = json.load(inf)
            allycode = self.allycode_line_edit.text()
            drm = TaskManager(self.table_name, cred)
            data = drm.get_records(allycode)
            table_widget = table_name_table_widget_dict.get(self.table_name)
            self.populate_table_widget_with_query_results(table_widget, data)
            

    def populate_table_widget_with_query_results(self, table_widget, query_result):
        column_labels = next(query_result)
        table_widget.setColumnCount(len(column_labels))
        table_widget.setHorizontalHeaderLabels(column_labels)

        table_widget.setRowCount(0)
        for row_number, row_content in enumerate(query_result):
            table_widget.insertRow(row_number)
            for column_number, cell_value in enumerate(row_content):
                table_widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(cell_value)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())