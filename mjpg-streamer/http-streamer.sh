#!/bin/bash

export LD_LIBRARY_PATH="/home/tsukasa/mjpg-streamer/mjpg-streamer-experimental"
STREAMER="$LD_LIBRARY_PATH/mjpg_streamer" #Streamerフルパス指定

RES="320x240" #画面サイズX
FPS="10"  #フレームレート

#Webサーバー設定
WWWDOC="$LD_LIBRARY_PATH/www"
PORT="8080"

#起動コマンド
$STREAMER -i "input_uvc.so -y -n -f $FPS -r $RES -d /dev/video0" -o "output_http.so -w $WWWDOC -p $PORT"
