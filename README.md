****Giriş****

Veri, harf veya sayı olarak kodlanmış ham bilgidir. Günümüzde bilgi teknolojilerinin hızla ilerlemesi ve veri kullanımının artmasıyla birlikte, işlemlerimizin büyük bir kısmı dijital ortamlarda gerçekleştirilmektedir. Bu verilerin analizi, çağımızın en önemli konularından biri olmuştur.

E-ticaret sektöründe müşteri bilgilerini ve işlem verilerini etkili bir şekilde analiz etmek büyük bir önem taşır. Büyük veri analitiği, bu bağlamda müşteri davranışlarını anlamak ve satış stratejileri geliştirmek için kullanılan kritik bir teknolojidir. Bu projede, büyük veri teknolojileri kullanılarak e-ticaret sepet analizleri gerçekleştirilmiş ve elde edilen veriler doğrultusunda satış stratejileri geliştirilmiştir.
Büyük veri teknolojileri kullanılarak e-ticaret sepet analizleri gerçekleştirilmiş ve elde edilen veriler doğrultusunda satış stratejileri geliştirilmiştir. Lokal ortamda oluşturulan veriler, ürün ve kullanıcı bilgilerini içeren veri setlerinden rastgele seçilerek simüle edilmiştir. Her bir veri kaydına, üretim saati ve satın alma durumu bilgisi eklenmiştir. Veriler, Apache Kafka kullanılarak JSON formatında uzak bir sunucuya aktarılmış ve daha sonra bu veriler başka bir sunucudan çekilerek Apache Spark ile analiz edilmiştir.

Proje kapsamında hem toplu analiz (batch analysis) hem de gerçek zamanlı analiz (real-time analysis) gerçekleştirilmiştir. Ayrıca, birliktelik analizi ile müşterilerin bir ürünü aldıktan sonra başka bir ürünü alma olasılıkları incelenmiş ve bu analizler sonucunda yeni satış stratejileri geliştirilmiştir. Bu süreç, e-ticaret işletmelerinin müşteri alışkanlıklarını daha iyi anlamalarına ve bu bilgiler doğrultusunda stratejik kararlar almalarına olanak tanımaktadır. Bu da müşteri memnuniyetini artırmak ve satışları optimize etmek için önemli bir avantaj sağlamaktadır.


****Veri Üretimi ve Simülasyonu****
Veriler, “Amazon-Products.csv” dosyasından rastgele bir ürün ve “UsersDataset.csv” dosyasından rastgele bir kullanıcı seçilerek elde edilmektedir. Buna ek olarak, verilerin üretildiği tarih ve saat ile kullanıcının ilgili ürünü satın aldığını (“1”) veya sadece aradığını (“0”) gösteren bir satın alma durumu eklenmektedir. Bu veriler, JSON formatında oluşturularak uzaktaki Apache Kafka sunucusuna kaydedilmektedir.

Örnek bir veri;
{"UserID": "21888",
"Name": "Gerald Alegre",
"Gender": "Female",
"DOB": "1957-11-24",
"Interests": "'Beauty','Pets'",
"City": "Ibiporã",
"Country": "Brazil",
"ProductId": "392660",
"ProductName": "crocs Mens Santa Cruz Loafer",
"MainCategory": "stores",
"SubCategory": "Men's Fashion",
"Ratings": "4.1",
"NoOfRatings": "16408.0",
"DiscountPrice": " $23.36",
"ActualPrice": " $51.93",
"PurchaseStatus": 1,
"Timestamp": "2024-06-20 14:28:42"}


**Apache Kafka Entegrasyonu**
Apache Kafka, yüksek hacimli veri akışlarını gerçek zamanlı olarak işlemek ve yönetmek için kullanılan açık kaynaklı, dağıtık bir veri akış platformudur. Kafka, verileri birçok sunucuda dağıtarak yüksek ölçeklenebilirlik ve güvenilirlik sağlar, düşük gecikme ile büyük veri hacimlerini hızlıca işleyebilir. Mesajları yayıncı-abone modeli ile üreticilerden tüketicilere iletir, kalıcı depolama özelliği ile veri kaybını minimize eder. Gerçek zamanlı veri analitiği, veri entegrasyonu, log toplama ve mikro hizmetler arası iletişim gibi alanlarda yaygın olarak kullanılır.

