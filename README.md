# Hopfield Network
## 程式簡介
### 使用說明：
> 透過視覺化界面展示「Hopfield Network」的使用方法

*  <p style="color:red">右方可以選擇訓練資料：「Basic_Training」、「Bonus_Training」</p>

*  所有資料皆以3張圖為一組，且「Bonus_Training」可以再細選子訓練集：「Bonus-x」

* 「訓練」後即產生所選資料的訓練結果

* 訓練後，可透過滑鼠點擊左側的圖片來選擇「測試資料」，並可「加入雜訊」

* 「驗證」後下方會產生Hopfield Network的 ( 聯想 ) 結果

### 範例圖：
![](https://i.imgur.com/dN95xtw.jpg)

## Hopfield Network 演算法
### 演算法簡介
> 應用於各方面的一種「聯想式學習」演算法
* 模擬人類記憶中聯想的神經網路，又分為「自聯想」、「異聯想」

  * 自聯想： 看到模糊不清的照片，依然能辨別出原來的風貌
  
  * 異聯想： 聽到相對論，想到愛因斯坦的名字
  
* Hopfield 是用於「自聯想」型的類神經網路

* 聯想記憶的表達方式為 <img src="https://render.githubusercontent.com/render/math?math=Y = W X">，目標就是找到適合的 W，讓 X 聯想( 回想 )起 Y
  * X - 輸入
  * Y - 聯想結果
  * W - 網路鍵結值
  
* W 的學習有很多種方法：**Hebbian rule**、Projection rule...，此處使用前者。

* 輸入、輸出向量都必須是二元值 ( 0、1 ) 或雙極值 ( -1、1 )，但在Hebbian rule的學習法則下，兩者的學習公式會有些微差別：
  * 輸入輸出為二元值 ( 0、1 )時，W更新公式： 
  
     <img src="https://render.githubusercontent.com/render/math?math=\Delta w_{ij} = s_{i} * s_{j}">
  * 輸入輸出為雙極值 ( -1、1 )，W更新公式 ( 4用於取整數，可有可無 )：
  
     <img src="https://render.githubusercontent.com/render/math?math=\Delta w_{ij} = 4 (s_{i}-1/2) * (s_{j}-1/2)">
  
* **神經網路架構圖：**  
  <img src="https://i.imgur.com/AtccqVU.png">  

### 演算法步驟
> 下述的「學習階段」、「回想階段」之相關數學證明請參考原始Paper
#### 1. 學習階段

#### 2. 回想階段
