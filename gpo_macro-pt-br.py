import tkinter as tk
from tkinter import scrolledtext
import pydirectinput
import pyautogui
import time
import threading
from pynput import mouse
import keyboard
import os
import json
from datetime import datetime

# --- LÓGICA TÉCNICA (TOTALMENTE PRESERVADA) ---
pydirectinput.PAUSE = 0.01 
pyautogui.PAUSE = 0.01
CONFIG_FILE = 'config.json'

IMAGENS = {
    'open': 'btn_open.png',
    'continue': 'btn_continue.png',
    'match': 'match_found.png'
}

class GPOMacroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPO BATTLE ROYALE MACRO v1.0")
        self.root.geometry("550x950") # Aumentei um pouco a largura para caber as coords
        self.root.configure(bg="#0f0f0f")

        self.running = False
        self.partidas_feitas = 0
        self.actions = {
            'queue':        {'label': '1. Queue', 'coords': None},
            'br_mode':      {'label': '2. BR Mode', 'coords': None},
            'solos':        {'label': '3. Solos Selection', 'coords': None},
            'menu_status':  {'label': '4. Menu Status', 'coords': None},
            'stats':        {'label': '5. Strength Upgrade', 'coords': None}
        }
        self.hotkeys = {'start': 'f1', 'stop': 'f2'}
        self.coord_labels = {} # Dicionário para gerenciar as labels de X,Y
        
        self.load_config()
        self.create_widgets()
        self.setup_hotkeys()

    def log(self, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, f"[{ts}] {msg}\n")
        self.log_area.see(tk.END)
        self.log_area.configure(state='disabled')

    # --- MÉTODOS DE EXECUÇÃO MANTIDOS ---
    def smooth_move(self, tx, ty, duration=1.0):
        if not self.running: return
        sx, sy = pydirectinput.position()
        steps = 30
        sleep_per_step = duration / steps
        for i in range(1, steps + 1):
            if not self.running: break
            curr_x = sx + (tx - sx) * (i / steps)
            curr_y = sy + (ty - sy) * (i / steps)
            pydirectinput.moveTo(int(curr_x), int(curr_y))
            time.sleep(sleep_per_step)

    def hardware_click(self, x, y, duration=1.0):
        if not self.running: return
        self.smooth_move(x, y, duration)
        time.sleep(0.3)
        pydirectinput.click()
        time.sleep(0.5)

    def find_and_click(self, img_key, desc, click=True, confidence=0.7):
        if not self.running: return False
        try:
            path = IMAGENS.get(img_key)
            pos = pyautogui.locateOnScreen(path, confidence=confidence, grayscale=True)
            if pos:
                if click:
                    self.log(f"📸 {desc} detectado!")
                    center = pyautogui.center(pos)
                    self.hardware_click(center.x, center.y)
                return True
        except: pass
        return False

    def setup_hotkeys(self):
        keyboard.unhook_all()
        keyboard.add_hotkey(self.hotkeys['start'], self.start_macro)
        keyboard.add_hotkey(self.hotkeys['stop'], self.stop_macro)

    def start_macro(self):
        # Fail-safe: Não inicia se houver botões sem mapear
        for k, v in self.actions.items():
            if v['coords'] is None:
                self.log(f"⚠️ ERRO: Configure {k} primeiro!")
                return
        if not self.running:
            self.running = True
            self.log("🔥 STATUS: EXECUTANDO")
            threading.Thread(target=self.main_loop, daemon=True).start()

    def stop_macro(self):
        self.running = False
        self.log("🛑 STATUS: PARADO")

    def main_loop(self):
        try:
            while self.running:
                self.log("🖱️ Iniciando Fila...")
                self.hardware_click(*self.actions['queue']['coords'])
                self.hardware_click(*self.actions['br_mode']['coords'])
                self.hardware_click(*self.actions['solos']['coords'])

                self.log("📡 Aguardando Match Found...")
                while self.running:
                    if self.find_and_click('match', "Match Found", click=False):
                        self.log("✅ Partida Iniciada!")
                        break
                    time.sleep(2)

                self.log("⌛ Loading do Mundo (105s)...")
                for i in range(105):
                    if not self.running: break
                    time.sleep(1)

                if self.running:
                    self.log("📂 Upando Strength...")
                    pydirectinput.press('m')
                    time.sleep(2.0)
                    self.hardware_click(*self.actions['menu_status']['coords'])
                    self.smooth_move(*self.actions['stats']['coords'])
                    for _ in range(15):
                        if not self.running: break
                        pydirectinput.click()
                        time.sleep(0.8)
                    pydirectinput.press('m')
                    time.sleep(3.0)

                if self.running:
                    self.log("⚔️ Combate Berserker (120s Spam)...")
                    pydirectinput.press('1')
                    time.sleep(2.0)
                    start_combat = time.time()
                    match_report_found = False

                    while self.running and not match_report_found:
                        if time.time() - start_combat < 120:
                            pydirectinput.click()
                        if time.time() % 3 < 0.1:
                            if self.find_and_click('open', "Open Report", click=True):
                                match_report_found = True
                        time.sleep(0.01)

                    self.log("🧹 Finalizando recompensas...")
                    timeout_continue = time.time() + 25
                    while self.running and time.time() < timeout_continue:
                        if self.find_and_click('continue', "Continue"):
                            break
                        time.sleep(2.5)

                self.partidas_feitas += 1
                self.root.after(0, lambda: self.lbl_count.config(text=str(self.partidas_feitas)))
                self.log(f"🏁 Ciclo {self.partidas_feitas} OK.")

        except Exception as e:
            self.log(f"❌ Erro: {e}")
            self.stop_macro()

    # --- UI ESTILIZADA COM FEEDBACK DE COORDENADAS ---
    def create_widgets(self):
        header = tk.Frame(self.root, bg="#1a1a1a", pady=20)
        header.pack(fill="x")
        tk.Label(header, text="GPO BATTLE ROYALE MACRO", font=("Impact", 18), bg="#1a1a1a", fg="#00ff00").pack()
        
        dash_frame = tk.Frame(self.root, bg="#0f0f0f", pady=10)
        dash_frame.pack(fill="x")
        tk.Label(dash_frame, text="PARTIDAS CONCLUÍDAS", font=("Arial", 9, "bold"), bg="#0f0f0f", fg="#777").pack()
        self.lbl_count = tk.Label(dash_frame, text=str(self.partidas_feitas), font=("Impact", 32), bg="#0f0f0f", fg="#fff")
        self.lbl_count.pack()

        btn_frame = tk.Frame(self.root, bg="#0f0f0f", pady=10)
        btn_frame.pack(fill="x", padx=20)
        self.btn_start = tk.Button(btn_frame, text="START (F1)", font=("Arial", 10, "bold"), bg="#004400", fg="#0f0", 
                                   width=15, height=2, command=self.start_macro, relief="flat")
        self.btn_start.pack(side="left", expand=True, padx=5)
        self.btn_stop = tk.Button(btn_frame, text="STOP (F2)", font=("Arial", 10, "bold"), bg="#440000", fg="#f44", 
                                  width=15, height=2, command=self.stop_macro, relief="flat")
        self.btn_stop.pack(side="right", expand=True, padx=5)

        tk.Label(self.root, text="MAPEAMENTO DE COORDENADAS", font=("Arial", 9, "bold"), bg="#0f0f0f", fg="#555").pack(pady=(15, 5))

        for key, data in self.actions.items():
            row = tk.Frame(self.root, bg="#1a1a1a", pady=5)
            row.pack(fill="x", padx=20, pady=2)
            
            tk.Button(row, text="MAP", font=("Arial", 8, "bold"), bg="#333", fg="#fff", width=5, relief="flat",
                      command=lambda k=key: self.start_selection(k)).pack(side="left", padx=5)
            
            tk.Label(row, text=data['label'], font=("Arial", 9), bg="#1a1a1a", fg="#aaa", width=18, anchor="w").pack(side="left")
            
            # Label das Coordenadas (A Mágica acontece aqui)
            coords_text = f"({data['coords'][0]}, {data['coords'][1]})" if data['coords'] else "(0, 0)"
            coords_color = "#00ff00" if data['coords'] else "#ff4444"
            
            c_lbl = tk.Label(row, text=coords_text, font=("Consolas", 9, "bold"), bg="#1a1a1a", fg=coords_color, width=12)
            c_lbl.pack(side="right", padx=10)
            self.coord_labels[key] = c_lbl

        tk.Label(self.root, text="SYSTEM LOG", font=("Arial", 9, "bold"), bg="#0f0f0f", fg="#555").pack(pady=(15, 0))
        self.log_area = scrolledtext.ScrolledText(self.root, width=60, height=12, bg="#000", fg="#00ff00", 
                                                 font=("Consolas", 8), borderwidth=0, highlightthickness=1, 
                                                 highlightbackground="#333")
        self.log_area.pack(pady=10, padx=20)

    def update_ui_coords(self, key):
        coords = self.actions[key]['coords']
        if coords:
            self.coord_labels[key].config(text=f"({coords[0]}, {coords[1]})", fg="#00ff00")
        else:
            self.coord_labels[key].config(text="(0, 0)", fg="#ff4444")

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    for k in self.actions:
                        if k in data['coords']: 
                            self.actions[k]['coords'] = tuple(data['coords'][k])
            except: pass

    def save_config(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'coords': {k: v['coords'] for k, v in self.actions.items()}, 'hotkeys': self.hotkeys}, f)

    def start_selection(self, key):
        self.log(f"📍 Mapeando: {key}")
        def on_click(x, y, btn, pressed):
            if pressed:
                self.actions[key]['coords'] = (int(x), int(y))
                self.save_config()
                self.update_ui_coords(key)
                return False
        with mouse.Listener(on_click=on_click) as l: l.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = GPOMacroApp(root)
    root.mainloop()
