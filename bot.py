from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext
)

from config import BOT_TOKEN
from data.syllabus import BRANCHES
from notes.text_notes import get_text_notes
from image_notes.image_generator import generate_image
from ai.ai_explainer import explain_topic
from keyboards.menus import make_menu


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Select Branch:",
        reply_markup=make_menu(BRANCHES.keys(), "BRANCH")
    )


def handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    level, value = query.data.split("|")

    if level == "BRANCH":
        context.user_data["branch"] = value
        query.edit_message_text(
            "Select Semester:",
            reply_markup=make_menu(BRANCHES[value].keys(), "SEM")
        )

    elif level == "SEM":
        branch = context.user_data["branch"]
        context.user_data["sem"] = value
        query.edit_message_text(
            "Select Subject:",
            reply_markup=make_menu(BRANCHES[branch][value], "SUB")
        )

    elif level == "SUB":
        context.user_data["subject"] = value
        topics = list(get_text_notes(value, None).keys())

        query.edit_message_text(
            "Select Topic:",
            reply_markup=make_menu(topics, "TOPIC")
        )

    elif level == "TOPIC":
        context.user_data["topic"] = value
        query.edit_message_text(
            "Choose Output:",
            reply_markup=make_menu(
                ["Text Notes", "Image Notes", "Ask AI"],
                "OUT"
            )
        )

    elif level == "OUT":
        subject = context.user_data["subject"]
        topic = context.user_data["topic"]

        if value == "Text Notes":
            query.edit_message_text(get_text_notes(subject, topic))

        elif value == "Image Notes":
            img = generate_image(topic, get_text_notes(subject, topic))
            query.message.reply_photo(photo=open(img, "rb"))

        elif value == "Ask AI":
            query.edit_message_text("🤖 Thinking...")
            ai_text = explain_topic(subject, topic)
            query.edit_message_text(ai_text)


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
