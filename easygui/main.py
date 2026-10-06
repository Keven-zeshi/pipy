import easygui

# Exibe uma caixa de mensagem simples
easygui.msgbox("Olá! Bem-vindo ao EasyGUI.", title="Mensagem")

# Pergunta o nome do usuário
nome = easygui.enterbox("Qual é o seu nome?", title="Entrada de Nome")

# Verifica se o usuário digitou algo
if nome:
  # Pergunta do tipo Sim/Não
  continuar = easygui.ynbox(
      f"Prazer, {nome}. Você gosta de programar em Python?",
      title="Pergunta",
      choices=("Sim", "Não"),
  )

  if continuar:
    easygui.msgbox("Que ótimo! Continue praticando.", title="Sucesso")
  else:
    easygui.msgbox("Sem problemas, há muitas outras áreas!", title="Até logo")
else:
    easygui.msgbox("Você cancelou a operação.", title="Cancelado")
