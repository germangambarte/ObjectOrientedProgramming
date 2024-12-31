class SalesManager:
    __billing: list

    def __init__(self):
        self.__billing = [[0] * 5] * 7
        print(self.__billing)

    def add_bill(self, day: int, branch: int, amount: float):
        self.__billing[branch - 1][day - 1] += amount

    def total_billing_by_branch(self, branch: int):
        branch_to_evalueate = self.__billing[branch - 1]
        sum = 0
        for day in branch_to_evalueate:
            sum += day
        return sum

    def get_max_billed_branch_by_day(self, day: int):
        max = 0
        branch_max_index = None
        for branch in range(0, 5):
            bill = self.__billing[branch][day - 1]
            if bill > max:
                max = bill
                branch_max_index = branch

        return branch_max_index + 1

    def get_min_bil_by_week(self):
        min = 99999999
        branch_index = None

        for index, branch in enumerate(self.__billing):
            sum = 0
            for billed in branch:
                sum += billed
            if sum < min:
                min = sum
                branch_index = index


if __name__ == '__main__':
    sl = SalesManager()
