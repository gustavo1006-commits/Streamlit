import streamlit as st
from streamlit_extras.let_it_rain import rain
import time
import os
from pathlib import Path

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Para o Meu Amor", page_icon="❤️")

# --- LÓGICA PARA ENCONTRAR AS IMAGENS ---
# Isso garante que o Streamlit encontre as fotos dentro da pasta 'pratica'
diretorio_atual = Path(__file__).parent

def carregar_imagem(nome_arquivo):
    caminho_completo = diretorio_atual / nome_arquivo
    if caminho_completo.exists():
        return str(caminho_completo)
    return None

# --- CONTEÚDO DO APP ---
st.title("Não Desista da Gente Amor 💌💘")

st.subheader("Oi, minha princesa linda! Espero que você esteja bem e que Deus esteja te protegendo e cuidando de você. Mas eu sei que Ele está, segurando sua mão em cada passo e te dando a força necessária para enfrentar esse momento difícil. 🙏")

def carinho():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

if st.button("Clique para receber amor"):
    carinho()

# --- EXIBIÇÃO DAS IMAGENS ---
col1, col2, col3 = st.columns(3)

with col1:
    img1 = carregar_imagem("imagem1.jfif")
    if img1: st.image(img1, width=150, caption="Você é a razão do meu sorriso.❤️")
    
    img2 = carregar_imagem("imagem2.jfif")
    if img2: st.image(img2, width=150, caption="Te amo mais do que palavras podem dizer.❤️")

with col2:
    img3 = carregar_imagem("imagem3.jfif")
    if img3: st.image(img3, width=150, caption="Você é meu sonho que se tornou realidade.❤️")
    
    img4 = carregar_imagem("imagem4.jfif")
    if img4: st.image(img4, width=150, caption="Seu amor é meu maior tesouro.❤️")

with col3:
    img5 = carregar_imagem("imagem5.jfif")
    if img5: st.image(img5, width=150, caption="Amo cada detalhe que te faz único.❤️")
    
    img6 = carregar_imagem("imagem6.jfif")
    if img6: st.image(img6, width=150, caption="Estar ao seu lado é meu lugar favorito.❤️")

# --- TEXTOS ---
st.write("---") # Linha divisória
st.write("**Duda, meu grande amor,** Espero que você goste desta surpresa. Estou aqui para dizer que está sendo muito difícil ficar sem você ao meu lado. O modo como me apaixonou por você é inexplicável; é um amor que nem todas as palavras do mundo poderiam descrever. Eu te amo como nunca amei ninguém.")

st.write("Quero que saiba que esse sentimento não é dependência, é o amor mais verdadeiro, minha princesa. Me apaixonei por você por completo: por cada detalhe, pelos seus olhos, pelo seu doce sorriso e pela pessoa incrível que você é. Me apaixonei até pelas letras do seu nome e pelo som da sua voz. Adoro te ver feliz! Sou, e sempre serei, completamente apaixonado por você. 💘")

st.info("Duda, eu entendo sua decisão e sei o quanto essa fase está sendo difícil para você. Entre os problemas da família e o cansaço do trabalho, eu sei que seu peso está grande.")

st.text("Queria estar aí para segurar sua mão, pois acredito que o companheirismo é a base de tudo. Mas respeito seu tempo e seu espaço. Estou aqui focando na minha evolução com Deus e me tornando o homem que Ele deseja que eu seja.")

st.text("Quando você estiver pronta para pensar em nós, faça isso com carinho e oração. Eu te prometo: vou te fazer a mulher mais feliz do mundo. Estamos aprendendo com os erros, e meu coração está voltado para o nosso futuro.")

st.text("Desde o dia em que você terminou comigo, eu não sei mais o que é dormir direito. Acordo a noite toda e sonho com a gente juntos todos os dias. Acordo na madrugada só para ver se você enviou alguma mensagem... Sinto que perdi uma parte de mim, aquela parte que me completava diariamente.")

st.text("Mas está tudo bem. Eu vou estar aqui te esperando, não importa quanto tempo leve. Vou esperar você ficar bem e estarei aqui como um novo homem. Penso em você toda hora, em todos os momentos e em qualquer lugar que eu vá. Onde você está, eu estou; o meu pensamento te segue, minha saudade te persegue e, claro, o meu amor não envelhece.")

st.text("Você não sai da minha mente e eu nem quero que saia. Eu quero é você, eu amo só você. Vou estar aqui, meu amor, te esperando... 💘")
        
st.title("EU TE AMOOOO MEU AMOR❤️")

st.write("✨ **Você é meu mundo/meu tudo/meu tesouro/minha outra metade.**")
st.write("✨ **Você me completa/me faz feliz.**")
st.write("✨ **Eu sou apaixonado por você/Estou perdidamente apaixonado.**")
st.write("✨ **Eu não me imagino sem você.**")
st.write("✨ **Você é a pessoa que eu escolho todos os dias.**")
st.write("✨ **Você é a menina dos meus olhos.**")

st.success("É isso, meu amor. Vou te deixar no seu tempo e vou estar aqui orando todos os dias pela gente. Quando estiver bem, volta, por favor, minha razão de viver. Eu te amo eternamente! Estou aqui te esperando, viu? Beijos, cuida da sua família e de você também. 🙏💘")