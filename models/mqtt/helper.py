import paho.mqtt.client as paho
import socket
import json
import sys



def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

global mqtt_status

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    # print("Read successful")
    if "mqtt" in data:
        user = data["mqtt"]["user"]
        password = data["mqtt"]["password"]
        broker = data["mqtt"]["broker"]
        transport = data["mqtt"]["transport"]
        password = data["mqtt"]["password"]
        topic = data["mqtt"]["topic"]
        mqtt_status = True
        market = data["coinbasepro"]["config"]["base_currency"]+"-"+data["coinbasepro"]["config"]["quote_currency"]
    else:
        user = ""
        password = ""
        broker = ""
        transport = ""
        password = ""
        topic = ""
        mqtt_status = False
# user = "mqtt_user"
# password = "ChestyPuller1775!"

if transport == "websockets":
    port = 9001
elif transport == "tcp":
    port = 1883
else:
    port = 1883
broker_address = broker
published = False

# set set_user, password, broker, port, transport
class MQTT:
    def __init__(self):
        print("Initializing MQTT")
        # self.client1 = paho.Client(client_id="", clean_session=True, userdata)

    def set_Market(m):
        global market
        market = m
    def set_mqtt_status(s):
        global mqtt_status
        mqtt_status = s
    def set_user(u):
        global user
        user = u
        print("user: " + user)
    def set_password(p):
        global password
        password = p

    def set_broker(b):
        global broker_address
        broker_address = b
    def set_port(p):
        global port
        port = p

    def set_transport(t):
        global transport
        transport = t
    def get_status():
        # return mqtt_status
        return True
    def get_user():
        return user
    def get_password():
        return password
    def get_broker():
        return broker_address
    def get_transport():
        return transport
    def get_port():
        global port
        # print(transport)
        if transport == "websockets":
            port = 9001
        elif transport == "tcp":
            port = 1883
        else:
            port = 1883
        return port
    def get_market():
        return market



def on_publish(client, userdata, result):  # create function for callback
    #  if published:
    # print("data published \n")
    #     published=True
    pass

def on_disconnect():
    # print("Disconnected result code " + str(rc))
    client1.loop_stop()

def on_message(client, userdata, message):
    pass
    # message_txt = str(message.payload.decode("utf-8"))
    # print("message received " + message.topic + " " + message_txt)

def on_connect():
    print("Conected to MQTT server")

def recconnect():
    print("reconnecting...")


# def send_mqtt():
#     # client1 = paho.Client(client_id="", clean_session=True, userdata=None, transport=transport)  # create client object
#     # client1.connect_async(MQTT.get_broker(), MQTT.get_port())
#     # client1.on_publish = on_publish  # assign function to callback
#     return client1


def on_connect(client, userdata, flags, rc):
    print("Opening MQTT connection...")


def mqtt_test_publish(t,c):
    # print(MQTT.get_status())
    if(MQTT.get_status()):
        client1.publish(topic + "/" + MQTT.get_market() + "/"  + t, c)
    else:
        # print("MQTT not configured")
        pass

if(internet()):
    client1 = paho.Client(client_id="", clean_session=True, userdata=None, transport=transport)  # create client object
    client1.connect_async(MQTT.get_broker(), MQTT.get_port())
    client1.on_publish = on_publish  # assign function to callback
    # client1 = send_mqtt()
    # client1.on_message = on_message
    client1.on_connect = on_connect
    client1.loop_start()  # start the loop
else:
    sys.exit("No network conectivity")

