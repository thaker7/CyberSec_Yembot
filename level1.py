from info import *

list_btn = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text="الخطة الدراسية", callback_data="plan")
b2 = types.InlineKeyboardButton(text="مستوى أول  Level 1", callback_data="level1")
b3 = types.InlineKeyboardButton(text="مستوى ثاني Level 2", callback_data="level2")
list_btn.add(b1)
list_btn.add(b2, b3)

def call_plan(call):
  if call.data == "plan":
      bot.send_message(call.message.chat.id, "جاري ارسال الخطة الدراسية، يرجى الأنتظار !")
      bot.send_document(call.message.chat.id, open("cyber_security_plan.pdf", "rb"))

def call_level1(call):
    if call.data == "level1":
        keyboard = [
            [types.InlineKeyboardButton(text="الترم الأول Term 1", callback_data="level1_term1")],
            [types.InlineKeyboardButton(text="الترم الثاني Term 2", callback_data="level1_term2")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر الترم لاظهار المواد المتعلقه به (Level 1)", reply_markup=reply_markup)
# ======================================================================================================================
    elif call.data == "level1_term1":
        keyboard = [
            [types.InlineKeyboardButton(text="اللغة العربية", callback_data="arabic"), types.InlineKeyboardButton(text="اللغة الأنجليزية (1)", callback_data="english_1")],
            [types.InlineKeyboardButton(text="مهارة تلاوة القران الكريم وتجويده", callback_data="quran")],
            [types.InlineKeyboardButton(text="مبادئ الرياضيات", callback_data="principles_mathematics")],
            [types.InlineKeyboardButton(text="مبادئ البرمجة ++C", callback_data="principles_programming")],
            [types.InlineKeyboardButton(text="أساسيات الحاسوب", callback_data="fundamentals_computer"), types.InlineKeyboardButton(text="مهارات الحاسوب", callback_data="computer_skills")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر المادة التي تريدها (Level1_Term1)", reply_markup=reply_markup)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "arabic":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (اللغة العربية)، يرجى الأنتظار !")
        for i in range(1, 3):
            bot.send_document(call.message.chat.id, open(f"level_1/term1/arabic/lecture_{i}.pdf", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "english_1":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (اللغة الأنجليزية (1))، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_1/term1/english1/interchange_level_1_student_book.pdf", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "quran":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (القران الكريم)، يرجى الأنتظار !")
        for i in range(1, 3):
            bot.send_document(call.message.chat.id, open(f"level_1/term1/quran/lecture_{i}.docx", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "principles_mathematics":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة (مبادئ الرياضيات) بعد !")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "principles_programming":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="principles_programming_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="principles_programming_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (مبادئ البرمجة)", reply_markup=reply_markup)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "principles_programming_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (مبادئ البرمجة نظري)، يرجى الأنتظار !")
        for i in range(1, 8):
            bot.send_document(call.message.chat.id, open(f"level_1/term1/principles_programming/see/lecture_{i}.pdf", "rb"))

        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/see/break_continue.docx", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/see/examples_c++.pdf", "rb"))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "principles_programming_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال تمارين مادة (مبادئ البرمجة عملي)، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/week_days(if).cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/week_days(switch).cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/degree.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/calculate_rate.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/single_marride.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/swap.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/dollars_yemen.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/find_values.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/perimeter_area.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/numerical_factoria.pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/solving_exercises2.pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term1/principles_programming/lab/bank.cpp", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "fundamentals_computer":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="fundamentals_computer_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="fundamentals_computer_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (أساسيات الحاسوب)", reply_markup=reply_markup)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "fundamentals_computer_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (أساسيات الحاسوب نظري)، يرجى الأنتظار !")
        for i in range(0, 11):
            bot.send_document(call.message.chat.id, open(f"level_1/term1/fundamentals_computer/see/lecture_{i}.pdf", "rb"))
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "fundamentals_computer_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (أساسيات الحاسوب عملي)، يرجى الأنتظار !")
        for i in range(1, 9):
            bot.send_document(call.message.chat.id, open(f"level_1/term1/fundamentals_computer/lab/lecture_{i}.pdf", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "computer_skills":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة (مهارات الحاسوب) بعد !")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "level1_term2":
        keyboard = [
            [types.InlineKeyboardButton(text="ثقافة اسلامية", callback_data="islamic_culture"), types.InlineKeyboardButton(text="اللغة الأنجليزية (2)", callback_data="english_2")],
            [types.InlineKeyboardButton(text="أساسيات الأمن السيبراني", callback_data="cyber_security")],
            [types.InlineKeyboardButton(text="برمجة الحاسوب ++C", callback_data="computer_programming")],
            [types.InlineKeyboardButton(text="التفاضل والتكامل", callback_data="calculus")],
            [types.InlineKeyboardButton(text="التفكير الناقد", callback_data="critical_thinking")],
            [types.InlineKeyboardButton(text="مهارات الاتصال", callback_data="communication_skills"), types.InlineKeyboardButton(text="تنمية المهارات القيادية", callback_data="leadership_skills")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر المادة التي تريدها (Level1_Term2)", reply_markup=reply_markup)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "islamic_culture":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (ثقافة اسلامية)، يرجى الأنتظار !")
        for i in range(1, 6):
            bot.send_document(call.message.chat.id, open(f"level_1/term2/islamic_culture/lecture_{i}.pdf", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "english_2":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (اللغة الأنجليزية (2))، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_1/term2/englich_2/interchange_Level1_student_book.pdf", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "cyber_security":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (أساسيات الأمن السيبراني)، يرجى الأنتظار !")
        for i in range(1, 7):
            bot.send_document(call.message.chat.id, open(f"level_1/term2/cyber_security/lecture_{i}.pptx", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "computer_programming":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="computer_programming_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="computer_programming_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (برمجة الحاسوب)", reply_markup=reply_markup)

    elif call.data == "computer_programming_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (برمجة الحاسوب نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_1/term2/computer_programming/see/lecture_{i}.pptx", "rb"))

    elif call.data == "computer_programming_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال تمارين مادة (برمجة الحاسوب عملي)، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_1/term2/computer_programming/lab/smallest.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term2/computer_programming/lab/recursive_pwr.cpp", "rb"))
        bot.send_document(call.message.chat.id, open("level_1/term2/computer_programming/lab/recursive_seq.cpp", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "calculus":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة (التفاضل والتكامل) بعد !")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "critical_thinking":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (التفكير الناقد)، يرجى الأنتظار !")
        for i in range(1, 7):
            bot.send_document(call.message.chat.id, open(f"level_1/term2/critical_thinking/lecture_{i}.pdf", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "communication_skills":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (مهارات الاتصال)، يرجى الأنتظار !")
        for i in range(1, 5):
            bot.send_document(call.message.chat.id, open(f"level_1/term2/communication_skills/lecture_{i}.pptx", "rb"))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "leadership_skills":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة (تنمية المهارات القيادية)، يرجى الأنتظار !")
        for i in range(1, 6):
            bot.send_document(call.message.chat.id, open(f"level_1/term2/leadership_skills/lecture_{i}.pdf", "rb"))
