import telebot
import Constants

apiKey = Constants.API_KEY

bot = telebot.TeleBot(apiKey)

#Start message
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot. Use /help to see what I can do.")

#Help message
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /ListOKGroupsID \n /ListNotOKGroupsID \n /sendTestLinks(DevTool) \n to report links as ok or not ok use: \n /ok + link_1; link_2 \n /notOK + link_1; link_2 \n multilinking is possible by seperating with a ;")

#Dev Tool to send links
@bot.message_handler(commands=['sendTestLinks']) # This is a developer Tool and should not be used in the final version
def sendTestLinks(message): 
        for i in range(2):
            bot.reply_to(message, "Here are following links: \n https://www.google.com")


#Eval Links
@bot.message_handler(commands=['ok'])
def linkOK(message):
    links = message.text 
    links = links.replace("/ok", "").strip()
    links = links.split(";")
    bot.reply_to(message, "Here are following links marked as ok:")

    groupedLinks = "\n"

    for link in links:
        groupedLinks = groupedLinks + str(link).strip() + "\n"

    bot.reply_to(message, groupedLinks)

    bot.reply_to(message, "These links will be forwarded to the according Groups")
    for chatID in Constants.OK_Group:
        bot.send_message(chat_id=chatID, text = groupedLinks + "These Links are OK")

@bot.message_handler(commands=['notOK'])
def linkNotOK(message):
    links = message.text 
    links = links.replace("/notOK", "").strip()
    links = links.split(";")
    bot.reply_to(message, "Here are following links marked as not ok:")

    groupedLinks = "\n"

    for link in links:
        groupedLinks = groupedLinks + str(link).strip() + "\n"

    bot.reply_to(message, groupedLinks)

    bot.reply_to(message, "These links will be forwarded to the according Groups")

    for chatID in Constants.Not_OK_Group:
        bot.send_message(chat_id=chatID, text = groupedLinks + "These Links are not OK")




##Listing Groups
#List Groups for link is "OK Groups"
@bot.message_handler(commands=['ListOKGroups'])
def ListOKGroupsMessage(message):
    groupString = "\n"
    for group in Constants.OK_Group:
        groupString = groupString + f"{group} \n" 

    bot.reply_to(message, "Here are the following groups marked with ok:" + groupString)

#List Groups for link is "not OK Groups"
@bot.message_handler(commands=['ListNotOKGroups'])
def ListNotOKGroupsMessage(message):
    groupString = "\n"
    for group in Constants.Not_OK_Group:
        groupString = groupString + f"{group} \n" 

    bot.reply_to(message, "Here are the following groups marked with not ok:" + groupString)
    
"""   
##Add member to groups
#Add member for link is "OK Groups"

@bot.message_handler(commands=['AddToOKGroup'])
def AddToOKGroup(message):
    group = message.text
    Constants.OK_Group.append(group.replace("/AddToOKGroup", "").strip())


#add member Groups for link is "not OK Groups"
"""
print("Hey, I am up....")
bot.polling()