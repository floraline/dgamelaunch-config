#!/bin/bash

source $DGL_CONF_HOME/crawl-git.conf

if [[ $UID != 0 ]]; then
    echo "$0 must be run as root!"
    exit 1
fi

if [[ $1 == -v || $1 == --verbose ]]; then
    verbose=1
else
    verbose=0
fi

verbiate() {
    ((verbose)) && echo "$@" >&2
}

quietly() {
    "$@" >/dev/null 2>&1
}

failures=()
skip=0 succ=0 fail=0 sent=0
shopt -s nullglob
#for ttyrec in "$TTYRECDIR"/*/*.ttyrec; do
find "$TTYRECDIR" -type f \( -name "*.ttyrec" \)|while read ttyrec; do

    # If anyone has it open, skip it.
    if quietly lsof "$ttyrec"; then
        verbiate -n "."
        let ++skip
        continue
    fi
    if bzip2 "$ttyrec"; then
        let ++succ
        #verbiate -n "+"
        s3_user="$(basename $(dirname $ttyrec))"
        if quietly /usr/local/bin/s3cmd put -P "$ttyrec.bz2" "s3://crawl-kelbi-org/ttyrec/$s3_user/"; then
            let ++sent
            rm "$ttyrec.bz2"
            verbiate -n "^"
        else
            verbiate -n "+"
        fi
    else
        let ++fail
        verbiate -n "X"
        failures+=( "$ttyrec" )
    fi
done
verbiate

if (( failed || verbose )); then
    printf "compressed ttyrec\n"
    #printf "%d succeeded\t%d failed\t%d skipped\n" "$succ" "$fail" "$skip"
    #printf "%d archived" "$sent"
    if (( failed )); then
        printf "\nFailing files:\n"
        printf "  %s\n" "${failures[@]}"
        exit 1
    fi
    printf "\n"
fi

exit 0
