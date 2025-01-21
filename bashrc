# ~/.bashrc

### Variables
export http_proxy=""                   # Define HTTP proxy if needed
export https_proxy=""

### Display prompt
customize_prompt() {
    PS1="\[\033[32m\]\u@\h \w $(if [[ $? -ne 0 ]]; then echo -e '\[\033[31m\]'; fi)\$ \[\033[00m\]"
}
PROMPT_COMMAND=customize_prompt

### History
export HISTIGNORE="ls:ll"              # Ignore ls and ll commands
HISTCONTROL=ignorespace:ignoredups     # Ignore commands starting with space and duplicates
shopt -s histappend                    # Append without overwriting history
HISTSIZE=1000                          # Max commands in session history
HISTFILESIZE=10000                     # Max commands in total history file
HISTTIMEFORMAT="%d/%m/%y %T"           # Add date and time in history
bind '"\e[A": history-search-backward' # Enhanced search with UP
bind '"\e[B": history-search-forward'  # Enhanced search with DOWN
bind '"\C-@":"clear\n"'                # Clear the screen easily using CTRL + Space.
### 
alias ls='ls --color=auto'
alias ll='ls -lrth --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

