#!/bin/sh -ex

if [ "$BSD" ]; then
    PATH=/usr/local/lib/bsd-bin:$PATH
    export PATH
fi

export bashcomp_bash=bash
env

if [ -z "${CI-}" ]; then
    mkdir -p /work
    cp -a . /work
    cd /work
fi

autoreconf -i
./configure
make -j

xvfb-run make distcheck \
    PYTESTFLAGS="--verbose --numprocesses=auto --dist=loadfile"
