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

## Perfromans

### Classification Report
|     | Precision | Recall | F1-Score | Support |
| --- | --------- | ------ | -------- | ------- |
| Cat | 0.99      | 0.65   | 0.79     | 1837    |
| Dog | 0.75      | 0.99   | 0.85     | 1912    |

### Confusion Matrix
|     | Cat  | Dog  |
| --- | ---- | ---- |
| Cat | 1197 | 640  |
| Dog | 14   | 1898 |

### Accuracy ve Loss
![acc-loss](image/performance.jpg)

## Grup Üyeleri
- Yasin Tarakçı - [GitHub](https://github.com/ysntrkc) | [LinkedIn](https://www.linkedin.com/in/yasintarakci)
- Gülnur Ögür - [GitHub](https://github.com/gulnurogur) | [LinkedIn](https://www.linkedin.com/in/gulnurogur/)
- Hatice İkbal Göllüce - [GitHub](https://github.com/haticeikbal) | [LinkedIn](https://www.linkedin.com/in/haticeikbalgolluce/)
- Kübra Küçükkartal - [GitHub](https://github.com/hkubrakkartal) | [LinkedIn](https://www.linkedin.com/in/hatice-kubra-kucukkartal/)
- Ali Mert Kocaman - [GitHub](https://github.com/alimert2209) | [LinkedIn](https://www.linkedin.com/in/alimertkocaman/)
- Cansu Karahan - [GitHub](https://github.com/cansukarahann) | [LinkedIn](https://www.linkedin.com/in/cansu-karahan/)
