# from PyQt5.QtCore import Qt
import json
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout,
    QListWidget, QTextEdit,
    QLineEdit, QInputDialog,
    QMessageBox
)

app = QApplication(sys.argv)

main_window = QWidget()
main_window.setWindowTitle("Science Notes")
main_window.resize(1000, 800)
with open("notes_data.json", 'r', encoding="utf-8") as f:
    notes = json.load(f)

###########   Objects   ###########
#   labels
notions_lbl = QLabel("Замітки")
tags_lbl = QLabel("Теги")

#   buttons
create_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти")
add_tag_btn = QPushButton("Додати до замітки")
unpin_note_tag = QPushButton("Відкріпити замітку")
search_by_tag_btn = QPushButton("Знайти за тегом")

#  lists
list_of_notes = QListWidget()
list_of_notes.addItems(notes)
tags_list = QListWidget()

note_text_edit = QTextEdit()
tag_input = QLineEdit()
tag_input.setPlaceholderText("Введіть тег:")

#   layouts
main_layout = QHBoxLayout()
main_layout.addWidget(note_text_edit)
right_layout = QVBoxLayout()
right_layout.addWidget(notions_lbl)
right_layout.addWidget(list_of_notes)
right_button_layout = QHBoxLayout()
right_button_layout.addWidget(create_note_btn)
right_button_layout.addWidget(delete_note_btn)
right_layout.addWidget(save_note_btn)
right_layout.addLayout(right_button_layout)
right_layout.addWidget(tags_lbl)
right_layout.addWidget(tags_list)
right_layout.addWidget(tag_input)
right_button_layout2 = QHBoxLayout()
right_button_layout2.addWidget(add_tag_btn)
right_layout.addWidget(search_by_tag_btn)
right_layout.addLayout(right_button_layout2)
right_button_layout2.addWidget(unpin_note_tag)
main_layout.addLayout(right_layout)

############   functions   ############
def show_notes():
    name = list_of_notes.selectedItems()[0].text()
    note_text_edit.setText(notes[name]["text"])
    tags_list.clear()
    tags_list.addItems(notes[name]["tags"])

def add_note():
    note_name, ok = QInputDialog.getText(
        main_window, "Додати замітку?", "Назва:"
    )
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_of_notes.addItem(note_name)

create_note_btn.clicked.connect(add_note)
list_of_notes.itemClicked.connect(show_notes)
# save_note_btn.clicked.connect(save_note)

main_window.setLayout(main_layout)
main_window.show()
if __name__ == '__main__':
    sys.exit(app.exec_())