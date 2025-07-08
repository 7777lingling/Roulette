# 輪盤抽獎遊戲 (Roulette)

這是一個用 Python Flask 製作的網頁版輪盤抽獎遊戲，支援自訂選項與數字輪盤兩種模式，並有美觀的動畫介面。

## 主要功能
- 自訂選項輪盤（可自訂名稱與權重）
- 數字輪盤（可設定範圍、排除數字、去重）
- 輪盤動畫、指針、結果顯示
- 響應式設計，手機/電腦皆可用

## 啟動方式
1. 安裝 Python 3.x
2. 安裝 Flask：
   ```bash
   pip install flask
   ```
3. 啟動伺服器：
   ```bash
   python app.py
   ```
4. 用瀏覽器開啟 http://127.0.0.1:5000

## 目錄結構
- app.py
- templates/
  - index.html
  - custom_mode.html
  - number_roulette.html
  - result.html

---

如有問題歡迎提 issue！ 