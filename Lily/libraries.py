import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from Lily.nltk_utils import bag_of_words, tokenize, stem
from Lily.model import NeuralNet

import nltk
import nextcord as discord

import time
import os

nltk.download('punkt')

from dotenv import load_dotenv

from yaspin import yaspin

with yaspin():
    load_dotenv()

print("Loaded virtual environment.")


import random
import json
import torch
from Lily.model import NeuralNet
from Lily.nltk_utils import bag_of_words, tokenize
import os
import multiprocessing

import numpy as np
import random
import glob
import requests

import torch
import torch.nn as nn

from torch.utils.data import Dataset, DataLoader
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

from Lily.nltk_utils import bag_of_words, tokenize, stem
import nltk

nltk.download('punkt')

from Lily.model import NeuralNet

import whisper
import pyaudio
import wave
import nextcord as discord
import webbrowser

import datetime
import time

from pyskyqremote.skyq_remote import SkyQRemote

import wikipediaapi
import requests
from bs4 import BeautifulSoup

from pydub import AudioSegment
import webrtcvad

from datetime import datetime
now = datetime.now()

from scipy.io import wavfile
import noisereduce as nr

from tuyapy import TuyaApi
import sys
