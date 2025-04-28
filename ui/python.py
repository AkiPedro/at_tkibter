import tkinter as tk

def salvar_nome():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    
    if nome and endereco:
        with open("cadastro_salvo.txt", "a") as arquivo:  
            arquivo.write(f"Nome salvo: {nome}\n")  
            arquivo.write(f"Endereco salvo: {endereco}\n\n")
        label_status.config(text="Cadastro salvo com sucesso!", fg="green")
    else:
        label_status.config(text="Digite um nome e um endereco!", fg="red")

root = tk.Tk()
root.title("Cadastro")
root.geometry("300x250")

label_nome = tk.Label(root, text="Digite um nome:")
label_nome.pack(pady=5)

entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

label_endereco = tk.Label(root, text="Digite um endereço:")
label_endereco.pack(pady=5)

entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="Salvar", command=salvar_nome)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=10)

root.mainloop()