def update_technical_indicators(df_last):
    low = df_last["low"].values[0]
    high = df_last["high"].values[0]
    open = df_last["open"].values[0]
    volume = df_last["volume"].values[0]
    close = df_last["close"].values[0]
    close_pc = df_last["close_pc"].values[0]
    close_cpc = df_last["close_cpc"].values[0]
    cma = df_last["cma"].values[0]
    sma20 = df_last["sma20"].values[0]
    sma50 = df_last["sma50"].values[0]
    sma200 = df_last["sma200"].values[0]
    ema8 = df_last["ema8"].values[0]
    ema12 = df_last["ema12"].values[0]
    ema26 = df_last["ema26"].values[0]

    mqtt_test_publish("technical_indicators/" + "low", low)
    mqtt_test_publish("technical_indicators/" + "high", high)
    mqtt_test_publish("technical_indicators/" + "open", open)
    mqtt_test_publish("technical_indicators/" + "volume", volume)
    mqtt_test_publish("technical_indicators/" + "close", close)
    mqtt_test_publish("technical_indicators/" + "close_pc", close_pc)
    mqtt_test_publish("technical_indicators/" + "close_cpc", close_cpc)
    mqtt_test_publish("technical_indicators/" + "cma", cma)
    mqtt_test_publish("technical_indicators/" + "sma20", sma20)
    mqtt_test_publish("technical_indicators/" + "sma50", sma50)
    mqtt_test_publish("technical_indicators/" + "sma200", sma200)
    mqtt_test_publish("technical_indicators/" + "ema8", ema8)
    mqtt_test_publish("technical_indicators/" + "ema12", ema12)
    mqtt_test_publish("technical_indicators/" + "ema26", ema26)

    goldencross = bool(df_last["goldencross"].values[0])
    deathcross = bool(df_last["deathcross"].values[0])
    bullsma50 = bool(df_last["bullsma50"].values[0])
    mqtt_test_publish("technical_indicators/" + "goldencross", goldencross)
    mqtt_test_publish("technical_indicators/" + "deathcross", deathcross)
    mqtt_test_publish("technical_indicators/" + "bullsma50", bullsma50)

    fbb_mid = df_last["fbb_mid"].values[0]
    fbb_upper0_236 = df_last["fbb_upper0_236"].values[0]
    fbb_upper0_382 = df_last["fbb_upper0_382"].values[0]
    fbb_upper0_5 = df_last["fbb_upper0_5"].values[0]
    fbb_upper0_618 = df_last["fbb_upper0_618"].values[0]
    fbb_upper0_786 = df_last["fbb_upper0_786"].values[0]
    fbb_upper1 = df_last["fbb_upper1"].values[0]
    fbb_lower0_236 = df_last["fbb_lower0_236"].values[0]
    fbb_lower0_382 = df_last["fbb_lower0_382"].values[0]
    fbb_lower0_5 = df_last["fbb_lower0_5"].values[0]
    fbb_lower0_618 = df_last["fbb_lower0_618"].values[0]
    fbb_lower0_786 = df_last["fbb_lower0_786"].values[0]
    fbb_lower1 = df_last["fbb_lower1"].values[0]
    rsi14 = df_last["rsi14"].values[0]
    stochrsi14 = df_last["stochrsi14"].values[0]
    smastoch14 = df_last["smastoch14"].values[0]
    rsi_value = df_last["rsi_value"].values[0]

    mqtt_test_publish("technical_indicators/" + "fbb_mid", fbb_mid)
    mqtt_test_publish("technical_indicators/" + "fbb_upper0_236", fbb_upper0_236)
    mqtt_test_publish("technical_indicators/" + "fbb_upper0_382", fbb_upper0_382)
    mqtt_test_publish("technical_indicators/" + "fbb_upper0_5", fbb_upper0_5)
    mqtt_test_publish("technical_indicators/" + "fbb_upper0_618", fbb_upper0_618)
    mqtt_test_publish("technical_indicators/" + "fbb_upper0_786", fbb_upper0_786)
    mqtt_test_publish("technical_indicators/" + "fbb_upper1", fbb_upper1)
    mqtt_test_publish("technical_indicators/" + "fbb_lower0_236", fbb_lower0_236)
    mqtt_test_publish("technical_indicators/" + "fbb_lower0_382", fbb_lower0_382)
    mqtt_test_publish("technical_indicators/" + "fbb_lower0_5", fbb_lower0_5)
    mqtt_test_publish("technical_indicators/" + "fbb_lower0_618", fbb_lower0_618)
    mqtt_test_publish("technical_indicators/" + "fbb_lower0_786", fbb_lower0_786)
    mqtt_test_publish("technical_indicators/" + "fbb_lower1", fbb_lower1)
    mqtt_test_publish("technical_indicators/" + "rsi14", rsi14)
    mqtt_test_publish("technical_indicators/" + "stochrsi14", stochrsi14)
    mqtt_test_publish("technical_indicators/" + "smastoch14", smastoch14)
    mqtt_test_publish("technical_indicators/" + "rsi_value", rsi_value)

    rsi15 = bool(df_last["rsi15"].values[0])
    rsi15co = bool(df_last["rsi15co"].values[0])
    rsi85 = bool(df_last["rsi85"].values[0])
    rsi85co = bool(df_last["rsi85co"].values[0])
    williamsr14 = bool(df_last["williamsr14"].values[0])

    mqtt_test_publish("technical_indicators/" + "rsi15", rsi15)
    mqtt_test_publish("technical_indicators/" + "rsi15co", rsi15co)
    mqtt_test_publish("technical_indicators/" + "rsi85", rsi85)
    mqtt_test_publish("technical_indicators/" + "rsi85co", rsi85co)
    mqtt_test_publish("technical_indicators/" + "williamsr14", williamsr14)

    macd = df_last["macd"].values[0]
    signal = df_last["signal"].values[0]
    obv = df_last["obv"].values[0]
    obv_pc = df_last["obv_pc"].values[0]
    ema13 = df_last["ema13"].values[0]
    elder_ray_bull = df_last["elder_ray_bull"].values[0]
    elder_ray_bear = df_last["elder_ray_bear"].values[0]

    mqtt_test_publish("technical_indicators/" + "macd", macd)
    mqtt_test_publish("technical_indicators/" + "signal", signal)
    mqtt_test_publish("technical_indicators/" + "obv", obv)
    mqtt_test_publish("technical_indicators/" + "obv_pc", obv_pc)
    mqtt_test_publish("technical_indicators/" + "ema13", ema13)
    mqtt_test_publish("technical_indicators/" + "elder_ray_bull", elder_ray_bull)
    mqtt_test_publish("technical_indicators/" + "elder_ray_bear", elder_ray_bear)

    eri_buy = bool(df_last["eri_buy"].values[0])
    eri_sell = bool(df_last["eri_sell"].values[0])
    ema8gtema12 = bool(df_last["ema8gtema12"].values[0])
    ema8gtema12co = bool(df_last["ema8gtema12co"].values[0])
    ema8ltema12 = bool(df_last["ema8ltema12"].values[0])
    ema8ltema12co = bool(df_last["ema8ltema12co"].values[0])
    ema12gtema26 = bool(df_last["ema12gtema26"].values[0])
    ema12gtema26co = bool(df_last["ema12gtema26co"].values[0])
    ema12ltema26 = bool(df_last["ema12ltema26"].values[0])
    ema12ltema26co = bool(df_last["ema12ltema26co"].values[0])
    sma50gtsma200 = bool(df_last["sma50gtsma200"].values[0])
    sma50gtsma200co = bool(df_last["sma50gtsma200co"].values[0])
    sma50ltsma200 = bool(df_last["sma50ltsma200"].values[0])
    sma50ltsma200co = bool(df_last["sma50ltsma200co"].values[0])
    macdgtsignal = bool(df_last["macdgtsignal"].values[0])
    macdgtsignalco = bool(df_last["macdgtsignalco"].values[0])
    macdltsignal = bool(df_last["macdltsignal"].values[0])
    macdltsignalco = bool(df_last["macdltsignalco"].values[0])

    mqtt_test_publish("technical_indicators/" + "eri_buy", eri_buy)
    mqtt_test_publish("technical_indicators/" + "eri_sell", eri_sell)
    mqtt_test_publish("technical_indicators/" + "ema8gtema12", ema8gtema12)
    mqtt_test_publish("technical_indicators/" + "ema8gtema12co", ema8gtema12co)
    mqtt_test_publish("technical_indicators/" + "ema8ltema12", ema8ltema12)
    mqtt_test_publish("technical_indicators/" + "ema8ltema12co", ema8ltema12co)
    mqtt_test_publish("technical_indicators/" + "ema12gtema26", ema12gtema26)
    mqtt_test_publish("technical_indicators/" + "ema12gtema26co", ema12gtema26co)
    mqtt_test_publish("technical_indicators/" + "ema12ltema26", ema12ltema26)
    mqtt_test_publish("technical_indicators/" + "ema12ltema26co", ema12ltema26co)
    mqtt_test_publish("technical_indicators/" + "sma50gtsma200co", sma50gtsma200co)
    mqtt_test_publish("technical_indicators/" + "sma50ltsma200", sma50ltsma200)
    mqtt_test_publish("technical_indicators/" + "macdgtsignal", macdgtsignal)
    mqtt_test_publish("technical_indicators/" + "macdgtsignalco", macdgtsignalco)
    mqtt_test_publish("technical_indicators/" + "macdltsignal", macdltsignal)
    mqtt_test_publish("technical_indicators/" + "macdltsignalco", macdltsignalco)

    min_di14 = df_last["-di14"].values[0]
    plu_di14 = df_last["+di14"].values[0]
    adx14 = df_last["adx14"].values[0]
    adx14_trend = df_last["adx14_trend"].values[0]
    adx14_strength = df_last["adx14_strength"].values[0]

    mqtt_test_publish("technical_indicators/" + "min_di14", min_di14)
    mqtt_test_publish("technical_indicators/" + "plu_di14", plu_di14)
    mqtt_test_publish("technical_indicators/" + "adx14", adx14)
    mqtt_test_publish("technical_indicators/" + "adx14_trend", adx14_trend)
    mqtt_test_publish("technical_indicators/" + "adx14_strength", adx14_strength)
    # app = PyCryptoBot()
    # account = TradingAccount(app)
    # Stats(app, account).show()
    astral_buy = bool(df_last["astral_buy"].values[0])
    astral_sell = bool(df_last["astral_sell"].values[0])
    # This will display a table of the df_last dataframe
    # print("**********************Start 8DF Array***************************")
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', 1000)
    # pd.set_option('display.colheader_justify', 'center')
    # pd.set_option('display.precision', 3)
    # from IPython.display import display
    # display(df_last)
    # print("**********************End 8DF Array***************************")

    # mqtt_test_publish("Date-Time", str(now))
    # mqtt_test_publish("Market", bullbeartext)
    # mqtt_test_publish("Granularity", _app.printGranularity())
    # mqtt_test_publish("Price", str(price))
    # DF = (str((price-df["close"].max()) / (df["close"].max()) * 100))
    # mqtt_test_publish("% from DF HIGH", DF)
    # mqtt_test_publish("Margin",  "0")
    # mqtt_test_publish("Profit", "0")
    # mqtt_test_publish("Stop Loss", "0")

