from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def make_menu(items, prefix):
    keyboard = []
    for i in items:
        keyboard.append([
            InlineKeyboardButton(i, callback_data=f"{prefix}|{i}")
        ])
    return InlineKeyboardMarkup(keyboard)
