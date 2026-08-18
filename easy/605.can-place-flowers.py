# @leet start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # first i think i should handle the
        # edgecases, like the corners and an single element array
        # i also need to handle n being 0, in that case i should aways return True

        possible_plants = 0  # this should be out here so it does not reset

        track = flowerbed.copy()

        for index, plot in enumerate(track):
            # Handling 0 n
            if n == 0:
                return True

            # Handling 1 plot flowerbed
            if len(track) == 1:
                if plot == 1:
                    return False
                else:
                    return True

            # I think i should keep count of how many times i could plant
            # and if that count is >= to n i return True

            # 0,0,1 can be planted in the 0 index
            if index == 0 and (track[index + 1] == 0 and plot == 0):
                possible_plants += 1
                track[index] = 1

            # here i am handling the last index
            elif index == len(track) - 1:
                if track[index - 1] == 0 and plot == 0:
                    possible_plants += 1
                    track[index] = 1

            elif index > 0:
                if (track[index - 1] == 0 and track[index + 1] == 0) and plot == 0:
                    possible_plants += 1
                    track[index] = 1

        return possible_plants >= n


# @leet end
