from src.Training import Training


class TrainingsManager:
    __trainings: [Training]

    def __init__(self, trainings=[]):
        self.__trainings = trainings

    def get_trainings(self):
        return self.__trainings

    def add_training(self, training):
        self.__trainings.append(training)
