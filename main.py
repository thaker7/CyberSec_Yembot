from reply import *
from level1 import *
from level2 import *
from host import keep_alive

# -------------------- الأوامر --------------------
@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.reply_to(msg, "🛡 مرحبا بك " + msg.chat.first_name + ' ' + msg.chat.last_name + " في قناة الأمن السيبراني\n\nالقناة تحوي كل محاضرات تخصص الأمن السيبراني\n\n- ارسل كلمة [قائمه] لعرض كل المواد 👍\n- ارسل [اسم الماده] مباشرة 👍")
# -------------------- الردود --------------------
@bot.message_handler(func=lambda msg : True)
def reply_message(msg):
    reply_func(msg)
# -------------------- ازرار شفافه --------------------
@bot.callback_query_handler(func=lambda call : True)
def calling(call):
    call_plan(call)
    call_level1(call)
    call_level2(call)

keep_alive()
bot.polling()