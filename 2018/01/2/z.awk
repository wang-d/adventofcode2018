#!/usr/bin/awk -f

function z (n) {
    sum += n
    if (sum in a) {
        printf("sum=%d\n", sum)
        exit
    }
    a[sum] = 1
}

{ print NR
    ns[NR - 1] = $1 }

END {
    printf("NR=%d\n", NR)
    z(0)
    for(i = 0; 1 < 2; i++) {
        z(ns[i % NR])
    }
}
