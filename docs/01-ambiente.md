# Ambiente e preparação

## Pré-requisitos
VirtualBox oficial, imagem Kali e imagem Metasploitable 2 obtidas de fontes oficiais.
Confirmar arquitetura e requisitos das versões escolhidas; registrar versões reais.
O Metasploitable 2 é legado e intencionalmente vulnerável. O DVWA antigo incluído nele
pode divergir do projeto atual: registrar a versão efetiva, sem misturar instruções.

## Configuração
1. Criar/importar as duas VMs. Como ponto de partida, reservar 2 vCPUs e 4 GB para Kali;
   1 vCPU e 1 GB para Metasploitable 2, ajustando conforme o computador e os requisitos.
2. No VirtualBox, criar uma rede host-only, por exemplo 192.168.56.0/24. Escolher IPs
   livres fora da faixa DHCP ou reservar endereços, evitando conflitos.
3. Conectar as duas VMs à mesma rede host-only. Desativar outros adaptadores no alvo.
4. Se Kali precisar de NAT para instalar pacotes, fazê-lo antes e removê-lo durante testes.
   Não habilitar roteamento ou compartilhamento entre as interfaces.
5. Criar snapshots antes das alterações. Desativar pastas compartilhadas e clipboard
   bidirecional no alvo. Não usar contas ou arquivos reais.
6. Confirmar no console de cada VM os endereços e as rotas.

No Kali:
```bash
ip -br address
ip route
```
No alvo legado, se `ip` não estiver disponível:
```bash
ifconfig
route -n
```

Com Kali temporariamente conectado aos repositórios oficiais, preparar ferramentas:
```bash
sudo apt update
sudo apt install medusa nmap smbclient ftp
```
Registrar os pacotes realmente instalados, não presumir versões:
```bash
dpkg-query -W medusa nmap smbclient ftp
medusa -d
medusa -M ftp -q
medusa -M smbnt -q
medusa -M web-form -q
```
A disponibilidade dos módulos depende da compilação. Não confundir falha de negociação
SMB com senha incorreta. Não enfraquecer a configuração do computador hospedeiro para
acomodar protocolos antigos; manter eventual compatibilidade restrita ao laboratório.

## Inventário mínimo
Registrar: data e fuso, versões VirtualBox/Kali/alvo/DVWA/Medusa, IPs, rotas, snapshots,
serviços habilitados e contas fictícias. Confirmar ausência de ponte e de saída externa
no alvo antes de qualquer tentativa. Não varrer a rede física.
