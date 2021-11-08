#!/usr/bin/env bash

function display_usage() {
    echo "usage: $0 {develop|hotfix|PREPROD|SIT|SIT2|UAT}"
}

function build_develop() {
    ### build develop stuff ###
    echo "building develop stuff"
}

function build_hotfix() {
    ### build hotfix stuff ###
    echo "building hotfix stuff"
}


function build_preprod() {
    ### build hotfixstuff ###
    echo "building preprod stuff"
}


function build_sit() {
    ### build sit stuff ###
    echo "building sit stuff"
}


function build_sit2() {
    ### build sit2 stuff ###
    echo "building sit2 stuff"
}


function build_uat() {
    ### build uat stuff ###
    echo "building uat stuff"
}


if [[ "$#" -ne 1 ]]; then
    echo "invalid number of parameters provided"
    display_usage
    exit 1
else 
    env=$1
    case $env in
        "develop")
            build_develop
            ;;
        "hotfix")
            build_hotfix
            ;;
        "PREPROD")
            build_preprod
            ;;
        "SIT")
            build_sit
            ;;
        "SIT2")
            build_sit2
            ;;
        "UAT")
            build_uat
            ;;
        *)
            echo "invalid parameter provided"
            display_usage
            exit 1
            ;;
    esac
fi
