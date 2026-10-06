import gradio as gr


# 1. Defina a função que processará as entradas
def processar_dados(nome, idade, gosta_python, imagem):
  sentenca = f"Olá, {nome}! Você tem {idade} anos."

  if gosta_python:
    sentenca += " Que bom que você curte Python! 🐍"
  else:
    sentenca += " Quem sabe você não muda de ideia depois? 😉"

  # O Gradio lida com imagens de forma nativa (recebe e pode retornar imagens)
  # Neste exemplo simples, apenas checamos se o usuário enviou uma foto
  if imagem is not None:
    sentenca += " Ah, e vi que você enviou uma imagem de perfil!"

  return sentenca


# 2. Monte a interface gráfica estruturando os inputs e outputs
demo = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(
            label="Seu Nome", placeholder="Digite aqui...", lines=1
        ),
        gr.Slider(
            minimum=0, maximum=100, value=25, step=1, label="Sua Idade"
        ),
        gr.Checkbox(label="Eu amo programar em Python"),
        gr.Image(
            label="Envie uma Foto (Opcional)",
            type="pil",
            sources=["upload", "webcam"],
        ),
    ],
    outputs=gr.Textbox(label="Resultado da Análise", lines=3),
    title="🤖 Meu Primeiro App com Gradio",
    description="Insira os dados abaixo para ver a mágica do processamento em tempo real.",
    theme="soft",  # Temas integrados: "default", "ocean", "soft", "glass", etc.
)

# 3. Execute o aplicativo
if __name__ == "__main__":
  demo.launch()
  # Dica: adicione share=True em launch() para gerar um link público temporário e enviar para amigos!
