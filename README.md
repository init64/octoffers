# 🐙💼 OctOffers
Search for job interviews automatically

### Supported Platforms
- **Djinni**
- **Indeed** (Private access only)

### Requirements
- **python 3.9+**
- **chrome webdriver**

### Quick start
1) **Install required dependency**
`pip install -r requirements.txt`
2) **Pull Private Drivers** (if you have access)
`git submodule init && git submodule update`
3) **Use OctOffers**
`python octoffers`

### Architecture diagram
![architecture](architecture.svg)

### Example use cases
- **Fetch about 50 jobs from djinni**
```bash
python octoffers djinni fetch devops --pages 5
```
- **Apply to all available jobs from djinni**
```bash
python octoffers djinni apply "Hello, I'm looking for job" # <-- This argument stands for cover letter
```

### DotENV sample
```env
DJINNI_SESSION_ID="sessionid_cookie:2193dhsa9h419d1"
```

