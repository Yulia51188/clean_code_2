# Robot maintenance 

This service kit allows you to contact the robot in emergency situations.

## How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables.

Interpreted in text last voice command: "Нужен селен". 

- `COMMAND`

.env example:

```
COMMAND="Нужен селен"
```

## Run

Launch on Linux(Python 3) or Windows as simple

```bash
$ python main.py
```

## You will see

```
$ python main.py

Проверка связи с роботом...
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         | ˱˱    ∙    ˲˲ 21/27 [78%] in 1s (16.3/s, eta: 0s)
```
```
Связь с роботом установлена!
```

### Don't forget! Three Laws of Robotics

**First Law.** A robot may not injure a human being or, through inaction, allow a human being to come to harm.

**Second Law.** A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.

**Third Law.** A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
