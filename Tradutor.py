import tkinter as tk
import googletrans
from googletrans import Translator


def traduzir_texto():
    texto_original = texto_input.get("1.0", tk.END).strip()
    idioma_destino = idioma_selecionado.get()

    translator = Translator()
    traducao = translator.translate(texto_original, dest=idioma_destino)
    texto_traduzido.delete("1.0", tk.END)
    texto_traduzido.insert(tk.END, traducao.text)


# Configuração da janela principal
janela = tk.Tk()
janela.title("Tradutor")
janela.geometry("360x300")

# para ver as configurações disponíveis
# print(janela.configure().keys())
# print(janela.configure().items())
print(janela.configure().values())

# para ver as cores disponíveis
print(janela.winfo_rgb("#d9d9d9"))
janela.configure(bg="#ffffff")

# Rótulo e entrada de texto para o texto original
# texto_label = tk.Label(janela, text="Texto original:")
# texto_label.pack()

texto_input = tk.Text(janela, height=5, width=40)
place_holder_input = "Digite o texto aqui..."
texto_input.insert(tk.END, place_holder_input)
padding = 5
texto_input.config(padx=padding, pady=padding)
texto_input.pack()

# Rótulo e caixa de seleção para o idioma de destino
idioma_label = tk.Label(janela, text="Selecione o idioma:")
idioma_label.configure(font="-family {Segoe UI} -size 12")
idioma_label.pack()

idiomas_disponiveis = googletrans.LANGUAGES
idioma_selecionado = tk.StringVar()
idioma_selecionado.set("portuguese")
caixa_selecao = tk.OptionMenu(janela, idioma_selecionado, *idiomas_disponiveis.values())
caixa_selecao.configure(font="-family {Segoe UI} -size 12")
caixa_selecao.pack()

# se quiser que o usuário digite o idioma
# idioma_selecionado_label = tk.Label(janela, text="Digite o idioma:")
# idioma_selecionado_label.pack()
# idioma_selecionado = tk.Entry(janela)
# idioma_selecionado.pack()

# Botão para realizar a tradução
botao = tk.Button(janela, text="Clique para traduzir", command=traduzir_texto)
botao.configure(bg="#84d4c9")
botao.configure(cursor="hand2")
botao.configure(font="-family {Segoe UI} -size 12")
botao.config(bd=5)
botao.pack()

# Rótulo e área de texto para o texto traduzido
# texto_traduzido_label = tk.Label(janela, text="Texto traduzido:")
# texto_traduzido_label.pack()

texto_traduzido = tk.Text(janela, height=5, width=40)
place_holder_out = "Tradução aparecerá aqui..."
texto_traduzido.insert(tk.END, place_holder_out)
padding = 5
texto_traduzido.config(padx=padding, pady=padding)
texto_traduzido.pack()

# Executa a janela principal
janela.mainloop()
