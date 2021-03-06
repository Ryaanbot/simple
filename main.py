import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/5180774841/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/5180774841')
   open(f"Users/5180774841/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 16625296
API_HASH = "a0dbae3d77218acb564bdf996ef990a7"
BOT_TOKEN = "5249125506:AAFOH8I-ZqayBi3zRVF30_xWNiIgo19Ovjk"
UPDATES_CHANNEL = "StarBotKanal"
OWNER= [1956262807]
PREMIUM=[1956262807]
bot = pyrogram.Client("bot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   return 0



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("??????????????? ????????????????????????????????? ??????????????????", url=f"https://t.me/ByWolk")],[InlineKeyboardButton("??? ????????????????????", callback_data="Login"), InlineKeyboardButton("?????? ?????????????? ????????????????", callback_data="Adding") ],[InlineKeyboardButton("?????? ???????????????????????? ????????????????", callback_data="Edit"), InlineKeyboardButton("???? ????????????????????????????????????", callback_data="Ish")],[InlineKeyboardButton("??????? ???????????????????????? ????????????", callback_data="Removeall"), InlineKeyboardButton("??? ???????????????????? ????????????????????", callback_data="Admin")],[InlineKeyboardButton("???????? ???????????????????? ????????????????????", url=f"https://t.me/StarBotKanal")]])
   await message.reply_text(f"??? **Merhaba** {message.from_user.mention} **\n\n??? Ben ??ye ??ekme Botuyum ,\n\n?? Bu Botu Kullanmak ??stiyorsan??z \nA??a????daki ??????????????? ??letisim ??????????????? Butonuna \nT??klay??p Yard??m ??steyebilirsiniz . . . \n\n ???> `Tamamen ??cretsizdir . . .` **", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@bot.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**??? Premium Kullan??c?? de??ilsiniz .**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await bot.ask(chat_id=message.chat.id, text="**??? Giri?? yapmak i??in ka?? hesap ekleyecekseniz . . .**")
      n = int(number.text)
      a+=n
      if n<1 :
         await bot.send_message(message.chat.id, """**??? Ge??ersiz Bi??im En Az 1 Say?? Girin . . .**""")
         return
      if a>100:
         await bot.send_message(message.chat.id, f"**??? Telefon numaras??n?? d??zg??n girin . . .**")
         return
      for i in range (1,n+1):
         number = await bot.ask(chat_id=message.chat.id, text="**??? ??imdi Telegram Hesab??n??z??n Telefon Numaras??n?? Girin . \n\n??rnek: **+14154566376 => 14154566376 ??eklinde**")
         phone = number.text
         if "+" in phone:
            await bot.send_message(message.chat.id, """** + Olmadan tekrar deneyin .**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await bot.send_message(message.chat.id, f"**{n}). Telefon: {phone} Ba??ar??yla Ayarland?? ???**")
         else:
            await bot.send_message(message.chat.id, """**??? Ge??ersiz Say?? Bi??imi Tekrar deneyin**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await bot.send_message(message.chat.id, f"**??? Hata: {e}**")
   return



# ------------------------------- Acc Login --------------------------------- #
@bot.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**??? Premium Kullan??c?? de??ilsiniz .**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"{e.x} Saniyelik Flood Var")
            return
         except PhoneNumberInvalidError:
            await message.reply("**??? Telefon Numaran??z Ge??ersiz.\n\nYeniden Ba??lamak i??in /start'a bas??n !**")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} yasakland??")
            continue
         try:
            otp = await bot.ask(message.chat.id, ("**??? Telefon numaran??za bir KOD g??nderildi, \nL??tfen KOD'u < 1 2 3 4 5 > ??eklinde girin. \n( Her say?? aras??ndaki bo??luk olmal?? !)**"), timeout=300)
         except TimeoutError:
            await message.reply("**Zaman S??n??r??na Ula????ld?? .\nYeniden Ba??lamak i??in /start'a bas??n !**")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("**Ge??ersiz Kod.\n\nYeniden Ba??lamak i??in /start'a bas??n !**")
            return
         except PhoneCodeExpiredError:
            await message.reply("**Kodun S??resi Doldu.\n\nYeniden Ba??lamak i??in /start'a bas??n !**")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await bot.ask(message.chat.id,"**Hesab??n??z??n ??ki Ad??ml?? Do??rulamas?? Var .\nL??tfen Parolan??z?? Girin .**",timeout=300)
            except TimeoutError:
               await message.reply("`Zaman S??n??r??na Ula????ld?? .\n\nYeniden Ba??lamak i??in /start'a bas??n !`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await bot.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/5180774841/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/5180774841/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="**??yi haber, ??u anda hesab??n??za herhangi bir s??n??r uygulanm??yor. bir ku?? kadar ??zg??rs??n** ???"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await bot.send_message(message.chat.id, f"Ba??ar??yla Giri?? Yap??ld??. ???\n\n**??sim :** {me.first_name}\n**Kullan??c?? Ad?? :** {me.username}\n**Numara :** {phone}\n**SpamBot :** {stats}**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await bot.send_message(message.chat.id, "**Telefon numaras??n?? girmediniz /start ile d??zenleyin.**")  
     except Exception as e:
      await bot.send_message(message.chat.id, f"**Error: {e}**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await bot.send_message(message.chat.id, f"**Giri?? Hesapi {s} Mevcut Hesap {po}**") 
 except Exception as e:
   await bot.send_message(message.chat.id, f"**Error: {e}**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@bot.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**??? Premium Kullan??c?? de??ilsiniz .**")
      return
   number = await bot.ask(chat_id=message.chat.id, text="**???> ??yesini Almak ??stedi??iniz Grubun Kullan??c?? Ad??n?? G??nderin (Link De??il)**")
   From = number.text
   number = await bot.ask(chat_id=message.chat.id, text="**???> ??yeyi Aktarmak ??stedi??iniz Grubun Kullan??c?? Ad??n?? G??nderin (Link De??il)**")
   To = number.text
   number = await bot.ask(chat_id=message.chat.id, text="**???> Ba??lang???? ????in Bir Say?? Belirleyin**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await bot.send_message(chat_id=message.chat.id, text=f"**???> ??ye ??ekme Ba??lat??ld?? ???**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nCreator ??????????????? @bywolk**"
                     await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     await bot.send_message(message.chat.id, f"**Error: {phone} Sonrakine Ge??erken Hata Olu??tu .**")
                     break
                  if dad>40:
                     r+="**\nCreator ??????????????? @bywolk**"
                     await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Ba??lang???? ??????Ekleme**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'Ba??arili'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nCreator ??????????????? @bywolk**"
                  await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                  await bot.send_message(chat_id=message.chat.id, text=f'**{s.seconds} Flood .\nSonraki Numaraya Ge??iliyor**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="Kullan??c?? Banl??"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await bot.send_message(chat_id=message.chat.id, text=f"{r}")
                     await bot.send_message(chat_id=message.chat.id, text=f"**??ok Fazla Flood .\nSonraki Numaraya Ta????n??yor**")
                     break
                  status = 'Flood'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}** ???> **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await bot.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Creator ??????????????? @bywolk")
 except Exception as e:
   await bot.send_message(message.chat.id, f"**Error: {e}\n\nCreator ??????????????? @bywolk**")
   return



# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**??? Premium Kullan??c?? de??ilsiniz .**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Kay??tl?? Numaralar :**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nCreator ??????????????? @bywolk**"
               await bot.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Kay??tl?? Numaralar**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nCreator ??????????????? @bywolk**"
         await bot.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@bot.on_message(filters.private & filters.command(["removeall"]))
async def removeall(lel, message):
 try:
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = []
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await bot.send_message(chat_id=message.chat.id,text="**??? Ba??ar??yla Tamamland??.**")
   except Exception as a:
      pass
 except Exception as e:
   await bot.send_message(message.chat.id, f"Error: {e}\n\nCreator ??????????????? @bywolk")
   return

@bot.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id not in PREMIUM:
      await bot.send_message(message.chat.id, f"**??? Premium Kullan??c?? de??ilsiniz .**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await bot.ask(chat_id=message.chat.id, text="**Kald??r??lacak Numaray?? G??nder .**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await bot.send_message(chat_id=message.chat.id,text="**??? Ba??ar??yla Tamamland?? .**")
   except Exception as a:
      pass
 except Exception as e:
   await bot.send_message(message.chat.id, f"**Error: {e}\n\nCreator ??????????????? @bywolk**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@bot.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("???????????????????????????????????????????????? ???", callback_data="Users")], [InlineKeyboardButton("???? ???????????????????????? ????????????", callback_data="Broadcast")],[InlineKeyboardButton("??????? ???????????????????????????????????? ????????????????", callback_data="New")], [InlineKeyboardButton("??????????????? ???????????????????????????????????????????????????? ????????????", callback_data="Check")]])
      await bot.send_message(chat_id=message.chat.id,text=f"**??? Merhaba** `{message.from_user.first_name}` **!\n\n??? ??ye Ekleme Bot'un Y??netici Paneline Ho?? Geldiniz .**", reply_markup=but)
   else:
      await bot.send_message(chat_id=message.chat.id,text="**Bot'un sahibi de??ilsiniz .**")



# ------------------------------- Buttons --------------------------------- #
@bot.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /login'e t??klaman??z yeterli.\n\nCreator ?????? @bywolk**""") 
   elif "Ish" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /phonesee'ye t??klaman??z yeterli.\n\nCreator ?????? @bywolk**""") 
   elif "Remove" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /removeall'a t??klaman??z yeterli.\n\nCreator ?????? @bywolk**""") 
   elif "Adding" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**Art??k bir ??ey yok..!\nGiri????? Hesaptan eklemeye ba??lamak i??in /adding t??klaman??z yeterli.\n\nCreator ?????? @bywolk**""") 
   elif "Edit" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /phone'a t??klaman??z yeterli.\n\nCreator ?????? @bywolk**""") 
   elif "Home" in k:
      await update.message.delete()
      await bot.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nEve Gitmek i??in /start'a t??klaman??z yeterli.\n\nCreator ?????? @bywolk**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await bot.send_message(update.message.chat.id,"L??tfen bekleyin...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**Yeni Kullan??c??n??n Kullan??c?? Kimli??ini G??nder\n\nCreator ?????? @bywolk**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await bot.send_message(chat_id=update.message.chat.id,text="Ba??ar??yla Tamamland??")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Creator ?????? @bywolk**"
         await bot.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Users???", callback_data="Users")], [InlineKeyboardButton("Broadcast????", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
         await bot.send_message(chat_id=update.message.chat.id,text=f"**Scraper Bot'un Y??netici Paneline Ho?? Geldiniz\n\nCreator ?????? @bywolk**", reply_markup=but)
      else:
         await bot.send_message(chat_id=update.message.chat.id,text="**Bot'un sahibi de??ilsiniz \n\nCreator ?????? @bywolk**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await bot.ask(chat_id=update.message.chat.id, text="**Yay??n i??in ??imdi ben mesaj??m\n\nCreator ?????? @bywolk**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await bot.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await bot.send_message(update.message.chat.id,f"{a} Sohbetlere Ba??ar??yla Yay??nland??\nBa??ar??s??z - {b} Sohbetlere!")
    except Exception as e:
      await bot.send_message(update.message.chat.id,f"**Hata: {e}\n\nCreator ?????? @bywolk**")




text = """
?????????????????????Members 
?????????????????? Scraping Bot
??????????????????
?????????????????? Scraper
?????????????????? Scraper Bot
??????????????????
?????????????????? 
?????????????????? 
"""
print(text)
print("Uyar??lm???? Ekleme Ba??ar??yla Ba??lad??........")
bot.run()
