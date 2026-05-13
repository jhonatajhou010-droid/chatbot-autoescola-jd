from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "autoescola_jd_secreta"

html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>IA Autoescola JD</title>

<style>

body{
    margin:0;
    font-family:Arial, sans-serif;
    background:#0f172a;
    color:white;
}

.chat{
    max-width:850px;
    margin:auto;
    height:100vh;
    display:flex;
    flex-direction:column;
}

.topo{
    background:#020617;
    color:#facc15;
    padding:18px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    border-bottom:1px solid #334155;
}

.conversa{
    flex:1;
    padding:20px;
    overflow-y:auto;
}

.mensagem{
    padding:14px 18px;
    border-radius:18px;
    margin-bottom:14px;
    max-width:75%;
    line-height:1.5;
    white-space:pre-line;
}

.bot{
    background:#1e293b;
    color:white;
    margin-right:auto;
}

.usuario{
    background:#facc15;
    color:#111827;
    margin-left:auto;
}

form{
    display:flex;
    gap:10px;
    padding:16px;
    background:#020617;
    border-top:1px solid #334155;
}

input{
    flex:1;
    padding:15px;
    border-radius:14px;
    border:none;
    font-size:16px;
    outline:none;
}

button{
    background:#facc15;
    color:#111827;
    border:none;
    padding:15px 22px;
    border-radius:14px;
    font-weight:bold;
    cursor:pointer;
}

.whatsapp{
    display:inline-block;
    background:#22c55e;
    color:white;
    padding:12px 16px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
    margin-top:8px;
}

</style>
</head>

<body>

<div class="chat">

<div class="topo">
🚗 IA Autoescola JD
</div>

<div class="conversa">

{% for msg in conversa %}

<div class="mensagem {{ msg.tipo }}">
{{ msg.texto|safe }}
</div>

{% endfor %}

</div>

<form method="POST">

<input
type="text"
name="mensagem"
placeholder="Digite sua mensagem..."
autocomplete="off"
required
>

<button type="submit">
Enviar
</button>

</form>

</div>

</body>
</html>
"""

def iniciar_conversa():

    session["etapa"] = "nome"

    session["conversa"] = [
        {
            "tipo":"bot",
            "texto":"Olá 😄\n\nEu sou a IA da Autoescola JD.\n\nQual é o seu nome?"
        }
    ]

def adicionar(tipo, texto):

    session["conversa"].append({
        "tipo":tipo,
        "texto":texto
    })

    session.modified = True

@app.route("/", methods=["GET", "POST"])

def home():

    if "conversa" not in session:
        iniciar_conversa()

    if request.method == "POST":

        mensagem = request.form.get("mensagem", "").strip()

        if mensagem != "":

            adicionar("usuario", mensagem)

            etapa = session.get("etapa")

            if etapa == "nome":

                session["nome"] = mensagem

                session["etapa"] = "opcao"

                adicionar(
                    "bot",
                    f"""
Prazer, {mensagem} 😄

Como eu poderia lhe ajudar hoje?

1 - Primeira habilitação
2 - Reciclagem ou cassação da CNH
3 - Renovação e categorias C, D e E
4 - Encerrar atendimento
"""
                )

            elif etapa == "opcao":

                if mensagem == "1":

                    session["etapa"] = "categoria"

                    adicionar(
                        "bot",
                        """
Ah, entendi 😄

Qual seria sua categoria?

A - Moto
B - Carro
A/B - Carro e Moto
"""
                    )

                elif mensagem == "2":

                    adicionar(
                        "bot",
                        """
Podemos ajudar com reciclagem ou cassação da CNH 😄

Para mais informações:

<a class='whatsapp'
href='https://wa.me/5514997600124'
target='_blank'>

📲 Chamar no WhatsApp

</a>
"""
                    )

                elif mensagem == "3":

                    adicionar(
                        "bot",
                        """
Podemos ajudar com renovação e categorias C, D e E 😄

Para mais informações:

<a class='whatsapp'
href='https://wa.me/5514997600124'
target='_blank'>

📲 Chamar no WhatsApp

</a>
"""
                    )

                elif mensagem == "4":

                    adicionar(
                        "bot",
                        "Atendimento encerrado 😄"
                    )

                else:

                    adicionar(
                        "bot",
                        "Opção inválida 😅"
                    )

            elif etapa == "categoria":

                categoria = mensagem.upper().replace(" ", "")

                if categoria == "A":

                    resposta = "Você escolheu categoria A - Moto 😄"

                elif categoria == "B":

                    resposta = "Você escolheu categoria B - Carro 😄"

                elif categoria == "AB" or categoria == "A/B":

                    resposta = "Você escolheu categoria A/B - Carro e Moto 😄"

                else:

                    adicionar(
                        "bot",
                        "Categoria inválida 😅"
                    )

                    return render_template_string(
                        html,
                        conversa=session["conversa"]
                    )

                session["etapa"] = "opcao"

                adicionar(
                    "bot",
                    f"""
{resposta}

Para mais informações:

<a class='whatsapp'
href='https://wa.me/5514997600124'
target='_blank'>

📲 Chamar no WhatsApp

</a>
"""
                )

    return render_template_string(
        html,
        conversa=session["conversa"]
    )

if __name__ == "__main__":
    app.run(debug=True)
    
