# 🐙💼 OctOffers
Automatic offers from any career website

### Supported Platforms
- **Djinni**
- **Indeed**

### DotENV sample
```env
DJINNI_SESSIONID="sessionid_cookie:2193dhsa9h419d1"
```

### Usage 
1) **Install required dependency**
`bundle install`
2) **Provide credentials**
`echo "SECRET='data'" > .env`
3) **Use OctOffers**
```bash
ruby bin/main.rb start djinni
ruby bin/main.rb help
```

### How to run tests 
`rake test`
