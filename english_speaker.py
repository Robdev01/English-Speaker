import customtkinter as ctk
from gtts import gTTS
import playsound
import os
import threading
from tkinter import messagebox

# === CONFIGURAÇÕES DO TEMA ===
ctk.set_appearance_mode("dark")  # dark | light | system
ctk.set_default_color_theme("blue")

# === FUNÇÃO DE FALA ===
def speak_text():
    text = text_box.get("0.0", "end").strip()
    if not text:
        messagebox.showwarning("Aviso", "Digite um texto em inglês primeiro!")
        return

    def run_tts():
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            filename = "voice_temp.mp3"
            tts.save(filename)
            playsound.playsound(filename)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        finally:
            if os.path.exists(filename):
                os.remove(filename)

    threading.Thread(target=run_tts).start()

# === JANELA PRINCIPAL ===
app = ctk.CTk()
app.title("English Speaker 🎧")
app.geometry("480x380")
app.resizable(False, False)

# === TÍTULO ===
title_label = ctk.CTkLabel(app, text="Digite o texto em inglês", font=("Segoe UI", 18, "bold"))
title_label.pack(pady=(25, 10))

# === CAIXA DE TEXTO ===
text_box = ctk.CTkTextbox(app, width=400, height=180, corner_radius=10, font=("Segoe UI", 13))
text_box.pack(pady=10)

# === BOTÃO DE FALAR ===
speak_button = ctk.CTkButton(app, text="🔊 Falar", command=speak_text, width=180, height=40, corner_radius=12, font=("Segoe UI", 14, "bold"))
speak_button.pack(pady=20)

# === RODAPÉ ===
footer_label = ctk.CTkLabel(app, text="Criado por Robson Calheira com Python", font=("Segoe UI", 11), text_color="gray")
footer_label.pack(pady=5)

# === LOOP PRINCIPAL ===
app.mainloop()
