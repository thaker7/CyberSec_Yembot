from info import *

def call_level2(call):
    if call.data == "level2":
        keyboard = [
            [types.InlineKeyboardButton(text="الترم الأول Term 1", callback_data="level2_term1")],
            [types.InlineKeyboardButton(text="الترم الثاني Term 2", callback_data="level2_term2")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر الترم لاظهار المواد المتعلقه به (Level 2)", reply_markup=reply_markup)
# ======================================================================================================================
    if call.data == "level2_term1":
        keyboard = [
            [types.InlineKeyboardButton(text="تصميم الويب", callback_data="web_design"), types.InlineKeyboardButton(text="مبادئ الشبكات", callback_data="networks1")],
            [types.InlineKeyboardButton(text="هياكل البيانات والخوارزميات ++C", callback_data="c++_ds")],
            [types.InlineKeyboardButton(text="البرمجة الموجهة للكائنات JAVA", callback_data="java_oop")],
            [types.InlineKeyboardButton(text="مقدمة الى قواعد البيانات", callback_data="database1")],
            [types.InlineKeyboardButton(text="الجبر الخطي", callback_data="linear_algebra"), types.InlineKeyboardButton(text="الهياكل المتقطعة", callback_data="discrete_structures")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر المادة التي تريدها (Level2_Term1)", reply_markup=reply_markup)

    elif call.data == "web_design":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="web_design_see"), types.InlineKeyboardButton(text="عملي", callback_data="web_design_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (تصميم الويب)", reply_markup=reply_markup)
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "web_design_see":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات (English)", callback_data="web_design_lectures_en"),
             types.InlineKeyboardButton(text="تلاخيصي عربي", callback_data="web_design_lectures_ar")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر لغة محاضرات (تصميم الويب نظري)", reply_markup=reply_markup)

    elif call.data == "web_design_lectures_en":
        bot.send_message(call.message.chat.id, "جاري ارسال المحاضرات (English)، يرجى الأنتظار !")
        for i in range(1, 5):
            bot.send_document(call.message.chat.id, open(f"term1/web_design/see/web_{i}_(html).pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/web_design/see/web_5_(css).pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/web_design/see/web_6_(css).pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/web_design/see/web_7_(js).pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/web_design/see/web_8_(js).pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/web_design/see)/examples_(js).pdf", "rb"))

    elif call.data == "web_design_lectures_ar":
        bot.send_message(call.message.chat.id, "جاري ارسال التلاخيص، يرجى الأنتظار !")
        for i in range(1, 9):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/web_design/see/my_lectures/lecture_{i}.txt", "rb"))

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "web_design_lab":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات HTML", callback_data="web_design_lab_html")],
            [types.InlineKeyboardButton(text="المحاضرات CSS", callback_data="web_design_lab_css")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (تصميم الويب عملي)", reply_markup=reply_markup)

    elif call.data == "web_design_lab_html":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات HTML عملي، يرجى الأنتظار !")
        for i in range(1, 7):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/web_design/lab/html_{i}.pdf", "rb"))

    elif call.data == "web_design_lab_css":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات CSS عملي، يرجى الأنتظار !")
        for i in range(1, 6):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/web_design/lab/css_{i}.pdf", "rb"))

# ----------------------------------------------------------------------------------------------------------------------
    elif call.data == "networks1":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="networks1_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="networks1_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (مبادئ الشبكات)", reply_markup=reply_markup)

    elif call.data == "networks1_see":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات (English)", callback_data="networks1_lectures_en"),
             types.InlineKeyboardButton(text="تلاخيصي عربي", callback_data="networks1_lectures_ar")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر لغة محاضرات (الشبكات)", reply_markup=reply_markup)

    elif call.data == "networks1_lectures_en":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات الشبكات (English)، يرجى الأنتظار !")
        for i in range(1, 9):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/Networks/see/network_{i}.pdf", "rb"))

    elif call.data == "networks1_lectures_ar":
        bot.send_message(call.message.chat.id, "جاري ارسال التلاخيص، يرجى الأنتظار !")
        for i in range(1, 9):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/Networks/see/my_lectures/lecture_{i}.txt", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "networks1_lab":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات العملي بعد !")

# ----------------------------------------------------------------------------------------------------------------------
    elif call.data == "c++_ds":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="c++_ds_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="c++_ds_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (هياكل البيانات والخوازميات)", reply_markup=reply_markup)

    elif call.data == "c++_ds_see":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات (English)", callback_data="c++_ds_lectures_en"),
             types.InlineKeyboardButton(text="تلاخيصي عربي", callback_data="c++_ds_lectures_ar")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر لغة محاضرات (هياكل البيانات والخوازميات نظري)", reply_markup=reply_markup)

    elif call.data == "c++_ds_lectures_en":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات ++C نظري (English)، يرجى الأنتظار !")
        for i in range(1, 9):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/data_structure/see/c++_{i}.pptx", "rb"))

    elif call.data == "c++_ds_lectures_ar":
        bot.send_message(call.message.chat.id, "جاري ارسال التلاخيص، يرجى الأنتظار !")
        for i in range(1, 9):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/data_structure/see/my_lectures/lecture_{i}.txt", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "c++_ds_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال تلاخيص ++C عملي، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_2/term1/data_structure/lab/sorting.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/data_structure/lab/search_item.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/data_structure/lab/insert_delete_item.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/data_structure/lab/binary_search.txt", "rb"))

# ----------------------------------------------------------------------------------------------------------------------
    elif call.data == "java_oop":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="java_oop_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="java_oop_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (البرمجة الموجهة للكائنات)", reply_markup=reply_markup)

    elif call.data == "java_oop_see":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات (English)", callback_data="java_oop_lectures_en"),
             types.InlineKeyboardButton(text="تلاخيصي عربي", callback_data="java_oop_lectures_ar")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر لغة محاضرات (البرمجة الموجهة للكائنات JAVA)", reply_markup=reply_markup)

    elif call.data == "java_oop_lectures_en":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات JAVA نظري (English)، يرجى الأنتظار !")
        for i in range(1, 7):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/java_oop/see/java_{i}.pptx", "rb"))

    elif call.data == "java_oop_lectures_ar":
        bot.send_message(call.message.chat.id, "جاري ارسال التلاخيص، يرجى الأنتظار !")
        for i in range(1, 7):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/java_oop/see/my_lectures/lecture_{i}.txt", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "java_oop_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال المحاضرات العملي، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_2/term1/java_oop/lab/classes_objects.pptx", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/java_oop/lab/inheritance.pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/java_oop/lab/abstraction.docx", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/java_oop/lab/abstract_class.docx", "rb"))

# ----------------------------------------------------------------------------------------------------------------------
    elif call.data == "database1":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="database1_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="database1_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (قواعد البيانات)", reply_markup=reply_markup)

    elif call.data == "database1_see":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات (English)", callback_data="database1_lectures_en"),
             types.InlineKeyboardButton(text="تلاخيصي عربي", callback_data="database1_lectures_ar")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر لغة محاضرات (قواعد البيانات)", reply_markup=reply_markup)

    elif call.data == "database1_lectures_en":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات قواعد البيانات نظري (English)، يرجى الأنتظار !")
        for i in range(1, 8):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/database/see/ch{i}.ppt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/see/create_new_table.pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/see/views.pdf", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/see/joins.pdf", "rb"))

    elif call.data == "database1_lectures_ar":
        bot.send_message(call.message.chat.id, "جاري ارسال التلاخيص، يرجى الأنتظار !")
        for i in range(1, 8):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/database/see/my_lectures/lecture_{i}.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/see/my_lectures/lecture_join.txt", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "database1_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال التلاخيص العملي، يرجى الأنتظار !")
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/create_database.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/create_tables.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/insert.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/select.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/update.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/views.txt", "rb"))
        bot.send_document(call.message.chat.id, open("level_2/term1/database/lab/join.txt", "rb"))

# ----------------------------------------------------------------------------------------------------------------------
    elif call.data == "linear_algebra":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات كاملة", callback_data="linear_algebra_lectures")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر محاضرات (الجبر الخطي)", reply_markup=reply_markup)

    elif call.data == "linear_algebra_lectures":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات الجبر الخطي، يرجى الأنتظار !")
        for i in range(1, 7):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/linear_algebra/lecture_{i}.pdf", "rb"))

