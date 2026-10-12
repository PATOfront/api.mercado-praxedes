from datetime import datetime
import webbrowser


def exibir_cabecalho():
  print("=" * 50)
  print("      ORGANIZADOR E MONITOR DE PREÇOS - MERCADO LIVRE")
  print("=" * 50)


def salvar_no_historico(termo, url):
  """Salva a busca realizada em um arquivo de texto organizado."""
  try:
    with open("historico_buscas.txt", "a", encoding="utf-8") as arquivo:
      data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
      arquivo.write(f"[{data_hora}] Produto: {termo.upper()}\n")
      arquivo.write(f"Link de Acesso: {url}\n")
      arquivo.write("-" * 50 + "\n")
    print("-> Histórico atualizado com sucesso no arquivo 'historico_buscas.txt'.")
  except Exception as e:
    print(f"Erro ao salvar no arquivo: {e}")


def executar_monitor():
  exibir_cabecalho()

  while True:
    print("\n" + "-" * 50)
    termo_busca = input(
        "Digite o produto que deseja buscar (ou digite 'sair' para encerrar): "
    ).strip()

    # Condição de saída do programa
    if termo_busca.lower() == "sair":
      print("\nEncerrando o monitor. Até logo!")
      break

    if not termo_busca:
      print("Por favor, digite um termo válido.")
      continue

    # Formata o termo para o padrão de URL do Mercado Livre (espaços viram hífens)
    termo_formatado = termo_busca.replace(" ", "-")
    url_ml = f"https://lista.mercadolivre.com.br/{termo_formatado}"

    print(f"\n[Processando] Buscando por: '{termo_busca}'...")

    # Salva no arquivo de texto
    salvar_no_historico(termo_busca, url_ml)

    # Pergunta se deseja abrir no navegador
    pergunta = input(
        "Deseja abrir a página de ofertas no seu navegador agora? (s/n): "
    ).strip().lower()

    if pergunta == "s":
      print("Abrindo o navegador...")
      webbrowser.open(url_ml)
      print("Pronto! Aba aberta com sucesso.")
    else:
      print("Busca registrada apenas no histórico.")


if __name__ == "__main__":
  executar_monitor()