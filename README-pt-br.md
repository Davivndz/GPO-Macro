# GPO-Macro
Computer Vision Automation

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-stable-green.svg)
![UI](https://img.shields.io/badge/UI-Tkinter-black.svg)

**GPO Macro** é uma ferramenta de automação de alta performance desenvolvida em Python, focada na otimização de ciclos no modo Battle Royale do Grand Piece Online (Roblox). O projeto utiliza visão computacional para tomada de decisão em tempo real e emulação de hardware para interação com o ambiente 3D.

## 🚀 Diferenciais Técnicos

* **Sentinel Vision:** Diferente de macros baseados em tempo, o Sentinel utiliza reconhecimento de imagem (OpenCV/PyAutoGUI) para identificar o fim de partidas e estados do servidor (Match Found).
* **Hardware Emulation:** Utiliza a biblioteca `pydirectinput` para enviar comandos de entrada de baixo nível (Scancodes), ignorando bloqueios comuns de APIs de entrada de software.
* **Safe Loading Logic:** Implementa buffers de segurança de 105s e loops de espera dinâmicos para suportar variações de latência de rede e carregamento de assets.
* **Visual Debug GUI:** Interface intuitiva desenvolvida em Tkinter com feedback em tempo real de coordenadas mapeadas e contador de ciclos concluídos.

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **PyAutoGUI / OpenCV:** Reconhecimento de padrões e visão computacional.
* **PyDirectInput:** Emulação de inputs de hardware para jogos.
* **Pynput:** Gerenciamento de eventos de mouse para calibração.
* **Keyboard:** Hooks globais para Hotkeys (F1/F2).
* **Tkinter:** Interface gráfica customizada.

## 📋 Como Usar

1. Preparação da Pasta
Extraia tudo: Não rode o bot direto de dentro do arquivo .zip. Extraia todos os arquivos para uma pasta na sua Área de Trabalho.

Arquivos Necessários: Certifique-se de que o .exe e as imagens (btn_open.png, match_found.png, etc.) estão na mesma pasta.

2. Configuração do Jogo
Modo de Janela: Deixe o Roblox em Modo Janela ou Janela Sem Bordas.

Resolução: O bot funciona melhor em resoluções padrão (como 1920x1080). Se ele não reconhecer os botões, você terá que tirar seus próprios prints e substituir os arquivos .png com o mesmo nome respectivamente.

3. Calibração (Obrigatório)
Antes de dar o Start, o bot precisa saber onde clicar no seu monitor:

Abra o GPO_Macro.exe como Administrador.

No jogo, vá até o menu principal.

No Macro, clique no botão MAP ao lado de "1. Queue" e, em seguida, clique no botão de Fila dentro do jogo.

Repita o processo para todos os 5 botões da lista.

Quando as coordenadas ao lado de cada botão ficarem VERDES, a calibração está concluída.

4. Controles
START (F1): Inicia o ciclo automático. O bot entrará na fila, esperará a partida, upará força e começará o spam de m1 esperar acabar a partida e repetir.

STOP (F2): Interrompe todas as ações do mouse e teclado imediatamente.

## 🧠 Visão de Engenharia

Este projeto foi desenvolvido com foco em **estabilidade e escalabilidade**. A arquitetura separa a lógica de interface (Main Thread) da lógica de execução (Worker Thread), garantindo que a GUI permaneça responsiva mesmo durante processos intensivos de busca visual.

---
*Aviso: Este software é um estudo técnico de automação e visão computacional. O uso em ambientes online deve respeitar os termos de serviço das plataformas.*
