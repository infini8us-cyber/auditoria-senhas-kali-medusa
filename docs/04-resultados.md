# Resultados e limitações

| Item | Estado | Evidência |
|---|---|---|
| Arquitetura e roteiro FTP/DVWA/SMB | Elaborados | Documentos deste projeto |
| Simulação determinística offline | Executada | `evidencias/simulacao-offline.json` |
| Duas VMs VirtualBox | Não configuradas neste ambiente | VirtualBox indisponível |
| Medusa contra serviços | Não executado | Ferramenta e VMs indisponíveis |
| Acesso FTP, web ou SMB real | Não validado | Sem logs de serviço ou capturas |
| Vídeo-aulas | Não verificadas | A conclusão depende do estudante |
| Slides PDF | Não acessados | Link mantido nas referências |
| GitHub/DIO | Pendente | Requer sessão autenticada e URL real |

## O que a simulação permite concluir
Em um conjunto fixo de três senhas, a força bruta alcança a credencial correta na terceira
tentativa sem bloqueio; com bloqueio após duas falhas, a terceira é recusada pelo modelo.
No spraying, uma senha é testada em três contas e acerta a terceira; falhas distribuídas
por duas contas não disparam o limiar didático de três contas com falhas.
O cenário adicional com três falhas em contas distintas dispara esse limiar.

Essas conclusões descrevem um programa didático, não a eficácia de um produto ou configuração
real. Não há tráfego de rede no programa, negociação SMB, cookies, CSRF ou autenticação FTP.

## Reflexão técnica
A vulnerabilidade não está apenas em uma senha fraca: exposição, protocolos e observabilidade
compõem o risco. Ferramentas automatizam tentativas, mas exigem interpretação de respostas,
controle de falsos positivos e validação manual mínima. Uma falha de ferramenta também é
um resultado documentável, desde que não seja confundida com proteção comprovada.

## Modelo para execução futura
Para cada cenário registrar: data/fuso, versões, alvo, pré-condições, quantidade de tentativas,
comando redigido, resultado, validação, logs do servidor, controle aplicado e reteste.
Identificar evidências por ID (FTP-01, WEB-01, SMB-01), sem preencher resultados antecipadamente.
