# 10000/50/25 Benchmark

## One Core Utilisation

randomi.py

### Conrads Setup (HDD)
	53.5 sec

### Conrads Setup (m.2 SSD)
	63.29 sec

### Tillmanns Setup (HDD)
	82.29 sec

## 4 Core Utilisation

randomi4c.py

### Conrads Setup (HDD)
	17.71 sec

### Conrads Setup (m.2 SSD)
	16.33 sec

## 8 Core Utilisation

randomiUnLi.py

### Conrads Setup (HDD)
	12.58 sec

### Conrads Setup (m.2 SSD)
	12.32 sec

## One Core Utilisation (Mk II)

randomi.py (Mk II)

### Conrads Setup (HDD)
	54.45 sec

### 8 Core Utilisation (Mk II)

randomi.py (Mk II)

### Conrads Setup (HDD)
	11.57 sec

### Tillmanns Setup (HDD)
	16.30 sec

### 16 Core Utilisation (Mk II)

randomi.py (Mk II)

### Tillmanns Setup (HDD)
	14.98 sec

### 16 Core Utilisation & Win Defender Folder exception(Mk II)

randomi.py (Mk II)

### Tillmanns Setup (RAMDISK)
	7.47 sec

### Tillmanns Setup (HDD)
	8.60 sec

## 32 Thread Utilisation & Win Defender Folder exception(Mk II)

randomi.py (Mk II)

### Tillmanns Setup (RAMDISK)
	7.54 sec

### Tillmanns Setup (HDD)
	7.77 sec

## Conclusions
- The limit for generating this benchmark seems to be at around 7.50 sec with the bottleneck being the CPU and the I/O system
- The generator randomI.py is pretty much as good as it needs to be at generating 10.000 entries in just about 8 seconds
- Further improvements could be:
	- Generating string values
	- Generating realistic data like adresses, names, phone numbers (...)
	- Exporting the data into an SQL database instead of files