#!/usr/bin/env python3
"""Modelo didático determinístico: nenhuma rede e nenhuma credencial real."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def tentativa(contas, usuario, senha, falhas, limite=None):
    if limite is not None and falhas.get(usuario, 0) >= limite:
        return "bloqueado"
    if contas.get(usuario) == senha:
        return "sucesso"
    falhas[usuario] = falhas.get(usuario, 0) + 1
    return "falha"

def rodada(contas, pares, limite=None):
    falhas = {}
    return [{"usuario": u, "resultado": tentativa(contas, u, s, falhas, limite)}
            for u, s in pares]

def alerta(eventos, limiar=3):
    # Todos os eventos desta amostra pertencem à mesma origem e janela sintética.
    return len({e["usuario"] for e in eventos if e["resultado"] == "falha"}) >= limiar

def main():
    senhas = (ROOT / "wordlists/senhas-lab.txt").read_text().splitlines()
    usuarios = (ROOT / "wordlists/usuarios-smb.txt").read_text().splitlines()
    spray = (ROOT / "wordlists/senha-spray.txt").read_text().strip()
    contas = {"lab_ana": "OutraSenhaA", "lab_bruno": "OutraSenhaB", "lab_carla": spray}
    brute = [("lab_ftp", s) for s in senhas]
    sem = rodada({"lab_ftp": spray}, brute)
    com = rodada({"lab_ftp": spray}, brute, limite=2)
    eventos_spray = rodada(contas, [(u, spray) for u in usuarios])
    tres_falhas = rodada(contas, [(u, "CandidataIncorreta") for u in usuarios])
    resultado = {
        "natureza": "simulacao_offline_sem_rede_nao_e_teste_Medusa",
        "forca_bruta_sem_bloqueio": sem,
        "forca_bruta_bloqueio_apos_duas_falhas": com,
        "spraying_uma_rodada": eventos_spray,
        "alerta_spray_limiar_tres_contas_com_falha": alerta(eventos_spray),
        "cenario_tres_falhas": tres_falhas,
        "alerta_tres_contas_com_falha": alerta(tres_falhas),
        "observacao": "O limiar de falhas pode perder sequencias com sucesso; ajustar com dados reais."
    }
    assert [e["resultado"] for e in sem] == ["falha", "falha", "sucesso"]
    assert [e["resultado"] for e in com] == ["falha", "falha", "bloqueado"]
    assert [e["resultado"] for e in eventos_spray] == ["falha", "falha", "sucesso"]
    assert not alerta(eventos_spray) and alerta(tres_falhas)
    destino = ROOT / "evidencias/simulacao-offline.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(resultado, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
