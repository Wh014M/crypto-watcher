# Crypto-watcher
# Coded by Adrijan Petek

import requests, json, PySimpleGUIWeb as sg, datetime
from json import (load as jsonload, dump as jsondump)
from os import path

SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}


def tim():
    tim = datetime.datetime.now()
    return (tim.strftime("%H:%M:%S %d-%m-%Y"))

def get():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def eth():
    url = 'https://www.bitstamp.net/api/v2/ticker/ethusd/'
    try:
        r = requests.get(url)
        eth = float(json.loads(r.text)['last'])
        return eth
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")



def eu():
    url = 'https://www.bitstamp.net/api/v2/ticker/btceur/'
    try:
        r = requests.get(url)
        bteth = float(json.loads(r.text)['last'])
        return bteth
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def eteu():
    url = 'https://www.bitstamp.net/api/v2/ticker/etheur/'
    try:
        r = requests.get(url)
        etheu = float(json.loads(r.text)['last'])
        return etheu
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def euus():
    url = 'https://www.bitstamp.net/api/v2/ticker/eurusd/'
    try:
        r = requests.get(url)
        eu = float(json.loads(r.text)['last'])
        return eu
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def xrus():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpusd/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xreu():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpeur/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def ltus():
    url = 'https://www.bitstamp.net/api/v2/ticker/ltcusd/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def lteu():
    url = 'https://www.bitstamp.net/api/v2/ticker/ltceur/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def bcus():
    url = 'https://www.bitstamp.net/api/v2/ticker/bchusd/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def bceu():
    url = 'https://www.bitstamp.net/api/v2/ticker/bcheur/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def paxusd():
    url = 'https://www.bitstamp.net/api/v2/ticker/paxusd/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def paxeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/paxeur/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xlmeu():
    url = 'https://www.bitstamp.net/api/v2/ticker/xlmeur/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

def xlmus():
    url = 'https://www.bitstamp.net/api/v2/ticker/xlmusd/'
    try:
        r = requests.get(url)
        xrp = float(json.loads(r.text)['last'])
        return xrp
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")


def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window

def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu',['Settings']]]
    
    layout =   [[sg.Menu(menu_def, tearoff=True)],
                [sg.Image('png/cw.png', size=(250, 100))],
                [sg.Text('1 EUR  =', font=('Helvetica', 11)), sg.Text('', size=(19,1), font=('Helvetica', 11), key='es'), sg.Text('', size=(20,1), font=('Helvetica', 11), key='_DATE_')],
                [sg.Text('')],
                [sg.Text('# ', font=('Helvetica', 13), size=(1,1)), sg.Text('Name', font=('Helvetica', 13), size=(24,1)), sg.Text(' Price USD', size=(15,1), font=('Helvetica', 13)), sg.Text(' Price EUR', size=(15,1), font=('Helvetica', 13))],
                [sg.Text('1 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/bit.png', size=(30, 30)), sg.Text('Bitcoin (BTC)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='coin'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='btceu')],
                [sg.Text('2 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/eth.png', size=(30, 30)), sg.Text('Ethereum (ETH)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='ethe'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='eteuro')],
                [sg.Text('3 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/xrp.png', size=(30, 30)), sg.Text('Ripple (XRP)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='xrp'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='xrpeu')],
                [sg.Text('4 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/lite.png', size=(30, 30)), sg.Text('Litecoin (LTC)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='ltcusd'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='ltceur')],
                [sg.Text('5 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/bch.png', size=(30, 30)), sg.Text('Bitcoin Cash (BCH)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='bcusd'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='bceur')],
                [sg.Text('6 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/pax.png', size=(30, 30)), sg.Text('Paxos Standard (PAX)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='paxu'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='paxe')],
                [sg.Text('7 ', font=('Helvetica', 12), size=(1,1)), sg.Image('png/stellar.png', size=(30, 30)), sg.Text('Stellar (XLM)', font=('Helvetica', 12), size=(20,1)), sg.Text('', size=(15,1), font=('Helvetica', 12),  key='xlmu'), sg.Text('', size=(15,1), font=('Helvetica', 13),  key='xlme')]]

    return sg.Window('CW', layout=layout,
                     font='Helvetica 18',
                     web_ip='127.0.0.1',
                     web_port=8888,
                     )

def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )
    while True:
        if window is None:
            window = create_main_window(settings)
        coinprice = get()
        btceuro = eu()
        time = tim()
        ethereum = eth()
        etheuro = eteu()
        eurusd = euus()
        xrpusd = xrus()
        xrpeur = xreu()
        ltcus = ltus()
        ltceu = lteu()
        bchusd = bcus()
        bcheur = bceu()
        paxus = paxusd()
        paxeur = paxeu()
        xlmeur = xlmeu()
        xlmusd = xlmus()
        event, values = window.Read(timeout=10)
        window.Element('_DATE_').Update(str(time))
        window.Element('coin').Update('$ '+str(coinprice))
        window.Element('ethe').Update('$ '+str(ethereum))
        window.Element('btceu').Update('€ '+str(btceuro))
        window.Element('eteuro').Update('€ '+str(etheuro))
        window.Element('es').Update('$ '+str(eurusd))
        window.Element('xrp').Update('$ '+str(xrpusd))
        window.Element('xrpeu').Update('€ '+str(xrpeur))
        window.Element('ltcusd').Update('$ '+str(ltcus))
        window.Element('ltceur').Update('€ '+str(ltceu))
        window.Element('bcusd').Update('$ '+str(bchusd))
        window.Element('bceur').Update('€ '+str(bcheur))
        window.Element('paxu').Update('$ '+str(paxus))
        window.Element('paxe').Update('€ '+str(paxeur))
        window.Element('xlme').Update('€ '+str(xlmeur))
        window.Element('xlmu').Update('$ '+str(xlmusd))


        if event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                save_settings(SETTINGS_FILE, settings, values)
        
        

        
    window.Close()   

main()
