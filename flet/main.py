import flet as ft

def main(page: ft.Page):
    # Configurações modernas da janela do aplicativo
    page.title = "Super App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 480
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK # Começa no modo escuro por padrão

    # Elementos de entrada e feedback
    input_nome = ft.TextField(
        label="Nome do participante", 
        hint_text="Digite um nome para adicionar à lista...", 
        width=320,
        border_radius=10
    )
    
    texto_resultado = ft.Text(
        value="Nenhum participante adicionado ainda.", 
        size=14, 
        italic=True, 
        color=ft.Colors.GREY_500
    )

    # Lista visual dinâmica para exibir os nomes cadastrados
    lista_usuarios = ft.ListView(
        expand=True, 
        spacing=10, 
        padding=10,
        height=180 # Limita a altura para criar uma barra de rolagem se tiver muitos nomes
    )

    # Contador visual de quantos nomes foram adicionados
    contador_status = ft.Text(value="Total: 0 participantes", weight=ft.FontWeight.W_500)

    # Função para alternar entre Modo Claro e Modo Escuro
    def alternar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            botao_tema.icon = ft.Icons.DARK_MODE
            botao_tema.tooltip = "Mudar para Modo Escuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            botao_tema.icon = ft.Icons.LIGHT_MODE
            botao_tema.tooltip = "Mudar para Modo Claro"
        page.update()

    # Botão de tema posicionado no topo
    botao_tema = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        tooltip="Mudar para Modo Claro",
        on_click=alternar_tema
    )

    # Função interna para remover um nome da lista
    def deletar_nome(e):
        # 'e.control.data' guarda o container da linha inteira que queremos deletar
        lista_usuarios.controls.remove(e.control.data)
        
        # Atualiza a contagem de pessoas restantes
        total = len(lista_usuarios.controls)
        contador_status.value = f"Total: {total} participantes"
        
        if total == 0:
            texto_resultado.value = "Todos os participantes foram removidos."
            texto_resultado.color = ft.Colors.ORANGE
            
        page.update()

    # Função de evento ativada pelo clique do botão Adicionar
    def acao_botao(e):
        nome_digitado = input_nome.value.strip()
        
        if nome_digitado:
            # Cria uma linha estilizada para o novo usuário com botão de lixeira incorporado
            linha_usuario = ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLUE_ACCENT),
                        ft.Text(nome_digitado, size=16, weight=ft.FontWeight.W_500),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                padding=10,
                border_radius=8,
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
            )

            # Cria o botão de deletar e passa a linha inteira dentro da propriedade 'data'
            botao_deletar = ft.IconButton(
                icon=ft.Icons.DELETE_OUTLINE,
                icon_color=ft.Colors.RED_400,
                data=linha_usuario,
                on_click=deletar_nome
            )
            
            # Adiciona o botão de deletar no final da nossa linha do usuário
            linha_usuario.content.controls.append(botao_deletar)

            # Insere o bloco visual completo dentro da nossa lista vertical
            lista_usuarios.controls.append(linha_usuario)
            
            # Atualiza textos de sucesso e contagem
            texto_resultado.value = f"'{nome_digitado}' adicionado com sucesso!"
            texto_resultado.color = ft.Colors.GREEN
            contador_status.value = f"Total: {len(lista_usuarios.controls)} participantes"
            
            # Limpa o campo de texto automaticamente para o próximo nome
            input_nome.value = ""
        else:
            texto_resultado.value = "Por favor, digite um nome válido!"
            texto_resultado.color = ft.Colors.RED

        page.update()

    # Botão moderno adaptado para Flet 1.0+
    botao_confirmar = ft.Button(
        content="Adicionar na Lista", 
        icon=ft.Icons.ADD, 
        on_click=acao_botao
    )

    # Card principal unificado contendo toda a interface organizada por colunas
    card_conteudo = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Row([
                        ft.Text("Membros do Projeto", size=22, weight=ft.FontWeight.BOLD),
                        botao_tema
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    input_nome,
                    botao_confirmar,
                    ft.Divider(),
                    
                    ft.Row([
                        ft.Text("Lista Cadastrada:", size=14, weight=ft.FontWeight.BOLD),
                        contador_status
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    lista_usuarios, # Aqui aparecem as caixas com nomes dinamicamente
                    ft.Divider(),
                    texto_resultado,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12,
            ),
            padding=20,
        )
    )

    # Adiciona a estrutura final à tela
    page.add(card_conteudo)

if __name__ == "__main__":
    ft.run(main)
