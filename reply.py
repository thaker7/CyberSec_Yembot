from level1 import *
from level2 import *

def reply_func(msg):
    if "سلام" in msg.text:
        bot.reply_to(msg, "وعليكم السلام ورحمة الله وبركاته \n\n ارسل [قائمة] أو [اسم الماده]")

    elif "help" in msg.text or "ساعد" in msg.text:
        bot.reply_to(msg, "اهلا " + msg.chat.first_name + " " + msg.chat.last_name + " من فضلك : \n\n 1) ارسل كلمة [قائمه] \n 2) ارسل [اسم الماده] مباشرة")

    elif "رئيس" in msg.text or "ريس" in msg.text:
        bot.reply_to(msg, "رئيس قسم الأمن السيبراني : د/ عزيز بن سماء ")

    elif "قائمة" in msg.text or "قائمه" in msg.text or "قايمه" in msg.text or "قايمة" in msg.text or "level" in msg.text or "مستوى" in msg.text:
        bot.reply_to(msg, "✔ اختر المستوى لاظهار المواد المتعلقه به", reply_markup=list_btn)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif "web design" in msg.text or "تصميم ويب" in msg.text or "تصميم الويب" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="web_design_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="web_design_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر القسم (تصميم الويب Level2_Term1)", reply_markup=reply_markup)
# ----------------------------------------------------------------------------------------------------------------------
    elif "c++ ds" in msg.text or "data structure" in msg.text or "هياكل البيانات" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="c++_ds_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="c++_ds_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر القسم (هياكل البيانات والخوازميات Level2_Term1)", reply_markup=reply_markup)
# ----------------------------------------------------------------------------------------------------------------------
    elif "java" in msg.text or "oop" in msg.text or "object oriented" in msg.text or "البرمجه الموجهه للكائنات" in msg.text or "البرمجة الموجهة للكائنات" in msg.text or "البرمجه الشيئيه" in msg.text or "البرمجة الشيئية" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="java_oop_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="java_oop_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر القسم (البرمجة الموجهة للكائنات Level2_Term1)", reply_markup=reply_markup)
# ----------------------------------------------------------------------------------------------------------------------
    elif "database2" in msg.text or "database 2" in msg.text or "introduction to database" in msg.text or "مقدمه الى قواعد البيانات" in msg.text or "مقدمة الى قواعد البيانات" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="database1_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="database1_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر القسم (مقدمة الى قواعد البيانات Level2_Term1)", reply_markup=reply_markup)
# ----------------------------------------------------------------------------------------------------------------------
    elif "linear algebra" in msg.text or "الجبر الخطي" in msg.text or "جبر خطي" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات كاملة", callback_data="linear_algebra_lectures")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر محاضرات (الجبر الخطي Level2_Term1)", reply_markup=reply_markup)
# ----------------------------------------------------------------------------------------------------------------------
    elif "discrete structure" in msg.text or "الهياكل المتقطعه" in msg.text or "الهياكل المتقطعة" in msg.text or "هياكل متقطعة" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="المحاضرات كاملة", callback_data="discrete_structures_lectures")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر محاضرات (الهياكل المتقطعة Level2_Term1)", reply_markup=reply_markup)
# ----------------------------------------------------------------------------------------------------------------------
    elif "principles netwotks" in msg.text or "data structure" in msg.text or "مبادئ البيانات" in msg.text or "مبادئ الشبكات" in msg.text or "شبكات 1" in msg.text or "شبكات1" in msg.text:
        keyboard = [
            [types.InlineKeyboardButton(text="نظري", callback_data="networks1_see"),
             types.InlineKeyboardButton(text="عملي", callback_data="networks1_lab")],
        ]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.reply_to(msg, "✔ اختر القسم (مبادئ الشبكات Level2_Term1)", reply_markup=reply_markup)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif "web development" in msg.text or "تطوير تطبيقات الويب" in msg.text or "تطوير الويب" in msg.text or "تطوير ويب" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة محاضرات مادة تطوير تطبيقات الويب بعد (Level2_Term2)")
    # ----------------------------------------------------------------------------------------------------------------------
    elif "database security" in msg.text or "database management" in msg.text or "database2" in msg.text or "database 2" in msg.text or "امن قواعد بيانات" in msg.text or "أمن قواعد بيانات" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة محاضرات مادة أمن وأدارة قواعد البيانات بعد (Level2_Term2)")
    # ----------------------------------------------------------------------------------------------------------------------
    elif "computer network" in msg.text or "network2" in msg.text or "network 2" in msg.text or "شبكات حاسوب" in msg.text or "شبكات كمبيوتر" in msg.text or "شبكات 2" in msg.text or "شبكات2" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة محاضرات مادة شبكات الحاسوب بعد (Level2_Term2)")
    # ----------------------------------------------------------------------------------------------------------------------
    elif "principles cryptography" in msg.text or "crypto" in msg.text or "encryp" in msg.text or "مبادئ تشفير" in msg.text or "تشفير" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة محاضرات مادة مبادئ التشفير بعد (Level2_Term2)")
    # ----------------------------------------------------------------------------------------------------------------------
    elif "computer organiz" in msg.text or "computer archite" in msg.text or "organiz" in msg.text or "archite" in msg.text or "معمارية" in msg.text or "معماريه" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة محاضرات مادة معمارية وتنظيم الحاسوب بعد (Level2_Term2)")
    # ----------------------------------------------------------------------------------------------------------------------
    elif "operating system" in msg.text or "system" in msg.text or "organization" in msg.text or "نظم تشغيل" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة محاضرات مادة مبادئ نظم التشغيل بعد (Level2_Term2)")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    else:
        bot.reply_to(msg, "الرجاء ارسال [قائمة] أو [أسم الماده]، والاقلاع عن اللعب 😒")
'''
    elif "database" in msg.text or "db" in msg.text or "قاعدة" in msg.text or "قاعده" in msg.text or "قواعد" in msg.text:
        bot.reply_to(msg,"لم تتم الأضافة بعد")

    elif "network" in msg.text or "net" in msg.text or "شبكات" in msg.text or "شبكه" in msg.text or "شبكة" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة المحاضرات بعد")

    elif "encryp" in msg.text or "تشفير" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة المحاضرات بعد")

    elif "system" in msg.text or "نظم" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة المحاضرات بعد")

    elif "computer" in msg.text or "حاسوب" in msg.text or "معماريه" in msg.text or "معمارية" in msg.text or "تنظيم" in msg.text:
        bot.reply_to(msg, "لم يتم أضافة المحاضرات بعد")
        
            elif "شعار" in msg.text:
        bot.send_photo(msg.chat.id, open("img/1.jpg","rb"))
'''