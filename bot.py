from ai.ai_explainer import explain_topic
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from keyboards.menus import make_menu
from data.syllabus import BRANCHES
from notes.text_notes import SUBJECT_NOTES, get_text_notes
from image_notes.image_generator import generate_image

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to B.Tech Bot\nSelect Branch:",
        reply_markup=make_menu(BRANCHES.keys(), "BRANCH")
    )

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    level, value = query.data.split("|")

    if level == "BRANCH":
        context.user_data["branch"] = value
        await query.edit_message_text(
            "Select Semester:",
            reply_markup=make_menu(BRANCHES[value].keys(), "SEM")
        )

    elif level == "SEM":
        branch = context.user_data["branch"]
        context.user_data["sem"] = value
        await query.edit_message_text(
            "Select Subject:",
            reply_markup=make_menu(BRANCHES[branch][value], "SUB")
        )

    elif level == "SUB":
        context.user_data["subject"] = value
        topics = SUBJECT_NOTES.get(value, {}).keys()

        if not topics:
            await query.edit_message_text("Topics coming soon 🙂")
            return

        await query.edit_message_text(
            "Select Topic:",
            reply_markup=make_menu(topics, "TOPIC")
        )


    elif level == "TOPIC":
        context.user_data["topic"] = value
        await query.edit_message_text(
            "Choose Output:",
            reply_markup=make_menu(["Text Notes", "Image Notes", "Ask AI"], 
            "OUT")
    )

    elif level == "OUT":
        subject = context.user_data["subject"]
        topic = context.user_data["topic"]

        if value == "Text Notes":
            notes = get_text_notes(subject, topic)
            await query.edit_message_text(notes)

        elif value == "Image Notes":
            notes = get_text_notes(subject, topic)
            img = generate_image(topic, notes)
            await query.message.reply_photo(photo=open(img, "rb"))

        elif value == "Ask AI":
            await query.edit_message_text("🤖 Thinking...")
            ai_text = explain_topic(subject, topic)
            await query.edit_message_text(ai_text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handler))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
