# from PyQt5.QtCore import Qt
import json
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout,
    QListWidget, QTextEdit,
    QLineEdit, QInputDialog,
)
from PyQt5.QtWidgets import QMessageBox

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
create_note_btn = QPushButton("Create new note")
delete_note_btn = QPushButton("Delete note")
save_note_btn = QPushButton("Save note")
rename_note_btn = QPushButton("Rename note")
add_tag_btn = QPushButton("Add tag")
unpin_note_tag = QPushButton("Delete tag")
search_by_tag_btn = QPushButton("Search by tag")

#  lists
list_of_notes = QListWidget()
list_of_notes.addItems(notes)
tags_list = QListWidget()

note_text_edit = QTextEdit()
tag_input = QLineEdit()
tag_input.setPlaceholderText("Type tag:")

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
right_layout.addWidget(rename_note_btn)
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
def create_error():
    error_box = QMessageBox()
    error_box.setWindowTitle("Error")
    error_box.setText("You did not select any note.")
    error_box.setIcon(QMessageBox.Warning)
    error_box.exec_()
def show_notes():
    name = list_of_notes.selectedItems()[0].text()
    note_text_edit.setText(notes[name]["text"])
    tags_list.clear()
    tags_list.addItems(notes[name]["tags"])

def add_note():
    note_name, ok = QInputDialog.getText(
        main_window, "Add Note?", "Name:"
    )
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_of_notes.addItem(note_name)

def save_note():
    if list_of_notes.selectedItems():
        key = list_of_notes.selectedItems()[0].text()
        notes[key]["text"] = note_text_edit.toPlainText()
        with open("notes_data.json", 'w', encoding="utf-8") as f:
            json.dump(notes, f, sort_keys=True, indent=2)

    else:
        create_error()

def delete_note():
    if list_of_notes.selectedItems():
        key = list_of_notes.selectedItems()[0].text()
        del notes[key]
        list_of_notes.clear()
        tags_list.clear()
        with open("notes_data.json", 'w', encoding="utf-8") as f:
            json.dump(notes, f, sort_keys=True, indent=2)
        list_of_notes.addItems(notes)
    else:
        create_error()

def rename_note():
    if list_of_notes.selectedItems():
        key = list_of_notes.selectedItems()[0].text()
        new_name, ok = QInputDialog.getText(
            main_window, "Rename note?", "New name:"
        )
        if ok and new_name != "":
            notes[new_name] = notes.pop(key)
            list_of_notes.clear()
            with open("notes_data.json", 'w', encoding="utf-8") as f:
                json.dump(notes, f, sort_keys=True, indent=2)
            list_of_notes.addItems(notes)

create_note_btn.clicked.connect(add_note)
list_of_notes.itemClicked.connect(show_notes)
save_note_btn.clicked.connect(save_note)
delete_note_btn.clicked.connect(delete_note)
rename_note_btn.clicked.connect(rename_note)

main_window.setLayout(main_layout)
main_window.show()
if __name__ == '__main__':
    sys.exit(app.exec_())