# 🐙💼 OctOffers
Automatic offers from any career website

### Supported Platforms
- **Djinni**
- **Indeed**

### Requirements
- **ruby** ~> 3.0 
- **chrome webdriver**

### DotENV sample
```env
DJINNI_SESSIONID="sessionid_cookie:2193dhsa9h419d1"
HEADLESS=1
```

### Usage 
1) **Install required dependency**
`bundle install`
2) **Provide credentials**
`echo "SECRET='data'" > .env`
3) **Use OctOffers**
```bash
ruby bin/main.rb fetch djinni devops
ruby bin/main.rb help
```

### How to run tests 
`rake test`
