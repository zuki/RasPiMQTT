# RasPiとiPod TouchをMQTTでつないでLチカ

ソースは[\[GUIDE\] Communicate between iOS and Raspberry Pi using MQTT](https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=196010&hilit=bluetooth+iOS&sid=4ae853ce600e4f9a88a5892f3ae83aeb)による

## 操作方法

### RasPi側

1. mosquiito が立ち上がっていること（serviceで立ち上がっているはず)

  ```bash
  $ sudo service mosquiito status
  $ sudo service mosquiito start        # 立ち上がってない場合
  ```

2. mosquittoクライアントを立ち上げる

  ```
  $ cd /home/pi/examples/mqtt
  $ ./mqtt-client.py
  ```

### iPos側

1. WiFi接続
2. `RaspiOperator` アプリを立ち上げる
3. [接続] ボタンを押してmqtt-clientに接続
4. スイッチのオンオフでLEDがオン・オフするはず
5. [切断] ボタンを押して切断
