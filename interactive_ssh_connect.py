#!/usr/bin/python3
"""
    @Last update: 06/12/2023
    @Version : 1.0
    @Author: Mohand TOUAHRI
    @Changelog:
    Date       | Ver   | Names            | Comments
    -----------|-------|------------------|---------------------------------------
    06/12/2023 | 1.0   | Mohand TOUAHRI   | Creation
"""

import curses
import subprocess

## ## ## ## ## ## ## 

USER="ADM-MTOUAHRI"
INFRA = {
    "Prod": {
        "Workers": {
            "Worker : "host_prod_xxx,
            "Worker : "host_prod_xxx,
            "Worker : "host_prod_xxx,
            "Worker : "host_prod_xxx,
            "Worker 92": "host_prod_xxx92",
        },
        "Nagios": {
            "Nagios : "host_prod_xxx,
        },
        "Traitement": {
            "Node : "host_prod_xxx,
            "Rh8 : "host_prod_xxx,
            "Rh7 : "host_prod_xxx,
        },
        "Broker": {
            "Rabbit : "host_prod_xxx,
            "Rabbit : "host_prod_xxx,
        },
        "InfluxDB": {
            "Inxlux : "host_prod_xxx,
            "Ilxlux : "host_prod_xxx,
        },
        "autre": {
            "tamwin synchro": "host_prod_xxx,
        },
    },
    "Qualif": {
        "Workers": {
            "Worker : "host_rec_xxx,
            "Worker : "host_rec_xxx,
        },
        "Nagios": {
            "Nagios : "host_rec_xxx,
        },
    },
    "Recette": {
        "Workers": {
            "Worker : "host_prod_xxx,
            "Worker : "host_prod_xxx,
        },
        "Nagios": {
            "Nagios : "host_rec_xxx,
        },
        "Traitement": {
            "Node": "host_rec_xxx",
            "Rh8 : "host_rec_xxx",
            "Rh8 : "host_rec_xxx",
        },
        "Broker": {
            "Rabbit : "host_prod_xxx",
            "Rabbit : "host_prod_xxx",
            "Rabbit : "host_prod_xxx",
        },
        "InfluxDB": {
            "Inxlux : "host_prod_xxx,
            "Inxlux : "host_prod_xxx,
        },
    },
    "Exit": {}
}

## ## ## ## ## ## ## 

def ssh_host_prod_xxx(stdscr, user, server):
    curses.endwin()
    print(f"Tentative : connexion SSH avec {user}@{server}...")
    ssh_command = f"ssh -t {user}@xx.xx.xxx.xx '{user}@xxxxxxxxxxx.fr@{server}:SSH:PART_XXXX_FLUXOUTILS-PART_XXXX_FLUXOUTILS_LINUX_REDHAT_PROD'"
    try:
        subprocess.run(ssh_command, shell=True)
    except KeyboardInterrupt:
        # Gérer l'interruption par Ctrl+C
        print("\nCommande SSH interrompue par l'utilisateur.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande SSH : {e}")

def ssh_host_rec_xxx(stdscr, user, server):
    curses.endwin()
    print(f"Tentative : connexion SSH avec {user}@{server}...")
    ssh_command = f"ssh -t '{user}@xxx.xxx.xxx.xxx' Interactive@{server}:SSH:PART_XXXX_FLUXOUTILS-PART_XXXX_FLUXOUTILS_LINUX_REDHAT_REC"
    try:
        subprocess.run(ssh_command, shell=True)
    except KeyboardInterrupt:
        # Gérer l'interruption par Ctrl+C
        print("\nCommande SSH interrompue par l'utilisateur.")
    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande SSH : {e}")

def draw_menu(stdscr, current_options, cursor_vertical):
    stdscr.clear()
    stdscr.addstr(0, 0, "-------------")
    stdscr.addstr(1, 0, "     Menu    ")
    stdscr.addstr(2, 0, "-------------")

    for idx, option in enumerate(current_options):
        if idx == cursor_vertical:
            stdscr.addstr(4 + idx, 0, "-> " + option, curses.A_REVERSE)
        else:
            stdscr.addstr(4 + idx, 0, "   " + option)
    stdscr.refresh()

def menu(stdscr):

    current_options = list(INFRA.keys())
    option_stack = []
    cursor_vertical = 0

    while True:
        draw_menu(stdscr, current_options, cursor_vertical)

        key = stdscr.getch()

        if key == curses.KEY_UP and cursor_vertical > 0:
            cursor_vertical -= 1
        elif key == curses.KEY_DOWN and cursor_vertical < len(current_options) - 1:
            cursor_vertical += 1
        elif key == curses.KEY_RIGHT:
            selected_option = current_options[cursor_vertical]
            selected_suboptions = INFRA
            for option, cursor in option_stack:
                selected_suboptions = selected_suboptions[option[cursor]]

            if selected_option in selected_suboptions and isinstance(selected_suboptions[selected_option], dict):
                option_stack.append((current_options, cursor_vertical))
                current_options = list(selected_suboptions[selected_option].keys())
                cursor_vertical = 0
        elif key == curses.KEY_LEFT:
            if option_stack:
                current_options, cursor_vertical = option_stack.pop()
        elif key == ord('\n'):
            selected_option = current_options[cursor_vertical]
            #selected_suboptions = options
            selected_suboptions = INFRA
            for option, cursor in option_stack:
                selected_suboptions = selected_suboptions[option[cursor]]

            if isinstance(selected_suboptions[selected_option], str):
                if "host_prod_xxx" in selected_suboptions[selected_option]: 
                    ssh_host_prod_xxx(stdscr, USER, selected_suboptions[selected_option])
                    break
                else:
                    ssh_host_rec_xxx(stdscr, USER, selected_suboptions[selected_option])
                    break
            elif selected_option == "Exit":
                break

if __name__ == '__main__':

    curses.wrapper(menu)
