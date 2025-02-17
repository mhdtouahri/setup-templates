#!/bin/bash
################################################################################
# PROGNAME : template.sh
# DESCRIPTION :Template vierge de script bash avec debug en couleur, gestion et 
#              rotation de log
# AUTHOR : "Mohand TOUAHRI"
# REVISION="Revision 0.0.0"
## _____________________________________________________________________________
## XX/xx/xxxx |0.0.0  | Mohand TOUAHRI   | Creation
################################################################################

### VARIABLES
LOG_FILE="/tmp/toto.log"
MAX_LOG_SIZE=1024000  # Taille max du fichier log (octets)
LOG_TO_FILE=false     
VERBOSE=false          # Afficher les logs en console
LOG_LEVEL="WARN"


### FUNCTIONS

print_help() {
    cat << EOF
Usage: $0 [OPTIONS]

Description :
Template de script bash avec debug en couleur, gestion et rotation de log.

Options :
    -d, --debug : active le mode debug
    -h, --help : affiche l'aide et quitte le script

Exemples :
    $0 -d
    $0 --help

EOF
}

rotate_logs() {
    local date=$()
    if [ -f "$LOG_FILE" ] && [ $(stat -c%s "$LOG_FILE") -ge $MAX_LOG_SIZE ]; then
        mv "$LOG_FILE" "$LOG_FILE.old":
        touch "$LOG_FILE"
    fi
}

log_message() {
    local level=${1^^}
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local script_name=$(basename "$0")

    local -A log_levels=( ["DEBUG"]=0 ["INFO"]=1 ["WARN"]=2 ["ERROR"]=3 )
    local -A colors=(
        [DEBUG]='\033[0;32m'  # vert
        [INFO]='\033[0;34m'   # Bleu
        [WARN]='\033[0;33m'   # Jaune
        [ERROR]='\033[0;31m'  # Rouge
        [NC]='\033[0m'        # Pas de couleur
    )

    local color="${colors[$level]:-${colors[NC]}}"

    if [ ${log_levels[$level]:-5} -ge ${log_levels[$LOG_LEVEL]} ]; then
        local formatted_message="$timestamp [$level] [$script_name] $message"
        if [ "$LOG_TO_FILE" = true ]; then
            echo "$formatted_message" >> "$LOG_FILE"
        fi
        if [ "$VERBOSE" = true ]; then
            echo -e "${color}${formatted_message}${colors[NC]}"
        fi
    fi
}

args_parsing() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -d|--debug) LOG_LEVEL="DEBUG"; VERBOSE=true; shift ;;
            -h|--help) print_help; exit 0 ;;
            *)
                echo "Invalid option: $1" >&2
                exit 1
                ;;
        esac
    done
}


### MAIN
args_parsing "$@"
rotate_logs

log_message "INFO" "Demarrage du script"
log_message "DEBUG" "Verification des parametres"
log_message "ERROR" "Erreur lors de la connexion a la BDD"
log_message "Warn" "Espace disc faible"
