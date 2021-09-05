
_get_repolink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $PETERCORD_REPO == "PETERCORDBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL0lsaGFtTWFuc2llei9USEUtUEVURVJDT1JEL2FyY2hpdmUvbWFzdGVyLnppcA=" | base64 -d
    elif [[ $PETERCORD_REPO == "PETERCORDBOT" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL0lsaGFtTWFuc2llei9USEUtUEVURVJDT1JEL2FyY2hpdmUvbWFzdGVyLnppcA=" | base64 -d
    elif [[ $PETERCORD_REPO =~ $regex ]]
    then
        if [[ $PETERCORD_REPO_BRANCH ]]
        then
            echo "${PETERCORD_REPO}/archive/${PETERCORD_REPO_BRANCH}.zip"
        else
            echo "${PETERCORD_REPO}/archive/master.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL0lsaGFtTWFuc2llei9USEUtUEVURVJDT1JEL2FyY2hpdmUvbWFzdGVyLnppcA=" | base64 -d
    fi
}


_set_bot () {
    local zippath
    zippath="PETERCORDBOT.zip"
    echo "  Downloading source code ..."
    wget -q $(_get_repolink) -O "$zippath"
    echo "  Unpacking Data ..."
    PETERCORDPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo "Done"
    echo "  Cleaning ..."
    rm -rf "$zippath"
    sleep 5
    cd $PETERCORDPATH
    echo "    Starting PETERCORDBOT   "
    echo "
                        ((((((PETERCORD USERBOT))))
                         ┏━━━━━━━━━━━━━━━━━━━ 
                         ┗━━━━━━━━━━━━━━━━━━━ 
    "

    python3 ../setup/updater.py ../requirements.txt requirements.txt
    python3 -m userbot
}

_set_bot
