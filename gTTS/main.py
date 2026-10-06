import os
from gtts import gTTS

# 1. Defina o texto que você quer que o robô fale
texto = "Olá! Esse é um teste de voz usando a biblioteca gTTS no seu baguiete."

# 2. Crie o objeto com o texto e o idioma (pt = português)
# tld="com.br" deixa o sotaque mais natural do Brasil
tts = gTTS(text=texto, lang="pt", tld="com.br", slow=False)

# 3. Salve o resultado em um arquivo de áudio
arquivo_audio = "audio_teste.mp3"
tts.save(arquivo_audio)

print(f"Áudio gerado com sucesso e salvo como: {arquivo_audio}")

# 4. (Opcional) Tenta tocar o áudio automaticamente no seu computador
# Funciona no Windows, Mac e Linux
try:
    os.system(f"start {arquivo_audio}" if os.name == "nt" else f"xdg-open {arquivo_audio}")
except Exception:
    print("Pronto! Agora é só abrir o arquivo .mp3 gerado para ouvir.")