# ------------------------------------------------------------------------------------------------------------------
    elif call.data == "discrete_structures":
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات كاملة", callback_data="discrete_structures_lectures")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر محاضرات (الهياكل المتقطعة)", reply_markup=reply_markup)

    elif call.data == "discrete_structures_lectures":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات الهياكل المتقطعه، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term1/discrete_structures/lecture_{i}.pdf", "rb"))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if call.data == "level2_term2":
        keyboard = [
            [types.InlineKeyboardButton(text="معمارية وتنظيم الحاسوب", callback_data="computer_organization"), types.InlineKeyboardButton(text="شبكات الحاسوب", callback_data="computer_networks")],
            [types.InlineKeyboardButton(text="تطوير تطبيقات الويب Laravel", callback_data="web_development")],
            [types.InlineKeyboardButton(text="امن وادارة قواعد البيانات", callback_data="database_security")],
            [types.InlineKeyboardButton(text="مبادئ التشفير #C", callback_data="encryption"), types.InlineKeyboardButton(text="مبادئ نظم التشغيل", callback_data="operating_systems")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "✔ اختر المادة التي تريدها (Level2_Term2)", reply_markup=reply_markup)

    elif call.data == "web_development":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="web_development_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="web_development_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (تطوير تطبيقات الويب)", reply_markup=reply_markup)

    elif call.data == "web_development_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات تطوير تطبيقات الويب (نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/web_development/see/web_{i}.pptx", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "web_development_lab":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة (تطوير تطبيقات الويب عملي) بعد !")
        bot.send_document(call.message.chat.id, open(f"level_2/term2/web_development/lab/php_laravel_view.pptx", "rb"))
# -----------------------------------------------------------------------------------------------------------------------
    elif call.data == "database_security":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="database_security_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="database_security_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (امن وادارة قواعد البيانات)", reply_markup=reply_markup)

    elif call.data == "database_security_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات امن وادارة قواعد البيانات (نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/database2/see/db_{i}.pptx", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "database_security_lab":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة امن وادارة قواعد البيانات (عملي) بعد !")
# -----------------------------------------------------------------------------------------------------------------------
    elif call.data == "computer_networks":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="computer_networks_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="computer_networks_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (شبكات الحاسوب)", reply_markup=reply_markup)

    elif call.data == "computer_networks_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة شبكات الحاسوب (نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/networks2/see/net_{i}.pdf", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "computer_networks_lab":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة شبكات الحاسوب (عملي) بعد !")
# -----------------------------------------------------------------------------------------------------------------------
    elif call.data == "encryption":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="encryption_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="encryption_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (مبادئ التشفير)", reply_markup=reply_markup)

    elif call.data == "encryption_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة مبادئ التشفير (نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/encryption/see/encrypt_{i}.pdf", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "encryption_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة مبادئ التشفير (عملي)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/encryption/lab/lab_{i}.pdf", "rb"))
