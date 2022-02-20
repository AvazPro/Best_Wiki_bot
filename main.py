from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
import settings
import requests

updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update, context: CallbackContext):

	update.message.reply_text('Assalom aleykum! Wikipediada ma`lumot qidiruvchi '
	'botga hush kelibsiz! Biron nima izlash uchun /search '
	 'va so`rovingizni yozing. Misol uchun /search Steve Jobs')
	 
def search(update: Update, context:CallbackContext):
	args = context.args
	search_text = ''.join(args)
	response = requests.get('https://en.wikipedia.org/w/api.php',{
		'action':'opensearch',
		'search': search_text,
		'limit': 1,
		'namespace': 0,
		'format':'json',
		}),

result = 'response.json()'
     
link = result[3]

if len(link):
			print(link[0])
else:
			update.message\
			.reply_text('Sizning so`rovimgiz bo`yicha hech nima yo`q')	
print('none')

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start)) 
dispatcher.add_handler(CommandHandler('search', search)) 


updater.start_polling()
updater.idle()