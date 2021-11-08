#!/usr/bin/env bash

function display_usage() {
    echo "usage: $0 {PREPROD|SIT|SIT2|UAT}"
}

function run_preprod_tests() {
    ### regression tests preprod ###
    echo "regression tests preprod"
}

function run_sit_tests() {
    ### regression tests sit ###
    echo "regression tests sit"
}

function run_support_tests() {
    ### regression tests support ###
    echo "regression tests support"
}

function run_uat_tests() {
    ### regression tests uat ###
    echo "regression tests uat"
}


if [[ "$#" -ne 1 ]]; then
    echo "invalid number of parameters provided"
    display_usage
    exit 1
else 
    env=$1
    case $env in
        "PREPROD")
            run_preprod_tests
            ;;
        "SIT")
            run_sit_tests
            ;;
        "SIT2")
            run_support_tests
            ;;
        "UAT")
            run_uat_tests
            ;;
        *)
            echo "invalid environment provided"
            display_usage
            exit 1
            ;;
    esac
fi
