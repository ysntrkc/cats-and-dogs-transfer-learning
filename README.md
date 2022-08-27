# Cats vs Dogs Transfer Learning Projesi

## Tanım
Bu proje AI Summer Camp'22 kapsamında geliştirdiğimiz ikinci projedir. Bu projede Cats and Dogs veri setini kullandık. Kodları çalıştırmak için veri setini [buradan](https://www.microsoft.com/en-us/download/details.aspx?id=54765) indirip [data](data/) klasörüne zip olarak atmanız gerekmektedir.

## Önişlem
- Bu aşamada ilk olarak veriyi zipten çıkardık.
- Sonraki aşamada fotoğrafları yeniden boyutlandırdık ve dosya isminin başına cat veya dog ekleyerek farklı bir klasöre kaydettik.
- Son aşamada da dosyaları train, test ve validation olarak farklı klasörlere ayırdık.

## Model
- Bu aşamada ilk olarak train, test ve validation klasörlerindeki dosyaları farklı listelere dosya isimlerini ekledik.
- Dosyaları ismine göre tek tek okuyarak fotoğrafları arraylere çeviriyoruz.
- Sonrasında arraydeki verileri normalize ettik.
- VGG16 modelini base model olarak aldık ve üzerine birkaç adım daha ekleyerek modelimizi oluşturduk.
- Sonrasında modeli eğittik.
- Test veri setiyle bir tahmin yapıp sonuçlarını aldık.

## Gereksinimler
- Python 3.6 veya üstü
- TensorFlow 2.5
- Diğer gereksinimleri de [requirements.txt](requirements.txt) dosyasında görebilirsiniz.

## Perfromans
- Bu sonuçları NVIDIA RTX A6000 ekran kartına sahip Windows bir makine kullanarak elde ettik.

### Accuracy ve Loss
![acc-loss](image/performance.jpg)


### Confusion Matrix
- Bu tablodaki sonuçları test veri seti ile elde ettik.

|            | Pred Cat | Pred Dog |
| ---------- | -------- | -------- |
| Actual Cat | 1233     | 600      |
| Actual Dog | 13       | 1903     |

### Classification Report
- Bu tablodaki sonuçları test veri seti ile elde ettik.

|     | Precision | Recall | F1-Score | Support |
| --- | --------- | ------ | -------- | ------- |
| Cat | 0.99      | 0.67   | 0.80     | 1833    |
| Dog | 0.76      | 0.99   | 0.86     | 1916    |



## Grup Üyeleri
- Yasin Tarakçı - [GitHub](https://github.com/ysntrkc) | [LinkedIn](https://www.linkedin.com/in/yasintarakci)
- Gülnur Ögür - [GitHub](https://github.com/gulnurogur) | [LinkedIn](https://www.linkedin.com/in/gulnurogur)
- Hatice İkbal Göllüce - [GitHub](https://github.com/haticeikbal) | [LinkedIn](https://www.linkedin.com/in/haticeikbalgolluce/)
- Kübra Küçükkartal - [GitHub](https://github.com/hkubrakkartal) | [LinkedIn](https://www.linkedin.com/in/hatice-kubra-kucukkartal/)
- Ali Mert Kocaman - [GitHub](https://github.com/alimert2209) | [LinkedIn](https://www.linkedin.com/in/alimertkocaman/)
- Cansu Karahan - [GitHub](https://github.com/cansukarahann) | [LinkedIn](https://www.linkedin.com/in/cansu-karahan/)
