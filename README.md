# 🐙💼 OctOffers
Octoffers is a tool that automatically hunts down suitable jobs and applies for you on major job boards.

![resultsfromindeed](./assets/indeed_result.png)

### Supported Platforms
- **Djinni**
- **Indeed** (Private)

### Requirements
- **python 3.9+**
- **chrome webdriver**

### Quick start
1) **Install required dependency**
`pip install -r requirements.txt`
2) **Pull Private Drivers** (if you have access)
`git submodule update --init --recursive`
3) **Use OctOffers**
`python octoffers`

### Example use cases
- **Fetch about 50 jobs from djinni**
```bash
python octoffers djinni fetch devops --pages 5
```
- **Apply to all available jobs from djinni**
```bash
python octoffers djinni apply "Hello, I'm looking for job" # <-- This argument stands for cover letter
```

### `.env` sample
```env
DJINNI_SESSION_ID="sessionid_cookie:2193dhsa9h419d1"
```

### Questions & Anwsers
- **Q:** Does Octoffers offer customization of applications or cover letters, or is it more of a basic submission tool?
    - **A:** Customization depends on the driver, if specific career platform is hard to automate, most likely that `apply()` submission method will be more basic.
- **Q:** What is the success rate of Octoffers applications compared to manual ones?
    - **A:** It depends on the role that you're applying for,

### Software architecture
![architecture](./assets/architecture.svg)
