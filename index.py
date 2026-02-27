#importando as bibliotecas
from selenium import webdriver #abre e contrala o navegador sozinho
from selenium.webdriver.common.by import By #o tipo de busca, o que ele vai buscar
from selenium.webdriver.common.keys import Keys #vai permitir que o bot use as teclas do teclado
import time #trabalhando com o tempo para não fazer o whatsapp cair

#Configuração do navegador
driver = webdriver.Chrome()  
driver.get("https://web.whatsapp.com")

print("Escaneie o QR code...")
time.sleep(30) #tempo para escanear o QR code

print("Bot iniciado.")

#Função para enviar mensagem 
def send_message(text):
    text_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    text_box.send_keys(text)
    text_box.send_keys(Keys.ENTER)

#Função para responder as mensagens

def answer_text():
    try:
        #Coleta todas as mensagens recebidas
        messages = driver.find_elements(By.CLASS_NAME, "message-in")
        
        if messages:
            last_message = messages[-1].text

            #Logica simples de resposta 
            if "oi" in last_message.lower():
                send_message("Olá, Eu sou um bot de automação!")

            elif "Tchau" in last_message.lower():
                send_message("Até mais!")
            
            else: 
                send_message("Estou aprendendo ainda. Desculpe.")

    except:
        pass

last_answer = ""

def answer_text():
    global last_answer # Usamos global para alterar a variável fora da função
    try:
        messages = driver.find_elements(By.CLASS_NAME, "message-in")
        
        if messages:
            last_message = messages[-1].text.lower()

            # SÓ RESPONDE SE A MENSAGEM FOR NOVA
            if last_message != last_answer:
                print(f"Nova mensagem encontrada: {last_message}")
                
                if "oi" in last_message:
                    send_message("Olá, Eu sou um bot de automação!")
                elif "tchau" in last_message:
                    send_message("Até mais!")
                else: 
                    send_message("Estou aprendendo ainda. Desculpe.")
                
                # Agora marcamos essa mensagem como respondida
                last_answer = last_message

    except Exception as e:
        print(f"Erro: {e}")


#Loop Infinito
while True:
    answer_text()
    time.sleep(5)