# -----------------------------------------------------------------------------------------------------------------------
    elif call.data == "computer_organization":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="computer_organization_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="computer_organization_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (معمارية وتنظيم الحاسوب)", reply_markup=reply_markup)

    elif call.data == "computer_organization_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة معمارية وتنظيم الحاسوب (نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/computer_organization/see/lecture_{i}.pdf", "rb"))
            if i == 2:
                bot.send_document(call.message.chat.id, open(f"level_2/term2/computer_organization/see/lecture_2(2).pdf", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "computer_organization_lab":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة معمارية وتنظيم الحاسوب (عملي)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/computer_organization/lab/exercises_{i}.pdf", "rb"))
# -----------------------------------------------------------------------------------------------------------------------
    elif call.data == "operating_systems":
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="operating_systems_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="operating_systems_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(call.message.chat.id, "اختر القسم (مبادئ نظم التشغيل)", reply_markup=reply_markup)

    elif call.data == "operating_systems_see":
        bot.send_message(call.message.chat.id, "جاري ارسال محاضرات مادة مبادئ نظم التشغيل (نظري)، يرجى الأنتظار !")
        for i in range(1, 10):
            bot.send_document(call.message.chat.id, open(f"level_2/term2/operating_systems/see/os_{i}.pptx", "rb"))
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif call.data == "operating_systems_lab":
        bot.send_message(call.message.chat.id, "لم يتم أضافة محاضرات مادة مبادئ نظم التشغيل (عملي) بعد !")
# -----------------------------------------------------------------------------------------------------------------------