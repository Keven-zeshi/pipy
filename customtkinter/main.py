import customtkinter as ctk

# Configurações globais de aparência (Tema do Sistema, Escuro ou Claro)
ctk.set_appearance_mode("System")  # Opções: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opções: "blue", "green", "dark-blue"


class MeuApp(ctk.CTk):

  def __init__(self):
    super().__init__()

    # Configuração da janela principal
    self.title("Exemplo CustomTkinter")
    self.geometry("450x300")
    self.resizable(False, False)

    # --- Elementos da Interface (Widgets) ---

    # Título principal
    self.label_titulo = ctk.CTkLabel(
        self,
        text="Bem-vindo ao CustomTkinter!",
        font=ctk.CTkFont(size=20, weight="bold"),
    )
    self.label_titulo.pack(padx=20, pady=(20, 10))

    # Campo de Entrada (Entry) para o nome
    self.entry_nome = ctk.CTkEntry(
        self, placeholder_text="Digite o seu nome...", width=250
    )
    self.entry_nome.pack(padx=20, pady=10)

    # Botão Interativo
    self.botao_enviar = ctk.CTkButton(
        self, text="Confirmar", command=self.acao_botao
    )
    self.botao_enviar.pack(padx=20, pady=10)

    # Texto de Resultado (Label dinâmico)
    self.label_resultado = ctk.CTkLabel(
        self, text="", font=ctk.CTkFont(size=14, slant="italic")
    )
    self.label_resultado.pack(padx=20, pady=20)

  # --- Funções de Evento (Callbacks) ---
  def acao_botao(self):
    nome_usuario = self.entry_nome.get()

    if nome_usuario.strip() != "":
      # Altera o texto do label na tela dinamicamente
      self.label_resultado.configure(
          text=f"Olá, {nome_usuario}! Sua interface moderna está funcionando.",
          text_color="#10b981",  # Cor verde (sucesso)
      )
    else:
      self.label_resultado.configure(
          text="Por favor, digite um nome válido!",
          text_color="#ef4444",  # Cor vermelha (erro)
      )


# Inicializa e roda o aplicativo
if __name__ == "__main__":
  app = MeuApp()
  app.mainloop()
