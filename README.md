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
![](https://i.imgur.com/TbLk2fK.png)

## Hopfield Network 演算法
### 演算法簡介
> 應用於各方面的一種「聯想式學習」演算法
* 模擬人類記憶中聯想的神經網路，又分為「自聯想」、「異聯想」

  * 自聯想： 看到模糊不清的照片，依然能辨別出原來的風貌
  
  * 異聯想： 聽到相對論，想到愛因斯坦的名字
  
* Hopfield 是用於「自聯想」型的類神經網路

* 聯想記憶的表達方式為 <img src="https://render.githubusercontent.com/render/math?math=Y = W X">，目標就是找到適合的 W，讓 X 聯想( 回想 )起 Y
  * X - 輸入，為n x 1的矩陣 
  
  * Y - 聯想結果，為n x 1的矩陣 
  
  * W - 網路鍵結值，為n x n的矩陣 
  
* W 的學習有很多種方法：**Hebbian rule**、Projection rule...。

* 輸入、輸出向量都必須是雙極值 ( -1、1 ) 或 二元值 ( 0、1 )，但在Hebbian rule的學習法則下，兩者的學習公式會有些微差別：
  > w 表示第 j 到第 i 個神經元的鍵結值，x 表示資料的第 i 維或第 j 維

  * 輸入輸出為雙極值 ( -1、1 )，W更新公式 ，：
  
     <img src="https://render.githubusercontent.com/render/math?math=\Delta w_{ij} = x_{i} * x_{j}">
     
  * 輸入輸出為二元值 ( 0、1 )時，W更新公式 ( 4用於取整數，可有可無 )： 
  
     <img src="https://render.githubusercontent.com/render/math?math=\Delta w_{ij} = 4 (x_{i}-{1 \over 2}) * (x_{j}-{1 \over 2})">
     

     
* **神經網路架構圖：**  
  <img src="https://i.imgur.com/AtccqVU.png">  

### 演算法步驟
> 下述的「學習階段」、「回想階段」之相關數學證明請參考原始Paper
#### 1. 學習階段
此程式採用Hebbian rule學習法中的雙極值 ( -1、1 )輸入輸出，參數簡介：
* N筆輸入向量，每一筆有P個維度，表示成 x

* W為P x P的矩陣，預設為0矩陣(避免正回授

* I為單位矩陣

<img src="https://render.githubusercontent.com/render/math?math=x_i=[x_{i1},...,x_{ip}]"> , <img src="https://render.githubusercontent.com/render/math?math=i=1, 2,...,N">


<img src="https://render.githubusercontent.com/render/math?math=W = \begin{bmatrix}w_{11} \quad \dots \quad w_{1p} \\ \vdots \quad \ddots \quad \vdots \\ w_{p1} \quad \dots \quad w_{pp} \end{bmatrix} ={1 \over p} \sum_{k=1}^{N}x_k*{x_k}^T-{N \over p}I">

W透過上述公式訓練一次後即完成( 只要訓練一次就可以了!! )。另外此處與簡介最後一點所提的公式是一樣的，上述表達是單個鍵結值的單次更新，可以透過矩陣與sigma來表示全部資料的更新。此處很不好理解，必須用一點想像力，如果有疑問可以來信詢問。

> 為什麼要減去單位矩陣？為了讓W的對角為0，Hopfield在原始Paper中，神經元並不會連到自己

#### 2. 回想階段

