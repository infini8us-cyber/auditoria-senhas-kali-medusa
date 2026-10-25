# Publicação e entrega

Nome sugerido: `auditoria-senhas-kali-medusa`.
Descrição: Estudo técnico sobre auditoria de senhas em FTP, DVWA e SMB com Kali Linux e
Medusa, arquitetura de laboratório isolado, simulação offline e medidas de prevenção.

## GitHub pela interface
1. Entrar na própria conta GitHub; não compartilhar senha ou token no chat.
2. Criar repositório com o nome sugerido e visibilidade pública.
3. Extrair o ZIP e enviar o conteúdo da pasta `medusa-lab`, preservando as subpastas.
   O `README.md` deve estar na raiz, não dentro de outra pasta com o nome do projeto.
4. Revisar os arquivos e confirmar o commit. Não enviar o ZIP como único conteúdo.
5. Abrir a URL pública para confirmar README e links relativos.

## Alternativa com Git
Dentro da pasta extraída:
```bash
git init -b main
git add README.md docs scripts wordlists evidencias images .gitignore
git commit -m 'Adiciona estudo documental de auditoria de senhas'
```
Após criar um repositório vazio no GitHub, adicionar a URL HTTPS real copiada da página:
```bash
git remote add origin URL_HTTPS_REAL_DO_REPOSITORIO
git push -u origin main
```
A URL acima é um marcador; substituir pela URL real. Autenticar pelo mecanismo oficial
do GitHub, sem inserir tokens na URL ou no repositório.

## DIO
Assistir às vídeo-aulas, revisar a modalidade documental e usar o texto de
[descricao-entrega.txt](../descricao-entrega.txt). Em “Entregar Projeto”, preencher a URL
real do repositório e a descrição. Verificar a confirmação de envio na plataforma.
Nenhuma dessas ações é marcada como realizada antecipadamente.

## Checklist
- [x] Arquitetura e escopo documentados.
- [x] Cenários e listas fictícias incluídos.
- [x] Medidas de defesa e limitações explicitadas.
- [x] Simulação offline executada e identificada.
- [ ] Vídeo-aulas assistidas e conferidas pelo estudante.
- [ ] Repositório público criado e conteúdo publicado.
- [ ] Link e descrição enviados na DIO; confirmação verificada.

A execução em VMs é uma extensão opcional desta modalidade documental. Se realizada,
atualizar os estados e incluir apenas evidências efetivamente produzidas.
