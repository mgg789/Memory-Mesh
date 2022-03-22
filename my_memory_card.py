from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right,wrong1,wrong2,wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Сколько лет Анатолию', '1', '1234', '45', '29'))
questions_list.append(Question('Какого материка нет?', 'Гренландия', 'Сев. Америка', 'Австралия', 'Антарктида'))
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Выбери перевод слова "переменная"', 'variable', 'variation', 'variant', 'changing'))

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбран    
    
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def ask(q):
    shuffle(ans)
    ans[0].setText(q.right)
    ans[1].setText(q.wrong1)
    ans[2].setText(q.wrong2)
    ans[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if ans[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неправильно!')
def next_question():
    window.current += 1
    if  window.current == len(questions_list):
        window.current = -1
    q = questions_list[window.current]
    ask(q)

def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

app = QApplication([])
window = QWidget()
window.current = -1
window.setWindowTitle('Memory Card')
window.resize(500, 250)

lb_Question = QLabel('Тут будет вопрос')
btn_OK = QPushButton('Ответить')
btn_OK.clicked.connect(click_OK)

# панель вопроса
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

ans = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 

# панель ответа
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("Правильно/Неправильно")
lb_Correct = QLabel("Тут будет правильный ответ")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=Qt.AlignHCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5) # пробелы между содержимым

AnsGroupBox.hide()
 
window.setLayout(layout_card)
next_question()

window.show()
app.exec()