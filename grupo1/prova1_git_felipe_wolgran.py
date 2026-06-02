# ============================================================
#  PROVA PRÁTICA — Git & GitHub
# ============================================================
#
#  INSTRUÇÕES:
#  1. Faça o clone do repositório
#  2. Copie o arquivo prova_git_nome_sobrenome.py e renomei para prova_git_seu_nome_sobrenome.py
#  2. Preencha seus dados na função cadastrar_aluno() abaixo
#  3. Execute o arquivo para verificar.
#  4. Faça o commit com a mensagem: "prova: SEU_NOME SEU_SOBRENOME"
#  5. Suba com: git push origin main
#
# ============================================================

alunos_cadastrados = []


def cadastrar_aluno(matricula: str, nome: str, sobrenome: str):
    """
    Cadastra o aluno na lista de alunos_cadastrados.
    Não permite matrícula ou nome duplicado.
    """
    for aluno in alunos_cadastrados:
        if aluno["matricula"] == matricula:
            print(f" Matrícula {matricula} já cadastrada.")
            return
        if aluno["nome"] == nome and aluno["sobrenome"] == sobrenome:
            print(f"Aluno {nome} {sobrenome} já cadastrado.")
            return

    alunos_cadastrados.append({
        "matricula": matricula,
        "nome":      nome,
        "sobrenome": sobrenome
    })
    print(f"Aluno cadastrado: {matricula} — {nome} {sobrenome}")


def listar_arquivos_alterados(commits: list) -> list:
    """
    Recebe uma lista de commits (cada um com 'hash' e 'arquivos')
    e retorna todos os arquivos alterados, sem repetição e em
    ordem alfabética.
    """
    arquivos = set()
    for commit in commits:
        for arquivo in commit["arquivos"]:
            arquivos.add(arquivo)
    return sorted(arquivos)


# ============================================================
#  PREENCHA SEUS DADOS ABAIXO
#  cadastrar_aluno("matricula", "nome", "sobrenome")
# ============================================================

cadastrar_aluno("2026111510424", "Felipe", "Wolgran")

# ============================================================
#  NÃO ALTERE O CÓDIGO ABAIXO
# ============================================================

def verificar():
    COMMITS = [
        {"hash": "a1b2c3d", "arquivos": ["index.html", "style.css"]},
        {"hash": "b2c3d4e", "arquivos": ["style.css", "script.js"]},
        {"hash": "c3d4e5f", "arquivos": ["index.html", "README.md"]},
    ]

    print("\n" + "=" * 44)
    print("  VERIFICAÇÃO")
    print("=" * 44)

    if not alunos_cadastrados or not alunos_cadastrados[-1]["matricula"].strip():
        print("  ✗ Preencha seus dados em cadastrar_aluno().")
        print("=" * 44 + "\n")
        return

    aluno = alunos_cadastrados[-1]
    print(f"  Aluno: {aluno['matricula']} — {aluno['nome']} {aluno['sobrenome']}")
    print("-" * 44)

    try:
        resultado = listar_arquivos_alterados(COMMITS)
        esperado  = ["README.md", "index.html", "script.js", "style.css"]

        assert isinstance(resultado, list), "Deve retornar uma lista."
        assert resultado == esperado, (
            f"Esperado: {esperado}\n  Obtido:   {resultado}"
        )

        print("Função correta!")
        print("Agora faça o commit e o push!")
    except Exception as e:
        print(f"Falhou: {e}")

    print("=" * 44 + "\n")


if __name__ == "__main__":
    verificar()