Linux işletim sistemi üzerine kurulan Apache kafka’ya, çeşitli ağ protokollerini (SSH, Telnet, rlogin ve seri bağlantılar) destekleyen ve Windows işletim sisteminde uzaktaki bilgisayarlara bağlanmayı sağlayan açık kaynaklı bir terminal emülatör olan “Putty.exe” ile bağlanılmaktadır.


**Apache Spark Entegrasyonu**
Apache Spark, büyük veri işleme için geliştirilmiş, açık kaynaklı bir veri analiz motorudur. Hızlı, genel amaçlı ve genişletilebilir olmasıyla bilinir. Spark, veri kümelerini bellek içi işlemeyle hızlı analiz yapabilen ve MapReduce modelinden daha yüksek performans sağlayan bir sistemdir. Çeşitli veri işleme görevlerini kolaylaştırmak için Spark SQL, Spark Streaming, MLlib ve GraphX gibi modülleri içerir. Ayrıca, Hadoop, Cassandra, HBase ve S3 gibi birçok veri kaynağıyla uyumludur ve geniş bir ekosisteme sahiptir. Spark, büyük veri analizini daha hızlı, esnek ve kullanıcı dostu hale getirir.


************************ENGLISH************************

**Introduction**
Data is raw information coded as letters or numbers. With the rapid advancement of information technologies and the increasing use of data, a large portion of our operations are conducted in digital environments. The analysis of this data has become one of the most important topics of our time.

In the e-commerce sector, effectively analyzing customer information and transaction data is of great importance. Big data analytics is a critical technology used in this context to understand customer behaviors and develop sales strategies. In this project, basket analyses in e-commerce were conducted using big data technologies, and sales strategies were developed based on the obtained data. The data, created in a local environment, were simulated by randomly selecting from datasets containing product and user information. Each data record was supplemented with the production time and purchase status information. The data was transferred to a remote server in JSON format using Apache Kafka, and then these data were retrieved from another server and analyzed with Apache Spark.

Both batch analysis and real-time analysis were conducted within the scope of the project. Additionally, with association analysis, the likelihood of customers purchasing another product after buying a certain product was examined, and new sales strategies were developed based on these analyses. This process enables e-commerce businesses to better understand customer habits and make strategic decisions based on this information. This provides a significant advantage in increasing customer satisfaction and optimizing sales.

**Data Generation and Simulation**
The data is obtained by randomly selecting a product from the "Amazon-Products.csv" file and a user from the "UsersDataset.csv" file. In addition, the date and time when the data was generated and a purchase status indicating whether the user bought the relevant product ("1") or just searched for it ("0") are added. This data is created in JSON format and saved to a remote Apache Kafka server.

An example data entry:
{"UserID": "21888",
"Name": "Gerald Alegre",
"Gender": "Female",
"DOB": "1957-11-24",
"Interests": "'Beauty','Pets'",
"City": "Ibiporã",
"Country": "Brazil",
"ProductId": "392660",
"ProductName": "crocs Mens Santa Cruz Loafer",
"MainCategory": "stores",
"SubCategory": "Men's Fashion",
"Ratings": "4.1",
"NoOfRatings": "16408.0",
"DiscountPrice": " $23.36",
"ActualPrice": " $51.93",
"PurchaseStatus": 1,
"Timestamp": "2024-06-20 14:28:42"}

**Apache Kafka Integration**
Apache Kafka is an open-source, distributed data streaming platform used to handle and manage high volumes of data streams in real-time. Kafka provides high scalability and reliability by distributing data across many servers, and it can quickly process large volumes of data with low latency. It transfers messages from producers to consumers using a publish-subscribe model and minimizes data loss with its persistent storage feature. It is widely used in areas such as real-time data analytics, data integration, log collection, and communication between microservices.

Apache Kafka, installed on a Linux operating system, is accessed using “Putty.exe,” an open-source terminal emulator supporting various network protocols (SSH, Telnet, rlogin, and serial connections) and allowing connection to remote computers on Windows operating systems.

**Apache Spark Integration**
Apache Spark is an open-source data analytics engine developed for big data processing. It is known for being fast, general-purpose, and extensible. Spark can perform rapid analysis with in-memory processing of datasets and provides higher performance than the MapReduce model. It includes modules such as Spark SQL, Spark Streaming, MLlib, and GraphX to facilitate various data processing tasks. Additionally, it is compatible with many data sources like Hadoop, Cassandra, HBase, and S3 and has a broad ecosystem. Spark makes big data analytics faster, more flexible, and user-friendly.
