import requests
import smtplib

def email_my_ip():

  try:
    url='https://api.ipify.org'
    r = requests.get(url)

    from_address='pickles5388@gmail.com'
    to_address='pickles5388@gmail.com'
    app_pw='rqfncpzztqdhnsqd'

    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_address, app_pw)
    s.sendmail(from_address, to_address, r.text)
    s.quit()

    return r.text
    # print(r.text)

  except requests.exceptions.RequestException as e:

    print(e)
    return None





if __name__ == '__main__':
  email_my_ip()
