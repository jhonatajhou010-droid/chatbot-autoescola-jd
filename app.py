from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "autoescola_jd_secreta"

html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    width:100%;
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
    scroll-behavior:smooth;
}

.mensagem{
    padding:14px 18px;
    border-radius:18px;
    margin-bottom:14px;
    max-width:90%;
    line-height:1.5;
    white-space:pre-line;
    font-size:17px;
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
    padding:18px;
    border-radius:14px;
    border:none;
    font-size:17px;
    outline:none;
}

button{
    background:#facc15;
    color:#111827;
    border:none;
    padding:18px 24px;
    border-radius:14px;
    font-weight:bold;
    cursor:pointer;
    font-size:17px;
}

.whatsapp{
    display:inline-block;
    background:#22c55e;
    color:white;
    padding:14px 18px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
    margin-top:8px;
}

@media(max-width:768px){

    .chat{
        height:100dvh;
    }

    .topo{
        font-size:20px;
        padding:16px;
    }

    .conversa{
        padding:14px;
    }

    .mensagem{
        font-size:16px;
        max-width:92%;
    }

    form{
        padding:12px;
        gap:8px;
    }

    input{
        font-size:16px;
        padding:16px;
    }

    button{
        font-size:16px;
        padding:16px 18px;
    }
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
placeholder="Digite sua dúvida..."
autocomplete="off"
required
>

<button type="submit">
Enviar
</button>

</form>

</div>

<script>

window.onload = function() {

    var conversa = document.querySelector(".conversa");

    conversa.scrollTop = conversa.scrollHeight;

};

</script>

</body>
</html>
"""

def iniciar_conversa():

    session["conversa"] = [
        {
            "tipo":"bot",
            "texto":"Olá 😄\n\nEu sou a IA da Autoescola JD.\n\nComo posso te ajudar hoje?"
        }
    ]

def adicionar(tipo, texto):

    session["conversa"].append({
        "tipo":tipo,
        "texto":texto
    })

    session.modified = True

def tem_palavra(texto, palavras):

    for palavra in palavras:

        if palavra in texto:
            return True

    return False

def botao_whatsapp():

    return """
Para mais informações e valores, chame no WhatsApp:

<b>14 99760-0124</b>

<a class='whatsapp'
href='https://wa.me/5514997600124'
target='_blank'>

📲 Chamar no WhatsApp

</a>
"""

def responder(mensagem):

    texto = mensagem.lower()

    if tem_palavra(texto, [
        "categoria c",
        "categoria d",
        "categoria e",
        "cnh c",
        "cnh d",
        "cnh e",
        "letra c",
        "letra d",
        "letra e",
        "caminhao",
        "caminhão",
        "ônibus",
        "onibus",
        "carreta",
        "mudar categoria",
        "adicionar categoria"
    ]):

        return """
As categorias C, D e E são para quem já possui CNH e deseja mudar ou adicionar uma nova categoria 😄

Categoria C:
Indicada para veículos de carga, como caminhões.

Categoria D:
Indicada para transporte de passageiros, como ônibus e vans.

Categoria E:
Indicada para veículos articulados, como carretas.

O processo normalmente envolve:

1 - Exames obrigatórios
2 - Verificação da situação da CNH
3 - Processo de mudança de categoria
4 - Aulas práticas
5 - Exame prático

Documentos normalmente solicitados:

- RG
- CPF
- Comprovante de endereço
- CNH atual

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "carro e moto",
        "a e b",
        "categoria a e b",
        "a/b",
        "ab",
        "ao mesmo tempo"
    ]):

        return """
Sim 😄

É possível tirar CNH de carro e moto ao mesmo tempo escolhendo a categoria A/B.

O processo normalmente envolve:

1 - Cadastro inicial
2 - Exames médico e psicotécnico
3 - Curso teórico
4 - Prova teórica
5 - Aulas práticas
6 - Exames práticos

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "primeira habilitação",
        "primeira cnh",
        "tirar cnh",
        "tirar minha cnh",
        "quero tirar",
        "habilitação",
        "cnh nova",
        "carteira de motorista"
    ]):

        return """
Para tirar sua primeira habilitação, o processo normalmente passa por algumas etapas:

1 - Cadastro do candidato
2 - Exame médico
3 - Exame psicotécnico
4 - Curso teórico
5 - Prova teórica
6 - Aulas práticas
7 - Exame prático

Você pode tirar categoria A, B ou A/B.

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "moto",
        "categoria a",
        "cnh a"
    ]):

        return """
A categoria A é para quem deseja conduzir moto.

O processo normalmente inclui:

1 - Cadastro
2 - Exames obrigatórios
3 - Curso teórico
4 - Prova teórica
5 - Aulas práticas
6 - Exame prático

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "carro",
        "categoria b",
        "cnh b"
    ]):

        return """
A categoria B é para quem deseja conduzir carro.

O processo normalmente inclui:

1 - Cadastro
2 - Exames obrigatórios
3 - Curso teórico
4 - Prova teórica
5 - Aulas práticas
6 - Exame prático

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "renovar",
        "renovação",
        "cnh vencida",
        "vencida"
    ]):

        return """
Para renovar sua CNH normalmente você precisa:

1 - Solicitar a renovação
2 - Fazer exame médico
3 - Regularizar taxas
4 - Aguardar emissão da nova CNH

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "reciclagem",
        "reciclar",
        "suspensa",
        "suspensão",
        "cassada",
        "cassação"
    ]):

        return """
O processo de reciclagem normalmente envolve:

1 - Verificar situação da CNH
2 - Cumprir prazo determinado
3 - Fazer curso de reciclagem
4 - Realizar prova

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "documentos",
        "documento",
        "rg",
        "cpf"
    ]):

        return """
Normalmente são solicitados:

- RG
- CPF
- Comprovante de endereço

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "prova teórica",
        "prova teorica",
        "o que cai",
        "detran"
    ]):

        return """
A prova teórica costuma envolver:

- Legislação
- Placas
- Direção defensiva
- Primeiros socorros
- Meio ambiente

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "psicotécnico",
        "psicotecnico",
        "exame médico",
        "exame medico"
    ]):

        return """
O exame médico e psicotécnico avaliam se o candidato possui condições para dirigir.

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "reprovei",
        "reprovar",
        "reprova",
        "exame prático",
        "exame pratico"
    ]):

        return """
Se houver reprovação no exame prático será necessário remarcar nova tentativa.

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "pontos",
        "pontuação",
        "pontuacao",
        "multa",
        "multas"
    ]):

        return """
A pontuação da CNH varia conforme as infrações registradas.

""" + botao_whatsapp()

    elif tem_palavra(texto, [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    ]):

        return """
Olá 😄

Me diga sua dúvida sobre CNH que eu tento te ajudar.
"""

    else:

        return """
Não consegui entender totalmente sua dúvida 😅

Você pode perguntar por exemplo:

- Quero tirar minha CNH
- Quero renovar minha CNH
- Minha CNH foi suspensa
- Quero categoria D
- Quero CNH de caminhão
- Reprovei no exame prático

""" + botao_whatsapp()

@app.route("/", methods=["GET", "POST"])

def home():

    if "conversa" not in session:
        iniciar_conversa()

    if request.method == "POST":

        mensagem = request.form.get("mensagem", "").strip()

        if mensagem != "":

            adicionar("usuario", mensagem)

            resposta = responder(mensagem)

            adicionar("bot", resposta)

    return render_template_string(
        html,
        conversa=session["conversa"]
    )

if __name__ == "__main__":
    app.run(debug=True)
