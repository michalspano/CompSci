#! /bin/bash

function main() {
    DELAY=1
    printf 'Running City-landscape, opening all pbms.\n'
    sleep $DELAY

    # Check valid out
    FILE_EXT='pbm'
    if [ ! -f "out/out_mapN.${FILE_EXT}" ]; then
        printf '[    F    ]    Source not found\n'
        exit 1  # This will exit Makefile
    fi

    printf '[   OK   ]   Status \n'

    sleep $DELAY
}

# Invoke main func
main