import asyncio
import serial
import telegram

# Configurațiile Telegram
TOKEN = "7059496794:AAEBw5L60f6uM_dMtAGAt5eSgSZiCHQK30"
chat_id = '-4784110072'
bot = telegram.Bot(token=TOKEN)

# Configurația portului serial
SERIAL_PORT = "/dev/ttyUSB0"  # Poate fi alt port pe Raspberry Pi (ex: /dev/ttyACM0 sau /dev/ttyAMA0)
BAUD_RATE = 9600

# Funcția pentru a trimite mesaje Telegram
async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

# Funcția pentru a citi datele din portul serial
async def read_serial():
    # Deschide portul serial
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        while True:
            # Citește datele trimise de Arduino
            if ser.in_waiting > 0:
                message = ser.readline().decode('utf-8').strip()
                
                # Verifică mesajul și trimite mesajul corespunzător
                if message == "1":
                    await send_message("Totul functioneaza corespunzator", chat_id)
                elif message == "2":
                    await send_message("Urgenta, foc", chat_id)
                elif message == "3":
                    await send_message("Atentie, nivel ridicat mare de gaz", chat_id)
                elif message == "4":
                    await send_message("Umiditate ridicata", chat_id)
                elif message == "5":
                    await send_message("Temperatura ridicata", chat_id)
                else:
                    print(f"Mesaj necunoscut: {message}")

# Funcția principală care rulează codul asincron
async def main():
    await read_serial()

if __name__ == "__main__":
    asyncio.run(main())
