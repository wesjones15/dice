# FROM frolvlad/alpine-python2
# FROM python:3
FROM sjawhar/pygame
ADD dice_v5_2_pyg.py /
ADD diceScoreIdea.py /
# RUN pip install --upgrade pip
# RUN pip -v install pygame
CMD { 'python3', 'dice_v5_2_pyg.py' }