# 🐙💼 OctOffers
Search for job interviews automatically

### Architecture overview
![architecture](architecture.svg)

### Supported Platforms
- **Djinni**

### Requirements
- **python 3.9+**
- **chrome webdriver**

### DotENV sample
```env
DJINNI_TOKEN="sessionid_cookie:2193dhsa9h419d1"
HEADLESS=1
```

### Usage 
1) **Install required dependency**
`pip install -r requirements.txt`
2) **Use OctOffers**
```bash
python octoffers djinni --apply
```
