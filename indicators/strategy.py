import pandas as pd
import talib

def generate_signals(df, period=14, fast_ema=9, slow_ema=21):
    df['sar'] = talib.SAR(df['high'], df['low'], acceleration=0.02, maximum=0.2)
    df['willr'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=period)
    df['ema_fast'] = talib.EMA(df['close'], timeperiod=fast_ema)
    df['ema_slow'] = talib.EMA(df['close'], timeperiod=slow_ema)

    conditions = (df['close'] > df['sar']) & (df['willr'] < -80) & (df['ema_fast'] > df['ema_slow'])
    return conditions
