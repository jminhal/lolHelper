import requests
import urllib.request
import re
import bs4 as bs




def user(nick):
    infoUser = []
    # the target we want to open
    url = 'https://u.gg/lol/profile/euw1/' + nick
    res = requests.get(url)
    #http_respone 200 means OK status
    if res.status_code == 200:
        print('Success!')

        info = str(bs.BeautifulSoup(urllib.request.urlopen(url).read(), 'lxml'))

        try:
            urs = '(?<=("summonerName":")).*?(?=("},"playerOverviewKpis"))'
            urs = str(re.search(urs, info).group(0))
        except:
            urs = 0
        if urs == 0:
            infoUser.append(0)
            return infoUser
        else:
            rank = '(?<=("tier":")).*?(?=(","wins"))'
            rank = str(re.search(rank, info).group(0))
            tier = '(?<=(,"rank":")).*?(?=(","role":))'
            tier = str(re.search(tier, info).group(0))
            lp ='(?<=(,"lp":)).*?(?=(,"promoProgress":))'
            lp = str(re.search(lp, info).group(0))
            wins='(?<=(","wins":)).*?(?=(},{"__typename"))'
            wins = str(re.search(wins, info).group(0))
            loses='(?<=(,"losses":)).*?(?=(,"lp":))'
            loses = re.search(loses, info).group(0)
            base=int(wins)+int(loses)
            wr=0
            if base>0:
                wr=str(int(wins)*100/(base))
            # add information to the array
            infoUser.append(urs)
            infoUser.append(rank)
            infoUser.append(tier)
            infoUser.append(lp)
            infoUser.append(wins)
            infoUser.append(loses)
            infoUser.append(wr)
            return infoUser
    # http_response 500 server error
    elif res.status_code == 500:
        print('Server dead.')

