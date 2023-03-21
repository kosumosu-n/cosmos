// カウントを増やすボタンのイベントリスナー
document.getElementById("increment").addEventListener("click", function() {
    // カウントを取得
    let count = parseInt(document.getElementById("count").innerHTML);
    // カウントを増やす
    count++;
    // カウントを更新
    document.getElementById("count").innerHTML = count.toString();
  });
  
  // リセットボタンのイベントリスナー
  document.getElementById("reset").addEventListener("click", function() {
    // カウントを0にリセット
    document.getElementById("count").innerHTML = "0";
  });