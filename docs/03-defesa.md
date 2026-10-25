# Mitigação, detecção e reteste

| Risco | Controle preventivo | Evidência para avaliar |
|---|---|---|
| Senhas previsíveis/reutilizadas | Senhas longas e exclusivas; bloquear senhas comuns | Conta com senha antiga deixa de autenticar após troca |
| Muitas tentativas na mesma conta | Limitação progressiva, bloqueio temporário e alertas | Falhas correlacionadas por conta e horário |
| Uma senha contra várias contas | Correlação entre usuários e origens | Contagem de contas distintas com falhas na mesma janela |
| FTP sem proteção | Substituir por SFTP ou alternativa com criptografia | Serviço antigo desativado e novo acesso validado |
| Exposição SMB | Firewall, segmentação, versões suportadas e permissões mínimas | Acesso permitido somente a redes autorizadas |
| Abuso de sessão web | MFA quando suportado, cookies protegidos e gestão de sessão | Fluxo rejeita sessão expirada e exige fatores previstos |
| Enumeração indevida | Restringir consultas anônimas e permissões | Consulta sem credencial passa a ser negada |

SFTP não é FTP com TLS: é um protocolo distinto sobre SSH. Criptografar o transporte
protege os dados em trânsito, mas não elimina ataques de adivinhação de senha.
MFA depende do serviço e da arquitetura; não é uma opção universal do FTP ou SMB legado.
Bloqueio agressivo pode permitir negação de serviço contra contas legítimas.

## Regra didática
Alertar quando uma origem acumular falhas em pelo menos três contas distintas numa janela
de cinco minutos. É apenas um ponto de partida: NAT, aplicações compartilhadas e erros
operacionais podem gerar falsos positivos; tentativas distribuídas exigem correlação adicional.

## Indicadores
- Taxa de autenticações válidas: sucessos / tentativas de autenticação, separando erros de conexão.
- Tempo de detecção: instante do alerta menos início da sequência relevante.
- Contas atingidas: usuários distintos com tentativas na janela.
- Efetividade do controle: comparar mesmo conjunto finito antes/depois e verificar login legítimo.
- Cobertura de logs: serviços com registros utilizáveis / serviços do escopo.

Não há métricas medidas em serviços reais nesta entrega. A simulação demonstra apenas
limiares e contagens sintéticas. O reteste de laboratório deve usar as mesmas entradas,
registrar configuração antes/depois e confirmar que usuários legítimos continuam acessando.
