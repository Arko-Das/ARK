#!/usr/bin/env bash
# Tool Name :- IP-Traker
# Author :- ARKODAS
# Date :- 10/10/2019

case "$1" in
  -m)
    php modules/.tracem.php
  ;;
  -t)
    case "$#" in
    2)
      php modules/.traceip.php $2
    ;;
    *)
      echo "error : invalid arguments !!"
      echo "use: ip-tracer -t <target_ip>"
    ;;
    esac
  ;;
  -u)
    php modules/.update.php
    exit
  ;;
  update)
    php modules/.update.php
    exit
  ;;
  start)
    php .IP-Tracer.php
    exit
  ;;
  -rm)
    php modules/.uninstall.php
    exit
  ;;
  *)
    echo "Usage: ip-tracer [command]... [arguments]..."
    echo " Commands:"
    echo " -t <target_ip>      to trace target ip."
    echo " -d                to trace your own ip."
    echo " -h                  to show help."
    echo " -u                  to update ip-trackr."
    echo " help                to show help."
    echo " update              to update ip-tracer."
    echo " start               to start ip-tracer menu."
esac