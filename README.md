# Auditoria de senhas com Kali Linux e Medusa

Projeto educacional — Bootcamp Santander Cibersegurança / DIO.

**Modalidade: estudo técnico documental com exemplos reproduzíveis e simulação offline.**
**Estado: documentação e simulação offline concluídas; FTP/DVWA/SMB em VMs não executados.**
Nenhum acesso a serviço real foi validado. A simulação Python não substitui Medusa ou VMs.
As vídeo-aulas e o PDF de slides não foram verificados nesta elaboração.

## Objetivo
Compreender força bruta e password spraying, projetar um laboratório isolado e relacionar
falhas de autenticação a controles preventivos e de detecção. O enunciado permite a
modalidade documental, adotada pela indisponibilidade de VirtualBox e Medusa neste ambiente.

## Conceitos
- Força bruta: diversas senhas candidatas para uma conta. Listas pequenas representam apenas um subconjunto, não uma busca exaustiva.
- Password spraying: uma ou poucas senhas candidatas em várias contas. O bloqueio por conta, isoladamente, pode não detectar a distribuição.
- Enumeração: levantamento de detalhes, como usuários e serviços; não significa acesso obtido.
- Autenticação válida não implica autorização para todos os recursos.
- Porta aberta não comprova vulnerabilidade nem senha fraca.

## Arquitetura proposta
| Elemento | Função | Endereço ilustrativo |
|---|---|---|
| Kali Linux | Nmap, Medusa e clientes de validação | 192.168.56.10/24 |
| Metasploitable 2 | Serviços FTP/SMB e DVWA | 192.168.56.20/24 |
| Hospedeiro | VirtualBox e administração | 192.168.56.1/24 |

Usar uma interface host-only por VM, sem ponte e sem encaminhamento externo.
Host-only inclui o hospedeiro; rede interna é um modo diferente, limitado às VMs.
Os IPs são exemplos: confirmar no console antes de qualquer comando. Detalhes em
[Ambiente](docs/01-ambiente.md).

## Conteúdo e sequência
1. [Configurar o ambiente](docs/01-ambiente.md).
2. [Estudar e reproduzir os cenários](docs/02-cenarios.md).
3. [Analisar mitigação e detecção](docs/03-defesa.md).
4. [Consultar resultados e limitações](docs/04-resultados.md).
5. [Publicar e entregar](docs/05-entrega.md).
6. [Consultar fontes](docs/06-referencias.md).

## Executar a simulação offline
Requer Python 3, sem dependências externas e sem acesso à rede:
```bash
python3 scripts/simulacao_offline.py
```
Ela usa contas sintéticas em memória, compara força bruta e spraying, demonstra bloqueio
por conta e avalia uma regra didática de detecção entre contas. Não descobre usuários,
não transmite credenciais e não ataca serviços. Saída efetivamente produzida em
[evidencias/simulacao-offline.json](evidencias/simulacao-offline.json).

## Escopo e dados
Os comandos documentados destinam-se exclusivamente às VMs locais do exercício.
As wordlists contêm dados fictícios e devem ser substituídas somente por contas do laboratório.
Não há credenciais de produção, dados corporativos ou cookies neste repositório.
Os registros operacionais brutos ficam fora do versionamento até revisão.

## Conclusão
O risco de autenticação depende de senhas, exposição dos serviços e capacidade de detectar
tentativas. A comparação documental sustenta uma defesa em camadas: senhas exclusivas,
limitação de tentativas, MFA quando suportado, segmentação e correlação de eventos.
O resultado demonstrado é o comportamento do modelo offline; a eficácia em FTP, DVWA e
SMB depende de execução futura e coleta de evidências reais.
