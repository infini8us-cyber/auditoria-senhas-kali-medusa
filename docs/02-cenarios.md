# Procedimentos reproduzíveis — não executados em VMs

Todos os exemplos abaixo usam exclusivamente o IP ilustrativo 192.168.56.20.
Confirmar que esse IP pertence à VM autorizada; não executar por mera coincidência de IP.
Executar a partir da raiz do projeto. Criar diretório local de registros:
```bash
mkdir -p evidencias/privado
```

## 1. Inventário limitado de serviços
```bash
nmap -sV -p 21,80,139,445 192.168.56.20 -oN evidencias/privado/servicos.txt
```
Verificar quais serviços de fato respondem. Uma porta filtrada ou fechada exige análise
de rede/serviço antes do teste de autenticação.

## 2. FTP: várias senhas para uma conta
Pré-condição: criar no alvo uma conta descartável `lab_ftp`, com senha de exercício
`LabSomente123`, e verificar que o serviço permite seu login. A criação depende da imagem;
um administrador local deve usar `sudo adduser lab_ftp` e definir a senha interativamente.
A lista tem três candidatas, sendo a válida a terceira. Teste limitado a uma conta:
```bash
medusa -h 192.168.56.20 -u lab_ftp -P wordlists/senhas-lab.txt -M ftp -t 1 -f -O evidencias/privado/ftp.txt
```
`-h`: alvo; `-u`: usuário único; `-P`: arquivo de senhas; `-M`: módulo;
`-t 1`: uma tentativa concorrente; `-f`: interromper o host após o primeiro sucesso;
`-O`: arquivo de registro, que pode conter a senha e deve permanecer privado.
Não usar `-r` como limite entre logins: essa opção trata de retentativas de conexão.

Validação manual mínima:
```bash
ftp 192.168.56.20
```
Digitar a conta e a senha de laboratório; após autenticação, usar `pwd`, depois `bye`.
Registrar a resposta real. Não transferir ou modificar arquivos como prova.

## 3. DVWA: formulário web e estado de sessão
Pré-condições: acessar apenas a URL local, autenticar na interface de laboratório,
registrar versão e nível de segurança. Caso escolha o nível Low, alterar somente o DVWA
isolado e restaurar o snapshot ao terminar. A alteração não foi feita nesta entrega.

Procedimento de automação a reproduzir:
1. Usar o formulário do módulo Brute Force, distinguindo-o do login inicial do DVWA.
2. Nas ferramentas de desenvolvedor, registrar método, caminho, campos, cookies e token
   de uma tentativa inválida. Cookies/tokens nunca entram no GitHub.
3. Repetir com uma credencial conhecida de laboratório e identificar uma diferença
   confiável de conteúdo. HTTP 200 isoladamente não representa sucesso.
4. Conferir a ajuda local `medusa -M web-form -q`; verificar se o módulo suporta método,
   campos, sessão e critérios de resposta dessa versão do formulário.
5. Configurar o módulo conforme essa ajuda e limitar a uma conta e três senhas fictícias.
   Registrar o comando efetivo em arquivo privado, com sessão redigida na versão pública.
6. Se o formulário requerer atualização de token por tentativa e o módulo não suportar
   esse fluxo, registrar a incompatibilidade; não tratar a saída como auditoria válida.
7. Validar manualmente o eventual resultado e encerrar a sessão.

Não se fornece uma linha universal de `web-form`: caminho, parâmetros e estado variam
entre versões. O modelo offline incluído demonstra a lógica finita de tentativas,
sem afirmar que houve automação bem-sucedida contra DVWA.

## 4. SMB: enumeração e password spraying
Pré-condições: contas fictícias `lab_ana`, `lab_bruno` e `lab_carla` criadas no alvo e
cadastradas no Samba. Em imagens compatíveis, o administrador pode usar `adduser` para
cada conta e `sudo smbpasswd -a NOME` para cadastrar a senha SMB interativamente.
Definir apenas `lab_carla` com `LabSomente123`; usar outras senhas descartáveis nas demais.

Enumeração restrita ao alvo, se o servidor permitir sessão anônima:
```bash
rpcclient -U '' -N 192.168.56.20 -c 'enumdomusers'
```
Se negar acesso, registrar a negativa. Para continuar, utilizar uma conta administrativa
somente do laboratório, com senha solicitada interativamente:
```bash
rpcclient -U lab_admin 192.168.56.20 -c 'enumdomusers'
```
Esse segundo exemplo exige a existência e as permissões da conta; não presume que ela
já esteja configurada. Selecionar somente as três contas fictícias confirmadas. O arquivo
incluído é uma lista de exemplo, não resultado de enumeração.

Uma rodada, uma senha, três usuários:
```bash
medusa -h 192.168.56.20 -U wordlists/usuarios-smb.txt -P wordlists/senha-spray.txt -M smbnt -t 1 -O evidencias/privado/smb.txt
```
Não executar novas rodadas ou tentar contornar bloqueios. Se houver bloqueio, indisponibilidade
ou negociação incompatível, interromper e registrar. SMB moderno e Samba antigo podem
exigir parâmetros diferentes; conferir ajuda e protocolos antes de interpretar a saída.

Validação, sem gravar senha na linha de comando:
```bash
smbclient -L //192.168.56.20 -U lab_carla
```
A listagem confirma somente o que a resposta realmente permitir. Acesso a compartilhamento
não é equivalente a privilégio administrativo.

## Encerramento
Encerrar sessões, desativar as VMs ou restaurar snapshots. Revisar e redigir registros antes
de copiá-los para `images/` ou `evidencias/`. Descrever o que falhou com a mesma precisão
usada para eventuais sucessos. Resultados deste roteiro permanecem não executados.
