class ZeroTriplets:
    def __init__(self, num_list):
        self.num_list = num_list

    def get_triplets_adding_to_zero(self):
        num_list_length = len(self.num_list)
        triplets_list = []

        for i in range(0, num_list_length - 2):
            for j in range(i+1, num_list_length - 1):
                for k in range(j+1, num_list_length):
                    if self.num_list[i] + self.num_list[j] + self.num_list[k] == 0:
                        triplets_list.append([self.num_list[i], self.num_list[j],
                                              self.num_list[k]])

        return triplets_list


triplet1 = ZeroTriplets([-25, -10, -7, -3, 2, 4, 8, 10])

print("Triplets that add to zero are:", triplet1.get_triplets_adding_to_zero())
