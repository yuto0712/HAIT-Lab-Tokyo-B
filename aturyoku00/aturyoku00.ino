int val = 0; //変数を設定しておく
void setup() {
  pinMode(13,OUTPUT);
Serial.begin(9600); 
}

void loop() { //電源が切れるまで繰り返し実行される
val = analogRead(0); //アナログピンから値を読み取る。0はピン番号
//Serial.println(val); //シリアルポートへ出力。printlnで改行してくれる
delay(700); //1000ms（1秒）ごとに実行
if (val > 20 and val < 100) {
  Serial.println("H");
  digitalWrite(13,HIGH);
  delay(500);
  }
else  {
  digitalWrite(13,LOW);
  Serial.println("L");
  //Serial.println(val);
  delay(500);
  }
}
