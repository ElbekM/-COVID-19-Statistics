import telebot
from telebot import types
from telebot import apihelper
from countryList import *
import COVID19Py

'''
Bot for tracking statistics of coronavirus cases around the world.

Statistic data provided by Worldwide Data repository operated by 
the Johns Hopkins University Center for Systems Science and Engineering 
(JHU CSSE)

Author: Elbek_M
'''

covid19 = COVID19Py.COVID19()

bot = telebot.TeleBot('YOUR TELEGRAM ID') #!!!PLACE YOUR ID!!!

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('List of countries')
	btn2 = types.KeyboardButton('Сases all over the world')
	markup.add(btn1, btn2)

	send_message = f"<b>Hello {message.from_user.first_name}!</b>\nTo get statistics on COVID-19" \
		f" enter the name of the country, for example: USA, Russia, Uzbekistan and etc.\n\n" \
        f"Statistic data provided by Worldwide Data repository operated by the " \
        f"Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == 'list of countries':
		final_message = listOfCountries()
	elif get_message_bot == 'сases all over the world':
		population = 7700100000
		location = covid19.getLatest()
		final_message = f"<u>Worldwide data:</u>\n<b>Сases: </b>{location['confirmed']:,}\n<b>Deaths: </b>{location['deaths']:,}\n" \
			f"Percentage of cases: {round(location['confirmed'] * 100 / population, 3):,}%"
	else:
		county_id = getByCountryName(get_message_bot)
		if (county_id):
			location = covid19.getLocationByCountryCode(county_id)
			date = location[0]['last_updated'].split("T")
			time = date[1].split(".")
			final_message = f"<u>Country-wide data:</u>\nPopulation: {location[0]['country_population']:,}\n" \
					f"Last updated: {date[0]} {time[0]}\n<b>" \
					f"Сases: </b>{location[0]['latest']['confirmed']:,}\n<b>Deaths: </b>" \
					f"{location[0]['latest']['deaths']:,}"
		else:
			final_message = 'Country not found'

	bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
